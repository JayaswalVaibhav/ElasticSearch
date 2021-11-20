from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search


# user_request = "Wanted"
# query_body = {
#     "query": {
#         "bool": {
#             "must": [{
#                 "match": {
#                     "title": user_request
#                 }}]
#         }
#     }
# }


# query_body = {
#   "query": {
#     "bool": {
#       "must": [{
#         "match": {
#           "title": user_request
#         }},
#         {"match": {
#           "director": user_request
#         }}]
#       }
#     }
#   }


def search_movie(name):
    es = Elasticsearch([{'host': '192.168.0.103', 'port': 9200}])

    s = Search(using=es, index="netflix_ml")
    # query_body = {
    #     "query": {
    #         "bool": {
    #             "must": [{
    #                 "match": {
    #                     "title": name
    #                 }}]
    #         }
    #     }
    # }
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

    # query_body = {
    #         "_source": [],
    #         "size": 0,
    #         "min_score": 0.5,
    #         "query": {
    #             "bool": {
    #                 "must": [
    #                     {
    #                         "match_phrase_prefix": {
    #                             "title": {
    #                                 "query": "{}".format(name)
    #                             }ls

    #                         }
    #                     }
    #                 ],
    #                 "filter": [],
    #                 "should": [],
    #                 "must_not": []
    #             }
    #         },
    #         "aggs": {
    #             "auto_complete": {
    #                 "terms": {
    #                     "field": "title.keyword",
    #                     "order": {
    #                         "_count": "desc"
    #                     },
    #                     "size": 25
    #                 }
    #             }
    #         }
    #     }
    a = es.search(index="netflix_ml", body=query_body)
    return a['hits']['hits']

# print("query hits:", len(ans["hits"]["hits"]))
# hits = ans["hits"]["hits"]
#
# for num, doc in enumerate(hits):
#     print("Title: {} and Director: {}".format(doc['_source']['title'], doc['_source']['director']))
