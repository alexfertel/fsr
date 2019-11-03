# fsr

File System Retrieval

# Information Retrieval Model

This information retrieval system uses the **Latent Semantic Indexing Model**.

The main idea in this model is to map each document and query vector into a lower dimensional space which is associated with concepts.

This is accomplished by mapping the index term vectors into this lower dimensional space.

For further details on this model, please refer to [here](https://nlp.stanford.edu/IR-book/html/htmledition/latent-semantic-indexing-1.html).

# Requirements

The following Python packages are required:

* eel
* nltk
* scipy
* numpy
* scikit-learn
* pdfminer3

In addition, the *wordnet* lemmatizer and the stopwords from the *nltk* package need to be installed separately by executing the following instructions in a Python shell:

```python
nltk.download('wordnet')
nltk.download('stopwords')
```

# Running it

To run it, use:

```python
python3 main.py
```



