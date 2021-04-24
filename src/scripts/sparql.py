# This is place for SPARQL methods
from SPARQLWrapper import SPARQLWrapper, JSON


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
    RET = {}
    for hit in result["results"]["bindings"]:
        # We want the "value" attribute of the "comment" field
        RET[hit["GENRE"]["value"]] = hit["BOOKS"]["value"]
    return RET
