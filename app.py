import json
import os
from flask import Flask, render_template, url_for

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

@app.route('/calculadora/')
def calculadora():
    content = load_content()
    return render_template('calculator.html', content=content)

@app.route('/portal-operativo/')
def portal_operativo():
    content = load_content()
    return render_template('dashboard_op.html', content=content)

@app.route('/portal-operativo/cotizacion/')
def quotation():
    content = load_content()
    return render_template('quotation.html', content=content)

@app.route('/portal-operativo/checklist/')
def checklist():
    content = load_content()
    return render_template('checklist.html', content=content)

@app.route('/portal-operativo/carta-poder/')
def carta_poder():
    content = load_content()
    return render_template('carta_poder.html', content=content)

@app.route('/portal-operativo/contrato/')
def contract():
    content = load_content()
    return render_template('contract.html', content=content)

if __name__ == '__main__':
    app.run(debug=True)