# This is place for SPARQL methods
import json
from SPARQLWrapper import SPARQLWrapper, JSON
#from pprint import pprint  #for debug, remember to pip install pprint if not installed


def test():
    return 'no witam'


def anotherTest():
    return 'Power of json!'


def generateData():
    return {
        1: {
            "customerId": 246,
            "name": "John Hammond",
            "country": "United States",
        },
        2: {
            "customerId": 236,
            "name": "ADRIAN",
            "country": "GRZEGORZ",
        },
        3: {
            "customerId": 246,
            "name": "HUBERT",
            "country": "ZOSIA",
        },
    }


def generateGenreChart():
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery("""
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX dc: <http://purl.org/dc/elements/1.1/>
        PREFIX : <http://dbpedia.org/resource/>
        PREFIX dbpedia2: <http://dbpedia.org/property/>
        PREFIX dbpedia: <http://dbpedia.org/>
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        SELECT (SAMPLE(?bind) AS ?GENRE)(COUNT (?book) as ?BOOKS)  WHERE
         { ?book a  <http://schema.org/Book> .
         {?book <http://dbpedia.org/property/genre> ?genre .
            FILTER(LANGMATCHES(LANG(?genre), 'en'))
            ?genre bif:contains "Thriller" .
            BIND(str("Thriller") as ?bind)}UNION
         {?book <http://dbpedia.org/property/genre> ?genre .
            FILTER(LANGMATCHES(LANG(?genre), 'en'))
            ?genre bif:contains "Drama" .
            BIND(str("Drama") as ?bind)}UNION
         {?book <http://dbpedia.org/property/genre> ?genre .
            FILTER(LANGMATCHES(LANG(?genre), 'en'))
            ?genre bif:contains "Comedy".
            BIND(str("Comedy") as ?bind)}UNION
         {?book <http://dbpedia.org/property/genre> ?genre .
            FILTER(LANGMATCHES(LANG(?genre), 'en'))
            ?genre bif:contains "Romance".
            BIND(str("Romance") as ?bind)}UNION
         {?book <http://dbpedia.org/property/genre> ?genre .
            FILTER(LANGMATCHES(LANG(?genre), 'en'))
            ?genre bif:contains "Fantasy".
            BIND(str("Fantasy") as ?bind)}UNION
         {?book <http://dbpedia.org/property/genre> ?genre .
            FILTER(LANGMATCHES(LANG(?genre), 'en'))
            ?genre bif:contains "Biography".
            BIND(str("Biography") as ?bind)}UNION
         {?book <http://dbpedia.org/property/genre> ?genre .
            FILTER(LANGMATCHES(LANG(?genre), 'en'))
            ?genre bif:contains "Mystery".
            BIND(str("Mystery") as ?bind)}UNION
         {?book <http://dbpedia.org/property/genre> ?genre .
            FILTER(LANGMATCHES(LANG(?genre), 'en'))
            ?genre bif:contains "Poetry".
            BIND(str("Poetry") as ?bind)}UNION
         {?book <http://dbpedia.org/property/genre> ?genre .
            FILTER(LANGMATCHES(LANG(?genre), 'en'))
            ?genre bif:contains "Non-fiction".
            BIND(str("Non-fiction") as ?bind)}UNION
         {?book <http://dbpedia.org/property/genre> ?genre .
            FILTER(LANGMATCHES(LANG(?genre), 'en'))
            ?genre bif:contains "Science-Fiction".
            BIND(str("Science-Fiction") as ?bind)}
        }GROUP BY ?bind ORDER BY DESC (?BOOKS)
    """)
    sparql.setReturnFormat(JSON)
    result = sparql.query().convert()
    pprint(result)
    RET = {}
    for hit in result["results"]["bindings"]:
        RET[hit["GENRE"]["value"]] = hit["BOOKS"]["value"]
    return RET
#generateGenreChart()

def generateCountryOfOriginChart(param):
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery("""
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX dc: <http://purl.org/dc/elements/1.1/>
        PREFIX : <http://dbpedia.org/resource/>
        PREFIX dbpedia2: <http://dbpedia.org/property/>
        PREFIX dbpedia: <http://dbpedia.org/>
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        SELECT  ?out ?national (COUNT (?book) as ?BOOKS )  WHERE
        { ?book a  <http://schema.org/Book> .
         ?book <http://dbpedia.org/property/genre> ?genre .
            FILTER(LANGMATCHES(LANG(?genre), 'en'))
            ?genre bif:contains \"""" + param + """\" .
            ?book  <http://dbpedia.org/property/author> ?author .
            ?author <http://dbpedia.org/property/nationality> ?nationality .
            OPTIONAL{?nationality foaf:name ?national .} .
            BIND(IF(exists{?nationality foaf:name ?national},
            ?national,?nationality) AS ?out)

        }ORDER BY DESC (?BOOKS)LIMIT 10
    """)
    sparql.setReturnFormat(JSON)
    result = sparql.query().convert()
    RET = {}
    for hit in result["results"]['bindings']:
        RET[hit["out"]["value"]] = hit["BOOKS"]["value"]
    return RET


def generateListOfAllAuthors():
    #gets you 1 column full of authors
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery("""
            select distinct ?author
            where {
            ?book rdf:type <http://schema.org/Book>;
            <http://dbpedia.org/ontology/author> ?author
            }
        """)
    sparql.setReturnFormat(JSON)
    result = sparql.query().convert()
    RET = []
    for hit in result["results"]["bindings"]:
        tmp = hit["author"]["value"]
        tmp = tmp.replace("http://dbpedia.org/resource/","")
        tmp = tmp.replace("_"," ")
        RET.append(tmp)
    return RET

#pprint(generateListOfAllAuthors())

def findBookOfAuthor(author):
    author = author.replace(" ", "_")
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    query = """
            select ?author ?book(group_concat(?genre;
            SEPARATOR = ", ") as ?genres)
            where
            {
            ?book
            rdf:type<http://schema.org/Book>;
            <http://dbpedia.org/property/genre> ?genre;
            <http://dbpedia.org/ontology/author> ?author.FILTER
            regex(?author, "insertNameHere")
            } group
            by ?book ?author
        """
    query = query.replace("insertNameHere", author)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    result = sparql.query().convert()
    RET = {}
    for hit in result["results"]['bindings']:
        title = hit["book"]["value"]
        title = title.replace("http://dbpedia.org/resource/","")
        title = title.replace("_"," ")
        genreList = hit["genres"]["value"]
        genreList = genreList.replace("http://dbpedia.org/resource/", "")
        genreList = genreList.replace("_", " ")
        RET[title] = genreList
    return result

#findBookOfAuthor("Lemony Snicket")

def getListOfCountriesAndNumberOfBooks():
    #gets you 2 columns: countries and total number of books from there
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    query = """
    select ?country count(?country) as ?numberOfBooks
    where {
    ?book rdf:type <http://schema.org/Book>;
    <http://dbpedia.org/property/country> ?country .
    FILTER(LANGMATCHES(LANG(?country), 'en'))
    OPTIONAL{?country foaf:name ?commonName.} .
        BIND(IF(exists{?country foaf:name ?commonName},
        ?commonName,?country) AS ?out)
    } group by ?country
    """
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    result = sparql.query().convert()
    RET = {}
    for hit in result["results"]['bindings']:
        country = hit["country"]["value"]
        numb = hit["numberOfBooks"]["value"]
        RET[country] = numb
    return RET

# pprint(getListOfCountriesAndNumberOfBooks())

def getAuthorsAndNumberOfTheirBooks():
    #gets you 2 columns: author and total number of their books

    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    query = """
            select ?author count(?book) as ?numberOfBooks
            where{
            ?book rdf:type<http://schema.org/Book>;
            <http://dbpedia.org/property/genre> ?genre;
            <http://dbpedia.org/ontology/author> ?author
            } group by ?author
        """
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    result = sparql.query().convert()
    RET = {}
    for hit in result["results"]['bindings']:
        author = hit["author"]["value"]
        author = author.replace("http://dbpedia.org/resource/","")
        author = author.replace("_", " ")
        numb = hit["numberOfBooks"]["value"]
        RET[author] = numb
    return RET

#pprint(getAuthorsAndNumberOfTheirBooks())

def getListOfCountriesAndNumberOfBooksInGenre(desiredGenre):
    #gets you 2 columns: countries and total number of books from there
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    query = """
    select ?country count(?country) as ?numberOfBooks
    where {
    ?book rdf:type <http://schema.org/Book>;
    <http://dbpedia.org/property/country> ?country;
    <http://dbpedia.org/property/genre> ?genre.FILTER
     regex(?genre, "insertGenreHere","i") . 
    FILTER(LANGMATCHES(LANG(?country), 'en'))
    OPTIONAL{?country foaf:name ?commonName.} .
        BIND(IF(exists{?country foaf:name ?commonName},
        ?commonName,?country) AS ?out)
    } group by ?country
    """
    query = query.replace("insertGenreHere",desiredGenre)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    result = sparql.query().convert()
    RET = {}
    for hit in result["results"]['bindings']:
        country = hit["country"]["value"]
        numb = hit["numberOfBooks"]["value"]
        RET[country] = numb
    return RET

#pprint(getListOfCountriesAndNumberOfBooksInGenre("comedy"))

def getListOfAuthorsAndTheirAbstracts():
    # gets you 2 columns: authors and their abstracts
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    query = """
            select ?author (count(?book) as ?numberOfBooks) ?abstract
            where{
            ?book a <http://schema.org/Book> .
            ?book <http://dbpedia.org/property/author> ?author .
            ?author <http://dbpedia.org/ontology/abstract> ?abstract . 
            FILTER(LANGMATCHES(LANG(?abstract), 'en'))
            } group by ?author ?abstract
        """
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    result = sparql.query().convert()
    RET = {}
    for hit in result["results"]['bindings']:
        author = hit["author"]["value"]
        author = author.replace("http://dbpedia.org/resource/","")
        author = author.replace("_"," ")
        author = author.replace("@en", "")
        abstract = hit["abstract"]["value"]
        abstract = abstract.replace("@en", "")
        RET[author] = abstract
    return RET

#pprint(getListOfAuthorsAndTheirAbstracts())

def juzZapomnialemCoTaFunkcjaRobiMozeszZastapicTaNazweAleSzczerzeMamToGdzies(origin):
    origin = origin.replace(" ","_")
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    query = """
        select distinct ?out ?name
        where {
        ?book a <http://schema.org/Book> .
        ?book <http://dbpedia.org/property/country> ?country .
        FILTER(LANGMATCHES(LANG(?country), 'en')) . 
        ?country bif:contains "insertNameHere" .
        ?book <http://dbpedia.org/property/name> ?name .
        ?book <http://dbpedia.org/property/author> ?author .
        optional {?author foaf:name ?aname . } .
        bind (if (exists {?author foaf:name ?aname . }, ?aname, ?author) as ?out)}
    """
    query = query.replace("insertNameHere", origin)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    result = sparql.query().convert()
    RET = {}
    for hit in result["results"]['bindings']:
        author = hit["name"]["value"]
        author = author.replace("http://dbpedia.org/resource/", "")
        author = author.replace("_", " ")
        author = author.replace("@en", "")
        abstract = hit["out"]["value"]
        abstract = abstract.replace("@en", "")
        abstract = abstract.replace("http://dbpedia.org/resource/", "")
        RET[author] = abstract
    return RET
#pprint(juzZapomnialemCoTaFunkcjaRobiMozeszZastapicTaNazweAleSzczerzeMamToGdzies("United States"))

"""
select ?author (count(?book) as ?numberOfBooks) ?abstract
            where{
            ?book a <http://schema.org/Book> .
            ?book <http://dbpedia.org/property/author> ?author .
            ?author <http://dbpedia.org/ontology/abstract> ?abstract . 
            FILTER(LANGMATCHES(LANG(?abstract), 'en'))
            } group by ?author ?abstract
"""

"""
select distinct ?out ?name
    where {
    ?book a <http://schema.org/Book> .
    ?book <http://dbpedia.org/property/country> ?country .
    FILTER(LANGMATCHES(LANG(?country), 'en')) . 
    ?country bif:contains "United_States" .
    ?book <http://dbpedia.org/property/name> ?name .
    ?book <http://dbpedia.org/property/author> ?author .
    optional {?author foaf:name ?aname . } .
    bind (if (exists {?author foaf:name ?aname . }, ?aname, ?author) as ?out)
    }
    """

"""
select distinct ?out ?name
    where {
    ?book a <http://schema.org/Book> .
    ?book <http://dbpedia.org/property/country> ?country .
    FILTER(LANGMATCHES(LANG(?country), 'en')) . 
    ?country bif:contains "United_States" .
    ?book <http://dbpedia.org/property/name> ?name .
    ?book <http://dbpedia.org/property/author> ?author .
    optional {?author foaf:name ?aname . } .
    bind (if (exists {?author foaf:name ?aname . }, ?aname, ?author) as ?out)
    }
"""