from flask import Flask, render_template, jsonify
import sys
from scripts import sparql

app = Flask(__name__, template_folder='templates', static_folder='public')
app.config['DEBUG'] = True

#main page
@app.route('/')
def index():
    return render_template('index.html', genres=sparql.generateGenreChart())

@app.route('/country/<name>')
def country(name):
    return render_template('country.html', countries=sparql.generateCountryOfOriginChart(name))

@app.route('/genre/<name>')
def getGenre(name):
    return render_template('page2.html')

#example method if we will use ajax
@app.route('/:api/getData', methods=['GET'])
def data():
    return jsonify({"data": sparql.anotherTest()})

@app.route('/:api/getTable', methods=['GET'])
def table():
    return jsonify({"table": sparql.generateData()})

@app.route('/:api/getChart', methods=['GET'])
def chart():
    return jsonify({"chart": sparql.generateChart()})

@app.route('/:api/getDoughnutChart', methods=['GET'])
def doughnutChart():
    return jsonify({"chart": sparql.generateGenreChart()})

#page loa
@app.errorhandler(404)
def handle_404(e):
    return 'Kochany przybyszu, nie ma takiej strony :('