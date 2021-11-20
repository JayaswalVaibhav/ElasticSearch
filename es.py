from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

def search_movie(name):
    es = Elasticsearch([{'host': '192.168.0.103', 'port': 9200}])

    s = Search(using=es, index="netflix_ml")
    
    query_body = {
      "from": 0,
      "size": 20,
      "query": {
        "multi_match": {
          "query": name,
          "fields": ["title^2", "director","cast"]
        }
      }
    }

    a = es.search(index="netflix_ml", body=query_body)
    return a['hits']['hits']
