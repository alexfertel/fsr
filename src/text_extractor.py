import os
from os.path import join, getsize
from .pdf_extractor import extract_pdfs

def extract_text(path):
    files = read_dir(path)
    # print(files)
    result = extract_txts(files['txts']) + extract_pdfs(files['pdfs'])
    print(result)
    return result

def read_dir(path):
    files = {'txts': [], 'pdfs': []}
    for root, dirs, filenames in os.walk(path):
        for name in filenames:
            if name.endswith('.txt'):
                files['txts'].append(os.path.join(root, name))
            elif name.endswith('.pdf'):
                files['pdfs'].append(os.path.join(root, name))

    return files
        
def extract_txts(files):
    extracted = []
    for f in files:
        with open(f) as fd:
            try:
                text = fd.read()
            except:
                continue
            extracted.append((f, text))
    return extracted
    

