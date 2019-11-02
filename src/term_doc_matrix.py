from sklearn.feature_extraction.text import TfidfVectorizer
from .preprocessing import pre_process, stop_words
import numpy as np     


def tfidf(documents):
    '''
    Returns the term-document association matrix using tf-idf as weights
    and the vocabulary 
    '''

    vectorizer = TfidfVectorizer(min_df=1, analyzer=pre_process, stop_words=stop_words)
    X = vectorizer.fit_transform(documents)
    return X.T, vectorizer.get_feature_names()


if __name__ == "__main__":
    # TESTS
    corpus = [
        'This is the first document.',
        'This document is the second document.',
        'And this is the third one.',
        'Is this the first document?',
    ]
    print(tfidf(corpus))