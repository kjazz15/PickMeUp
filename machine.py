from sklearn.pipeline import Pipeline
import dill as pickle
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import TruncatedSVD
from sklearn import metrics
import nltk
import csv
from nltk.stem.porter import PorterStemmer
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.multiclass import OneVsOneClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
import numpy as np


stemmer = PorterStemmer()
def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
	stemmed_item = stemmer.stem(item)
	'''
	newstring = ""
	for each_letter in stemmed_item:
		if each_letter.isalpha():
			newstring +=each_letter
	'''
	if len(stemmed_item) > 2:
        	stemmed.append(stemmed_item)
    return stemmed


def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    return stems

def save_classifier(current_classifier, filename='data/classifier1'):
	with open(filename, 'wb') as f:
		pickle.dump(current_classifier, f)

def open_classifier(filename='data/classifier1'):
	with open(filename, 'rb') as f:
		return pickle.load(f)
class Machine:
	def __init__(self):
		self.x = []
		self.y = []
		self.x_t = []
		self.y_t = []


	def get_data(self, dataset='train21'):
		x = []
		y = []
		with open('./data/'+dataset, 'r') as f:
			for row in f:
				if list(row) != ['\n']:
					line_split = row.split(';')
					y.append(line_split[0].rstrip())
					x.append(line_split[1].rstrip())
		return x, y 

	def make_classifier(self): 
		self.x, self.y = self.get_data()
		self.x_t, self.y_t = self.get_data('test')

		classifier = Pipeline([
			#('vectorizer', CountVectorizer(analyzer='word',strip_accents='unicode', stop_words='english', binary=True )),
    			('tfidf', TfidfVectorizer(ngram_range=(1,2), tokenizer=tokenize, analyzer='word')),
    			#('scaler', StandardScaler(with_mean=False)),
    			#('reduce', TruncatedSVD(n_components=15)),
    			#('tfidf', TfidfTransformer()),
    			('clf', MultinomialNB())])

		self.classifier = classifier.fit(self.x, self.y)
	
	def predict(self, vector):
		return self.classifier.predict(vector)
			
if __name__ == "__main__": 
    man = Machine() 
    classifier = open_classifier()
    x_test, y_test = man.get_data('test')
    y_classified = classifier.predict(x_test)
    print max(classifier.predict_proba(['i fucking hate you']).toarray())
    print max(classifier.predict_proba(['but i love you']).toarray())
    print max(classifier.predict_proba(['i really hate keagan']).toarray())

    print accuracy_score(y_test, y_classified)
