import eel
from .fsr_api import FileSystemRetrieval
from .latent_semantic import LatentSemanticModel

retrieval_system = None

@eel.expose
def use_model(model):
    print("Loading model...")
    if model == 'vector':
        use_vector_model()
    else:
        use_lsi_model()        
    print("Model loaded!")

def use_vector_model():
    global retrieval_system
    # retrieval_system = FileSystemRetrieval(VECTOR MODEL HERE)

def use_lsi_model():
    global retrieval_system
    retrieval_system = FileSystemRetrieval(LatentSemanticModel(80))
   
@eel.expose
def change_directory(new_dir):
    global retrieval_system
    # TODO: Validate directory !?
    
    if not retrieval_system:
        retrieval_system = FileSystemRetrieval(LatentSemanticModel(80))
    return retrieval_system.index_directory(new_dir)

@eel.expose
def query(keywords):
    global retrieval_system
    rank = retrieval_system.query_directory(keywords)
    print("Ranked documents!")
    print("Returning query result.")
    return rank