import eel
from .fsr_api import FileSystemRetrieval
from .latent_semantic import LatentSemanticModel

retrieval_system = None

@eel.expose
def init_app():
    use_lsi_model()

@eel.expose
def use_vector_model():
    global retrieval_system
    # retrieval_system = FileSystemRetrieval(VECTOR MODEL HERE)

@eel.expose
def use_lsi_model():
    global retrieval_system
    retrieval_system = FileSystemRetrieval(LatentSemanticModel(80))
   
@eel.expose
def change_directory(new_dir):
    global retrieval_system
    # TODO: Validate directory !?

    return retrieval_system.index_directory(new_dir)

@eel.expose
def query(keywords):
    global retrieval_system
    return retrieval_system.query_directory(keywords)