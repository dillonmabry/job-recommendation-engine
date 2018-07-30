from flask import Flask, request, jsonify, Response
from nlp import NLP
from worker import scrape_and_mail
from flask_cors import CORS

ALLOWED_EXTENSIONS = set(['docx', 'doc'])

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})
NLP = NLP()
TASKS = {} # celery tasks

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/upload', methods=['PUT'])
def upload_file():
    # check if the post request has the file part
    if 'file' not in request.files:
        return Response("No file present", status=500, mimetype="application/json")
    file = request.files['file']
    if file.filename == '':
        return Response("No filename detected", status=500, mimetype="application/json")
    if file and allowed_file(file.filename):
        keywords = NLP.extract_keywords(file)
        # mail queue for tasks
        task_id = len(TASKS)
        TASKS[task_id] = scrape_and_mail.delay(keywords)
        response = {'id': task_id, 'keywords': keywords}
        return jsonify(response)

@app.route('/api/tasks', methods=['GET'])
def list_tasks():
    tasks = [{'id': task_id, 'done': task.ready()}
             for task_id, task in TASKS.items()]
    return jsonify(tasks)

@app.route('/api/task/<int:task_id>', methods=['GET'])
def get_task(task_id):
    if task_id not in TASKS:
        return Response("No task found with id specified", status=404, mimetype="application/json")
    task = TASKS[task_id]
    response = {'id': task_id}
    if task.ready():
        response['done'] = task.get()
    return jsonify(response)

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')
