# Job Recommendation Engine
**This is for HTTPS setup only**
## Backend Instructions
- Install Backend:
```
./install.sh
```
- Configure config file (change config-example.py to "config.py")
- To run:
```
redis-server
celery -A worker worker --loglevel=debug
python app.py
```
Send POST with doc/docx file (resume) for analyzing:
```
curl -i -X PUT -H "Content-Type: multipart/form-data" -F "file=@sample_resume.docx" -F "email=rapid.dev.solutions@gmail.com" localhost:5000/api/upload
```
Responses (Task queue):
```
curl localhost:5000/api/tasks
``` 
```
curl localhost:5000/api/task/<task-id>
```

## Frontend Instructions
- Navigate to frontend
```
npm install
npm start
```
- App should be running on http://localhost:3000

## SSL Deployment Instructions
```
./install-certs.sh
```
- Ensure certs are created for backend/ and local /opt/traefik directories
- Ensure correct config information
```
docker-compose up --build
```

## Deployment Instructions
- Supports docker-compose containers
```
docker-compose up --build
```
- When running in development mode, change the redis broker url and updated config.py for backend services to be localhost rather than the docker-compose set .env variable
