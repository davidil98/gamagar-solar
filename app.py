import json
import os
from flask import Flask, render_template

app = Flask(__name__)

def load_content():
    try:
        data_path = os.path.join(os.path.dirname(__file__), 'data', 'content.json')
        with open(data_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

@app.route('/')
def index():
    content = load_content()
    return render_template('index.html', content=content)

if __name__ == '__main__':
    app.run(debug=True)