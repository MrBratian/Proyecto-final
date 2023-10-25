import string
import unicodedata
import nltk
from langdetect import detect

try:
  nltk.data.find('tokenizers/punkt')
except LookupError:
  nltk.download('punkt')
import re

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
    # Retornar las 100 palabras más frecuentes
    palabras_mas_frecuentes = {}
    for palabra, frecuencia in sorted(frecuencia_palabras.items(), key=lambda x: x[1], reverse=True)[:100]:
        palabras_mas_frecuentes[palabra] = frecuencia
    return palabras_mas_frecuentes

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
def obtener_palabras_frecuentes_sin_stopwords(contenido, n=50):
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
      palabras_mas_frecuentes_dict = {word: freq for word, freq in palabras_mas_frecuentes}
      return palabras_mas_frecuentes_dict



#Función que identifica los personajes y el número de veces que aparece
def is_roman_numeral(s):
  return bool(re.match(r'^(?=[MDCLXVI])M*(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$', s))

def Identificar_personajes_con_su_frecuencia(contenido):
  personajes = {}
  str_contenido = " ".join(contenido)
  idioma = detect(str_contenido)

    # Definir palabras prohibidas y stopwords según el idioma
  palabras_prohibidas = []
  stopwords_idioma = stopwords.stopwords(idioma)

  matches = re.findall(r'\b(?:[A-ZÁÉÍÓÚÜÑ][a-zA-ZÁÉÍÓÚÜÑáéíóúüñ]*)(?:[-\s][A-ZÁÉÍÓÚÜÑ][a-zA-ZÁÉÍÓÚÜÑáéíóúüñ]*)*\b', str_contenido)
  matches = [match for match in matches if match.lower() not in [word.lower() for word in palabras_prohibidas]]
  matches = [match for match in matches if match.lower() not in stopwords_idioma]
  lugares = identificar_lugares(contenido)

  # Eliminar personajes que coincidan con lugares
  for personaje in matches:
      for lugar in lugares:
          if personaje.lower() in lugar.lower() or lugar.lower() in personaje.lower():
              break  # Si hay una coincidencia con algún lugar, no se agrega al diccionario
      else:
            # Este bloque se ejecuta solo si el bucle for se completa sin interrupciones
          if not is_roman_numeral(personaje):
              if not re.search(r'\.\s' + re.escape(personaje), str_contenido):
                  if personaje not in personajes:
                      personajes[personaje] = 1
                  else:
                      personajes[personaje] += 1
  return personajes

del_words_esp = ["Y", "O", "Ni", "Tampoco", "Además", "Asimismo", "Por lo tanto", "Por consiguiente", "En consecuencia", "Sin embargo", "A pesar de", "Aunque", "Por otro lado", "Mientras que", "Por el contrario", "A su vez", "Por ende", "Por lo que", "Dado que", "Puesto que", "Ya que", "A fin de que", "Con el fin de", "En resumen", "En conclusión", "Finalmente", "De hecho", "Es decir", "O sea", "Por ejemplo", "En otras palabras", "En primer lugar", "En segundo lugar", "Por último", "Primeramente", "En cambio", "Por lo general", "En realidad", "Por supuesto", "El", "La", "Los", "Las", "Un", "Una", "Unos", "Unas","Y", "Había", "Una vez", "Cuando", "Desde", "Érase una vez", "Aquel día", "Siempre", "Al principio", "Finalmente", "En aquel lugar", "Todo comenzó cuando", "Una fría mañana", "Contigo", "Oriente", "Occidente", "Sabio", "Santo Grial", "Muro", "Museo", "Organización", "Universidad", "Amnistía", "Internacional", "Organización", "Banco", "Mundial", "Fondo Monetario", "Día", "Año", "Navidad", "Revolución", "Viernes Santo", "Libro", "Niño", "Internacional", "Radio", "Voluntarios", "Fiesta", "Lirio", "Padrino", "Mago", "Noche", "Gioconda", "Persistencia", "Memoria", "Titanic", "Excalibur", "Santo Grial", "Muro de Berlín", "Museo Universitario de Ciencias y Artes", "Organización de las Naciones Unidas", "Real", "Academia", "Lengua", "Universidad", "Nacional", "Mujer", "Revolución", "Día", "Independencia", "Revolución", "Libro", "Mundial", "Cáncer", "Radio", "Voluntarios", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre", "Padrino", "Mago", "Gioconda", "Médico", "Profesor", "Ingeniero", "Abogado", "Enfermero", "Arquitecto", "Contable", "Actor", "Cantante", "Escritor", "Científico", "Periodista", "Chef", "Policía", "Bombero", "Astronauta", "Psicólogo", "Terapeuta", "Economista", "Electricista", "Plomero", "Carpintero", "Mecánico", "Diseñador", "Artista", "Veterinario", "Farmacéutico", "Conductor de camión", "Agricultor", "Comerciante", "Banquero", "Piloto", "Soldado", "Fotógrafo", "Actor de voz", "Modelo", "Terapeuta físico", "Terapeuta", "OMS", "ONU", "FBI", "CIA", "NASA", "UE", "OTAN", "UEFA", "UNICEF", "FMI", "OMC", "NATO", "CNN", "BBC", "UFO", "NYPD", "DIY", "VIP", "CEO", "AI", "FAQ", "UNESCO", "AIDS", "GPS", "WiFi","antiguo", "medieval", "renacimiento", "barroco", "ilustración", "siglo", "romanticismo", "antiguo", "clásico", "imperio", "griego", "romano", "mesopotamia", "Filosofía", "Aristóteles", "Platón", "Sumeria", "Esparta", "Atenas", "Imperio Romano", "Jeroglíficos", "Zeus", "medieval", "caballeros", "castillo", "reino", "feudal", "edad oscura", "Caballero", "Castillo", "Cruzadas", "Inquisición", "Caballeros templarios", "Vassallo", "Nobleza", "Peste negra", "Herejía", "renacimiento", "humanismo", "arte", "ciencia", "leonardo", "da vinci", "Miguel Ángel", "Galileo Galilei", "Copérnico", "Reforma protestante", "Iluminismo", "barroco", "artístico", "contrarreforma", "caravaggio", "versalles", "luis xiv", "Contrarreforma", "Música barroca", "Teatro barroco", "Siglo de Oro", "Pintura barroca", "Literatura barroca", "Arquitectura barroca", "ilustración", "razón", "voltaire", "iluminismo", "enciclopedia", "revolución francesa", "Revolución intelectual", "Derechos humanos", "Racionalismo", "Empirismo", "Separación de poderes", "Literatura ilustrada", "Siglo de las luces", "siglo xix", "romanticismo", "revolución industrial", "victoriano", "Darwin", "Marx", "Imperialismo", "Nacionalismo","Realismo", "Beethoven", "Impresionismo", "Revolución Haitiana", "siglo xx", "guerras mundiales", "revolución rusa", "movimiento civil", "tecnología", "contemporáneo", "Guerra Fría", "Holocausto", "Socialismo", "Comunismo", "Guerra de Vietnam", "Guerra en Irak", "Contracultura", "Siglo XX", "Egipto", "Mesopotamia", "Sumeria", "Esparta", "Atenas", "Jerusalén", "Filosofía antigua", "Mitología griega", "Helenismo", "Arte romano", "Imperio persa", "Babilonia", "Cartago", "Sociedades antiguas", "Historia clásica", "Europa medieval", "Reyes medievales", "Caballeros medievales", "Camino de Santiago", "Inquisición española", "Caballeros templarios", "Reyes católicos", "Renacimiento italiano", "Mona Lisa", "Mecenas del Renacimiento", "Humanismo renacentista", "Reforma protestante", "Contrarreforma católica", "Barroco italiano", "Pintura barroca flamenca", "Siglo de Oro español", "Luis XIV de Francia", "La Ilustración", "Revolución francesa", "Napoleón Bonaparte", "Revolución industrial", "Victoria del Reino Unido", "Darwinismo", "Karl Marx", "Imperialismo europeo", "Primera Guerra Mundial", "Revolución rusa", "Movimiento de los derechos civiles", "Guerra de Vietnam", "Guerra de Irak", "Guerra fría", "Muro de Berlín", "Siglo I", "Siglo II", "Siglo I", "Siglo II", "Siglo III", "Siglo IV", "Siglo V", "Siglo VI", "Siglo VII", "Siglo VIII", "Siglo IX", "Siglo X", "Siglo XI", "Siglo XII", "Siglo XIII", "Siglo XIV", "Siglo XV", "Siglo XVI", "Siglo XVII", "Siglo XVIII", "Siglo XIX", "Siglo XX","tecnología", "internet", "redes", "smartphone", "globalización", "Tecnología", "Internet", "Redes sociales", "Smartphone", "globalización", "cambio climático", "sostenibilidad", "inteligencia artificial", "ciberseguridad", "desarrollo sostenible", "energía renovable", "pandemia", "criptomonedas", "Comercio electrónico", "innovación", "sostenibilidad", "redes", "inteligencia", "cambio climático", "medio ambiente", "industria", "consumo", "contemporáneo", "modernidad", "ciencia", "tecnológico", "sociedad", "digital", "información", "avances", "covid-19", "tecnologías", "sociales", "smart", "sostenible", "ambiental", "energías limpias", "conectividad", "sociedad digital", "cibernética", "modernización", "industrialización", "desarrollo tecnológico", "internet de las cosas", "big data", "ciberseguridad", "medicina moderna", "tecnología avanzada", "realidad virtual", "inteligencia artificial avanzada", "investigación científica", "nuevos medios", "innovación tecnológica", "sociedad conectada", "economía digital", "teletrabajo", "educación en línea", "cultura pop", "transformación digital", "empresas tecnológicas", "startups", "tendencias contemporáneas", "sistemas de información", "Big Tech", "redes sociales", "innovaciones tecnológicas", "tecnología móvil", "redes inalámbricas", "inteligencia de datos", "robótica avanzada", "computación cuántica", "tecnología espacial", "vehículos eléctricos", "energía solar", "medicina de precisión", "tecnología genética", "realidad aumentada", "tecnología wearable", "aprendizaje automático", "economía colaborativa", "tecnología blockchain", "tecnología de la salud", "educación en línea", "streaming de video", "comercio electrónico", "cultura de las redes sociales", "empresas de tecnología", "ciudad inteligente", "tecnología financiera", "automatización industrial", "inteligencia de negocios", "ciberataques", "ciberseguridad empresarial", "tecnología verde", "vehículos autónomos", "teletrabajo permanente", "telemedicina", "tecnología de entretenimiento", "nube de datos", "privacidad en línea", "criptomoneda digital", "medios digitales", "startups de salud", "tecnología educativa", "inteligencia artificial en atención médica", "energía renovable", "biotecnología", "tecnología de la nube", "realidad virtual extendida", "drones de consumo", "tecnología de vehículos autónomos", "siglo XXI","futurología", "innovación", "tecnología", "exploración", "colonización", "teletransportación", "futurología", "innovación", "tecnología de vanguardia", "robótica avanzada", "exploración espacial", "colonización de otros planetas", "singularidad tecnológica", "teletransportación", "inteligencia artificial superinteligente", "nanotecnología", "realidad aumentada", "bioingeniería", "medicina regenerativa", "energía limpia", "viajes en el tiempo", "clonación humana", "avances científicos", "prospectiva", "espacio exterior", "tecnología futurista", "transhumanismo", "máquinas inteligentes", "inteligencia artificial avanzada", "nanorobots", "realidad virtual", "biotecnología", "fusión nuclear", "propulsión espacial", "agujeros de gusano", "sociedad futura", "nanotecnología", "realidad aumentada", "bioingeniería", "medicina regenerativa", "energía limpia", "viajes en el tiempo", "clonación humana", "avances científicos", "prospectiva", "espacio exterior", "tecnología futurista", "transhumanismo", "máquinas inteligentes", "inteligencia artificial avanzada", "nanorobots", "realidad virtual", "biotecnología", "fusión nuclear", "propulsión espacial", "agujeros de gusano", "sociedad futura", "exploración cósmica", "colonización de Marte", "inteligencia artificial cuántica", "teletransporte cuántico", "genética avanzada", "tecnología de viajes espaciales", "nanomateriales", "tecnología de propulsión a chorro", "rejuvenecimiento biológico", "energía de fusión", "computación cuántica", "realidad virtual total", "ciudades sostenibles", "tecnología de vehículos voladores", "exploración oceánica", "vida extraterrestre", "turismo espacial", "clonación de órganos", "energía solar avanzada", "tecnología de invisibilidad", "colonización lunar", "conexiones cerebro-máquina", "biología sintética", "energía de antimateria", "telepatía cuántica", "reciclaje espacial", "tecnología de la teleportación", "inteligencia artificial en la educación", "edición genética", "tecnología de nanocámaras", "realidad aumentada en medicina", "realidad virtual terapéutica", "tecnología de alimentos del futuro", "tecnología de realidad virtual para juegos", "expansión del universo", "exploración de exoplanetas", "tecnología de energía eólica", "agricultura vertical", "tecnología de vida en otros planetas", "tecnología de propulsión a velocidad de la luz", "internet cuántico", "tecnología de imágenes cerebrales", "tecnología de vehículos autónomos aéreos", "robots inteligentes", "realidad aumentada en la educación", "tecnología de viajes en el tiempo", "telepatía avanzada", "biorrobots", "tecnología de dispositivos vestibles avanzados", "televisión holográfica", "tecnología de control mental", "tecnología de recolección de energía", "tecnología de viajes en el tiempo cuántico", "realidad aumentada para el entretenimiento", "tecnología de teletransportación humana", "biología sintética avanzada", "tecnología de propulsión de iones", "robots asistentes", "tecnología de comunicación por ondas cerebrales", "realidad virtual para el turismo", "tecnología de traducción de idiomas avanzada", "tecnología de energía de hidrógeno", "tecnología de aceleración de partículas", "células solares de próxima generación", "tecnología de alimentos del futuro", "vehículos autónomos terrestres", "tecnología de impresión 3D avanzada", "Siglo XXI", "Siglo XXII", "Siglo XXIII", "Siglo XXIV", "Siglo XXV", "Siglo XXVI", "Siglo XXVII", "Siglo XXVIII", "Siglo XXIX", "Siglo XXX", "Siglo XXXI", "Siglo XXXII", "Siglo XXXIII", "Siglo XXXIV", "Siglo XXXV", "Siglo XXXVI", "Siglo XXXVII", "Siglo XXXVIII", "Siglo XXXIX", "Siglo XL", "Siglo XLI", "Siglo XLII", "Siglo XLIII", "Siglo XLIV", "Siglo XLV", "Siglo XLVI", "Siglo XLVII", "Siglo XLVIII", "Siglo XLIX", "Siglo L", "Siglo LI", "Siglo LII", "Siglo LIII", "Siglo LIV", "Siglo LV", "Siglo LVI", "Siglo LVII", "Siglo LVIII", "Siglo LIX", "Siglo LX", "Siglo LXI", "Siglo LXII", "Siglo LXIII", "Siglo LXIV", "Siglo LXV", "Siglo LXVI", "Siglo LXVII", "Siglo LXVIII", "Siglo LXIX", "Siglo LXX", "Siglo LXXI", "Siglo LXXII", "Siglo LXXIII", "Siglo LXXIV", "Siglo LXXV", "Siglo LXXVI", "Siglo LXXVII", "Siglo LXXVIII", "Siglo LXXIX", "Siglo LXXX", "Siglo LXXXI", "Siglo LXXXII", "Siglo LXXXIII", "Siglo LXXXIV", "Siglo LXXXV", "Siglo LXXXVI", "Siglo LXXXVII", "Siglo LXXXVIII", "Siglo LXXXIX", "Siglo XC", "Siglo XCI", "Siglo XCII", "Siglo XCIII", "Siglo XCIV", "Siglo XCV", "Siglo XCVI", "Siglo XCVII", "Siglo XCVIII", "Siglo XCIX", "Siglo C"]

del_words_fr = ["Et", "Ou", "Ni", "Non plus", "De plus", "Ainsi", "Par conséquent", "Donc", "En conséquence", "Cependant", "Malgré", "Bien que", "D'autre part", "Tandis que", "Au contraire", "À son tour", "Par conséquent", "Donc", "Étant donné que", "Puisque", "Comme", "Afin que", "Dans le but de", "En résumé", "En conclusion", "Finalement", "En fait", "C'est-à-dire", "Autrement dit", "En premier lieu", "En deuxième lieu", "Enfin", "Premièrement", "Par contre", "En général", "En réalité", "Bien sûr", "Le", "La", "Les", "Un", "Une", "Des", "Et", "Il y avait", "Une fois", "Quand", "Depuis", "Il était une fois", "Ce jour-là", "Toujours", "Au début", "Enfin", "À cet endroit", "Tout a commencé quand", "Un matin froid", "Avec toi", "Orient", "Occident", "Sage", "Saint Graal", "Mur", "Musée", "Organisation", "Université", "Amnistie", "International", "Organisation", "Banque", "Mondiale", "Fonds monétaire", "Jour", "An", "Noël", "Révolution", "Vendredi Saint", "Livre", "Enfant", "International", "Radio", "Volontaires", "Fête", "Lys", "Parrain", "Magicien", "Nuit", "La Joconde", "Persistance", "Mémoire", "Titanic", "Excalibur", "Saint Graal", "Mur de Berlin", "Musée universitaire des sciences et des arts", "Organisation des Nations Unies", "Réel", "Académie", "Langue", "Université", "Femme", "Révolution", "Jour", "Indépendance", "Révolution", "Livre", "Mondial", "Cancer", "Radio", "Volontaires", "Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre", "Parrain", "Magicien", "Médecin", "Professeur", "Ingénieur", "Avocat", "Infirmière", "Architecte", "Comptable", "Acteur", "Chanteur", "Écrivain", "Scientifique", "Journaliste", "Chef", "Policier", "Pompier", "Astronaute", "Psychologue", "Thérapeute", "Économiste", "Électricien", "Plombier", "Menuisier", "Mécanicien", "Designer", "Artiste", "Vétérinaire", "Pharmacien", "Chauffeur de camion", "Agriculteur", "Commerçant", "Banquier", "Pilote", "Soldat", "Photographe", "Doubleur", "Mannequin", "Thérapeute physique", "Thérapeute", "OMS", "ONU", "FBI", "CIA", "NASA", "UE", "OTAN", "UEFA", "UNICEF", "FMI", "OMC", "OTAN", "CNN", "BBC", "OVNI", "NYPD", "FAÇON", "VIP", "PDG", "IA", "FAQ", "UNESCO", "SIDA", "GPS", "WiFi"]

del_words_en = ["And", "Or", "Neither", "Nor", "Furthermore", "Likewise", "Therefore", "Consequently", "In consequence", "However", "Despite", "Although", "On the other hand", "While", "On the contrary", "In turn", "Hence", "So", "Since", "Given that", "As", "In order to", "To", "In summary", "In conclusion", "Finally", "Actually", "That is", "In other words", "First", "Second", "Finally", "Primarily", "On the other hand", "Generally", "In reality", "Of course", "The", "The", "The", "The", "A", "A", "Some", "Some", "And", "There was", "Once upon a time", "When", "From", "Once upon a time", "That day", "Always", "At the beginning", "Finally", "In that place", "Everything started when", "A cold morning", "With you", "East", "West", "Wise", "Holy Grail", "Wall", "Museum", "Organization", "University", "Amnesty", "International", "Organization", "Bank", "World", "International Monetary Fund", "Day", "Year", "Christmas", "Revolution", "Good Friday", "Book", "Child", "International", "Radio", "Volunteers", "Party", "Lily", "Godfather", "Wizard", "Night", "Mona Lisa", "Persistence", "Memory", "Titanic", "Excalibur", "Holy Grail", "Berlin Wall", "University Museum of Science and Arts", "United Nations", "Royal", "Academy", "Language", "National", "Woman", "Revolution", "Day", "Independence", "Revolution", "Book", "World", "Cancer", "Radio", "Volunteers", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December", "Godfather", "Wizard", "Mona Lisa", "Doctor", "Teacher", "Engineer", "Lawyer", "Nurse", "Architect", "Accountant", "Actor", "Singer", "Writer", "Scientist", "Journalist", "Chef", "Police", "Firefighter", "Astronaut", "Psychologist", "Therapist", "Economist", "Electrician", "Plumber", "Carpenter", "Mechanic", "Designer", "Artist", "Veterinarian", "Pharmacist", "Truck driver", "Farmer", "Merchant", "Banker", "Pilot", "Soldier", "Photographer", "Voice actor", "Model", "Physical therapist", "Therapist", "WHO", "UN", "FBI", "CIA", "NASA", "EU", "NATO", "UEFA", "UNICEF", "IMF", "WTO", "NATO", "CNN", "BBC", "UFO", "NYPD", "DIY", "VIP", "CEO", "AI", "FAQ", "UNESCO", "AIDS", "GPS", "WiFi"]

del_words_deut = ["Und", "Oder", "Weder", "Noch", "Darüber hinaus", "Ebenso", "Deshalb", "Folglich", "Infolgedessen", "Jedoch", "Obwohl", "Andererseits", "Während", "Im Gegensatz dazu", "Im Gegenzug", "Folglich", "Daher", "So", "Da", "Da", "Um zu", "Um", "Zusammenfassend", "Zusammenfassend", "Schließlich", "Tatsächlich", "Das heißt", "Das heißt", "Beispielsweise", "Mit anderen Worten", "Erstens", "Zweitens", "Schließlich", "Zunächst", "Andererseits", "Im Allgemeinen", "Tatsächlich", "Natürlich", "Der", "Die", "Die", "Die", "Ein", "Eine", "Einige", "Einige", "Und", "Es gab", "Es war einmal", "Wenn", "Von", "Es war einmal", "An diesem Tag", "Immer", "Am Anfang", "Schließlich", "An diesem Ort", "Alles begann, als", "An einem kalten Morgen", "Mit dir", "Osten", "Westen", "Weise", "Heiliger Gral", "Mauer", "Museum", "Organisation", "Universität", "Amnestie", "International", "Organisation", "Bank", "Welt", "Internationaler Währungsfonds", "Tag", "Jahr", "Weihnachten", "Revolution", "Karfreitag", "Buch", "Kind", "International", "Radio", "Freiwillige", "Party", "Lilie", "Pate", "Zauberer", "Nacht", "Mona Lisa", "Beharrlichkeit", "Erinnerung", "Titanic", "Excalibur", "Heiliger Gral", "Berliner Mauer", "Universitätsmuseum für Wissenschaft und Kunst", "Vereinte Nationen", "Königlich", "Akademie", "Sprache", "National", "Frau", "Revolution", "Tag", "Unabhängigkeit", "Revolution", "Buch", "Welt", "Krebs", "Radio", "Freiwillige", "Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember", "Pate", "Zauberer", "Mona Lisa", "Arzt", "Lehrer", "Ingenieur", "Anwalt", "Krankenschwester", "Architekt", "Buchhalter", "Schauspieler", "Sänger", "Schriftsteller", "Wissenschaftler", "Journalist", "Koch", "Polizei", "Feuerwehrmann", "Astronaut", "Psychologe", "Therapeut", "Ökonom", "Elektriker", "Installateur", "Tischler", "Mechaniker", "Designer", "Künstler", "Tierarzt", "Apotheker", "Truckfahrer", "Bauer", "Händler", "Bankier", "Pilot", "Soldat", "Fotograf", "Synchronsprecher", "Modell", "Physiotherapeut", "Therapeut", "WHO", "UNO", "FBI", "CIA", "NASA", "EU", "NATO", "UEFA", "UNICEF", "IWF", "WTO", "NATO", "CNN", "BBC", "UFO", "NYPD", "DIY", "VIP", "CEO", "KI", "FAQ", "UNESCO", "AIDS", "GPS", "WLAN"]

del_words_port= ["E", "Ou", "Nem", "Tampouco", "Além disso", "Do mesmo modo", "Portanto", "Consequentemente", "Em consequência", "No entanto", "Apesar de", "Embora", "Por outro lado", "Enquanto", "Ao contrário", "Por sua vez", "Assim", "Então", "Já que", "Uma vez que", "Visto que", "Dado que", "A fim de que", "Para", "Em resumo", "Em conclusão", "Finalmente", "Na realidade", "Ou seja", "Por exemplo", "Em outras palavras", "Em primeiro lugar", "Em segundo lugar", "Finalmente", "Primeiramente", "Em contrapartida", "Geralmente", "Na realidade", "Claro", "O", "A", "Os", "As", "Um", "Uma", "Alguns", "Algumas", "E", "Havia", "Era uma vez", "Quando", "Desde", "Era uma vez", "Naquele dia", "Sempre", "No início", "Finalmente", "Naquele lugar", "Tudo começou quando", "Em uma manhã fria", "Contigo", "Oriente", "Ocidente", "Sábio", "Santo Graal", "Muro", "Museu", "Organização", "Universidade", "Anistia", "Internacional", "Organização", "Banco", "Mundial", "Fundo Monetário Internacional", "Dia", "Ano", "Natal", "Revolução", "Sexta-feira Santa", "Livro", "Criança", "Internacional", "Rádio", "Voluntários", "Festa", "Lírio", "Padrinho", "Mago", "Noite", "Mona Lisa", "Persistência", "Memória", "Titanic", "Excalibur", "Santo Graal", "Muro de Berlim", "Museu Universitário de Ciências e Artes", "Nações Unidas", "Real", "Academia", "Língua", "Nacional", "Mulher", "Revolução", "Dia", "Independência", "Revolução", "Livro", "Câncer", "Rádio", "Voluntários", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro", "Padrinho", "Mago", "Mona Lisa", "Médico", "Professor", "Engenheiro", "Advogado", "Enfermeiro", "Arquiteto", "Contador", "Ator", "Cantor", "Escritor", "Cientista", "Jornalista", "Chef", "Polícia", "Bombeiro", "Astronauta", "Psicólogo", "Terapeuta", "Economista", "Eletricista", "Encanador", "Carpinteiro", "Mecânico", "Designer", "Artista", "Veterinário", "Farmacêutico", "Motorista de caminhão", "Fazendeiro", "Comerciante", "Bancário", "Piloto", "Soldado", "Fotógrafo", "Dublador", "Modelo", "Fisioterapeuta", "Terapeuta", "OMS", "ONU", "FBI", "CIA", "NASA", "UE", "OTAN", "UEFA", "UNICEF", "FMI", "OMC", "OTAN", "CNN", "BBC", "ÓVNI", "NYPD", "Faça você mesmo", "VIP", "CEO", "IA", "FAQ", "UNESCO", "AIDS", "GPS", "Wi-Fi"]



#Función que identifica los personajes principales
def personajes_principales(contenido):
    personajes_frecuencia = Identificar_personajes_con_su_frecuencia(contenido)
    frecuencia_maxima = max(personajes_frecuencia.values(), default=0)
    porcentaje_minimo = 0.6
    personajes_principales = {personaje: frecuencia for personaje, frecuencia in personajes_frecuencia.items()
                            if frecuencia >= porcentaje_minimo * frecuencia_maxima}

    return personajes_principales


#Función que identifica los lugares en el texto
def identificar_lugares(contenido):
  str_contenido = " ".join(contenido)
  lugares_identificados = []
  palabras_clave = [
'ciudad', 'pueblo', 'aldea', 'país', 'región', 'lugar',
'calle', 'avenida', 'plaza', 'barrio', 'casa', 'edificio',
'montaña', 'río', 'lago', 'océano', 'mar', 'playa','castillo','reino','reinos','países','pueblos','aldeas','ciudades','regiones','calles','avenidas','plazas','estancia',
'barrios', 'casas', 'edificios', 'montañas', 'ríos',
'bosque', 'selva', 'pradera', 'desierto', 'isla', 'península',
'continente', 'valle', 'meseta', 'colina', 'cordillera', 'volcán',
'caverna', 'cueva', 'glaciar', 'cascada', 'canyon', 'mesa',
'parque', 'reserva', 'zoológico', 'jardín', 'estadio', 'teatro',
'museo', 'biblioteca', 'escuela', 'universidad', 'hospital', 'iglesia',
'sinagoga', 'mezquita', 'templo', 'catedral', 'monasterio', 'santuario',
'mercado', 'tienda', 'centro comercial', 'restaurante', 'café', 'bar',
'hotel', 'posada', 'motel', 'hostal', 'aeropuerto', 'estación',  
'puerto', 'terminal', 'parada', 'cruce', 'intersección', 'rotatoria',
'granja', 'rancho', 'plantación', 'viñedo', 'huerto', 'campo',
'fábrica', 'planta', 'almacén', 'taller', 'laboratorio', 'oficina',
'gimnasio', 'piscina', 'establo', 'corral', 'hangar', 'garaje',
'prisión', 'cárcel', 'comisaría', 'tribunal', 'juzgado', 'cementerio',
'estación espacial', 'base militar', 'campamento', 'cueva', 'pueblo fantasma',
'parque de diversiones', 'circo', 'feria', 'zona residencial', 'urbanización',
'mercado', 'tienda', 'centro comercial', 'restaurante', 'café', 'bar',
'hotel', 'posada', 'motel', 'hostal', 'aeropuerto', 'estación',
'puerto', 'terminal', 'parada', 'cruce', 'intersección', 'rotatoria',
'granja', 'rancho', 'plantación', 'viñedo', 'huerto', 'campo',
'fábrica', 'planta', 'almacén', 'taller', 'laboratorio', 'oficina',
'gimnasio', 'piscina', 'establo', 'corral', 'hangar', 'garaje',
'prisión', 'cárcel', 'comisaría', 'tribunal', 'juzgado', 'cementerio',
'estación espacial', 'base militar', 'campamento', 'cueva', 'pueblo fantasma',
'parque de diversiones', 'circo', 'feria', 'zona residencial', 'urbanización',
'faro', 'farol', 'torre', 'observatorio', 'plaza de toros', 'estación de tren',
'estación de autobuses', 'cruce de peatones', 'puente', 'túnel', 'acueducto',
'fuente', 'escultura', 'monumento', 'obelisco', 'arco de triunfo', 'ruinas',
'muelle', 'embarcadero', 'suburbio', 'vecindario', 'terminal de autobuses',
'cabina', 'choza', 'cabaña', 'estación de esquí', 'resort', 'spa',
'pista de esquí', 'parque nacional', 'reserva natural', 'reserva de vida salvaje',
'coto de caza', 'acantilado', 'ladera', 'tierras altas', 'pantano',
'laguna', 'charca', 'manantial', 'fiordo', 'ría', 'bahía', 'ensenada',
'isleta', 'cayo', 'rincón', 'cabo', 'península', 'meseta', 'altiplano',
'llanura', 'estuario', 'delta', 'archipiélago', 'grupo de islas', 'islote',
'monte', 'cima', 'cumbre', 'collado', 'paso de montaña', 'llanura aluvial',
'acantilado', 'precipicio', 'cuesta', 'depresión', 'garganta', 'géiser',
'fuente termal', 'río subterráneo', 'valle fluvial', 'delta fluvial', 'cascada',
'catarata', 'arroyo', 'riachuelo', 'torrente', 'rambla', 'cienaga', 'ciénaga',
'balsa', 'hondonada', 'corriente', 'desfiladero', 'cima', 'hito', 'mojón',
'hitu', 'referencia', 'punto de referencia', 'mirador', 'área de descanso',
'área de picnic', 'campamento de base', 'refugio', 'albergue', 'hospedaje', 'lodge',
'residencia', 'campamento',
'mercado nocturno', 'cafetería', 'food truck', 'puesto de frutas', 'quiosco',
'boutique', 'salón de belleza', 'lavandería', 'cine', 'club nocturno', 'galería de arte',
'estudio de yoga', 'parque temático', 'pista de patinaje', 'pista de BMX', 'parque acuático',
'estación de servicio', 'taller de reparación', 'estudio de música', 'estadio de fútbol',
'pista de atletismo', 'parque de skate', 'pista de tenis', 'campo de golf', 'jardín botánico',
'zona arqueológica', 'monasterio', 'mezquita histórica', 'teatro al aire libre', 'estación de metro',
'teleférico', 'vivero de plantas', 'cibercafé', 'aula de conferencias', 'estudio de diseño',
'parque de diversiones acuáticas', 'pista de carreras', 'pista de drag', 'aeródromo', 'observatorio astronómico',
'pueblo de montaña', 'villa junto al mar', 'complejo turístico', 'posada de lujo', 'refugio de montaña',
'albergue juvenil', 'pabellón de conciertos', 'plaza de mercado', 'callejón histórico', 'fuente ornamental',
'mirador panorámico', 'campamento ecoturístico', 'pueblo pesquero', 'mercado de artesanías', 'feria de antigüedades',
'zona de juegos para niños', 'jardín de rosas', 'arrecife de coral', 'tienda de surf', 'puerto deportivo',
'granja de avestruces', 'parque de aventuras', 'casa de huéspedes', 'torre de observación', 'centro de convenciones',
'pabellón de eventos', 'estación de radio', 'biblioteca digital', 'estudio de fotografía', 'parque nacional marino',
'parque de aves', 'santuario de mariposas', 'refugio de vida silvestre', 'bosque de bambú', 'rancho de caballos',
'sendero de escalada', 'pista de BMX', 'parque de cuerdas altas', 'piscina de olas', 'lago subterráneo',
'cueva de cristales', 'valle de las luciérnagas', 'reserva geotérmica', 'pueblo medieval', 'ruinas romanas',
'catedral gótica', 'fuerte histórico', 'observatorio de aves', 'santuario de elefantes', 'parque de mariposas',
'campo de lavanda', 'plantación de té', 'viñedo orgánico', 'reserva de bisontes', 'refugio de elefantes',
'pueblo indígena', 'ruinas mayas', 'cenote escondido', 'lago de aguas termales', 'parque de esculturas',
'zona de acampada', 'pueblo costero', 'cueva submarina', 'arrecife de coral', 'parque histórico',
'ruta de senderismo', 'pista de ciclismo', 'fábrica de chocolate', 'pueblo artístico', 'bosque encantado'
# Continentes
'África', 'América', 'Asia', 'Europa', 'Oceanía',
# Países
'Estados Unidos', 'China', 'India', 'Brasil', 'Indonesia', 'Pakistán',
'Bangladesh', 'Nigeria', 'Rusia', 'México', 'Japón', 'Etiopía', 'Filipinas',
'Egipto', 'Vietnam', 'República Democrática del Congo', 'Turquía', 'Irán', 'Alemania',
'Tailandia', 'Reino Unido', 'Francia', 'Italia', 'Tanzania', 'Sudáfrica', 'Myanmar',
'Kenia', 'Corea del Sur', 'Colombia', 'España', 'Ucrania', 'Argentina', 'Argelia',
'Sudán', 'Irak', 'Afganistán', 'Polonia', 'Canadá', 'Marruecos', 'Uzbekistán',
'Perú', 'Angola', 'Malasia', 'Mozambique', 'Ghana', 'Yemen', 'Nepal', 'Venezuela',
'Australia', 'Canadá', 'Chile', 'Ecuador', 'Finlandia', 'Grecia', 'Hungría', 'Islandia',
'Jamaica', 'Kazajistán', 'Laos', 'Madagascar', 'Nicaragua', 'Omán', 'Panamá', 'Qatar',
'Rumanía', 'Serbia', 'Túnez', 'Uganda', 'Vanuatu', 'Zambia', 'Zimbabue', 'El Cairo', 'Ciudad del Cabo', 'Lagos', 'Nairobi', 'Casablanca', 'Yakarta', 'Lagos', 'Johannesburgo', 'El Cabo', 'Durban',
    'Nueva York', 'Ciudad de México', 'Toronto', 'Los Ángeles', 'Chicago', 'Washington D.C.', 'Vancouver', 'Montreal', 'Atlanta', 'Houston',
    'Sao Paulo', 'Buenos Aires', 'Río de Janeiro', 'Bogotá', 'Lima', 'Caracas', 'Quito', 'Asunción', 'Montevideo', 'Santiago',
    'Tokio', 'Pekín', 'Mumbai', 'Estambul', 'Dubái', 'Delhi', 'Shanghái', 'Pekín', 'Moscú', 'Yakarta', 'Seúl', 'Karachi', 'Bangkok', 'Hong Kong', 'Singapur', 'Manila',
    'París', 'Londres', 'Berlín', 'Roma', 'Madrid',"Montevideo", 'Ámsterdam', 'Praga', 'Viena', 'Varsovia', 'Atenas', 'Budapest', 'Estocolmo', 'Lisboa', 'Moscú', 'Zúrich',
    'Sídney', 'Melbourne', 'Auckland', 'Wellington', 'Brisbane', 'Perth', 'Adelaida', 'Canberra', 'Christchurch', 'Queenstown',
    'Nueva Delhi', 'Pretoria', 'Osaka', 'Jerusalén', 'El Vaticano', 'Riad', 'Doha', 'Abu Dhabi', 'Kuwait City', 'Manama', 'Amán', 'Amán', 'Teherán', 'Bagdad', 'Kabul',
    'Nairobi', 'Casablanca', 'Dakar', 'Luanda', 'Addis Abeba', 'Accra', 'Maputo', 'Abiyán', 'Dar es Salaam', 'Abuja', 'Dakar', 'Kigali', 'Windhoek', 'Libreville', 'Brazzaville',
    'Bamako', 'Niamey', 'Conakry', 'Bissau', 'Banjul', 'Maseru', 'Lomé', 'Gaborone', 'Antananarivo', 'Lusaka', 'Lilongüe', 'Bujumbura', 'Asmara', 'Yamena', 'Bangui', 'Mogadiscio',
    'Kampala', 'Libreville', 'Ouagadougou', 'Harare', 'Cotonú', 'Túnez', 'Yaundé'
  ] 
  patron_lugar = re.compile(r'\b(?:' + '|'.join(palabras_clave) + r')\b', re.IGNORECASE)

  coincidencias = patron_lugar.finditer(str_contenido)

  for coincidencia in coincidencias:
      inicio, fin = coincidencia.start(), coincidencia.end()

      # Asegurarse de obtener la palabra completa sin incluir comas u otros caracteres
      while inicio > 0 and str_contenido[inicio - 1].isalpha():
          inicio -= 1
      while fin < len(str_contenido) and str_contenido[fin].isalpha():
          fin += 1

      lugar_encontrado = str_contenido[inicio:fin]

      # Verificar si la palabra siguiente después de la coincidencia inicia con mayúscula
      siguiente_palabra = str_contenido[fin:].split()[0] if fin < len(str_contenido) else None
      palabras_siguientes = [lugar_encontrado]

      while siguiente_palabra and (siguiente_palabra[0].isupper() or siguiente_palabra.lower() == 'de'):
          palabras_siguientes.append(siguiente_palabra)
          fin += len(siguiente_palabra) + 1  # +1 para tener en cuenta el espacio entre palabras
          siguiente_palabra = str_contenido[fin:].split()[0] if fin < len(str_contenido) else None

      if len(palabras_siguientes) > 1 and palabras_siguientes[-1].lower() == 'de' and siguiente_palabra and siguiente_palabra[0].isupper():
          palabras_siguientes.append(siguiente_palabra)

      lugar_final = " ".join(palabras_siguientes)

      if lugar_final not in lugares_identificados:
          lugares_identificados.append(lugar_final)

  return lugares_identificados
  
def imprimir_lugares(identificados):
  for idx, lugar in enumerate(identificados, start=1):
      print(f"{idx}. {lugar}")
            
#Función que identifica el tiempo de una obra
def identificar_tiempo_obra(contenido,x):
  idioma=x
  palabras = [palabra.lower() for palabra in nltk.word_tokenize(' '.join(contenido))]

  count_antiguo = 0
  count_contemporaneo = 0
  count_futuro = 0

  for palabra in palabras:
      if palabra in ["antiguo", "medieval", "renacimiento", "barroco", "ilustración", "siglo", "romanticismo", "antiguo", "clásico", "imperio", "griego", "romano", "mesopotamia", "Filosofía", "Aristóteles", "Platón", "Sumeria", "Esparta", "Atenas", "Imperio Romano", "Jeroglíficos", "Zeus", "medieval", "caballeros", "castillo", "reino", "feudal", "edad oscura", "Caballero", "Castillo", "Cruzadas", "Inquisición", "Caballeros templarios", "Vassallo", "Nobleza", "Peste negra", "Herejía", "renacimiento", "humanismo", "arte", "ciencia", "leonardo", "da vinci", "Miguel Ángel", "Galileo Galilei", "Copérnico", "Reforma protestante", "Iluminismo", "barroco", "artístico", "contrarreforma", "caravaggio", "versalles", "luis xiv", "Contrarreforma", "Música barroca", "Teatro barroco", "Siglo de Oro", "Pintura barroca", "Literatura barroca", "Arquitectura barroca", "ilustración", "razón", "voltaire", "iluminismo", "enciclopedia", "revolución francesa", "Revolución intelectual", "Derechos humanos", "Racionalismo", "Empirismo", "Separación de poderes", "Literatura ilustrada", "Siglo de las luces", "siglo xix", "romanticismo", "revolución industrial", "victoriano", "Darwin", "Marx", "Imperialismo", "Nacionalismo","Realismo", "Beethoven", "Impresionismo", "Revolución Haitiana", "siglo xx", "guerras mundiales", "revolución rusa", "movimiento civil", "tecnología", "contemporáneo", "Guerra Fría", "Holocausto", "Socialismo", "Comunismo", "Guerra de Vietnam", "Guerra en Irak", "Contracultura", "Siglo XX", "Egipto", "Mesopotamia", "Sumeria", "Esparta", "Atenas", "Jerusalén", "Filosofía antigua", "Mitología griega", "Helenismo", "Arte romano", "Imperio persa", "Babilonia", "Cartago", "Sociedades antiguas", "Historia clásica", "Europa medieval", "Reyes medievales", "Caballeros medievales", "Camino de Santiago", "Inquisición española", "Caballeros templarios", "Reyes católicos", "Renacimiento italiano", "Mona Lisa", "Mecenas del Renacimiento", "Humanismo renacentista", "Reforma protestante", "Contrarreforma católica", "Barroco italiano", "Pintura barroca flamenca", "Siglo de Oro español", "Luis XIV de Francia", "La Ilustración", "Revolución francesa", "Napoleón Bonaparte", "Revolución industrial", "Victoria del Reino Unido", "Darwinismo", "Karl Marx", "Imperialismo europeo", "Primera Guerra Mundial", "Revolución rusa", "Movimiento de los derechos civiles", "Guerra de Vietnam", "Guerra de Irak", "Guerra fría", "Muro de Berlín", "Siglo I", "Siglo II", "Siglo I", "Siglo II", "Siglo III", "Siglo IV", "Siglo V", "Siglo VI", "Siglo VII", "Siglo VIII", "Siglo IX", "Siglo X", "Siglo XI", "Siglo XII", "Siglo XIII", "Siglo XIV", "Siglo XV", "Siglo XVI", "Siglo XVII", "Siglo XVIII", "Siglo XIX", "Siglo XX"]:
          count_antiguo += 1
      elif palabra in ["tecnología", "internet", "redes", "smartphone", "globalización", "Tecnología", "Internet", "Redes sociales", "Smartphone", "globalización", "cambio climático", "sostenibilidad", "inteligencia artificial", "ciberseguridad", "desarrollo sostenible", "energía renovable", "pandemia", "criptomonedas", "Comercio electrónico", "innovación", "sostenibilidad", "redes", "inteligencia", "cambio climático", "medio ambiente", "industria", "consumo", "contemporáneo", "modernidad", "ciencia", "tecnológico", "sociedad", "digital", "información", "avances", "covid-19", "tecnologías", "sociales", "smart", "sostenible", "ambiental", "energías limpias", "conectividad", "sociedad digital", "cibernética", "modernización", "industrialización", "desarrollo tecnológico", "internet de las cosas", "big data", "ciberseguridad", "medicina moderna", "tecnología avanzada", "realidad virtual", "inteligencia artificial avanzada", "investigación científica", "nuevos medios", "innovación tecnológica", "sociedad conectada", "economía digital", "teletrabajo", "educación en línea", "cultura pop", "transformación digital", "empresas tecnológicas", "startups", "tendencias contemporáneas", "sistemas de información", "Big Tech", "redes sociales", "innovaciones tecnológicas", "tecnología móvil", "redes inalámbricas", "inteligencia de datos", "robótica avanzada", "computación cuántica", "tecnología espacial", "vehículos eléctricos", "energía solar", "medicina de precisión", "tecnología genética", "realidad aumentada", "tecnología wearable", "aprendizaje automático", "economía colaborativa", "tecnología blockchain", "tecnología de la salud", "educación en línea", "streaming de video", "comercio electrónico", "cultura de las redes sociales", "empresas de tecnología", "ciudad inteligente", "tecnología financiera", "automatización industrial", "inteligencia de negocios", "ciberataques", "ciberseguridad empresarial", "tecnología verde", "vehículos autónomos", "teletrabajo permanente", "telemedicina", "tecnología de entretenimiento", "nube de datos", "privacidad en línea", "criptomoneda digital", "medios digitales", "startups de salud", "tecnología educativa", "inteligencia artificial en atención médica", "energía renovable", "biotecnología", "tecnología de la nube", "realidad virtual extendida", "drones de consumo", "tecnología de vehículos autónomos", "siglo XXI"]:
          count_contemporaneo += 1
      elif palabra in ["futurología", "innovación", "tecnología", "exploración", "colonización", "teletransportación", "futurología", "innovación", "tecnología de vanguardia", "robótica avanzada", "exploración espacial", "colonización de otros planetas", "singularidad tecnológica", "teletransportación", "inteligencia artificial superinteligente", "nanotecnología", "realidad aumentada", "bioingeniería", "medicina regenerativa", "energía limpia", "viajes en el tiempo", "clonación humana", "avances científicos", "prospectiva", "espacio exterior", "tecnología futurista", "transhumanismo", "máquinas inteligentes", "inteligencia artificial avanzada", "nanorobots", "realidad virtual", "biotecnología", "fusión nuclear", "propulsión espacial", "agujeros de gusano", "sociedad futura", "nanotecnología", "realidad aumentada", "bioingeniería", "medicina regenerativa", "energía limpia", "viajes en el tiempo", "clonación humana", "avances científicos", "prospectiva", "espacio exterior", "tecnología futurista", "transhumanismo", "máquinas inteligentes", "inteligencia artificial avanzada", "nanorobots", "realidad virtual", "biotecnología", "fusión nuclear", "propulsión espacial", "agujeros de gusano", "sociedad futura", "exploración cósmica", "colonización de Marte", "inteligencia artificial cuántica", "teletransporte cuántico", "genética avanzada", "tecnología de viajes espaciales", "nanomateriales", "tecnología de propulsión a chorro", "rejuvenecimiento biológico", "energía de fusión", "computación cuántica", "realidad virtual total", "ciudades sostenibles", "tecnología de vehículos voladores", "exploración oceánica", "vida extraterrestre", "turismo espacial", "clonación de órganos", "energía solar avanzada", "tecnología de invisibilidad", "colonización lunar", "conexiones cerebro-máquina", "biología sintética", "energía de antimateria", "telepatía cuántica", "reciclaje espacial", "tecnología de la teleportación", "inteligencia artificial en la educación", "edición genética", "tecnología de nanocámaras", "realidad aumentada en medicina", "realidad virtual terapéutica", "tecnología de alimentos del futuro", "tecnología de realidad virtual para juegos", "expansión del universo", "exploración de exoplanetas", "tecnología de energía eólica", "agricultura vertical", "tecnología de vida en otros planetas", "tecnología de propulsión a velocidad de la luz", "internet cuántico", "tecnología de imágenes cerebrales", "tecnología de vehículos autónomos aéreos", "robots inteligentes", "realidad aumentada en la educación", "tecnología de viajes en el tiempo", "telepatía avanzada", "biorrobots", "tecnología de dispositivos vestibles avanzados", "televisión holográfica", "tecnología de control mental", "tecnología de recolección de energía", "tecnología de viajes en el tiempo cuántico", "realidad aumentada para el entretenimiento", "tecnología de teletransportación humana", "biología sintética avanzada", "tecnología de propulsión de iones", "robots asistentes", "tecnología de comunicación por ondas cerebrales", "realidad virtual para el turismo", "tecnología de traducción de idiomas avanzada", "tecnología de energía de hidrógeno", "tecnología de aceleración de partículas", "células solares de próxima generación", "tecnología de alimentos del futuro", "vehículos autónomos terrestres", "tecnología de impresión 3D avanzada", "Siglo XXI", "Siglo XXII", "Siglo XXIII", "Siglo XXIV", "Siglo XXV", "Siglo XXVI", "Siglo XXVII", "Siglo XXVIII", "Siglo XXIX", "Siglo XXX", "Siglo XXXI", "Siglo XXXII", "Siglo XXXIII", "Siglo XXXIV", "Siglo XXXV", "Siglo XXXVI", "Siglo XXXVII", "Siglo XXXVIII", "Siglo XXXIX", "Siglo XL", "Siglo XLI", "Siglo XLII", "Siglo XLIII", "Siglo XLIV", "Siglo XLV", "Siglo XLVI", "Siglo XLVII", "Siglo XLVIII", "Siglo XLIX", "Siglo L", "Siglo LI", "Siglo LII", "Siglo LIII", "Siglo LIV", "Siglo LV", "Siglo LVI", "Siglo LVII", "Siglo LVIII", "Siglo LIX", "Siglo LX", "Siglo LXI", "Siglo LXII", "Siglo LXIII", "Siglo LXIV", "Siglo LXV", "Siglo LXVI", "Siglo LXVII", "Siglo LXVIII", "Siglo LXIX", "Siglo LXX", "Siglo LXXI", "Siglo LXXII", "Siglo LXXIII", "Siglo LXXIV", "Siglo LXXV", "Siglo LXXVI", "Siglo LXXVII", "Siglo LXXVIII", "Siglo LXXIX", "Siglo LXXX", "Siglo LXXXI", "Siglo LXXXII", "Siglo LXXXIII", "Siglo LXXXIV", "Siglo LXXXV", "Siglo LXXXVI", "Siglo LXXXVII", "Siglo LXXXVIII", "Siglo LXXXIX", "Siglo XC", "Siglo XCI", "Siglo XCII", "Siglo XCIII", "Siglo XCIV", "Siglo XCV", "Siglo XCVI", "Siglo XCVII", "Siglo XCVIII", "Siglo XCIX", "Siglo C"]:
          count_futuro += 1


  threshold_antiguo = 10
  threshold_contemporaneo = 10
  threshold_futuro = 10

  if count_antiguo >= threshold_antiguo:
    return "Anterior a la Edad Contemporánea"
  elif count_futuro >= threshold_futuro:
    return "Obra futurista"
  elif count_contemporaneo >= threshold_contemporaneo:
    return "Edad Contemporánea"
  else:
    if idioma==2:
        return "No hay un tiempo especifico"
    elif idioma==1:
        return"There is no specific time"
    elif idioma == 3:
        return"Il n'y a pas d'heure précise"
    elif idioma == 4:
      return"Es gibt keine bestimmte Zeit"
    elif idioma == 5:
      return"Não há horário específico"







