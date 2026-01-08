import librosa

# Try to read default SR from config, fallback to 16000
try:
    from ..config import DEFAULT_SAMPLE_RATE as DEFAULT_SR
except Exception:
    DEFAULT_SR = 16000

def load_audio(path, sr=None):
    """Load audio file using librosa. Returns (y, sr)."""
    if sr is None:
        sr = DEFAULT_SR
    try:
        y, sr = librosa.load(path, sr=sr, mono=True)
        return y, sr
    except Exception as e:
        raise RuntimeError(f"Failed to load audio '{path}': {e}") from e