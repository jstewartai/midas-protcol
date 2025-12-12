"""
Lightweight logging utilities for the MIDAS protocol.

Logging is intentionally minimal and structured to support
post-hoc analysis and external visualization tools.
"""

import json
from typing import Any, Dict


def log_event(event_type: str, payload: Dict[str, Any]) -> None:
    """
    Emit a structured log event as JSON.

    Parameters:
    - event_type: short label for the event category
    - payload: dictionary of event data
    """
    record = {
        "event": event_type,
        "data": payload,
    }
    print(json.dumps(record))


def log_metrics(turn: int, drift: float, preservation: float) -> None:
    """
    Log drift and preservation metrics for a given turn.
    """
    log_event(
        "metrics",
        {
            "turn": turn,
            "D": drift,
            "P": preservation,
        },
    )


def log_state(turn: int, state: str) -> None:
    """
    Log interaction state text (optional, may be disabled by config).
    """
    log_event(
        "state",
        {
            "turn": turn,
            "text": state,
        },
    )


def log_collapse(turn: int, reason: str) -> None:
    """
    Log detection of a collapse condition.
    """
    log_event(
        "collapse",
        {
            "turn": turn,
            "reason": reason,
        },
    )
