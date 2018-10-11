# BookMark
## - Book Aggregator and Meta Search Engine
--- 
Helping user to find meta data about book from an aggregated data source.

# DATA PIPELINE
![](https://github.com/MariaChowdhury/BookMark/blob/master/pipeline.png)
---
# Data:
Data is collected from different sources such as Kaggle, http://onlinebooks.library.upenn.edu/  and Project Gutenberg
---
# Data Processing:
The data is processed using Spark.
---
# Database:
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
---
# Front End:
Flask is used as the front end for Elasticsearch. 
