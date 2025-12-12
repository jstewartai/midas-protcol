"""
Configuration defaults for the MIDAS protocol.

These values reflect the defaults specified in the paper.
They are intentionally conservative and intended as starting points,
not universal optima.
"""


# === Interaction Settings ===

DEFAULT_TURNS = 50
DEFAULT_STABILITY_WINDOW = 5


# === Metric Thresholds ===

DRIFT_COLLAPSE_THRESHOLD = 0.5
PRESERVATION_THRESHOLD = 0.8
PRESERVATION_STREAK = 3


# === Invariant Toggles ===

ENABLE_INVARIANTS = True
ENABLE_CORRECTION_IMMEDIACY = True
ENABLE_EXACT_RESURFACING = True
ENABLE_CONTINUITY_OF_STATE = True
ENABLE_CHANNEL_SEPARATION = True


# === Logging ===

LOG_INTERMEDIATE_STATES = True
LOG_METRICS = True
