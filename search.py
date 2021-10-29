from re import search
from elasticsearch import Elasticsearch , helpers

es = Elasticsearch([{'host': 'localhost', 'port':1900}])

es = Elasticsearch()


def get_search_results_by_name(token):
    body = {
        "from":0,
        "size":3,
        "query": {
            "match": {
                "Full_Name":token
            }
        }
    }

    res = es.search(index="sl_cricketers", body=body)
    return res
def get_search_results_by_born(token):
    body = {
        "from":0,
        "size":3,
        "query": {
            "match": {
                "Born":token
            }
        }
    }

    res = es.search(index="sl_cricketers", body=body)
    return res

def get_search_results_by_birth_day(to , from_d):
    body = {
        "from":0,
        "size":3,
        "query": {
            "range": {
                "Born" :{
                    "lt": to,
                    "gt": from_d
                }
            }
        }
    }

    res = es.search(index="sl_cricketers", body=body)
    return res


def get_multi_search_results(phrase):

    token  = phrase.strip().split(" ")

    frequent_words = ["ක්රීඩා","කළ","කල","ක්රීඩකයන්", "පන්දු" ,"යවන්නන්","සහා","හා"]

    print(token)
    for word in token:
        if word in frequent_words:
            token.remove(word)
    search_token = " ".join(token)
    search_token = search_token.replace("පිතිකරැවන්", "පිතිකරණය")
    search_token = search_token.replace("දකුණත්", "දකුණු අත")
    search_token = search_token.replace("වමත්", "වම් අත")
    print(search_token)
    body = {
            "from":0,
            "size":20,
            "query": {
                "multi_match" : {
                    "query":   search_token, 
                    "type" : "most_fields",
                    "fields": ["Born","Carrer","*_Style"],
                    "operator":   "or"
                }
            },
            "aggs":{
                "Born Filter":{
                    "terms":{
                        "field":"Born.keyword",
                        "size":10
                    }
                },
                "Name Filter":{
                    "terms":{
                        "field":"Full_Name.keyword",
                        "size":10
                    }
                },
                "Carrer Filter":{
                    "terms":{
                        "field":"Carrer.keyword",
                        "size":10
                    }
                },
                "Batting Style Filter":{
                    "terms":{
                        "field": "Batting_Style.keyword",
                        "size":10
                    }
                },
                 "Bowling Style Filter":{
                    "terms":{
                        "field": "Bowling_Style.keyword",
                        "size":10
                    }
                }

            }
         }
    res = es.search(index="sl_cricketers", body=body)
    #print(res)
    return res
#aggregation = res['aggregations']
#hits = res['hits']['hits']
#num_results = len(hits)

#print(hits)
#print(num_results)
#res = es.get(index="sl_cricket", doc_type="sentences", id=1)

#print(res)