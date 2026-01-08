import boto3
import json
import os
import time
from src.dsp.features import extract_features

s3 = boto3.client("s3")

BUCKET = "audio-analysis-michael-0724"
KEY = "uploads/Odyssey.wav"  # change to any file in uploads/

def main():
    print(f"Downloading s3://{BUCKET}/{KEY}")
    local_path = "/tmp/audio.wav"

    # Download from S3
    s3.download_file(BUCKET, KEY, local_path)

    print("Processing...")
    features = extract_features(audio_path=local_path)

    # Save results back to S3
    result_key = f"processed/{os.path.basename(KEY).replace('.wav', '_features.json')}"
    print(f"Uploading results to s3://{BUCKET}/{result_key}")
    s3.put_object(
        Bucket=BUCKET,
        Key=result_key,
        Body=json.dumps(features)
    )

    print("Done! Results stored in S3.")
    print(features)

    # Sleep to keep logs visible
    time.sleep(60)

if __name__ == "__main__":
    main()
