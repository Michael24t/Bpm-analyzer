from src.dsp.features import extract_features
import time

#quick test script to run inside ECS container

print("Container started... running test extraction")

result = extract_features("/app/scripts/Odyssey.wav")
print(">>> RESULT:", result)

print("Sleeping 5 minutes so ECS doesn't exit...")
time.sleep(300)
