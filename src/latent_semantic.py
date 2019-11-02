from .term_doc_matrix import tfidf as term_doc_matrix
from .preprocessing import pre_process
from collections import defaultdict
from scipy import linalg
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
      
      # Add the query to the tf-idf matrix
      query_col = [0] * len(self.vocabulary)
      freq = defaultdict(int)
      for item in query_tokens: 
         freq[item] += 1
      for token in query_tokens:
         if token in self.vocabulary:
            index = self.vocabulary.index(token)
            query_col[index] = freq[token] * self.idf_weights[index] 
      query_tfidf = np.insert(self.tfidf_table.todense(), 0, query_col, axis=1)

      # Apply SVD decomposition
      K,singulars,D = linalg.svd(query_tfidf, full_matrices=False)

      # Reduce dimensions of concept space
      new_dimension = int(len(singulars) * self.s / 100)
      K = K[...,0:new_dimension]
      singulars = singulars[0:new_dimension]
      S = linalg.diagsvd(singulars, new_dimension, new_dimension)
      D = D[0:new_dimension,...]
      query_tfidf = K.dot(S).dot(D)

      # Compute document-to-document matrix and sort rank of all documents with respect to the query
      doc_to_doc = query_tfidf.T.dot(query_tfidf)
      results = [(doc_to_doc[0,j], j-1) for j in range(1, doc_to_doc.shape[1])]
      results.sort(reverse=True)

      return results