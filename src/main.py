from flask import Flask, render_template, jsonify
import sys
from scripts import sparql

app = Flask(__name__, template_folder='templates', static_folder='public')
app.config['DEBUG'] = True

# main page

@app.route('/')
def index():
    return render_template('index.html', 
                            genres=sparql.generateGenreChart(),
                            authors=sparql.generateListOfAllAuthors(),
                            countries=sparql.generateListOfAllCountry())

@app.route('/countries')
def countries():
    return render_template('countries.html', 
                            countries=sparql.getListOfCountriesAndNumberOfBooks())

@app.route('/authors')
def authors():
    return render_template('authors.html',
                            authors=sparql.getListOfAuthorsAndTheirAbstracts())

@app.route('/country/<name>')
def country(name):
    return render_template('country.html',
                            country=name,
                            list=sparql.getAllBooksWithAuthorForCountry(name),
                            countries=sparql.generateListOfAllCountry())

@app.route('/author/<name>')
def author(name):
    return render_template('author.html',
                            author=sparql.findBookOfAuthor(name.replace(" ", "_")),
                            authors=sparql.generateListOfAllAuthors(),
                            name=name)

@app.route('/genre/<name>')
def getGenre(name):
    return render_template('genre.html',
                           countries=sparql.generateCountryOfOriginChart(name),
                           name=name,
                           list=sparql.getListOfCountriesAndNumberOfBooksInGenre(name))

# example method if we will use ajax


@app.route('/:api/getData', methods=['GET'])
def data():
    return jsonify({"data": sparql.anotherTest()})


@app.route('/:api/getTable', methods=['GET'])
def table():
    return jsonify({"table": sparql.generateData()})


@app.route('/:api/getChart', methods=['GET'])
def chart():
    return jsonify({"chart": sparql.generateChart()})


@app.route('/:api/getListOfCountriesAndNumberOfBooks', methods=['GET'])
def countriesList():
    return jsonify({"list": sparql.getListOfCountriesAndNumberOfBooks()})


# page loa


@app.errorhandler(404)
def handle_404(e):
    return 'Kochany przybyszu, nie ma takiej strony :('
