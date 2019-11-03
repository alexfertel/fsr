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

    corpus_folder = '/corpus/medicina_docs'

    # LSI Model test
    a = LatentSemanticModel(80)
    a.index(corpus)
    pprint.pprint(a.query("first document"))
     
    # TF-IDF test
    pprint.pprint(tfidf(corpus)[0])

    # FSR API test
    f = FileSystemRetrieval(LatentSemanticModel(100))
    f.index_directory(os.getcwd() + corpus_folder)
    pprint.pprint(f.query_directory('hemophilia and christmas disease, especially in regard to thespecific complication of pseudotumor formation (occurrence,pathogenesis, treatment, prognosis).'))