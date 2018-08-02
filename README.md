# Job Recommendation Engine
- Takes input from resume as doc/docx from potential job candidate
- Scrapes Indeed for potential listings using NLP
- Sends email as task in worker queue
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
`curl -i -X PUT -H "Content-Type: multipart/form-data" -F "file=@sample_resume.docx" -F "email=rapid.dev.solutions@gmail.com" localh
ost:5000/api/upload
`
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

## Deployment Instructions
- Supports docker-compose containers
```
docker-compose up --build
```
- When running in development mode, change the redis broker url and updated config.py for backend services to be localhost rather than the docker-compose set .env variable

## TODO:
 * [x] NLP for suggesting jobs
 * [x] Email notifications
 * [x] API for task management 
 * [X] Front-end for task management
 * [X] Front-end for users to upload resume, receive email for suggested jobs
 * [X] Docker compose for deployment (multi-container)
 * [ ] Add authentication for users and admins to see tasks
 * [ ] Integrate Redux
 * [ ] Integrate web sockets for real time task management
