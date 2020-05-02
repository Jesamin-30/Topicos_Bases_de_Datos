import spacy
import nltk
from nltk import SnowballStemmer
nlp = spacy.load('es_core_news_sm')


####--------------Stemming-----####
def normalize(text):
    doc = nlp(text)
    print (doc)
    words = [t.orth_ for t in doc if not t.is_punct] # Crea lista con las palabras del texto y elimina puntos
    lexical_tokens = [t.lower() for t in words if len(t)>=1 and t.isalpha()]
    return lexical_tokens


def stemming(text):
    spanish_stemmer=SnowballStemmer('spanish')
    tokens = normalize(text)

    stems= [spanish_stemmer.stem(token) for token in tokens]
    return stems
###########################################

####---------------Lematizacion-----####
def lematization(text):
    doc = nlp(text)
    lemmas = [tok.lemma_.lower() for tok in doc if not tok.is_punct]

    return lemmas
       
################################################
