import string
import unicodedata
from langdetect import detect
import nltk
#from nltk.corpus import stopwords
import stopwordsiso as stopwords

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

#Funcion que calcula las palabras sin repetir
def calcular_numero_distinto_palabras(contenido):
  str_contenido = ' '.join(contenido)
  palabras = str_contenido.split()
  numero_distinto_palabras = len(set(palabras))
  return numero_distinto_palabras

#Funcion que detecta el idioma del texto
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


#Funcion que cuenta las palabras sin contar las stopwords
def obtener_palabras_frecuentes_sin_stopwords(contenido, n=100):
      idiomas = identificar_idioma(contenido).values()
      stopwords_idioma = stopwords.load(idioma)
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

