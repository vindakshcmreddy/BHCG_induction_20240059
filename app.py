from flask import Flask, request, redirect, render_template
import json
import os

app = Flask(__name__)
DATA_FILE = 'data.json'

# converting a >json file into a python dictionery
def read_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE) as sample:
        return json.load(sample)

def write_data(data):
    with open(DATA_FILE, 'w') as sample:
        json.dump(data, sample, indent=2)

@app.route('/')
def index():
    data = read_data()
    return render_template('index.html', modules=data)

@app.route('/add', methods=['POST'])
def add_resource():
    week = request.form.get('week')
    title = request.form.get('title')
    res_type = request.form.get('type')
    url = request.form.get('url')

    if not week or not title or not res_type or not url:
        return "Missing data", 400

    data = read_data()
    resource = {
        "title": title,
        "type": res_type,
        "url": url
    }

    if week not in data:
        data[week] = []
    data[week].append(resource)
    write_data(data)
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete_resource():
    week = request.form.get('week')
    title = request.form.get('title')

    data = read_data()
    if week in data:
        original_len = len(data[week])
        data[week] = [r for r in data[week] if r['title'] != title]
        if len(data[week]) != original_len:
            write_data(data)

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
