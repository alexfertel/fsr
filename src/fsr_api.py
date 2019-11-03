from .text_extractor import extract_text

class FileSystemRetrieval:
    def __init__(self, retrieval_model):
        """
        Information Retrieval System using the local file system as database
        :param: retrieval_model: Instance of an information retrieval model with 2 methods: index & query.
        """
        self.retrieval_model = retrieval_model

    def index_directory(self, path):
        """
        Process and index the files located inside the directory determined by path.
        """
        # Extract text documents located in the directory
        documents = extract_text(path)

        # Save the path of documents so they can be used as results of a query
        self.doc_paths = [doc_path for (doc_path, _) in documents]

        # Tell retrieval model to index the documents
        texts = [text for (_, text) in documents]
        self.retrieval_model.index(texts)

    def query_directory(self, keywords):
        """
        Returns the paths of documents, sorted by the relevance of the document with respect to the query.
        """
        return [self.doc_paths[doc_index] for (_, doc_index) in self.retrieval_model.query(keywords)]