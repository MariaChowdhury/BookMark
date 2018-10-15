# BookMark
## - Book Aggregator and Meta Search Engine
 
Helping user to find meta data about book from an aggregated large scale data source. It allows people to provide search query and retrieve the desired result very fast. 

# DATA PIPELINE
![](https://github.com/MariaChowdhury/BookMark/blob/master/pipeline.png)

# Data:
Data is collected from different sources such as Kaggle, http://onlinebooks.library.upenn.edu/ and archived in to Amazon S3.

# Data Processing:
The data is processed using Spark to inject to data storage.

# Database:
Elastichsearch is used to store the data for fast retrieval.

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

# Front End:
Flask is used as the front end for Elasticsearch for user interaction.

# Presentation Link
---
https://docs.google.com/presentation/d/e/2PACX-1vTtJ7FquWDB7wQs4kiEwy9o-bUp6uo7fvyyrtDS4Zo8m3ZvLcNGGR3nOzm25hGmvc0K0MFqjgoZkeVG/pub?start=false&loop=false&delayms=3000
