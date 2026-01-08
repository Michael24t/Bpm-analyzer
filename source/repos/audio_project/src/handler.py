import json
import boto3
from src.dsp.features import extract_features  # Assuming this is your feature extraction function

s3 = boto3.client("s3")

def handler(event, context):
    """
    Lambda handler for audio processing and S3 upload.
    Expects event with 'audio_file_key' (S3 key) and 'bucket_name'.
    """
    try:
        bucket_name = event.get("bucket_name", "your-default-bucket") # replace with your default bucket
        audio_file_key = event.get("audio_file_key", "uploads/audio.wav") # replace with your default key
        
        # Download file from S3 (temporary local path)
        local_path = "/tmp/audio.wav"
        s3.download_file(bucket_name, audio_file_key, local_path)
        
        # Process audio
        features = extract_features(audio_path=local_path)
        
        # (Optional) Upload processed results back to S3
        result_key = f"processed/{audio_file_key.split('/')[-1].replace('.wav', '_features.json')}"
        s3.put_object(Bucket=bucket_name, Key=result_key, Body=json.dumps(features))
        
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Processing complete", "features": features})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }