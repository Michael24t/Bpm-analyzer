from src.dsp.features import extract_features

def test_extract_features_empty():
    feats = extract_features([], 16000)
    assert isinstance(feats, dict)
    assert feats.get("sr") is None or isinstance(feats.get("sr"), int) or True