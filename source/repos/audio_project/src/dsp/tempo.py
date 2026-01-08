import librosa
from deeprhythm import DeepRhythmPredictor

_model = None   # new tempo will load model when called

def get_model():
    global _model
    if _model is None:
        print("Loading DeepRhythmPredictor (first request)...")
        _model = DeepRhythmPredictor()
    return _model

def estimate_bpm(audio_path=None, y=None, sr=None, include_confidence=True):
    # Lazy load model
    model = get_model()

    # Load audio as before
    if audio_path:
        y, sr = librosa.load(audio_path)
    elif y is None or sr is None:
        raise ValueError("Must provide either audio_path or y and sr")

    if include_confidence:
        bpm, confidence = model.predict_from_audio(y, sr, include_confidence=True)
        return bpm, confidence
    else:
        bpm = model.predict_from_audio(y, sr)
        return bpm, None
