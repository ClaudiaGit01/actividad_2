from fastapi import FastAPI
from pydantic import BaseModel
import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.classify import NaiveBayesClassifier

nltk.download('punkt')

app = FastAPI()

data = [
    ("super deliciosa", "positive"),
    ("muy costosa", "negative"),
    ("q buena opcion", "positive"),
    ("muy fria", "negative"),
    ("es la mejor del mundo", "positive"),
    ("no me guto la salsa", "negative"),
    ("es una explision de sabor", "positive"),
    ("se demoro mucho", "negative"),
    ("cada vez q voy me enamoro mas", "positive"),
    ("me encanta el pan" , "positive"),
    ("The special effects in this movie were impressive", "positive"),
    ("ya le dije a todos que no me gusta", "negative"),
    ("muy caliente", "positive")
]

respuestas = {
   
    "positive": ["me alegra que te guste", "te esperamos de nuevo"],
    "negative": ["lo sentimos vamos a trabajar en esto", "vamos a mejorar"]
}
       
# Preprocesamiento de datos: Tokenización y extracción de características

def preprocess(text):
    tokens = nltk.word_tokenize(text)
    return {word: True for word in tokens}

# Aplicamos el preprocesamiento a los datos
featuresets = [(preprocess(text), sentimiento) for text, sentimiento in data]

# Entrenamos un clasificador utilizando Naive Bayes
classifier = nltk.NaiveBayesClassifier.train(featuresets)

# Chatbot
def chatbot(frase_usuario):
    categoria = preprocess(frase_usuario)
    sentimiento = classifier.classify(categoria)
    return random.choice(respuestas[sentimiento])

# Modelo para entrada de datos
class FraseEntrada(BaseModel):
    frase: str

# Endpoint del chatbot
@app.post("/chatbot/")
def obtener_respuesta(entrada: FraseEntrada):
    respuesta = chatbot(entrada.frase)
    return {"respuesta": respuesta}