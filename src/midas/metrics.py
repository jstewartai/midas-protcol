import unicodedata


def normalize_text(text: str) -> str:
    """
    Normalize text for reproducible character-level comparison.
    Applies Unicode NFC normalization and strips trailing newlines.
    """
    if text is None:
        return ""
    text = unicodedata.normalize("NFC", text)
    return text.rstrip("\n")


def levenshtein_distance(a: str, b: str) -> int:
    """
    Compute character-level Levenshtein distance between two strings.
    """
    if a == b:
        return 0
    if len(a) == 0:
        return len(b)
    if len(b) == 0:
        return len(a)

    prev_row = list(range(len(b) + 1))
    for i, ca in enumerate(a, start=1):
        curr_row = [i]
        for j, cb in enumerate(b, start=1):
            insert_cost = curr_row[j - 1] + 1
            delete_cost = prev_row[j] + 1
            substitute_cost = prev_row[j - 1] + (ca != cb)
            curr_row.append(min(insert_cost, delete_cost, substitute_cost))
        prev_row = curr_row

    return prev_row[-1]


def drift_metric(current: str, previous: str) -> float:
    """
    Compute normalized drift metric D(t) between successive outputs.
    D(t) = lev(S_t, S_{t-1}) / max(|S_t|, |S_{t-1}|)
    """
    current = normalize_text(current)
    previous = normalize_text(previous)

    if len(current) == 0 and len(previous) == 0:
        return 0.0
    if len(current) == 0 or len(previous) == 0:
        return 1.0

    distance = levenshtein_distance(current, previous)
    return distance / max(len(current), len(previous))


def preservation_fidelity(resurfaced: str, original: str) -> float:
    """
    Compute preservation fidelity P(t) for exact resurfacing.
    P(t) = 1 - (character mismatches / |original|)
    """
    resurfaced = normalize_text(resurfaced)
    original = normalize_text(original)

    if len(original) == 0:
        return 0.0

    mismatches = sum(
        1 for a, b in zip(resurfaced, original) if a != b
    )
    mismatches += abs(len(resurfaced) - len(original))

    return 1.0 - (mismatches / len(original))
