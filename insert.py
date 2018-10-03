#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 09:28:09 2018

@author: mariachowdhury
"""
from tqdm import tqdm
#import csv
#data_path="/Users/mariachowdhury/Downloads/Parser/online_books.json"
import json


from tqdm import tqdm
from elasticsearch import Elasticsearch, helpers
from pprint import pprint
from time import time
import json
import pdb
import sys

if __name__ == "__main__":
    es = Elasticsearch()
    actions = []
    data_path = sys.argv[1]

    body = json.loads("""{
      "mappings": {
          "properties": {
            "Title": {
              "type": "keyword"
            },
	    "Year":{
	     "type":"keyword" 
	  },
	   "Author":{
	    "type":"keyword"
	  }
          }
        }
      }
    """)

#    es.indices.create(index="books", body=body)



    data=[]
          
    for i, line in tqdm(enumerate(open(data_path))):

        items = json.loads(line)
	print items

        data.append({
            "_index": "books",
            "_type": "book",
            "_source": {
                "Title": items[ "Title"],
		"Year": items["Year"],
                "Author": items["Author"],
            }
        })
    

        if len(data) == 10:
            t0 = time()
            helpers.bulk(es, data)
            actions = []
            print("%d: inserted in %d seconds" % (i, time() - t0))
    
    helpers.bulk(es, data)
    data = []
