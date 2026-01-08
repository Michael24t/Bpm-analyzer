# src/dsp/features.py
import numpy as np
import librosa
from src.dsp.tempo import estimate_bpm

def extract_features(audio_path=None, y=None, sr=None):
    """
    Extract features: bpm, rms, spectral_centroid, zcr
    Can pass either audio_path or preloaded audio (y, sr)
    """

    # Load audio if path is given
    if audio_path:
        y, sr = librosa.load(audio_path)

    if y is None or sr is None:
        raise ValueError("Must provide either audio_path or y and sr")

    # Ensure y is float
    y = np.asarray(y, dtype=float)
    if y.size == 0:
        raise ValueError("Input audio is empty")

    # Predict BPM using DeepRhythmPredictor
    bpm, bpm_conf = estimate_bpm(y=y, sr=sr)

    # Other DSP features
    rms = float(np.mean(librosa.feature.rms(y=y)))
    centroid = float(np.mean(librosa.feature.spectral_centroid(y=y, sr=sr)))
    zcr = float(np.mean(librosa.feature.zero_crossing_rate(y)))

    return {
        "bpm": bpm,
        "bpm_confidence": bpm_conf,
        "rms": rms,
        "spectral_centroid": centroid,
        "zcr": zcr
    }
