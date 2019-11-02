from src.fsr_api import FileSystemRetrieval
from src.term_doc_matrix import tfidf
from src.latent_semantic import LatentSemanticModel
import os

if __name__ == "__main__":
   corpus = [
      'This is the first document.',
      'This document is the second document.',
      'And this is the third one.',
      'Is this the first document?',
   ]


   # LSI Model test
   # a = LatentSemanticModel(80)
   # a.index(corpus)
   # print(a.query("first"))
    
   # # TF-IDF test
   # print(tfidf(corpus)[0])

   # FSR API test
   # f = FileSystemRetrieval(LatentSemanticModel(100))
   # f.index_directory(os.getcwd()+'/a')
   # print(f.query_directory('first'))