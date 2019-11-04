"""
Evaluation for the Retrieval Information Models
"""

def precision(cnt_rr, cnt_r):
    """
    The precision is the ratio ``tp / (tp + fp)`` where ``tp`` is the number of
    true positives and ``fp`` the number of false positives. The precision is
    intuitively the ability of the classifier not to label as positive a sample
    that is negative.
    The best value is 1 and the worst value is 0.

    :param cnt_rr: |{relevant documents} ∩ {retrieved documents}| -> Total de Documentos relevantes recuperados
    :param cnt_r: |{retrieved documents}| -> Total de documentos recuperados
    :return: Numbers of relevant retrieved documents divided by the total of retrieved documents

    When cnt_r: ``true positive + false positive == 0``, precision returns 0 and
    raises ``UndefinedMetricWarning``.
    """
    if cnt_r == 0:
        return 0

    return cnt_rr / cnt_r


def recall(cnt_rr, cnt_r):
    """
    The recall is the ratio ``tp / (tp + fn)`` where ``tp`` is the number of
    true positives and ``fn`` the number of false negatives. The recall is
    intuitively the ability of the classifier to find all the positive samples.

    The best value is 1 and the worst value is 0.

    :param cnt_rr: |{relevant documents} ∩ {retrieved documents}|
    :param cnt_r: |{relevant documents}|
    :return: Numbers of relevant retrieved documents divided by the total of relevant documents
     When cnt_r: ``true positive + false negative == 0``, recall returns 0 and raises
    ``UndefinedMetricWarning``.
    """
    if cnt_r == 0:
        return 0

    return cnt_rr / cnt_r


def f_measure(cnt_rr, relevant_docs, retrieved_docs, beta=1):
    """
    The F1 score can be interpreted as a weighted average of the precision and
    recall, where an F1 score reaches its best value at 1 and worst score at 0.
    The relative contribution of precision and recall to the F1 score are
    equal. The formula for the F1 score is::
        F1 = 2 * (precision * recall) / (precision + recall)
        this is leaving beta with the default value -> 1

    By default beta = 1
    :param beta:  0 <= ß <= 1
    :param cnt_rr: |{relevant documents} ∩ {retrieved documents}|
    :param relevant_docs: |{relevant documents}|
    :param retrieved_docs: |{retrieved documents}|
    :return: The F1 score is the harmonic mean of the precision and recall
    """
    p = precision(cnt_rr, retrieved_docs)
    r = recall(cnt_rr, relevant_docs)

    return (1 + beta ** 2) / 1 / p + beta ** 2 / r


def r_precision(cnt_rr, relevant_docs):
    """

    :param cnt_rr: Total de documentos relevantes en los primeros R del ranking
    :param relevant_docs: Total de documentos relevantes
    :return:
    """
    return cnt_rr / relevant_docs
