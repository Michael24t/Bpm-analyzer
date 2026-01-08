import boto3

s3 = boto3.client("s3")

bucket_name = "audio-analysis-michael-0724"
object_key = "uploads/you.wav"
local_file_path = "scripts/you.wav"  # adjust if needed

s3.upload_file(local_file_path, bucket_name, object_key)

print("Upload successful!")
