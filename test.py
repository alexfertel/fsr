from src.fsr_api import FileSystemRetrieval
from src.term_doc_matrix import tfidf
from src.evaluation import *
from src.latent_semantic import LatentSemanticModel
import os
import json
import pprint

if __name__ == "__main__":
    # read query file
    path = os.getcwd() + '/corpus/query.txt'
    with open(path, 'r') as myfile:
        data = myfile.read()

    query = json.loads(data)
    corpus_folder = '/corpus/medicina_docs'
    top = []

    # # FSR API test
    f = FileSystemRetrieval(LatentSemanticModel(100))
    f.index_directory(os.getcwd() + corpus_folder)
    ranking = f.query_directory(query[0]["Text"])

    # Numero de respuestas que se quieren
    # Esto es necesario para calcular las medidas asi que es obligado entrarlo
    retrieved_documents = int(input("Cuantas respuestas desea: \n"))

    # Me quedo con los primero R del ranking
    for i in range(retrieved_documents):
        top.append((ranking[i].split("/")[-1]).split("\\")[-1])

    #####################
    # Evaluation Tester #
    #####################
    relevant_retrieved_doc = 0  # total de documentos recuperados que son relevantes
    relevant_docs = len(query[0]["RelevantDocuments"])  # total de documentos relevantes reales

    # Cuantos documentos son relevantes de los seleccionados
    for retri_doc in top:
        if retri_doc in query[0]["RelevantDocuments"]:
            relevant_retrieved_doc += 1

    # print(relevant_retrieved_doc)

    # Relevant Documents
    print("Relevants Documents: ")
    print(query[0]["RelevantDocuments"])

    # Retrived Documents
    print("Retrieved Documents: ")
    print(top)

    # Precision Test
    print("Precision Test: ")
    print(precision(relevant_retrieved_doc, retrieved_documents))

    # Recall Test
    print("Recall Test: ")
    print(recall(relevant_retrieved_doc, relevant_docs))

    # F-measure Test
    print("F-measure Test: ")
    print(f_measure(relevant_retrieved_doc, relevant_docs, retrieved_documents, beta=0.5))

    # F-measure Test
    print("F1-measure Test: ")
    print(f_measure(relevant_retrieved_doc, relevant_docs, retrieved_documents))

    # R-precision
    print("R-precision Test: ")
    print(r_precision(relevant_retrieved_doc, relevant_docs))
