from flask import Flask, request, jsonify
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
        return 'No file present'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file and allowed_file(file.filename):
        keywords = NLP.extract_keywords(file)
        # mail queue for tasks
        task_id = len(TASKS)
        TASKS[task_id] = scrape_and_mail.delay(keywords)
        response = {'result': task_id}
        return jsonify(response)

@app.route('/api/tasks', methods=['GET'])
def list_tasks():
    tasks = [{'id': task_id, 'done': task.ready()}
             for task_id, task in TASKS.items()]
    return jsonify(tasks)

@app.route('/api/task/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = TASKS[task_id]
    response = {'id': task_id}
    if task.ready():
        response['done'] = task.get()
    return jsonify(response)

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')
