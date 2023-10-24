import Funciones
import string
import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib as mpl
import os

print("Welcome to the Book Analyzer\n")
print("Select your language:")
print("1. English")
print("2. Español")
print("3. Français")
print("4. Deutsch")
print("5. Português")

opcion_lenguage = int(input("Input your option: "))

while True:
    if 1<=opcion_lenguage<=5:
        print("You have selected the option: ",opcion_lenguage)
        break
    else:
        print("You have selected an invalid option")
        opcion_lenguage = int(input("Input a valid option: "))
abecedario = string.ascii_lowercase 
frecuentes_por_idioma = {}
bucle = 1

if opcion_lenguage == 1:
  print("\nWelcome to the Book Analyzer. This program was created as a final project for the Computer Programming course at the National University of Colombia. The purpose of this project is the automatic analysis of texts to extract relevant information from its content. For this, the program performs different linguistic analyzes that allow characterizing and processing .txt files in a structured manner.\n")
  input("Press Enter to continue...")
  os.system('cls' if os.name == 'nt' else 'clear')
  direccion_libro = str(input("\nPlease enter the address of the text file you want to analyze (for your convenience, save the .txt file in the same program folder): "))
  try:
        with open(direccion_libro, 'r', encoding='utf-8') as archivo:
            contenido = archivo.readlines()
  except FileNotFoundError:
        # Si el archivo no se encuentra, mostrar un mensaje y salir del programa
        print(f"Error: File not found at the specified address:{direccion_libro}")
        bucle = 0  # Salir del bucle principal
  except Exception as e:
        # Capturar cualquier otra excepción y mostrar un mensaje de error
        print(f"Unexpected error while opening the file: {e}")
        bucle = 0  # Salir del bucle principal
  while bucle == 1:
        # Mostrar el menú y procesar la opción del usuario
        print("\nThe program offers the following tools for analyzing your text:\n",
          "1.  Count the number of characters in the text\n",
          "2.  Count the number of words in the text\n",
          "3.  Create a histogram of the frequency of each word in the text\n",
          "4.  Create a histogram of the length of words in the text\n",
          "5.  Display the top 100 most frequent words in the text\n",
          "6.  Calculate the number of distinct words in the text\n",
          "7.  Identify the language of the text\n",
          "8.  Display the top 50 most frequent words in the text excluding stopwords\n",
          "9.  Identify the characters in the work along with their mention frequency\n",
          "10. Main characters in the work\n",
          "11. Identify the places where the work takes place (only for texts in Spanish)\n",
          "12. Identify the time period in which the work takes place (only for texts in Spanish)\n"
          " 13. Exit")
        opcion_herramienta = int(input("Select the option you want to perform: "))

        while True:
            if 1 <= opcion_herramienta <=13:
                print("\nYou have chosen option number:", opcion_herramienta)
                break
            else:
                print("\nYou entered an invalid option")
                opcion_herramienta = int(input("Enter a valid option: "))

        if opcion_herramienta == 1:
                print('The number of characters in the text is: ', Funciones.contar_caracteres(contenido))
        elif opcion_herramienta == 2:
            print('The number of words in the text is:: ',Funciones.contar_palabras(contenido))
        elif opcion_herramienta == 3:
            print("To view the histogram, please go to the program output with which you are running the code")
            print("To continue, please close the program output with which you are running the code")
            x = list(abecedario)
            y = Funciones.calcular_frecuencia_letras(contenido, x)
            plt.title('Frequency of letters in the book', fontsize=30)
            plt.xlabel('Letters', fontsize=20)
            plt.ylabel('Frequency', fontsize=20)
            cmap = mpl.colormaps['RdYlGn']
            norm = colors.Normalize(vmin=min(y), vmax=max(y))
            histogram_abc = plt.bar(x, y, color=cmap(norm(y)))
            for bar in histogram_abc:
                yval = bar.get_height()
                plt.text(bar.get_x(), yval + .005, yval)
            plt.tight_layout()
            plt.show()
        elif opcion_herramienta== 4:
            print("To view the histogram, please go to the program output with which you are running the code")
            print("To continue, please close the program output with which you are running the code")
            x=list(Funciones.contar_palabras_por_longitud(contenido))
            y=list(Funciones.contar_palabras_por_longitud(contenido).values())
            cmap = mpl.colormaps['RdYlGn']
            norm = colors.Normalize(vmin=min(y), vmax=max(y))
            histogram_len = plt.bar(x, y, color=cmap(norm(y)))
            for bar in histogram_len:
                yval = bar.get_height()
                plt.text(bar.get_x(), yval + .005, yval)
            plt.title('Frequency of words by length', fontsize=30)
            plt.xlabel('Word Length', fontsize=20)
            plt.ylabel('Frecuencia', fontsize=20)
            plt.tight_layout()
            plt.show()  
        elif opcion_herramienta == 5:
            print(Funciones.contar_frecuencia_palabras(contenido))
        elif opcion_herramienta == 6:
          print("The distinct number of words present in your text is: ",end="")
          print(Funciones.calcular_numero_distinto_palabras(contenido))
        elif opcion_herramienta == 7:
          print("The language of your text is: ",end="")
          print(Funciones.identificar_idioma(contenido))
        elif opcion_herramienta == 8:
          print("The top 50 most frequent words in your text excluding stopwords are: ",end="")
          print(Funciones.obtener_palabras_frecuentes_sin_stopwords(contenido))
        elif opcion_herramienta == 9:
          print("The characters present in your text along with their frequencies are: ")
          personajes=Funciones.Identificar_personajes_con_su_frecuencia(contenido)
          personajes_ordenados = sorted(personajes.items(), key=lambda x: x[1], reverse=True)
          for i, (personaje, frecuencia) in enumerate(personajes_ordenados, start=1):
                print(f"{i}. {personaje} (Frecuency: {frecuencia})")
        elif opcion_herramienta == 10:
           print("The main characters in your text are: ")
           personajes=Funciones.personajes_principales(contenido)
           personajes_ordenados = sorted(personajes.items(), key=lambda x: x[1], reverse=True)
           for i, (personaje, frecuencia) in enumerate(personajes_ordenados, start=1):
              print(f"{i}. {personaje} (Frecuency: {frecuencia})")
        elif opcion_herramienta == 11:
          lugares_identificados=Funciones.identificar_lugares(contenido)
          h=[]
          for i in range(len(lugares_identificados)):
              if lugares_identificados[i] not in h:
                  h.append(lugares_identificados[i])
          print("The identified places in your text are: ")
          Funciones.imprimir_lugares(h) 
        elif opcion_herramienta == 12:
           print("The time period in which your text takes place is: \n",Funciones.identificar_tiempo_obra(contenido,opcion_lenguage)) 
        elif opcion_herramienta == 13:
          print("Exiting the program...")
          break
        bucle = int(input("\nDo you want to use the program again?\n1. Yes\n2. No\n"))
        if bucle==1:
          os.system('cls' if os.name=='nt' else 'clear')
        elif bucle==2:
          os.system('cls' if os.name=='nt' else 'clear')
          print("Exiting the program...")
          break

elif opcion_lenguage == 2:
 print(
"\nBienvenido a Book Analyzer. Este es un programa realizado como proyecto final para la materia de programación de computadores de la Universidad Nacional de Colombia. Este proyecto tiene como finalidad el analisis de textos de forma automatizada para extraer información relevante de su contenido. Para este fín el programa realiza distintos análisis lingüísticos que permiten caracterizar y procesar archivos txt de manera estructurada.\n",
)
 input("Oprima Enter para continuar...")
 os.system('cls' if os.name=='nt' else 'clear')

 direccion_libro = str(input("\nPor favor ingrese la dirección del archivo de texto que desea analizar (para su comodidad guarde el archivo .txt en la misma carpeta del programa): "))
 try:
      with open(direccion_libro, 'r', encoding='utf-8') as archivo:
          contenido = archivo.readlines()
 except FileNotFoundError:
      # Si el archivo no se encuentra, mostrar un mensaje y salir del programa
      print(f"Error: No se encontró el archivo en la dirección especificada: {direccion_libro}")
      bucle = 0  # Salir del bucle principal
 except Exception as e:
      # Capturar cualquier otra excepción y mostrar un mensaje de error
      print(f"Error inesperado al abrir el archivo: {e}")
      bucle = 0  # Salir del bucle principal
 while bucle == 1:
      # Mostrar el menú y procesar la opción del usuario
      print("\nEl programa ofrece las siguientes herramientas para el analisis de su texto:\n",
            "1.  Contar la cantidad de caracteres presentes en el texto \n",
            "2.  Contar la Cantidad de palabras presentes en el texto\n",
            "3.  Realizar un histograma de la frecuencia de cada palabra en el texto\n",
            "4.  Realizar un histograma de la longitud de las palabras presentes del texto \n",
            "5.  Mostrar las 100 palabras mas frecuentes en el texto\n",
            "6.  Calcular número distinto de palabras presentes en el texto\n",
            "7.  Identificar el idioma en que se encuentra el texto\n",
            "8.  Mostrar las 50 palabras mas frecuentes en el texto sin incluir stopwords\n",
            "9.  Identificar los personajes de la obra, junto a la frecuencia con la que se mencionan\n",
            "10. Personajes principales en la obra \n",
            "11. Identificar los lugares en los que se desarrolla la obra (solo para textos en español)\n",
            "12. Identificar el tiempo en el que transcurre la obra (solo para textos en español)\n"
            " 13. Salir")
      opcion_herramienta = int(input("Seleccione la opción que desea realizar:"))

      while True:
          if 1 <= opcion_herramienta <=13:
              print("\nHa elijido la opción número:", opcion_herramienta)
              break
          else:
              print("\nHa ingresado una opción invalida")
              opcion_herramienta = int(input("Ingrese una opción valida: "))

      if opcion_herramienta == 1:
              print('La cantidad de caracteres presentes en el texto son: ', Funciones.contar_caracteres(contenido))
      elif opcion_herramienta == 2:
          print('La cantidad de palabras presentes en el texto son: ',Funciones.contar_palabras(contenido))
      elif opcion_herramienta == 3:
          print("Para visualizar el histograma por favor dirigise hacia la  salida del programa con el cual esta ejecutando el código")
          print("Para continuar, por favor cierre la salida del programa con el cual esta ejecutando el código")
          x = list(abecedario)
          y = Funciones.calcular_frecuencia_letras(contenido, x)
          plt.title('Frecuencia de letras en el libro', fontsize=30)
          plt.xlabel('Letras', fontsize=20)
          plt.ylabel('Frecuencia', fontsize=20)
          cmap = mpl.colormaps['RdYlGn']
          norm = colors.Normalize(vmin=min(y), vmax=max(y))
          histogram_abc = plt.bar(x, y, color=cmap(norm(y)))
          for bar in histogram_abc:
              yval = bar.get_height()
              plt.text(bar.get_x(), yval + .005, yval)
          plt.tight_layout()
          plt.show()
      elif opcion_herramienta== 4:
          print("Para visualizar el histograma por favor dirigise hacia la  salida del programa con el cual esta ejecutando el código")
          print("Para continuar, por favor cierre la salida del programa con el cual esta ejecutando el código")
          x=list(Funciones.contar_palabras_por_longitud(contenido))
          y=list(Funciones.contar_palabras_por_longitud(contenido).values())
          cmap = mpl.colormaps['RdYlGn']
          norm = colors.Normalize(vmin=min(y), vmax=max(y))
          histogram_len = plt.bar(x, y, color=cmap(norm(y)))
          for bar in histogram_len:
              yval = bar.get_height()
              plt.text(bar.get_x(), yval + .005, yval)
          plt.title('Frecuencia de palabras por longitud', fontsize=30)
          plt.xlabel('Longitud de palabras', fontsize=20)
          plt.ylabel('Frecuencia', fontsize=20)
          plt.tight_layout()
          plt.show()  
      elif opcion_herramienta == 5:
          print(Funciones.contar_frecuencia_palabras(contenido))
      elif opcion_herramienta == 6:
        print("El número distinto de palabras presentes en su texto son: ",end="")
        print(Funciones.calcular_numero_distinto_palabras(contenido))
      elif opcion_herramienta == 7:
        print("El idioma de su  texto es: ",end="")
        print(Funciones.identificar_idioma(contenido))
      elif opcion_herramienta == 8:
        print("Las 50 palabras mas frecuentes en su texto sin tener en cuenta stopwords son: ",end="")
        print(Funciones.obtener_palabras_frecuentes_sin_stopwords(contenido))
      elif opcion_herramienta == 9:
        print("Los personajes presentes en su texto son: ")
        personajes=Funciones.Identificar_personajes_con_su_frecuencia(contenido)
        personajes_ordenados = sorted(personajes.items(), key=lambda x: x[1], reverse=True)
        for i, (personaje, frecuencia) in enumerate(personajes_ordenados, start=1):
              print(f"{i}. {personaje} (Frecuencia: {frecuencia})")
      elif opcion_herramienta == 10:
         print("Los personajes principales de su texto son: ")
         personajes=Funciones.personajes_principales(contenido)
         personajes_ordenados = sorted(personajes.items(), key=lambda x: x[1], reverse=True)
         for i, (personaje, frecuencia) in enumerate(personajes_ordenados, start=1):
            print(f"{i}. {personaje} (Frecuency: {frecuencia})")
      elif opcion_herramienta == 11:
        lugares_identificados=Funciones.identificar_lugares(contenido)
        h=[]
        for i in range(len(lugares_identificados)):
            if lugares_identificados[i] not in h:
                h.append(lugares_identificados[i])
        print("Los lugares identificados en su texto son: ")
        Funciones.imprimir_lugares(h)       
      elif opcion_herramienta == 12:
         print("El tiempo en el cual transcurre su texto es: \n",Funciones.identificar_tiempo_obra(contenido,opcion_lenguage)) 
      elif opcion_herramienta == 13:
        print("Saliendo del programa...")
        break
      bucle = int(input("\n Desea volver a utilizar el programa?\n1. Si\n2. No\n"))
      if bucle==1:
        os.system('cls' if os.name=='nt' else 'clear')
      elif bucle==2:
        os.system('cls' if os.name=='nt' else 'clear')
        print("Saliendo del programa...")
        break

elif opcion_lenguage == 3:
 print("\nBienvenue sur l'analyseur de livres. Ce programme a été créé comme projet final pour le cours de programmation informatique de l'Université Nationale de Colombie. Le but de ce projet est l'analyse automatisée de textes pour en extraire des informations pertinentes. À cette fin, le programme effectue différentes analyses linguistiques qui permettent de caractériser et de traiter les fichiers txt de manière structurée.\n")
 input("Appuyez sur Entrée pour continuer...")
 os.system('cls' if os.name=='nt' else 'clear')
 bucle = 1
 direccion_libro = str(input("\nVeuillez entrer l'adresse du fichier texte que vous souhaitez analyser (pour votre commodité, enregistrez le fichier .txt dans le même dossier que le programme): "))
 try:
      with open(direccion_libro, 'r', encoding='utf-8') as archivo:
          contenido = archivo.readlines()
 except FileNotFoundError:
      # Si le fichier n'est pas trouvé, afficher un message et quitter le programme
      print(f"Erreur : Le fichier n'a pas été trouvé à l'adresse spécifiée : {direccion_libro}")
      bucle = 0  # Quitter la boucle principale
 except Exception as e:
      # Capturer toute autre exception et afficher un message d'erreur
      print(f"Erreur inattendue lors de l'ouverture du fichier : {e}")
      bucle = 0  # Quitter la boucle principale
 while bucle == 1:
      # Afficher le menu et traiter l'option de l'utilisateur
      print("\nLe programme propose les outils suivants pour l'analyse de votre texte:\n",
            "1.  Compter le nombre de caractères présents dans le texte \n",
            "2.  Compter le nombre de mots présents dans le texte\n",
            "3.  Créer un histogramme de la fréquence de chaque mot dans le texte\n",
            "4.  Créer un histogramme de la longueur des mots présents dans le texte \n",
            "5.  Afficher les 100 mots les plus fréquents dans le texte\n",
            "6.  Calculer le nombre de mots distincts présents dans le texte\n",
            "7.  Identifier la langue dans laquelle se trouve le texte\n",
            "8.  Afficher les 50 mots les plus fréquents dans le texte sans inclure les stopwords\n",
            "9.  Identifier les personnages de l'œuvre, avec leur fréquence d'apparition\n",
            "10. Personnages principaux dans l'œuvre \n",
            "11. Identifier les lieux où se déroule l'œuvre (uniquement pour les textes en espagnol)\n",
            "12. Identifier le temps pendant lequel l'œuvre se déroule (uniquement pour les textes en espagnol)\n"
            " 13. Quitter")

      option_outil = int(input("Veuillez sélectionner l'option que vous souhaitez réaliser :"))

      while True:
          if 1 <= option_outil <= 13:
              print("\nVous avez choisi l'option numéro :", option_outil)
              break
          else:
              print("\nVous avez saisi une option invalide")
              option_outil = int(input("Veuillez saisir une option valide : "))

      if option_outil == 1:
          print("Le nombre de caractères présents dans le texte est : ", Funciones.contar_caracteres(contenido))
      elif option_outil == 2:
          print("Le nombre de mots présents dans le texte est : ", Funciones.contar_palabras(contenido))
      elif option_outil == 3:
          print("Pour visualiser l'histogramme, veuillez vous rendre à la sortie du programme avec lequel vous exécutez le code")
          print("Pour continuer, veuillez fermer la sortie du programme avec lequel vous exécutez le code")
          x = list(abecedario)
          y = Funciones.calcular_frecuencia_letras(contenido, x)
          plt.title('Fréquence des lettres dans le livre', fontsize=30)
          plt.xlabel('Lettres', fontsize=20)
          plt.ylabel('Fréquence', fontsize=20)
          cmap = mpl.colormaps['RdYlGn']
          norm = colors.Normalize(vmin=min(y), vmax=max(y))
          histogram_abc = plt.bar(x, y, color=cmap(norm(y)))
          for bar in histogram_abc:
              yval = bar.get_height()
              plt.text(bar.get_x(), yval + .005, yval)
          plt.tight_layout()
          plt.show()
      elif option_outil == 4:
          print("Pour visualiser l'histogramme, veuillez vous rendre à la sortie du programme avec lequel vous exécutez le code")
          print("Pour continuer, veuillez fermer la sortie du programme avec lequel vous exécutez le code")
          x = list(Funciones.contar_palabras_por_longitud(contenido))
          y = list(Funciones.contar_palabras_por_longitud(contenido).values())
          cmap = mpl.colormaps['RdYlGn']
          norm = colors.Normalize(vmin=min(y), vmax=max(y))
          histogram_len = plt.bar(x, y, color=cmap(norm(y)))
          for bar in histogram_len:
              yval = bar.get_height()
              plt.text(bar.get_x(), yval + .005, yval)
          plt.title('Fréquence des mots par longueur', fontsize=30)
          plt.xlabel('Longueur des mots', fontsize=20)
          plt.ylabel('Fréquence', fontsize=20)
          plt.tight_layout()
          plt.show()
      elif option_outil == 5:
          print(Funciones.contar_frecuencia_palabras(contenido))
      elif option_outil == 6:
          print("Le nombre distinct de mots présents dans votre texte est : ", end="")
          print(Funciones.calcular_numero_distinto_palabras(contenido))
      elif option_outil == 7:
          print("La langue de votre texte est : ", end="")
          print(Funciones.identificar_idioma(contenido))
      elif option_outil == 8:
          print("Les 50 mots les plus fréquents dans votre texte sans inclure les stopwords sont : ", end="")
          print(Funciones.obtener_palabras_frecuentes_sin_stopwords(contenido))
      elif option_outil == 9:
          print("Les personnages présents dans votre texte sont : ")
          personajes=Funciones.Identificar_personajes_con_su_frecuencia(contenido)
          personajes_ordenados = sorted(personajes.items(), key=lambda x: x[1], reverse=True)
          for i, (personaje, frecuencia) in enumerate(personajes_ordenados, start=1):
              print(f"{i}. {personaje} (Fréquence: {frecuencia})")
      elif option_outil == 10:
          print("Les personnages principaux de votre texte sont : ")
          personajes=Funciones.personajes_principales(contenido)
          personajes_ordenados = sorted(personajes.items(), key=lambda x: x[1], reverse=True)
          for i, (personaje, frecuencia) in enumerate(personajes_ordenados, start=1):
            print(f"{i}. {personaje} (Fréquence: {frecuencia})")
      elif option_outil == 11:
        lugares_identificados = Funciones.identificar_lugares(contenido)
        h = []
        for i in range(len(lugares_identificados)):
            if lugares_identificados[i] not in h:
                h.append(lugares_identificados[i])
        print("Les lieux identifiés dans votre texte sont : ")
        imprimir_lugares(h)       
      elif option_outil == 12:
          print("Le temps pendant lequel votre texte se déroule est : \n",
               Funciones.identificar_tiempo_obra(contenido,opcion_lenguage))
      elif option_outil == 13:
          print("Sortie du programme...")
          break
      bucle = int(input("\n Souhaitez-vous utiliser à nouveau le programme?\n1. Oui\n2. Non\n"))
      if bucle == 1:
          os.system('cls' if os.name == 'nt' else 'clear')
      elif bucle == 2:
          os.system('cls' if os.name == 'nt' else 'clear')
          print("Sortie du programme...")
          break

elif opcion_lenguage == 4:
 print("\nWillkommen beim Book Analyzer. Dieses Programm wurde als Abschlussprojekt für den Computerprogrammierkurs der Universidad Nacional de Colombia erstellt. Ziel dieses Projekts ist die automatische Analyse von Texten, um relevante Informationen aus ihrem Inhalt zu extrahieren. Zu diesem Zweck führt das Programm verschiedene linguistische Analysen durch, die eine strukturierte Kennzeichnung und Verarbeitung von .txt-Dateien ermöglichen.\n")
 input("Drücken Sie Enter, um fortzufahren...")
 os.system('cls' if os.name == 'nt' else 'clear')
 direccion_libro = str(input("\nBitte geben Sie die Adresse der Textdatei ein, die Sie analysieren möchten (zum Ihrer Bequemlichkeit, speichern Sie die .txt-Datei im gleichen Programmordner): "))
 try:
      with open(direccion_libro, 'r', encoding='utf-8') as archivo:
          contenido = archivo.readlines()
 except FileNotFoundError:
      # Wenn die Datei nicht gefunden wird, eine Meldung anzeigen und das Programm verlassen
      print(f"Fehler: Datei nicht gefunden unter der angegebenen Adresse: {direccion_libro}")
      bucle = 0  # Den Hauptloop verlassen
 except Exception as e:
      # Jegliche andere Ausnahme abfangen und eine Fehlermeldung anzeigen
      print(f"Unerwarteter Fehler beim Öffnen der Datei: {e}")
      bucle = 0  # Den Hauptloop verlassen
 while bucle == 1:
      # Menü anzeigen und die Benutzeroption verarbeiten
      print("\nDas Programm bietet die folgenden Werkzeuge zur Analyse Ihres Textes an:\n",
            "1.  Anzahl der Zeichen im Text zählen\n",
            "2.  Anzahl der Wörter im Text zählen\n",
            "3.  Histogramm der Häufigkeit jedes Wortes im Text erstellen\n",
            "4.  Histogramm der Länge der Wörter im Text erstellen\n",
            "5.  Die 100 häufigsten Wörter im Text anzeigen\n",
            "6.  Die Anzahl der verschiedenen Wörter im Text berechnen\n",
            "7.  Die Sprache des Textes identifizieren\n",
            "8.  Die 50 häufigsten Wörter im Text anzeigen, ohne Stoppwörter\n",
            "9.  Die Charaktere in der Arbeit zusammen mit ihrer Häufigkeit identifizieren\n",
            "10. Hauptcharaktere in der Arbeit\n",
            "11. Die Orte identifizieren, an denen die Arbeit stattfindet (nur für Texte auf Spanisch)\n",
            "12. Die Zeitspanne identifizieren, in der die Arbeit stattfindet (nur für Texte auf Spanisch)\n"
            " 13. Beenden")
      opcion_herramienta = int(input("Wählen Sie die Option aus, die Sie ausführen möchten: "))

      while True:
          if 1 <= opcion_herramienta <=13:
              print("\nSie haben die Option Nummer gewählt:", opcion_herramienta)
              break
          else:
              print("\nSie haben eine ungültige Option eingegeben")
              opcion_herramienta = int(input("Geben Sie eine gültige Option ein: "))

      if opcion_herramienta == 1:
          print('Die Anzahl der Zeichen im Text beträgt: ', Funciones.contar_caracteres(contenido))
      elif opcion_herramienta == 2:
          print('Die Anzahl der Wörter im Text beträgt: ', Funciones.contar_palabras(contenido))
      elif opcion_herramienta == 3:
          print("Um das Histogramm anzuzeigen, gehen Sie bitte zur Programmausgabe, mit der Sie den Code ausführen")
          print("Um fortzufahren, schließen Sie bitte die Programmausgabe, mit der Sie den Code ausführen")
          x = list(abecedario)
          y = Funciones.calcular_frecuencia_letras(contenido, x)
          plt.title('Häufigkeit der Buchstaben im Buch', fontsize=30)
          plt.xlabel('Buchstaben', fontsize=20)
          plt.ylabel('Häufigkeit', fontsize=20)
          cmap = mpl.colormaps['RdYlGn']
          norm = colors.Normalize(vmin=min(y), vmax=max(y))
          histogram_abc = plt.bar(x, y, color=cmap(norm(y)))
          for bar in histogram_abc:
              yval = bar.get_height()
              plt.text(bar.get_x(), yval + .005, yval)
          plt.tight_layout()
          plt.show()
      elif opcion_herramienta == 4:
          print("Um das Histogramm anzuzeigen, gehen Sie bitte zur Programmausgabe, mit der Sie den Code ausführen")
          print("Um fortzufahren, schließen Sie bitte die Programmausgabe, mit der Sie den Code ausführen")
          x = list(Funciones.contar_palabras_por_longitud(contenido))
          y = list(Funciones.contar_palabras_por_longitud(contenido).values())
          cmap = mpl.colormaps['RdYlGn']
          norm = colors.Normalize(vmin=min(y), vmax=max(y))
          histogram_len = plt.bar(x, y, color=cmap(norm(y)))
          for bar in histogram_len:
              yval = bar.get_height()
              plt.text(bar.get_x(), yval + .005, yval)
          plt.title('Häufigkeit der Wörter nach Länge', fontsize=30)
          plt.xlabel('Wortlänge', fontsize=20)
          plt.ylabel('Häufigkeit', fontsize=20)
          plt.tight_layout()
          plt.show()
      elif opcion_herramienta == 5:
          print(Funciones.contar_frecuencia_palabras(contenido))
      elif opcion_herramienta == 6:
          print("Die Anzahl der verschiedenen Wörter in Ihrem Text beträgt: ",end="")
          print(Funciones.calcular_numero_distinto_palabras(contenido))
      elif opcion_herramienta == 7:
          print("Die Sprache Ihres Textes ist: ",end="")
          print(Funciones.identificar_idioma(contenido))
      elif opcion_herramienta == 8:
          print("Die 50 häufigsten Wörter in Ihrem Text, ohne Stoppwörter, sind: ",end="")
          print(Funciones.obtener_palabras_frecuentes_sin_stopwords(contenido))
      elif opcion_herramienta == 9:
          print("Die Charaktere in Ihrem Text zusammen mit ihrer Häufigkeit sind: ")
          personajes=Funciones.Identificar_personajes_con_su_frecuencia(contenido)
          personajes_ordenados = sorted(personajes.items(), key=lambda x: x[1], reverse=True)
          for i, (personaje, frecuencia) in enumerate(personajes_ordenados, start=1):
              print(f"{i}. {personaje} (Häufigkeit: {frecuencia})")
      elif opcion_herramienta == 10:
          print("Die Hauptcharaktere in Ihrem Text sind: ")
          personajes=Funciones.personajes_principales(contenido)
          personajes_ordenados = sorted(personajes.items(), key=lambda x: x[1], reverse=True)
          for i, (personaje, frecuencia) in enumerate(personajes_ordenados, start=1):
              print(f"{i}. {personaje} (Häufigkeit: {frecuencia})")
      elif opcion_herramienta == 11:
        lugares_identificados = Funciones.identificar_lugares(contenido)
        h = []
        for i in range(len(lugares_identificados)):
            if lugares_identificados[i] not in h:
                h.append(lugares_identificados[i])
        print("Die identifizierten Orte in Ihrem Text sind:  ")
        Funciones.imprimir_lugares(h)       
      elif opcion_herramienta == 12:
          print("Die Zeitspanne, in der Ihr Text stattfindet, lautet: \n",
                Funciones.identificar_tiempo_obra(contenido,opcion_lenguage)) 
      elif opcion_herramienta == 13:
          print("Programm wird beendet...")
          break
      bucle = int(input("\nMöchten Sie das Programm erneut verwenden?\n1. Ja\n2. Nein\n"))
      if bucle == 1:
          os.system('cls' if os.name=='nt' else 'clear')
      elif bucle == 2:
          os.system('cls' if os.name=='nt' else 'clear')
          print("Programm wird beendet...")
          break

elif opcion_lenguage == 5:
 print("\nBem-vindo ao Analisador de Livros. Este programa foi criado como projeto final para a disciplina de Programação de Computadores da Universidad Nacional de Colombia. O objetivo deste projeto é a análise automática de textos para extrair informações relevantes de seu conteúdo. Para isso, o programa realiza diferentes análises linguísticas que permitem caracterizar e processar arquivos txt de maneira estruturada.\n") 
 input("Pressione Enter para continuar...")
 os.system('cls' if os.name == 'nt' else 'clear')
 endereco_livro = str(input("\nPor favor, insira o endereço do arquivo de texto que deseja analisar (para sua conveniência, salve o arquivo .txt na mesma pasta do programa): "))
 try:
    with open(endereco_livro, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.readlines()
 except FileNotFoundError:
    # Se o arquivo não for encontrado, exibir uma mensagem e sair do programa
    print(f"Erro: Arquivo não encontrado no endereço especificado: {endereco_livro}")
    bucle = 0  # Sair do loop principal
 except Exception as e:
    # Capturar qualquer outra exceção e exibir um mensagem de erro
    print(f"Erro inesperado ao abrir o arquivo: {e}")
    bucle = 0  # Sair do loop principal
 while bucle == 1:
    # Exibir o menu e processar a opção do usuário
    print("\nO programa oferece as seguintes ferramentas para análise do seu texto:\n",
          "1.  Contar o número de caracteres no texto\n",
          "2.  Contar o número de palavras no texto\n",
          "3.  Criar um histograma da frequência de cada palavra no texto\n",
          "4.  Criar um histograma do comprimento das palavras no texto\n",
          "5.  Exibir as 100 palavras mais frequentes no texto\n",
          "6.  Calcular o número de palavras distintas no texto\n",
          "7.  Identificar o idioma do texto\n",
          "8.  Exibir as 50 palavras mais frequentes no texto, excluindo stopwords\n",
          "9.  Identificar os personagens da obra, junto com a frequência com que são mencionados\n",
          "10. Personagens principais na obra\n",
          "11. Identificar os lugares onde a obra ocorre (apenas para textos em espanhol)\n",
          "12. Identificar o período de tempo em que a obra ocorre (apenas para textos em espanhol)\n"
          " 13. Sair")
    opcao_ferramenta = int(input("Selecione a opção que deseja executar: "))

    while True:
        if 1 <= opcao_ferramenta <= 13:
            print("\nVocê escolheu a opção número:", opcao_ferramenta)
            break
        else:
            print("\nVocê inseriu uma opção inválida")
            opcao_ferramenta = int(input("Insira uma opção válida: "))

    if opcao_ferramenta == 1:
        print('O número de caracteres no texto é: ', Funciones.contar_caracteres(conteudo))
    elif opcao_ferramenta == 2:
        print('O número de palavras no texto é:: ', Funciones.contar_palabras(conteudo))
    elif opcao_ferramenta == 3:
        print("Para visualizar o histograma, vá para a saída do programa com o qual está executando o código")
        print("Para continuar, feche a saída do programa com o qual está executando o código")
        x = list(abecedario)
        y = Funciones.calcular_frecuencia_letras(conteudo, x)
        plt.title('Frequência de letras no livro', fontsize=30)
        plt.xlabel('Letras', fontsize=20)
        plt.ylabel('Frequência', fontsize=20)
        cmap = mpl.colormaps['RdYlGn']
        norm = colors.Normalize(vmin=min(y), vmax=max(y))
        histograma_abc = plt.bar(x, y, color=cmap(norm(y)))
        for bar in histograma_abc:
            yval = bar.get_height()
            plt.text(bar.get_x(), yval + .005, yval)
            plt.tight_layout()
            plt.show()
    elif opcao_ferramenta == 4:
        print("Para visualizar o histograma, vá para a saída do programa com o qual está executando o código")
        print("Para continuar, feche a saída do programa com o qual está executando o código")
        x = list(Funciones.contar_palabras_por_longitud(conteudo))
        y = list(Funciones.contar_palabras_por_longitud(conteudo).values())
        cmap = mpl.colormaps['RdYlGn']
        norm = colors.Normalize(vmin=min(y), vmax=max(y))
        histograma_len = plt.bar(x, y, color=cmap(norm(y)))
        for bar in histograma_len:
            yval = bar.get_height()
            plt.text(bar.get_x(), yval + .005, yval)
            plt.title('Frequência de palavras por comprimento', fontsize=30)
            plt.xlabel('Comprimento da palavra', fontsize=20)
            plt.ylabel('Frequência', fontsize=20)
            plt.tight_layout()
            plt.show()
    elif opcao_ferramenta == 5:
        print(Funciones.contar_frecuencia_palabras(conteudo))
    elif opcao_ferramenta == 6:
        print("O número distinto de palavras presentes no seu texto é: ", end="")
        print(Funciones.calcular_numero_distinto_palabras(conteudo))
    elif opcao_ferramenta == 7:
        print("O idioma do seu texto é: ", end="")
        print(Funciones.identificar_idioma(conteudo))
    elif opcao_ferramenta == 8:
        print("As 50 palavras mais frequentes no seu texto, excluindo stopwords, são: ", end="")
        print(Funciones.obtener_palabras_frecuentes_sin_stopwords(conteudo))
    elif opcao_ferramenta == 9:
        print("Os personagens presentes no seu texto são: ")
        personagens = Funciones.Identificar_personajes_con_su_frecuencia(conteudo)
        personagens_ordenados = sorted(personagens.items(), key=lambda x: x[1], reverse=True)
        for i, (personagem, frequencia) in enumerate(personagens_ordenados, start=1):
              print(f"{i}. {personagem} (Frequência: {frequencia})")
    elif opcao_ferramenta == 10:
        print("Os personagens principais no seu texto são: ")
        personagens = Funciones.personajes_principales(conteudo)
        personagens_ordenados = sorted(personagens.items(), key=lambda x: x[1], reverse=True)
        for i, (personagem, frequencia) in enumerate(personagens_ordenados, start=1):
            print(f"{i}. {personagem} (Frequência: {frequencia})")
    elif opcao_ferramenta == 11:
        lugares_identificados = Funciones.identificar_lugares(conteudo)
        h = []
        for i in range(len(lugares_identificados)):
            if lugares_identificados[i] not in h:
                h.append(lugares_identificados[i])
        print("Os lugares identificados no seu texto são:")
        Funciones.imprimir_lugares(h)
    elif opcao_ferramenta == 12:
        print("O período de tempo no qual o seu texto ocorre é: \n",
              Funciones.identificar_tiempo_obra(conteudo,opcion_lenguage))
    elif opcao_ferramenta == 13:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Saindo do programa...")
        break
    bucle = int(input("\nDeseja usar o programa novamente?\n1. Sim\n2. Não\n"))
    if bucle == 1:
      os.system('cls' if os.name == 'nt' else 'clear')
    elif bucle == 2:
      os.system('cls' if os.name == 'nt' else 'clear')
      print("Saindo do programa...")
      break







