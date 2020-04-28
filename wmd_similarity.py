import warnings
import numpy
import gensim
import pandas as pd
from gensim import corpora, models
from gensim.models import Word2Vec 
import nltk
from nltk.tokenize import sent_tokenize ,word_tokenize
from nltk.stem import WordNetLemmatizer    #links words with similar meaning to one word
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
import scipy
import flask
import json
from flask import Flask, request, jsonify, render_template


import gensim.downloader as api
word_vectors = api.load("glove-wiki-gigaword-100")  # load pre-trained word-vectors from gensim-data

app=flask.Flask(__name__)
app.config["DEBUG"]=True

@app.route('/predict',methods=['POST'])
def predict():
	data=request.form["keywords"]
	data2=request.form["contents"]
	similarity = word_vectors.wmdistance(data, data2)
	print("score between keywords and contents: {:.6f}".format(similarity))
	result = {
		"keywords":data,
		"contents":data2,
        "similarity between keywords and contents are ": similarity
    }
	return jsonify(result=result)


if __name__ == "__main__":
    app.run(debug=True)
