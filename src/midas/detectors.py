"""
Detector stubs for MIDAS protocol.

These functions are intentionally minimal and model-agnostic.
They define *interfaces*, not preferred implementations.

Replicators are expected to replace or extend these detectors
and report their choices explicitly.
"""


def contradiction_detected(current: str, previous: str) -> bool:
    """
    Detect whether the current output contradicts the previous state.

    Default implementation:
    - Always returns False.

    Rationale:
    - Contradiction detection is an acknowledged source of variation.
    - This stub preserves protocol structure without imposing semantics.
    - Replication studies should substitute their own detectors.
    """
    return False


def repetition_detected(text: str, window: int = 3) -> bool:
    """
    Detect degenerate looping or repetition.

    Default implementation:
    - Always returns False.

    Rationale:
    - Loop detection strategies vary widely.
    - This placeholder avoids embedding assumptions.
    """
    return False


def low_preservation_streak(P, t: int, threshold: float = 0.8, streak: int = 3) -> bool:
    """
    Check whether preservation fidelity has fallen below threshold
    for a consecutive number of turns.

    Parameters:
    - P: list or array of preservation values
    - t: current turn index
    - threshold: minimum acceptable P(t)
    - streak: number of consecutive failures required

    Returns:
    - True if collapse condition is met
    """
    if t < streak:
        return False

    recent = P[t - streak + 1 : t + 1]
    return all(p < threshold for p in recent)
