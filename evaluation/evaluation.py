"""
Evaluation for the Retrieval Information Models
"""


def precision(cnt_rr, cnt_r):
    """

    :param cnt_rr: |{relevant documents} ∩ {retrieved documents}|
    :param cnt_r: |{retrieved documents}|
    :return: Numbers of relevant retrieved documents divided by the total of retrieved documents
    """
    return cnt_rr / cnt_r


def recall(cnt_rr, cnt_r):
    """
    :param cnt_rr: |{relevant documents} ∩ {retrieved documents}|
    :param cnt_r: |{relevant documents}|
    :return: Numbers of relevant retrieved documents divided by the total of relevant documents
    """
    return cnt_rr / cnt_r


def f_measure(cnt_rr, relevant_docs, retrieved_docs, beta=1):
    """
    By default beta = 1
    :param beta:  0 <= ß <= 1
    :param cnt_rr: |{relevant documents} ∩ {retrieved documents}|
    :param relevant_docs: |{relevant documents}|
    :param retrieved_docs: |{retrieved documents}|
    :return: The F1 score is the harmonic mean of the precision and recall
    """
    p = precision(cnt_rr, retrieved_docs)
    r = recall(cnt_rr, relevant_docs)

    return (1 + beta**2) / 1/p + beta**2/r


def r_precision(ranking, cnt_rr, retrieved_documents):
    """
    :param ranking: # in the ranking of relevant documents -> R
    :param cnt_rr: |RR| # of relevant documents recovered
    :param retrieved_documents: # of retrieved documents
    :return: -
    """
    return ranking - precision(cnt_rr, ranking)
