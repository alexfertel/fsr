from src.fsr_api import FileSystemRetrieval
from src.term_doc_matrix import tfidf
from src.latent_semantic import LatentSemanticModel
import os
import pprint

if __name__ == "__main__":
    corpus = [
        'This is the first document.',
        'This document is the second document.',
        'And this is the third one.',
        'Is this the first document?',
    ]

    # corpus_folder = 'src/corpus/medicina docs [BIG]'
    corpus_folder = '/home/alex/code/simulations/kojo/paper'

    # LSI Model test
    # a = LatentSemanticModel(100)
    # a.index(corpus)
    # pprint.pprint(a.query("first document"))
     
    # # TF-IDF test
    # pprint.pprint(tfidf(corpus)[0].todense())

    # # FSR API test
    f = FileSystemRetrieval(LatentSemanticModel(100))
    f.index_directory(corpus_folder)
    # pprint.pprint(f.query_directory('hemophilia and christmas disease, especially in regard to the specific complication of pseudotumor formation (occurrence,pathogenesis, treatment, prognosis).'))
    pprint.pprint(f.query_directory('mejora'))