# First install the package if you don't have it:
# pip install SPARQLWrapper

from SPARQLWrapper import SPARQLWrapper, JSON

# UniProt SPARQL endpoint
endpoint_url = "https://sparql.uniprot.org/sparql"

# Your protein IDs list (you can extend to all)
protein_ids = [
    "Q9C690", "Q9M352", "Q9LF09", "Q93V56", "P59169"
]

# SPARQL query template
query_template = """
PREFIX up: <http://purl.uniprot.org/core/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX uniprot: <http://purl.uniprot.org/uniprot/>

SELECT ?uniprotID ?proteinName ?speciesName ?goTerm ?goTermName
WHERE {{
  VALUES ?protein {{ {protein_list} }}
  
  OPTIONAL {{ ?protein up:recommendedName/up:fullName ?proteinName . }}
  OPTIONAL {{ ?protein up:organism/rdfs:label ?speciesName . }}
  OPTIONAL {{ 
    ?protein up:classifiedWith ?goTerm .
    ?goTerm rdfs:label ?goTermName .
  }}
  
  BIND(REPLACE(STR(?protein), "^.*uniprot/", "") AS ?uniprotID)
}}
ORDER BY ?uniprotID
"""

protein_list = " ".join([f"uniprot:{pid}" for pid in protein_ids])
query = query_template.format(protein_list=protein_list)

sparql = SPARQLWrapper(endpoint_url)
sparql.setQuery(query)
sparql.setReturnFormat(JSON)

results = sparql.query().convert()

for result in results["results"]["bindings"]:
    print({
        "UniProtID": result.get("uniprotID", {}).get("value", ""),
        "ProteinName": result.get("proteinName", {}).get("value", ""),
        "Species": result.get("speciesName", {}).get("value", ""),
        "GOTerm": result.get("goTerm", {}).get("value", ""),
        "GOTermName": result.get("goTermName", {}).get("value", "")
    })
