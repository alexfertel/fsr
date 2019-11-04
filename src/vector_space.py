from .term_doc_matrix import tfidf as term_doc_matrix
from .preprocessing import pre_process, stop_words
from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


class VectorSpaceModel:
    def index(self, documents):
        'Create indices for the documents'
        self.vectorizer = TfidfVectorizer(min_df=1, analyzer=pre_process, stop_words=stop_words)
        self.tfidf = self.vectorizer.fit_transform(documents)

    def query(self, query_doc):
        '''
        Return the ranks of all documents with respect to the query in non-increasing order.
        The documents are denoted by its index in the document list passed to the .index method.
        The similarity values are also included.
        
        i.e: sorted list of (similarity, document_index)
        '''
        
        # Add the query to the term-doc matrix
        query_tfidf = self.vectorizer.transform([query_doc])

        # Compute cosine similarity
        cos_similarity = cosine_similarity(query_tfidf, self.tfidf)

        # Sort documents using similarity with respect to the query
        results = [(cos_similarity[0,j], j) for j in range(cos_similarity.shape[1])]
        results.sort(reverse=True)

        return results