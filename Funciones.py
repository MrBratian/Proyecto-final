import string
import unicodedata
from langdetect import detect
import nltk
import stopwordsiso as stopwords
import re

abecedario = string.ascii_lowercase 

#Función contar palabras
def contar_palabras(contenido):
    
    str_contenido = ''.join(contenido)
    palabras = str_contenido.split()
    a=len(palabras)
    return a

#Función que lee la cantidad de caracteres que tiene el libro
def contar_caracteres(contenido):
     str_contenido=""
     for linea in contenido:
          str_contenido += linea.strip()
        
     a=len(str_contenido)
     return a

#Función que cuenta la cantidad de veces que se repite cada letra
def calcular_frecuencia_letras(contenido,abecedario):
    contenido = ''.join(contenido)
    contenido = unicodedata.normalize('NFKD', contenido.casefold())
    frecuencia_letras = {letra: 0 for letra in abecedario}
    for letra in contenido:
        if letra in frecuencia_letras:
            frecuencia_letras[letra] += 1
    a=[]
    for letra, frecuencia in frecuencia_letras.items():
        a.append(frecuencia)
    return a

#Función que muestra la frecuencia de la longitud de las palabras
def contar_palabras_por_longitud(contenido):
    str_contenido = ' '.join(contenido)  
    palabras = str_contenido.split()
    longitud_palabras = {}
    for palabra in palabras:
        longitud = len(palabra)
        if longitud not in longitud_palabras:
            longitud_palabras[longitud] = 1
        else:
            longitud_palabras[longitud] += 1
    return longitud_palabras

#Función que muestra las calcula la fecuncia de las palabras y muestra las 100 mas frecuentes
def contar_frecuencia_palabras(contenido):
    str_contenido = ''.join(contenido)
    palabras = str_contenido.split()
    frecuencia_palabras = {}
    
    # Contar la frecuencia de cada palabra
    for palabra in palabras:
        palabra = palabra.lower()  
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1
        else:
            frecuencia_palabras[palabra] = 1
    # Imprimir las 100 palabras más frecuentes
    print("\nLas 100 palabras más frecuentes son:")
    for palabra, frecuencia in sorted(frecuencia_palabras.items(), key=lambda x: x[1], reverse=True)[:100]:
        print(f"{palabra}: {frecuencia} veces")

#Función que calcula las palabras sin repetir
def calcular_numero_distinto_palabras(contenido):
  str_contenido = ' '.join(contenido)
  palabras = str_contenido.split()
  numero_distinto_palabras = len(set(palabras))
  return numero_distinto_palabras

#Función que detecta el idioma del texto
def identificar_idioma(contenido):
  str_contenido = ' '.join(contenido)
  idioma = detect(str_contenido)

  if idioma == 'en':
    return 'English'
  elif idioma == 'es':
    return 'Español'
  elif idioma == 'fr':
    return 'Français'
  elif idioma == 'de':
    return 'Deutsch'
  elif idioma == 'pt':
    return 'Português'
  else:
    return 'Unknown'

#Función que cuenta las palabras sin contar las stopwords
def obtener_palabras_frecuentes_sin_stopwords(contenido, n=100):
      str_contenido = ' '.join(contenido)
      idioma = detect(str_contenido)
      stopwords_idioma = stopwords.stopwords(idioma)
      str_contenido = ' '.join(contenido)
      palabras = str_contenido.split()
      palabras_filtradas = [palabra.lower() for palabra in palabras if palabra.lower() not in stopwords_idioma and palabra not in string.punctuation]
      frecuencia_palabras = {}
      for palabra in palabras_filtradas:
          if palabra in frecuencia_palabras:
              frecuencia_palabras[palabra] += 1 
          else:
              frecuencia_palabras[palabra] = 1
      palabras_mas_frecuentes = sorted(frecuencia_palabras.items(), key=lambda x: x[1], reverse=True)[:n]
      return palabras_mas_frecuentes

#Función que identifica los personajes y el número de veces que aparece















""""
def identificar_tiempo_obra(contenido):
  palabras_clave_por_periodo = {
      "Época Antigua": {"antiguo", "clásico", "imperio", "griego", "romano", "mesopotamia", "Filosofía", "Aristóteles", "Platón", "Sumeria", "Esparta", "Atenas", "Imperio Romano", "Jeroglíficos", "Zeus"},
      "Edad Medieval": {"medieval", "caballeros", "castillo", "reino", "feudal", "edad oscura", "Caballero", "Castillo", "Cruzadas", "Inquisición", "Caballeros templarios", "Vassallo", "Nobleza", "Peste negra", "Herejía"},
      "Renacimiento": {"renacimiento", "humanismo", "arte", "ciencia", "leonardo", "da vinci", "Miguel Ángel", "Galileo Galilei", "Copérnico", "Reforma protestante", "Iluminismo"},
      "Barroco": {"barroco", "artístico", "contrarreforma", "caravaggio", "versalles", "luis xiv", "Contrarreforma", "Música barroca", "Teatro barroco", "Siglo de Oro", "Pintura barroca", "Literatura barroca", "Arquitectura barroca"},
      "Siglo de la Ilustración": {"ilustración", "razón", "voltaire", "iluminismo", "enciclopedia", "revolución francesa", "Revolución intelectual", "Derechos humanos", "Racionalismo", "Empirismo", "Separación de poderes", "Literatura ilustrada", "Siglo de las luces"},
      "Siglo XIX": {"siglo xix", "romanticismo", "revolución industrial", "victoriano", "Darwin", "Marx", "Imperialismo", "Nacionalismo","Realismo", "Beethoven", "Impresionismo", "Revolución Haitiana"},
      "Siglo XX": {"siglo xx", "guerras mundiales", "revolución rusa", "movimiento civil", "tecnología", "contemporáneo", "Guerra Fría", "Holocausto", "Socialismo", "Comunismo", "Guerra de Vietnam", "Guerra en Irak", "Contracultura", "Siglo XX"},
    "Siglo XXI":{"Tecnología", "Internet", "Redes sociales", "Smartphone", "globalización", "cambio climático", "sostenibilidad", "inteligencia artificial", "ciberseguridad", "desarrollo sostenible", "energía renovable", "pandemia", "criptomonedas", "Comercio electrónico"},
    "Futuro":{"futurología", "innovación", "tecnología de vanguardia", "robótica avanzada", "exploración espacial", "colonización de otros planetas", "singularidad tecnológica", "teletransportación", "inteligencia artificial superinteligente", "nanotecnología", "realidad aumentada", "bioingeniería", "medicina regenerativa", "energía limpia", "viajes en el tiempo", "clonación humana"}
  }

  palabras = [palabra.lower() for palabra in nltk.word_tokenize(' '.join(contenido))]

  conteo_por_periodo = {periodo: 0 for periodo in palabras_clave_por_periodo}

  for palabra in palabras:
      for periodo, palabras_clave in palabras_clave_por_periodo.items():
          if palabra in palabras_clave:
              conteo_por_periodo[periodo] += 1

  tiempo_mas_probable = max(conteo_por_periodo, key=conteo_por_periodo.get)

  return tiempo_mas_probable

"""


