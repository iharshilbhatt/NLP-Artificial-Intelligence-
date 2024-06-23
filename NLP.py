# -*- coding: utf-8 -*-
"""AI NLP.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xLhWRYvErw726Upz1n5xl7yqX9Td4n2i

LAB 5 basics of NLP
"""

import spacy
import nltk

text = "Hello This is Harshil Bhatt from B.tech ICT Sem 6 TK2"

text[3]

type(text)

nlp=spacy.load("en_core_web_sm")

doc=nlp(text)

type(doc)

doc[3]

type(doc[3])

#noun chunks or noun phrases
for phrases in doc.noun_chunks:
  print(phrases)

doc

text1 = "yesterday West Indies beat Australia in Australia in a Test Match after 27 Years"

doc_1=nlp(text1)

doc_1

for phrases in doc_1.noun_chunks:
  print(phrases)

#Dependancy Parsing
from spacy import displacy

displacy.render(doc,style='dep',jupyter=True)

import string

print(string.punctuation)

#stopwords
from nltk.corpus import stopwords

nltk.download('stopwords')

stopwords.words('english')

#sentence Tokenization
text2 = "In Indian Test cricket History Virat Kohlis was the best captain, He is playing for India"

text2.split(",")

from nltk import sent_tokenize

nltk.download('punkt')

sent_tokenize(text2)

#stemming vs lemmatization
text = "I Studied the subject named A.I and then meeting Mr. Harshil at the meeting"

from nltk.stem.porter import *

stemmer=PorterStemmer()
for word in text.split():
  print(word, "-->",stemmer.stem(word))

doc=nlp(text)

for token in doc:
  print(token, "-->",token.pos_, "-->", token.lemma_)

"""LAB 6 Ngrams"""

#Ngrams using NLP concept
from nltk.util import ngrams

chunks=ngrams(sequence=nltk.word_tokenize(text),n=3)

for phrases in chunks:
  print(phrases)



import spacy
import nltk

text=[
    "My name is Harshil Bhatt.",
    "i live in Rajkot.",
    "I am studying at Marwadi university in ICT department.",
    "i am in 6th semester.",
    "i want job in cloud devops based company.",
    "i had also completed dipoma at Marwadi University.",
    "have a nice day."
]

nlp=spacy.load("en_core_web_sm")

text_combined=" ".join(text)

doc6=nlp(text_combined)

for phrases6 in doc6.noun_chunks:
  print(phrases6)

from spacy import displacy

displacy.render(doc6,style='dep',jupyter=True)