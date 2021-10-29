# Sinhala_SL_Crickerters_Search_App_ElasticSearch
 Sinahala SL crickerters Search Application ElasticSearch
 
## Usage
1. Start Elastic Search 
   Download -> https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html
2. create python virtual environment - > https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
3. install elasticsearch -> https://pypi.org/project/elasticsearch/
4. install Flask -> pip install Flask

## Corpus 
The Corpus contain following fields ,
1. Full name
2. Born ( Birthday and Birth Place)
3. Batting Style
4. Bowling Style
5. Carrer

## Data 
* Original data -> crickerters.csv
* Translated data -> crickerters_sinhala_2.csv
* Data transfer to the elasticsearch -> data_translation.py

## Indexing technique
Elasticsearch analysers are used in indexing.

## Main Use Cases
1. Search by term
* search by Name -> /searchBy/name
  you can search by crickerters names such as දුලීප් මෙන්ඩිස් , අර්ජුන රණතුංග
* search by Born -> /searchBy/born
  you can search born year such as 1969 , අගෝස්තු 12 or born place කොළඹ
2. Search by range
* you can search year ranges like from 1969 to 1970 -> /searchBy/bd

3. Multi search -> /search
### you can search quries like, 
* 1963 ක්රීඩා කළ දකුණත් පිතිකරැවන් සහා දකුණත් මන්දගාමී පන්දු යවන්නන්
* 1988 ක්රීඩා කළ කඩුලු රකින්නා

