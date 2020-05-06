import warnings
import numpy
import pandas as pd
import re
import nltk
from nltk.tokenize import sent_tokenize ,word_tokenize
from nltk.stem import WordNetLemmatizer    #links words with similar meaning to one word
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
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
stop_words = set(stopwords.words('english')) 


app=flask.Flask(__name__)
app.config["DEBUG"]=True


'''@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')'''

@app.route('/', methods=['POST']) #GET requests will be blocked
def json_example():
    req_data = request.get_json()
    #json is formatted as list, so we choose 1st element from list
    url_n1 = req_data 
    return '''
           The 1st url is: {}
           '''.format(url_n1) 

@app.route('/lower', methods=["GET", "POST"])
def lower_case():
    text1 = request.form['text']
    word = text1.lower()
    result = {
        "result": word
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

@app.route('/sent_tokenize', methods=["GET", "POST"])
def sent_tokenize():
    text = request.form['text']
    sent_tokenize = nltk.sent_tokenize(text)
    result = {
        "result": str(sent_tokenize) #remove str() if you want the output as list
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

@app.route('/word_tokenize', methods=["GET", "POST"])
def word_tokenize():
    text = request.form['text']
    word_tokenize = nltk.word_tokenize(text)
    result = {
        "result": str(word_tokenize) #remove str() if you want the output as list
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

@app.route('/spell_check', methods=["GET", "POST"])
def spell_check():
    text = request.form['text']
    spells = [spell(w) for w in (nltk.word_tokenize(text))]
    result = {
        "result": " ".join(spells)
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

@app.route('/lemmatize', methods=["GET", "POST"])
def lemmatize():
    from nltk.stem import WordNetLemmatizer
    wordnet_lemmatizer = WordNetLemmatizer()

    text = request.form['text']
    word_tokens = nltk.word_tokenize(text)
    lemmatized_word = [wordnet_lemmatizer.lemmatize(word) for word in
                       word_tokens]
    result = {
        "result": " ".join(lemmatized_word)
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

@app.route('/stemming', methods=["GET", "POST"])
def stemming():
    from nltk.stem import SnowballStemmer
    snowball_stemmer = SnowballStemmer('english')

    text = request.form['text']
    word_tokens = nltk.word_tokenize(text)
    stemmed_word = [snowball_stemmer.stem(word) for word in word_tokens]
    result = {
        "result": " ".join(stemmed_word)
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

@app.route('/remove_tags', methods=["GET", "POST"])
def remove_tags():
    import re
    text = request.form['text']
    cleaned_text = re.sub('<[^<]+?>', '', text)
    result = {
        "result": cleaned_text
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)


@app.route('/remove_numbers', methods=["GET", "POST"])
def remove_numbers():
    text = request.form['text']
    remove_num = ''.join(c for c in text if not c.isdigit())
    result = {
        "result": remove_num
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

@app.route('/remove_punct', methods=["GET", "POST"])
def remove_punct():
    from string import punctuation
    def strip_punctuation(s):
        return ''.join(c for c in s if c not in punctuation)

    text = request.form['text']
    text = strip_punctuation(text)
    result = {
        "result": text
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

@app.route('/remove_stopwords', methods=["GET", "POST"])
def remove_stopwords():
    from nltk.corpus import stopwords
    stopword = stopwords.words('english')
    text = request.form['text']
    word_tokens = nltk.word_tokenize(text)
    removing_stopwords = [word for word in word_tokens if word not in stopword]
    result = {
        "result": " ".join(removing_stopwords)
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)


@app.route("/keyword", methods=["GET","POST"])
def keyword():
    text = request.form['text']
    word = nltk.word_tokenize(text)
    pos_tag = nltk.pos_tag(word)
    chunk = nltk.ne_chunk(pos_tag)
    NE = [" ".join(w for w, t in ele) for ele in chunk if isinstance(ele, nltk.Tree)]
    result = {
        "result": NE
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)




if __name__ == '__main__':
    app.run(debug=True)       

