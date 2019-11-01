from nltk.stem import WordNetLemmatizer 
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

# Create Lemmatizer
lemmatizer = WordNetLemmatizer() 

# Create tokenizer
tokenizer = RegexpTokenizer("\w+")

# Spanish stop words list
stop_words = stopwords.words('english')


def pre_process(text):
   '''
   Returns document as a token list 
   The tokens are lemmatized and stop words are removed
   '''
   
   # Tokenize document
   tokens = tokenizer.tokenize(text)

   # Loop through tokens, convert to lower case,
   # remove Stop Words and apply lemmatization
   words = []
   for word in tokens:
      w = word.lower()
      if w in stop_words:
         continue
      words.append(lemmatizer.lemmatize(w))

   return words