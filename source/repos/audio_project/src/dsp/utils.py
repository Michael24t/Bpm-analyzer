def normalize_audio(y):
    """Placeholder normalization"""
    if not y:
        return y
    # Example: simple scaling
    maxv = max(abs(v) for v in y) or 1
    return [v / maxv for v in y]