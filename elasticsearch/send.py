from elasticsearch import Elasticsearch , helpers

es = Elasticsearch([{'host': 'localhost', 'port':1900}])

es = Elasticsearch()

doc_1 = {"sentence":"Hack COVID-19 is amazing!"}
doc_2 = {"sentence":"Hack-Quarantine is stunning!"}
doc_3 = {"sentence":"Hack is Amazing"}
doc_list = [doc_1, doc_2,doc_3]
for i in range(len(doc_list)):
    res = es.index(index="english", doc_type="sentences", id=i+1, body=doc_list[i])
    #res = es.index(index="cities", doc_type="places", id=i, body=doc_list[i])
    print(res)

