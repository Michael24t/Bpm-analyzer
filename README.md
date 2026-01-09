
# BPM-Analyzer

A web-based tool that analyzes uploaded audio files, extracts tempo (BPM), RMS, ZCR,  and spectral centroid and then returns results.


## Key Technologies

- Docker containerized application
- AWS Fargate (ECS) for running container 
- FastAPI backend 
- AWS S3 for storing uploaded files
- Elastic Load Balancer for web traffic routing


## features 

- Upload .wav, .mp3, or .flac files
- Extract BPM using librosa + DeepRhythm
- Return BPM, RMS, ZCR, and Spectral Centroid
- Deployed using real production infrastructure
## Architecture overview

User -> LoadBalancer -> ECS_Task -> FastAPI Container -> S3 bucket

1. ECS launches docker container which is running fastAPI among all other dependencies in requirments.txt
2. Load balancer will forward HTTP requests to container 
3. All uploaded files go to S3 
4. API will process audio and return BPM 
## For Running Locally 

Install dependencies withing requirement.txt and requirement-extra.txt 

```bash
  uvicorn app.main:app --reload
```
    
## Deployment

Proof of deployment to AWS 

![AWS ECS API](Deployment/ECS API.png)
![AWS ECR image](Deployment/ECR image.png)
![S3 bucket results](Deployment/S3 bucket.png)


## Demo 

- Fully working locally
- AWS cluster is currently paused for cost control. Please reach out to the email below if you would like me to turn everything back on for a demo.
- mikey724t@hotmail.com 


## Future integration

Mass upload music files to S3 for large scale analysis of files using AI agents



## Authors

- [@Michael Tumminia](https://github.com/Michael24t)

