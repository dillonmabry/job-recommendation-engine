from flask import Flask, request, jsonify
from nlp import extract_keywords
from worker import scrape_and_mail

ALLOWED_EXTENSIONS = set(['docx', 'doc'])

app = Flask(__name__)
TASKS = {} # celery tasks

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return 'No file present'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file and allowed_file(file.filename):
            keywords = extract_keywords(file)
            # mail queue for tasks
            task_id = len(TASKS)
            TASKS[task_id] = scrape_and_mail.delay(keywords)
            response = {'result': task_id}
            return jsonify(response)

@app.route('/', methods=['GET'])
def list_tasks():
    tasks = {task_id: {'ready': task.ready()}
             for task_id, task in TASKS.items()}
    return jsonify(tasks)

@app.route('/<int:task_id>', methods=['GET'])
def get_task(task_id):
    response = {'task_id': task_id}

    task = TASKS[task_id]
    if task.ready():
        response['result'] = task.get()
    return jsonify(response)

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')
