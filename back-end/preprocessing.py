from nltk.stem import WordNetLemmatizer 
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

# Create Lemmatizer
lemmatizer = WordNetLemmatizer() 

# Create tokenizer
tokenizer = RegexpTokenizer("\w+")

# Spanish stop words list
stop_words = stopwords.words('english')


def lemma_tokenizer(text):
   '''
   Custom tokenizer for sklearn's tfidfVectorizer
   Tokens are lemmatized
   '''
   
   # Tokenize document
   tokens = tokenizer.tokenize(text)

   # Loop through tokens and lemmatize them
   for i in range(len(tokens)):
      word = tokens[i]
      if word.lower() not in stop_words:
         tokens[i] = lemmatizer.lemmatize(word.lower())

   return tokens