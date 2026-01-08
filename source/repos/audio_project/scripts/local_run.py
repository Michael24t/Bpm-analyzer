# scripts/local_run.py
import sys
from src.dsp.features import extract_features

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m scripts.local_run <audio_file_path>")
        sys.exit(1)

    audio_file = sys.argv[1]

    try:
        features = extract_features(audio_path=audio_file)
    except Exception as e:
        print(f"Error processing audio: {e}")
        sys.exit(1)

    print("Extracted Features:")
    for k, v in features.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    main()
