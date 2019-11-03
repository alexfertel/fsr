from .term_doc_matrix import tfidf as term_doc_matrix
from .preprocessing import pre_process
from collections import defaultdict
from sklearn.decomposition import TruncatedSVD
import numpy as np


class LatentSemanticModel:
    def __init__(self, s, tfidf_table=None, vocabulary=None, idf_weights=None):
        # Precomputed indices can be retrieved from local storage and passed to this model
        if tfidf_table and vocabulary and idf_weights:
            self.tfidf_table = tfidf_table
            self.vocabulary = vocabulary
            self.idf_weights = idf_weights
        
        # The dimensionality of a reduced concept space (percentage)
        self.s = s

    def index(self, documents):
        'Create indices for the documents'
        self.tfidf_table, self.vocabulary, self.idf_weights = term_doc_matrix(documents)

    def query(self, query_doc):
        '''
        Return the ranks of all documents with respect to the query in non-increasing order.
        The documents are denoted by its index in the document list passed to the .index method.
        The similarity values are also included.
        
        i.e: sorted list of (similarity, document_index)
        '''

        # Preprocess the query
        query_tokens = pre_process(query_doc)
        
        # Add the query to the term-doc matrix
        query_col = [0] * len(self.vocabulary)
        freq = defaultdict(int)
        for item in query_tokens: 
            freq[item] += 1
        for token in query_tokens:
            if token in self.vocabulary:
                index = self.vocabulary.index(token)
                query_col[index] = freq[token] * self.idf_weights[index] 
        term_doc_matrix = np.insert(self.tfidf_table.todense(), 0, query_col, axis=0)

        # Apply SVD decomposition and reduce dimensions of concept space
        reduced_dimension = min(self.s, len(self.vocabulary)-1)
        svd = TruncatedSVD(n_components=reduced_dimension, algorithm='arpack')
        term_doc_matrix = svd.fit_transform(term_doc_matrix)

        # Compute document-to-document matrix and sort rank of all documents with respect to the query
        similarity_matrix = term_doc_matrix @ term_doc_matrix.T
        results = [(similarity_matrix[0,j], j-1) for j in range(1, similarity_matrix.shape[1])]
        results.sort(reverse=True)

        return results