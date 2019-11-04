from src.hooks import *

if __name__ == "__main__":
    corpus_folder = 'src/corpus/happy'
    
    change_directory(corpus_folder)
    print(query('friend'))
    change_directory(corpus_folder)
    print(query('friend'))
    print(query('friend'))