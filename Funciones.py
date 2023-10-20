import string
import unicodedata
from langdetect import detect
import nltk
try:
  nltk.data.find('tokenizers/punkt')
except LookupError:
  nltk.download('punkt')
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


def Identificar_personajes_con_su_frecuencia(contenido):
    personajes = {}
    str_contenido = " ".join(contenido)
    idioam=
    if idioma == 'es':
       palabras_prohibidas = del_words_esp
    elif idioma == 'en':
       palabras_prohibidas = del_words_en
    elif idioma == 'fr':
       palabras_prohibidas = del_words_fr
    elif idioma == 'de':
       palabras_prohibidas = del_words_deut
    else:
      palabras_prohibidas = del_words_port
       

    matches = re.findall(r'\b(?:[A-ZÁÉÍÓÚÜÑ][a-zA-ZÁÉÍÓÚÜÑáéíóúüñ]{2,}\s*){1,2}(?:[-\s][A-ZÁÉÍÓÚÜÑ][a-zA-ZÁÉÍÓÚÜÑáéíóúüñ]{2,})?\b', str_contenido)
    idioma = detect(str_contenido)
    matches = [match for match in matches if match.lower() not in stopwords.stopwords(idioma) and match.lower() not in palabras_prohibidas]
    for personaje in matches:
        if not re.search(r'\.\s' + re.escape(personaje), str_contenido):
            if personaje not in personajes:
                personajes[personaje] = 1
            else:
                personajes[personaje] += 1
    return personajes






#Función que identifica los personajes principales
def personajes_principales(contenido):
    personajes_frecuencia = Identificar_personajes_con_su_frecuencia(contenido)
    frecuencia_maxima = max(personajes_frecuencia.values(), default=0)
    porcentaje_minimo = 0.7
    personajes_principales = {personaje: frecuencia for personaje, frecuencia in personajes_frecuencia.items()
                            if frecuencia >= porcentaje_minimo * frecuencia_maxima}

    return personajes_principales
  
  

  

del_words_esp = ["Y", "O", "Ni", "Tampoco", "Además", "Asimismo", "Por lo tanto", "Por consiguiente", "En consecuencia", "Sin embargo", "A pesar de", "Aunque", "Por otro lado", "Mientras que", "Por el contrario", "A su vez", "Por ende", "Por lo que", "Dado que", "Puesto que", "Ya que", "A fin de que", "Con el fin de", "En resumen", "En conclusión", "Finalmente", "De hecho", "Es decir", "O sea", "Por ejemplo", "En otras palabras", "En primer lugar", "En segundo lugar", "Por último", "Primeramente", "En cambio", "Por lo general", "En realidad", "Por supuesto", "El", "La", "Los", "Las", "Un", "Una", "Unos", "Unas","Y", "Había", "Una vez", "Cuando", "Desde", "Érase una vez", "Aquel día", "Siempre", "Al principio", "Finalmente", "En aquel lugar", "Todo comenzó cuando", "Una fría mañana", "Contigo", "Oriente", "Occidente", "Sabio", "Santo Grial", "Muro", "Museo", "Organización", "Universidad", "Amnistía", "Internacional", "Organización", "Banco", "Mundial", "Fondo Monetario", "Día", "Año", "Navidad", "Revolución", "Viernes Santo", "Libro", "Niño", "Internacional", "Radio", "Voluntarios", "Fiesta", "Lirio", "Padrino", "Mago", "Noche", "Gioconda", "Persistencia", "Memoria", "Titanic", "Excalibur", "Santo Grial", "Muro de Berlín", "Museo Universitario de Ciencias y Artes", "Organización de las Naciones Unidas", "Real", "Academia", "Lengua", "Universidad", "Nacional", "Mujer", "Revolución", "Día", "Independencia", "Revolución", "Libro", "Mundial", "Cáncer", "Radio", "Voluntarios", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre", "Padrino", "Mago", "Gioconda", "Médico", "Profesor", "Ingeniero", "Abogado", "Enfermero", "Arquitecto", "Contable", "Actor", "Cantante", "Escritor", "Científico", "Periodista", "Chef", "Policía", "Bombero", "Astronauta", "Psicólogo", "Terapeuta", "Economista", "Electricista", "Plomero", "Carpintero", "Mecánico", "Diseñador", "Artista", "Veterinario", "Farmacéutico", "Conductor de camión", "Agricultor", "Comerciante", "Banquero", "Piloto", "Soldado", "Fotógrafo", "Actor de voz", "Modelo", "Terapeuta físico", "Terapeuta", "OMS", "ONU", "FBI", "CIA", "NASA", "UE", "OTAN", "UEFA", "UNICEF", "FMI", "OMC", "NATO", "CNN", "BBC", "UFO", "NYPD", "DIY", "VIP", "CEO", "AI", "FAQ", "UNESCO", "AIDS", "GPS", "WiFi"]

del_words_fr = ["Et", "Ou", "Ni", "Non plus", "De plus", "Ainsi", "Par conséquent", "Donc", "En conséquence", "Cependant", "Malgré", "Bien que", "D'autre part", "Tandis que", "Au contraire", "À son tour", "Par conséquent", "Donc", "Étant donné que", "Puisque", "Comme", "Afin que", "Dans le but de", "En résumé", "En conclusion", "Finalement", "En fait", "C'est-à-dire", "Autrement dit", "En premier lieu", "En deuxième lieu", "Enfin", "Premièrement", "Par contre", "En général", "En réalité", "Bien sûr", "Le", "La", "Les", "Un", "Une", "Des", "Et", "Il y avait", "Une fois", "Quand", "Depuis", "Il était une fois", "Ce jour-là", "Toujours", "Au début", "Enfin", "À cet endroit", "Tout a commencé quand", "Un matin froid", "Avec toi", "Orient", "Occident", "Sage", "Saint Graal", "Mur", "Musée", "Organisation", "Université", "Amnistie", "International", "Organisation", "Banque", "Mondiale", "Fonds monétaire", "Jour", "An", "Noël", "Révolution", "Vendredi Saint", "Livre", "Enfant", "International", "Radio", "Volontaires", "Fête", "Lys", "Parrain", "Magicien", "Nuit", "La Joconde", "Persistance", "Mémoire", "Titanic", "Excalibur", "Saint Graal", "Mur de Berlin", "Musée universitaire des sciences et des arts", "Organisation des Nations Unies", "Réel", "Académie", "Langue", "Université", "Femme", "Révolution", "Jour", "Indépendance", "Révolution", "Livre", "Mondial", "Cancer", "Radio", "Volontaires", "Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre", "Parrain", "Magicien", "Médecin", "Professeur", "Ingénieur", "Avocat", "Infirmière", "Architecte", "Comptable", "Acteur", "Chanteur", "Écrivain", "Scientifique", "Journaliste", "Chef", "Policier", "Pompier", "Astronaute", "Psychologue", "Thérapeute", "Économiste", "Électricien", "Plombier", "Menuisier", "Mécanicien", "Designer", "Artiste", "Vétérinaire", "Pharmacien", "Chauffeur de camion", "Agriculteur", "Commerçant", "Banquier", "Pilote", "Soldat", "Photographe", "Doubleur", "Mannequin", "Thérapeute physique", "Thérapeute", "OMS", "ONU", "FBI", "CIA", "NASA", "UE", "OTAN", "UEFA", "UNICEF", "FMI", "OMC", "OTAN", "CNN", "BBC", "OVNI", "NYPD", "FAÇON", "VIP", "PDG", "IA", "FAQ", "UNESCO", "SIDA", "GPS", "WiFi"]

del_words_en = ["And", "Or", "Neither", "Nor", "Furthermore", "Likewise", "Therefore", "Consequently", "In consequence", "However", "Despite", "Although", "On the other hand", "While", "On the contrary", "In turn", "Hence", "So", "Since", "Given that", "As", "In order to", "To", "In summary", "In conclusion", "Finally", "Actually", "That is", "In other words", "First", "Second", "Finally", "Primarily", "On the other hand", "Generally", "In reality", "Of course", "The", "The", "The", "The", "A", "A", "Some", "Some", "And", "There was", "Once upon a time", "When", "From", "Once upon a time", "That day", "Always", "At the beginning", "Finally", "In that place", "Everything started when", "A cold morning", "With you", "East", "West", "Wise", "Holy Grail", "Wall", "Museum", "Organization", "University", "Amnesty", "International", "Organization", "Bank", "World", "International Monetary Fund", "Day", "Year", "Christmas", "Revolution", "Good Friday", "Book", "Child", "International", "Radio", "Volunteers", "Party", "Lily", "Godfather", "Wizard", "Night", "Mona Lisa", "Persistence", "Memory", "Titanic", "Excalibur", "Holy Grail", "Berlin Wall", "University Museum of Science and Arts", "United Nations", "Royal", "Academy", "Language", "National", "Woman", "Revolution", "Day", "Independence", "Revolution", "Book", "World", "Cancer", "Radio", "Volunteers", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December", "Godfather", "Wizard", "Mona Lisa", "Doctor", "Teacher", "Engineer", "Lawyer", "Nurse", "Architect", "Accountant", "Actor", "Singer", "Writer", "Scientist", "Journalist", "Chef", "Police", "Firefighter", "Astronaut", "Psychologist", "Therapist", "Economist", "Electrician", "Plumber", "Carpenter", "Mechanic", "Designer", "Artist", "Veterinarian", "Pharmacist", "Truck driver", "Farmer", "Merchant", "Banker", "Pilot", "Soldier", "Photographer", "Voice actor", "Model", "Physical therapist", "Therapist", "WHO", "UN", "FBI", "CIA", "NASA", "EU", "NATO", "UEFA", "UNICEF", "IMF", "WTO", "NATO", "CNN", "BBC", "UFO", "NYPD", "DIY", "VIP", "CEO", "AI", "FAQ", "UNESCO", "AIDS", "GPS", "WiFi"]

del_words_deut = ["Und", "Oder", "Weder", "Noch", "Darüber hinaus", "Ebenso", "Deshalb", "Folglich", "Infolgedessen", "Jedoch", "Obwohl", "Andererseits", "Während", "Im Gegensatz dazu", "Im Gegenzug", "Folglich", "Daher", "So", "Da", "Da", "Um zu", "Um", "Zusammenfassend", "Zusammenfassend", "Schließlich", "Tatsächlich", "Das heißt", "Das heißt", "Beispielsweise", "Mit anderen Worten", "Erstens", "Zweitens", "Schließlich", "Zunächst", "Andererseits", "Im Allgemeinen", "Tatsächlich", "Natürlich", "Der", "Die", "Die", "Die", "Ein", "Eine", "Einige", "Einige", "Und", "Es gab", "Es war einmal", "Wenn", "Von", "Es war einmal", "An diesem Tag", "Immer", "Am Anfang", "Schließlich", "An diesem Ort", "Alles begann, als", "An einem kalten Morgen", "Mit dir", "Osten", "Westen", "Weise", "Heiliger Gral", "Mauer", "Museum", "Organisation", "Universität", "Amnestie", "International", "Organisation", "Bank", "Welt", "Internationaler Währungsfonds", "Tag", "Jahr", "Weihnachten", "Revolution", "Karfreitag", "Buch", "Kind", "International", "Radio", "Freiwillige", "Party", "Lilie", "Pate", "Zauberer", "Nacht", "Mona Lisa", "Beharrlichkeit", "Erinnerung", "Titanic", "Excalibur", "Heiliger Gral", "Berliner Mauer", "Universitätsmuseum für Wissenschaft und Kunst", "Vereinte Nationen", "Königlich", "Akademie", "Sprache", "National", "Frau", "Revolution", "Tag", "Unabhängigkeit", "Revolution", "Buch", "Welt", "Krebs", "Radio", "Freiwillige", "Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember", "Pate", "Zauberer", "Mona Lisa", "Arzt", "Lehrer", "Ingenieur", "Anwalt", "Krankenschwester", "Architekt", "Buchhalter", "Schauspieler", "Sänger", "Schriftsteller", "Wissenschaftler", "Journalist", "Koch", "Polizei", "Feuerwehrmann", "Astronaut", "Psychologe", "Therapeut", "Ökonom", "Elektriker", "Installateur", "Tischler", "Mechaniker", "Designer", "Künstler", "Tierarzt", "Apotheker", "Truckfahrer", "Bauer", "Händler", "Bankier", "Pilot", "Soldat", "Fotograf", "Synchronsprecher", "Modell", "Physiotherapeut", "Therapeut", "WHO", "UNO", "FBI", "CIA", "NASA", "EU", "NATO", "UEFA", "UNICEF", "IWF", "WTO", "NATO", "CNN", "BBC", "UFO", "NYPD", "DIY", "VIP", "CEO", "KI", "FAQ", "UNESCO", "AIDS", "GPS", "WLAN"]

del_words_port = ["E", "Ou", "Nem", "Tampouco", "Além disso", "Do mesmo modo", "Portanto", "Consequentemente", "Em consequência", "No entanto", "Apesar de", "Embora", "Por outro lado", "Enquanto", "Ao contrário", "Por sua vez", "Assim", "Então", "Já que", "Uma vez que", "Visto que", "Dado que", "A fim de que", "Para", "Em resumo", "Em conclusão", "Finalmente", "Na realidade", "Ou seja", "Por exemplo", "Em outras palavras", "Em primeiro lugar", "Em segundo lugar", "Finalmente", "Primeiramente", "Em contrapartida", "Geralmente", "Na realidade", "Claro", "O", "A", "Os", "As", "Um", "Uma", "Alguns", "Algumas", "E", "Havia", "Era uma vez", "Quando", "Desde", "Era uma vez", "Naquele dia", "Sempre", "No início", "Finalmente", "Naquele lugar", "Tudo começou quando", "Em uma manhã fria", "Contigo", "Oriente", "Ocidente", "Sábio", "Santo Graal", "Muro", "Museu", "Organização", "Universidade", "Anistia", "Internacional", "Organização", "Banco", "Mundial", "Fundo Monetário Internacional", "Dia", "Ano", "Natal", "Revolução", "Sexta-feira Santa", "Livro", "Criança", "Internacional", "Rádio", "Voluntários", "Festa", "Lírio", "Padrinho", "Mago", "Noite", "Mona Lisa", "Persistência", "Memória", "Titanic", "Excalibur", "Santo Graal", "Muro de Berlim", "Museu Universitário de Ciências e Artes", "Nações Unidas", "Real", "Academia", "Língua", "Nacional", "Mulher", "Revolução", "Dia", "Independência", "Revolução", "Livro", "Câncer", "Rádio", "Voluntários", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro", "Padrinho", "Mago", "Mona Lisa", "Médico", "Professor", "Engenheiro", "Advogado", "Enfermeiro", "Arquiteto", "Contador", "Ator", "Cantor", "Escritor", "Cientista", "Jornalista", "Chef", "Polícia", "Bombeiro", "Astronauta", "Psicólogo", "Terapeuta", "Economista", "Eletricista", "Encanador", "Carpinteiro", "Mecânico", "Designer", "Artista", "Veterinário", "Farmacêutico", "Motorista de caminhão", "Fazendeiro", "Comerciante", "Bancário", "Piloto", "Soldado", "Fotógrafo", "Dublador", "Modelo", "Fisioterapeuta", "Terapeuta", "OMS", "ONU", "FBI", "CIA", "NASA", "UE", "OTAN", "UEFA", "UNICEF", "FMI", "OMC", "OTAN", "CNN", "BBC", "ÓVNI", "NYPD", "Faça você mesmo", "VIP", "CEO", "IA", "FAQ", "UNESCO", "AIDS", "GPS", "Wi-Fi"]










  

def identificar_lugares(texto):
  lugares = {}
  texto=" ".join(texto)
  palabras = texto.split()
  palabras_incluidas = set()
  toponimos=["En","en","Bibioteca","los","Los","cerca de", "al sur de", "al norte de", "al este de", "al sur", "al este", "Al norte","Al sur", "Al este", "Al oeste", "En el medio", "En la periferia", "En la vecindad", "Hacia el sur", "Hacia el norte", "Hacia el este", "Hacia el oeste", "ciudad", "ciudades", "Ciudad", "plaza", "Plaza", "Plazas", "plazas", "Ciudades", "Camino","camino", "caminos","lugar", "Lugar", "Caminos", "calle","Calles", "Calle","calles", "pueblo","Pueblo", "Pueblos", "pueblos", "villa", "Villa", "villas", "Villas", "país", "País", "Países" ,"paises" ,"Países", "provincia", "Provincia", "provincias", "Provincias", "departamento", "Departamento", "departamentos", "Departamentos", "distrito","Distrito", "distritos", "Distritos", "barrio", "Barrio", "barrios", "Barrios", "calle", "Calle", "calles", "Calles", "avenida", "Avenida", "avenidas", "Avenidas", "avenida", "Avenida", "avenidas", "Bogotá", "Calí", "Medellín", "Boyaca", "Amazonas", "Antioquia", "Córdoba", "Arauca", "Cúcuta", "Guajira", "reino", "Reino", "taberna", "Taberna", "Casa", "casa", "Estados Unidos", "China", "Rusia", "India", "Brasil", "Canadá", "Alemania", "Francia", "Reino Unido", "Italia", "Japón", "Australia", "España", "México", "Argentina", "Sudáfrica", "Nigeria", "Egipto", "Kenia", "Nigeria", "Corea del Sur", "Arabia Saudita", "Irán", "Turquía", "Indonesia", "Pakistán", "Bangladesh", "Vietnam", "Tailandia", "Malasia", "Filipinas", "Singapur", "México", "Colombia", "Chile", "Perú", "Ecuador", "Venezuela", "Uruguay", "Costa Rica", "Cuba", "República Dominicana", "Guatemala", "Honduras", "El Salvador", "Nicaragua", "Panamá", "Bolivia", "Paraguay", "Qatar", "Emiratos Árabes Unidos", "Israel", "Jordania", "Irak", "Siria", "Afganistán", "Pakistán", "Nepal", "Bután", "Sri Lanka", "Maldivas", "Malí", "Senegal", "Ghana", "Costa de Marfil", "Angola", "Mozambique", "Marruecos", "Argelia", "Túnez", "Libia", "Sudán", "Etiopía", "Somalia", "Uganda", "Ruanda", "Burundi", "Tanzania", "Seychelles", "Madagascar", "Australia", "Nueva Zelanda", "Fiji", "Papúa Nueva Guinea", "Islas Salomón", "Kiribati", "Tuvalu", "Samoa", "Tonga", "Vanuatu", "Nauru", "Micronesia", "Palaos", "Islas Marshall", "Corea del Norte", "Mongolia", "Tayikistán", "Turkmenistán", "Uzbekistán", "Kazajistán", "Noruega", "Suecia", "Finlandia", "Dinamarca", "Portugal", "Países Bajos", "Bélgica", "Luxemburgo", "Suiza", "Austria", "República Checa", "Eslovaquia", "Hungría", "Eslovenia", "Croacia", "Ucrania", "Bielorrusia", "Polonia", "Armenia", "Grecia", "Taiwán", "Camboya"]

  for i, palabra in enumerate(palabras):
    sentences = sent_tokenize(text)
    geolocator = Nominatim(user_agent="place_recognition")

  # Extract entities and recognize places
    places = []
    for sentence in sentences:
        words = word_tokenize(sentence)
        tagged_words = nltk.pos_tag(words)
        named_entities = ne_chunk(tagged_words)

        for entity in named_entities:
            if isinstance(entity, nltk.Tree) and entity.label() == 'GPE':
              location_name = ' '.join([leaf[0] for leaf in entity.leaves()])
              location = geolocator.geocode(location_name)
              if location:
                  places.append({
                      'name': location_name,
                      'latitude': location.latitude,
                      'longitude': location.longitude
                  })

  return places

def identificar_tiempo_obra(contenido):
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
    return "No hay un tiempo especifico"


