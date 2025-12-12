"""
Run MIDAS harness in unstructured baseline mode.
"""

from midas.harness import run_midas


def dummy_model(prompt: str) -> str:
    """
    Placeholder model function.
    Echoes input to keep behavior deterministic.
    """
    return prompt


if __name__ == "__main__":
    run_midas(
        model_A=dummy_model,
        model_B=dummy_model,
        seed_text="Seed text for turn 0.",
        turns=10,
        invariants_enabled=False,
    )
