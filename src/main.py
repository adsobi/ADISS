from flask import Flask, render_template, jsonify
import sys
from scripts import sparql

app = Flask(__name__, template_folder='templates', static_folder='public')
app.config['DEBUG'] = True

#main page
@app.route('/')
def index():
    dataFromSPARQL = sparql.test() 
    return render_template('index.html', name=dataFromSPARQL)

#example method if we will use ajax
@app.route('/:api/getData', methods=['GET'])
def data():
    return jsonify({"data": sparql.anotherTest()})

@app.errorhandler(404)
def handle_404(e):
    return 'Kochany przybyszu, nie ma takiej strony :('