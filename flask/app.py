from flask import Flask
from flask import request
from flask import render_template
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch()
@app.route('/',methods=["GET","POST"])

def index():
	q=request.form.get("q")
	if q is not None:
		resp=es.search(index="my_index",doc_type="books", body={"query": { 'match': {'Title': q} }})
		return render_template('index.html',q=q,response=resp)
	return render_template('altindex.html')





if __name__ == "__main__":
    app.run(host="0.0.0.0",debug = True, port=80)
