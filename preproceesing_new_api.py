import warnings
import numpy
import pandas as pd
import re
import nltk
from nltk.tokenize import sent_tokenize ,word_tokenize
from nltk.stem import WordNetLemmatizer    #links words with similar meaning to one word
from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
from string import punctuation
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
import sklearn
import scipy
from scipy import spatial
import flask
from flask import request, jsonify
import json
nltk.download('stopwords')
stopword = set(stopwords.words('english')) 
import numpy as np

app=flask.Flask(__name__)
app.config["DEBUG"]=True
 

@app.route('/', methods=["GET", "POST"])
def lower_case():
    text = request.get_json()
    text1 = str(text['data'])
    
    word1 = text1.lower()
    def sent_tokenizer():
        sent_tokenize = nltk.sent_tokenize(text1)
        return sent_tokenize

    def word_tokenizer():
        word_tokenize = nltk.word_tokenize(text1)
        return word_tokenize
    def lemmatize():
        wordnet_lemmatizer = WordNetLemmatizer()
        word_tokens = nltk.word_tokenize(text1)
        word_tokens = re.sub("[^a-zA-Z]",  # Search for all non-letters
                              " ",          # Replace all non-letters with spaces
                              str(word_tokens) )    # Column and row to search    

        lemmatized_word = [wordnet_lemmatizer.lemmatize(word) for word in
                           word_tokens]
        
        return lemmatized_word

    def stemming():
    
        snowball_stemmer = SnowballStemmer('english')
        word_tokens = nltk.word_tokenize(text1)
        word_tokens = re.sub("[^a-zA-Z]",  # Search for all non-letters
                              " ",          # Replace all non-letters with spaces
                              str(word_tokens) )    # Column and row to search    

        stemmed_word = [snowball_stemmer.stem(word) for word in str(word_tokens)]
        
        
        return stemmed_word

    def remove_tags():
        cleaned_text = re.sub('<[^<]+?>', '', text1)
        return cleaned_text

    def remove_numbers():
        remove_num = ''.join(c for c in text if not c.isdigit())
        return remove_num

    def remove_punct():
        def strip_punctuation(s):
            return ''.join(c for c in s if c not in punctuation)
        text = strip_punctuation(text1)
        
        return text

    def remove_stopwords():
        word_tokens = nltk.word_tokenize(text1)
        removing_stopwords = [word for word in word_tokens if word not in stopword]
        return removing_stopwords

    def keyword():
        word = nltk.word_tokenize(text1)
        pos_tag = nltk.pos_tag(word)
        chunk = nltk.ne_chunk(pos_tag)
        NE = [" ".join(w for w, t in ele) for ele in chunk if isinstance(ele, nltk.Tree)]
        return NE

    result = {
        "lower": word1,
        "sent_tokenizerr": sent_tokenizer(),
        "word_tokenizerr": word_tokenizer(),
        "result": " ".join(lemmatize()),
        "stemming": " ".join(stemming()),
        "remove_tags": remove_tags(),
        "remove_numbers":remove_numbers(),
        "remove_punct":remove_punct(),
        "remove_stopwords": " ".join(remove_stopwords()),
        "result": keyword()

        
    
    }
    
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)       

