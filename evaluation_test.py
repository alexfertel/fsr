from src.fsr_api import FileSystemRetrieval
from src.term_doc_matrix import tfidf
from src.evaluation import *
from src.latent_semantic import LatentSemanticModel
import os
import json
import statistics
import pprint

if __name__ == "__main__":
    # read query file
    path = os.getcwd() + '/src/corpus/query.json'
    with open(path, 'r') as myfile:
        data = myfile.read()

    query = json.loads(data)
    corpus_folder = '/src/corpus/medicina_docs'
    top = {}

    # # FSR API test
    f = FileSystemRetrieval(LatentSemanticModel(100))
    f.index_directory(os.getcwd() + corpus_folder)
    # ranking = f.query_directory(query[0]["Text"])

    # Numero de respuestas que se quieren
    # Esto es necesario para calcular las medidas asi que es obligado entrarlo
    r_value = int(input("Que valor desea para R?: \n"))
    # Me quedo con los primero R del ranking
    ranking = []
    i = -1
    for elem in query:
        ranking.append(f.query_directory(elem["Text"]))
        print("Testing query with text: {}".format(elem["Text"]))

    for elem in ranking:
        i += 1
        top[i] = []
        for path, value, in elem:
            if value > 0.5:
                top[i].append((path.split("/")[-1]).split("\\")[-1])
    #####################
    # Evaluation Tester #
    #####################
    precision_data = []
    recall_data = []
    f_measure_data = []
    f1_measure_data = []
    r_precision_data = []
    for i in range(30):

        relevant_retrieved_doc = 0  # total de documentos recuperados que son relevantes
        r_precision_relevant = 0
        relevant_docs = len(query[i]["RelevantDocuments"])  # total de documentos relevantes reales

        # Cuantos documentos son relevantes de los seleccionados
        temp = 0
        for retri_doc in top[i]:
            if retri_doc in query[i]["RelevantDocuments"]:
                relevant_retrieved_doc += 1
                r_precision_relevant += 1 if r_value < temp else 0
                temp += 1

        print("relevant retrieved docs: " + str(relevant_retrieved_doc))
        print("relevant docs: " + str(relevant_docs))
        print("retrieved docs: " + str(len(top[i])))
        # Relevant Documents
        # print("Relevants Documents: ")
        # print(query[0]["RelevantDocuments"])

        # Retrived Documents
        # print("Retrieved Documents: ")
        # print(top)

        # Precision Test
        # print("Precision Test: ")
        # print(precision(relevant_retrieved_doc, retrieved_documents))
        precision_data.append(precision(relevant_retrieved_doc, len(top[i])))

        # Recall Test
        # print("Recall Test: ")
        # print(recall(relevant_retrieved_doc, relevant_docs))
        recall_data.append(recall(relevant_retrieved_doc, relevant_docs))

        # F-measure Test
        # print("F-measure Test: ")
        # print(f_measure(relevant_retrieved_doc, relevant_docs, retrieved_documents, beta=0.5))
        f_measure_data.append(f_measure(relevant_retrieved_doc, relevant_docs, len(top[i]), beta=0.5))

        # F-measure Test
        # print("F1-measure Test: ")
        f1_measure_data.append(f_measure(relevant_retrieved_doc, relevant_docs, len(top[i])))

        # R-precision
        # print("R-precision Test: ")
        r_precision_data.append(r_precision(r_precision_relevant, r_value))

    # print(precision_data)
    # print(recall_data)
    # print(f_measure_data)

    print(statistics.mean(precision_data))
    print(statistics.mean(recall_data))
    print(statistics.mean(f_measure_data))
    print(statistics.mean(f1_measure_data))
    print(statistics.mean(r_precision_data))
