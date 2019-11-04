import eel
import os
from .fsr_api import FileSystemRetrieval
from .latent_semantic import LatentSemanticModel
from .vector_space import VectorSpaceModel

retrieval_system = None

@eel.expose
def use_model(model):
    print("Loading model...")
    if model == 'vector':
        use_vector_model()
    else:
        use_lsi_model()        
    print("Model loaded!")

@eel.expose
def check_loaded():
    if retrieval_system:
        return True
    return False

def use_vector_model():
    global retrieval_system
    retrieval_system = FileSystemRetrieval(VectorSpaceModel())

def use_lsi_model():
    global retrieval_system
    retrieval_system = FileSystemRetrieval(LatentSemanticModel(100))
   
@eel.expose
def change_directory(new_dir):
    global retrieval_system
    # print(new_dir)
    return retrieval_system.index_directory(new_dir)

@eel.expose
def validate_dir(dir):
    is_valid = os.path.isdir(dir)
    print(is_valid)
    return is_valid

@eel.expose
def query(keywords):
    global retrieval_system
    rank = retrieval_system.query_directory(keywords)
    print("Ranked documents!")
    print("Returning query result.")
    print(rank)
    return rank
