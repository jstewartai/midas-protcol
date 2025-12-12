"""
MIDAS dual-LLM evaluation harness.

This module implements the core multi-turn interaction loop
described in WP 3.0 (v1.5), Appendix C.
"""

from typing import Callable

from midas.metrics import drift_metric, preservation_fidelity
from midas.detectors import (
    contradiction_detected,
    repetition_detected,
    low_preservation_streak,
)
from midas.logging import log_metrics, log_state, log_collapse
from midas.config import (
    DRIFT_COLLAPSE_THRESHOLD,
    PRESERVATION_THRESHOLD,
    PRESERVATION_STREAK,
)


def run_midas(
    model_A: Callable[[str], str],
    model_B: Callable[[str], str],
    seed_text: str,
    turns: int,
    invariants_enabled: bool = True,
) -> None:
    """
    Run a MIDAS interaction loop.

    Parameters:
    - model_A: generation function (Model A)
    - model_B: preservation function (Model B)
    - seed_text: initial interaction state H_0
    - turns: number of interaction turns
    - invariants_enabled: toggle for MIDAS invariant enforcement
    """

    previous_state = seed_text
    P = []
    D = []

    for t in range(1, turns + 1):

        # 1. Generation (Model A)
        S_t = model_A(previous_state)

        # 2. Exact resurfacing (Model B)
        prompt_R = "Repeat exactly:\n" + S_t
        R_t = model_B(prompt_R)

        # 3. Metric computation
        p_t = preservation_fidelity(R_t, S_t)
        d_t = drift_metric(S_t, previous_state)

        P.append(p_t)
        D.append(d_t)

        log_metrics(t, d_t, p_t)

        # 4. Optional invariant enforcement
        if invariants_enabled and contradiction_detected(S_t, previous_state):
            correction_prompt = (
                "INSTRUCTION: Identify contradictions between the two statements below.\n"
                "STATEMENT A (Previous):\n" + previous_state + "\n"
                "STATEMENT B (Current):\n" + S_t + "\n"
                "TASK: Output only the corrected version of STATEMENT B with contradictions resolved.\n"
                "Do NOT add explanations or commentary."
            )
            S_t = model_B(correction_prompt)

        # 5. State update
        next_state = R_t if invariants_enabled else S_t
        previous_state = next_state

        log_state(t, previous_state)

        # 6. Collapse detection
        if (
            d_t > DRIFT_COLLAPSE_THRESHOLD
            or low_preservation_streak(P, t - 1, PRESERVATION_THRESHOLD, PRESERVATION_STREAK)
            or repetition_detected(S_t)
        ):
            log_collapse(t, "collapse condition met")
            break
