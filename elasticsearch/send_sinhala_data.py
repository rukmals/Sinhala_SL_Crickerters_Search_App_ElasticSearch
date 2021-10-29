#import urllib2
#import json
import pandas as pd
from elasticsearch import Elasticsearch , helpers

es = Elasticsearch([{'host': 'localhost', 'port':1900}])

es = Elasticsearch()

df = pd.read_csv('E:\Flask_Apps\web app\corpus\crickerters_sinhala_2.csv')
#URL = "http://54.172.47.106:9200/songs/song/"

check = []

for i in range(len(df['Full Name'])):
    player_obj = {
                        "Full_Name" :df['Full Name'][i],
                        "Born" : df['Born'][i],
                        "Age" : df['Age'][i],
                        "Batting_Style" : df['Batting Style'][i],
                        "Bowling_Style" : df['Bowling Style'][i],
                        "Carrer" : df['Carrer'][i]
                }
    #print(player_obj)
    res = es.index(index="sl_cricketers", doc_type="sentences", id=i+1, body=player_obj)
    print(res)