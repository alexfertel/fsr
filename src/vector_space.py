from .term_doc_matrix import tfidf as term_doc_matrix
from .preprocessing import pre_process, stop_words
from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


class VectorSpaceModel:
    def __init__(self):
        pass
    
    def index(self, documents):
        """
        Create indices for the documents
        """
        self.vectorizer = TfidfVectorizer(min_df=1, analyzer=pre_process, stop_words=stop_words)
        self.tfidf = self.vectorizer.fit_transform(documents)

    def query(self, query_doc):
        """
        Return the ranks of all documents with respect to the query in non-increasing order.
        The documents are denoted by its index in the document list passed to the .index method.
        The similarity values are also included.
        
        i.e: sorted list of (similarity, document_index)
        """

        print(query_doc)
        # Add the query to the term-doc matrix
        query_tfidf = self.vectorizer.transform([query_doc])

        # Sort documents using similarity with respect to the query
        pairwise_similarity = query_tfidf * self.tfidf.T 
        arr = pairwise_similarity.toarray()
        row = arr[0]
        length = self.tfidf.shape[0]
        ind = np.argpartition(row, -length)[-length:]
        ind = ind[np.argsort(row[ind])]
        ind = np.flip(ind)

        return [(row[i], i) for i in ind]