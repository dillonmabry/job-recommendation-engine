# Job Recommendation Engine
- Takes input from resume as doc/docx from potential job candidate
- Scrapes Indeed for potential listings using NLP
- Sends email as task in worker queue
## DEV Instructions
Install:
```
./install.sh
```
To run:
```
redis-server
celery -A worker worker --loglevel=debug
python3 app.py
```
Send POST with doc/docx file (resume) for analyzing:
`curl -i -X POST -H "Content-Type: multipart/form-data" -F "file=@test/MabryDillonCurrentResume.docx" 0.0.0.0:5000/upload`
Responses (Task queue):
```
curl localhost:5000
``` 
```
curl localhost:5000/<task-id>
```
## PROD Instructions
*Dockerfile to be created soon
