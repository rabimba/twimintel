import warnings
import gensim
from gensim import corpora, models
from gensim.models import Word2Vec 
import scipy
import flask
import json
from flask import Flask, request, jsonify, render_template
import gensim.downloader as api
word_vectors = api.load("glove-wiki-gigaword-100")  # load pre-trained word-vectors from gensim-data

data_format={
    "keywords": 
        {
            "text": "mona "
        },
        
   
    "contents":
        {
        
            "text": "darling"
        }
}

app=flask.Flask(__name__)
app.config["DEBUG"]=True

@app.route('/predict',methods=['POST'])
def predict():
	text = request.get_json()
	text1 = str(text['keywords'])
	text2 = str(text['contents'])
	similarity = word_vectors.wmdistance(text1,text2)
	print("score between keywords and contents: {:.4f}".format(similarity))
	result = {"similarity between {} and {} are  ".format(text1,text2): similarity}
	result = {str(key): value for key, value in result.items()}
	return jsonify(result=result)


if __name__ == "__main__":
    app.run(debug=True)