import Funciones
import string
import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib as mpl

print("Welcome to the book analyzer")
print("Selec your language:")
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
direccion_libro = str(input("Ingrese la dirección del libro que desea analizar (para su comodidad guarde el archivo .txt en la misma carpeta del programa): "))
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
    print("\naca va la descripcion del programa")
    # Mostrar el menú y procesar la opción del usuario
    print("\nEl programa ofrece las siguientes herramientas:\n",
          "1. Contar caracteres\n",
          "2. Contar palabras\n",
          "3. Calcular frecuencia de letras\n",
          "4. Calcular palabras por longitud\n",
          "5. Calcular frecuencia de palabras\n",
          "6. Calcular número distinto de palabras\n",
          "7. Decir idioma\n",
          "8. 100 palabras mas frecuentes sin stopwords\n",
          "13. Salir")
    opcion_herramienta = int(input("Seleccione la opción que desea realizar:"))

    while True:
        if 1 <= opcion_herramienta <=13:
            print("\nYou have selected the option:", opcion_herramienta)
            break
        else:
            print("\nYou have selected an invalid option")
            opcion_herramienta = int(input("Input a valid option: "))
    
    if opcion_herramienta == 1:
        while True:
            print(Funciones.contar_caracteres(contenido))
    elif opcion_herramienta == 2:
        print(Funciones.contar_palabras(contenido))
    elif opcion_herramienta == 3:
        print("Revisar salida")
        print("Indicar al usuario que cierre la ventana")
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
        print("Revisar salida")
        print("Indicar al usuario que cierre la ventana")
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
      print("El número distinto de palabras que hay en el texto son:",end="")
      print(Funciones.calcular_numero_distinto_palabras(contenido))
    elif opcion_herramienta == 7:
      print("El idioma del texto es:",end="")
      print(Funciones.identificar_idioma(contenido))
    elif opcion_herramienta == 8:
      print(Funciones.obtener_palabras_frecuentes_sin_stopwords(contenido))
    #elif opcion_herramienta == 9:

    #elif opcion_herramienta == 10:

    #elif opcion_herramienta == 11:

    #elif opcion_herramienta == 12:

      
    elif opcion_herramienta == 13:
      print("Saliendo del programa...")
      break
    bucle = int(input("Desea volver a utilizar el programa?\n1. Si\n2. No\n"))
if bucle==2:
  print("Saliendo del programa...")




