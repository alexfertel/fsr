from sklearn.feature_extraction.text import TfidfVectorizer
from .preprocessing import pre_process, stop_words
import numpy as np     


def tfidf(documents):
    '''
    Returns the term-document association matrix using tf-idf as weights
    and the vocabulary 
    '''

    vectorizer = TfidfVectorizer(use_idf=True, min_df=1, analyzer=pre_process, stop_words=stop_words)
    X = vectorizer.fit_transform(documents)
    return X, vectorizer.get_feature_names(), vectorizer.idf_