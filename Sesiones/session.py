#JUEVES 10-03-2021 ---

#Ejercicios de comparación
# x = 2
# if x == 3 :
#  print("x es igual a 3") #Despues del if siempre debe ir con espacio antes del print
# print("Siempre se ejecuta")

#Como mostrar si es un número par o impar
#-> Asignar una variable
#-> Como le decimos a la maquina que es par o impar : calcular el residuo de la división entre dos.
#->Si el residuo es 0, entoces escribe que el número es par.
#->Si el residuo es 1, entoces el numero es impar.

# a = 10.45
# residuo = a%2
# if residuo == 0 :
#  print("el numero es par")
# elif residuo == 1 :
#  print("El número es impar")
# else:
#   print("Error")

# VIERNES 11-03-2021 ---
#Ejemplo ingresar un dato y mostrarlo
#Cuando se útiliza el input solito, siempre se toma como String
# a = int(input("ingrese un número: "))
# print(a)
#EJemplo de ingreso de Datos

# Nombre = input("Ingrese el nombre: ")
# Apellido = input("Ingrese el apellido: ")
# Edad = int(input("Ingrese la edad: "))

# print(Nombre, Apellido, "Tiene", Edad, "años")

#Manejando Líneas de texto

# Palabra = "David"
# # print(len(Palabra))

# Primera_Letra = Palabra[0]
# ultima_Letra = Palabra[-5]

# print(Primera_Letra)
# print(ultima_Letra)

#Selecionamos partes del texto
# Texto = "Hola como estas David"
# Nombre = Texto[16:21]
# print(Nombre)

#Mostrando Edad
# from datetime import datetime
# year_realtime = datetime.now()
# year_actuality = year_realtime.year
# year_user = int(input("Año: "))

# print("la edad es", year_actuality-year_user)

#Útilizar números aletorios en python

# import random
# random.seed()


# a = int(random.uniform(1,10))
# b = int(random.uniform(1,10))

# x = int(input("Ingre el primer número: "))
# y = int(input("Ingre el segundo número: "))
# z = int(input("Ingre el tercer número: "))

# #Rango de valores de 0-10

# print("\n")
# print("los número generados son",a,"y",b)
# if x==a or x==b or y==a or y==b or z==a or z==b:
#     print("¡Has ganado!")
# else:
#     print("Has perdido.")
    
#Condiciones Anidadas
# and : se deben cumplir las dos condiones a la vez.
# a = int(input('Ingrese un número: '))

# if a%5==0 and a%7==0:
#         print("El número es divisible entre 5 y 7.")

#Uso de la funcion range

# r = range(10,20)

# print(r[0])
# print(r[-1])

#CICLOS REPETIVOS
# lista = [4, -10, 50, 60,-5, 5]
# lista2 = ['David', "Pedro"]
# for c in lista2:
#   print(c[0])

# realizar la suma de 100 números
  #definir los número del 1 al 100
# numbers = range(1,101)

# suma = 0

# for c in numbers:
#   suma = suma + c
  

# print(suma)

#ESCRIBIR UNA PALABRA AL REVÉS

# Word = input('Ingrese una palabra: ')
# CountWord = len(Word)
# R = ""

# for i in range(1,CountWord+1):
#   R = R + Word[-1*i]

# print(R)

#CALCULAR EL FACTORIAL DE UN NÚMERO
# 0! = 1
# 1! = 1 #2!= 1x2 3!= 1x2x3

# n = 5
# fact = 1
# c = 1
#fact = 1x2x3x4x5

# for c in range(1,n+1):
#   fact = fact * c
# print(fact)

# #CICLO WHILE
# while c<=n:
#   fact=fact*c
#   c += 1
# print(fact)

#FUNCIONES

# def saludar(): #def es para palabra reservada para realizar una función
#   print("Hola")
# saludar();
  #funcion que calcule la raiz cuadrada de un numero 
  
# def cuadrado(x):
#   return x**2

# y = cuadrado(10)
# print(y)

# Funcion que lanza un datos

# def lanzar_dado():
#   import random
#   lanzamiento = random.randrange(1,7)
#   return lanzamiento


# def lanzar_dos_dados():
#   l1 = lanzar_dado() #SOlo se útilizan dentreo de la funcion
#   l2 = lanzar_dado()
#   return [l1, l2]
# l = lanzar_dos_dados()

# print("dados 1 : ", l[0], 'dado 2 : ', l[1])

# variables locas y variables globales
#Lanzar una un dado n veces

# def lanzar_n_dados(n):
#   list_save = []
#   for c in range(1,n+1):
#     lanzamiento = lanzar_dado()
#     list_save.append(lanzamiento)
#   return list_save

# L = lanzar_n_dados(3)
# print(L)
# print(L[0], L[1], L[2])

#Función que muestra los elementos de una lista.

# def mostrar_lista(lista):
#   n = len(lista)
#   for c in range(0, n):
#     print(lista[c])
# L = lanzar_n_dados(8)
# mostrar_lista(L)

#LISTAS EN PYTHON

# lista = [4, 8, 1.2, 1.14,'Juan', 'David'] 
# print(lista[0])
# print(lista[1])

# longitud_de_la_lista = len(lista)

# print(lista[-1])
# lista.append(10)
# print(lista[-1])

# lista.extend([2,5]) # se añaden todos los elemetos que necesito añadir de un solo tiro.
# print(lista[0:8]) #imprime todos los elementos de la lista.

# Busca el indice
# del lista[3] #elimia el indice de la lista
# lista.clear() #elimina todos los elementos.
# print(lista)
# lista[0] = 45 # Modifica el elemento que se encuentra en el indice.
# lista = lista + [10] #concatena a la lista el 10

# multiplicar la lista, lo que hace es realizar la lista dos veces.
# lista = lista*3
#lista de ceros

# lista de listas

# lista2 = [[1,2,3,4,5],['David', 'Monsalvo', 'Angulo'], [6,7,8,9,10]]

# lista3 = [[0]*3]*3
# print(lista3)

# FUNCION QUE INGRESE UN LISTA DE FORMA BI DEMENCIONAL Y QUE ME MUESTRE UNA MATRIZ
#Argumentos de Entrada: la lista
#Argumentos de Salida: NaN - No retora valores.

# lista2D = [[4,6],[7,9]]
# 4 6
# 7 9


# def mostrar_lista2D(lista2D):
#   filas = len(lista2D) #Número de Filas
#   for c in range(0, filas):
#     columnas = len(lista2D[c])
#     s = ""
#     for d in range(0, columnas):       
#        s = s + "\t" + str(lista2D[c][d])
#     print(s)
    # print(lista2D[c])

# L = [[1,2,3],[9,6,6],[14,15,16]]

# mostrar_lista2D(L)

#Realizar una funcion que genere una matriz identidad
#Argumerntos de entrada: #filas y # columnas, es una matriz cuadrada
#argumento de salida: Matriz  identidad de tamñano nxn

# n = 4
# 1000
# 0100
# 0010
# 0001

# A = [[0]*4]*4
# mostrar_lista2D(A)

# def matriz_identidad(n):
#   z = [[0]*n]*n
#   #barre las filas
#   for c in range(0,n):
#     #barre las columnas
#     for d in range(0,n):
#       if c==d:
#         z[c][d] = 1
#   return z
# I = matriz_identidad(7)
# mostrar_lista2D(I)


#MANEJOS DE DICCIONARIOS:

#Diccionarios = Es una estructura de datos de python
# Diccionario = {'nombre':['Juan', 'David'],
#                'edad' : 26,
#                'curso':['Python', 'Inglés']
#                }
# # print(Diccionario['curso'])
# Etiquetas = Diccionario.keys()
# Valores = Diccionario.values()
# Diccionario1 = Diccionario.copy() #Crea una copia exactamente igual
# Edad = Diccionario.get('edad')
# D = Diccionario.pop('edad') #Elimina la etiqueta.
# Diccionario.setdefault('cedula',12345)

# print(Diccionario)
# print(Etiquetas)
# print(Valores)
# print(Edad)

# for c in Diccionario:
#   print(c)


# Integrantes_Curso = {'Nombre': ['David', 'Juan'], 'edad': [21,16]}
# print(Integrantes_Curso['Nombre'][0])

#Diccionario de usuario y contraseña
# Usuario_CPU1 = {'Nombre': 'Juan', 'Nombre de usuario' : 'juan09', 'Contraseña': '1234'}
# Usuario_CPU2 = {'Nombre': 'David', 'Nombre de usuario' : 'david09', 'Contraseña': '5959'}

# lista = [Usuario_CPU1, Usuario_CPU2]

# Usuario_CPU3 = Usuario_CPU2.copy()
# Usuario_CPU3['Nombre'] = 'Juan David'
# Usuario_CPU3['Nombre de usuario'] = 'JD69'
# lista.append(Usuario_CPU3)

#Ejemplo con el pago en caja

# Transacción = {'día': 24, 'Costo': 50000, 'efectivo' : 50000, 'Nombre_del_cajero': 'David'}
# Transacción2 = Transacción.copy()
#Cambiar los datos con appends

#LISTAS DIFERENCIAS
# A = [[0,0,0],[0,0,0],[0,0,0]]
# print(A)
# B = [[0]*3]*3
# print(B)

#FOR ESPECIAL
#NO se necesita definir una varible en el for para iterar una variable
# a = 1
# for _ in range(3):
#   a += 1
# print(a)

# c = [[0]*3 for _ in range(3)]
# print(c)
# c[0][0] = 1
# print(c)

# CLASES:
# Python: POO
#Clases = Es una especie de conjunto, se puede crear elementos de esta clase
#Un elemento creado se llama instancia.

#0,1,2,3,4,5...
# (self, caracteristica) # ATRIBUTO
# (self, caracteristica, método) # MÉTODOS

# class NumeroNatural: #Definicion de la clase
#   def __init__(self, nombre, valor): #método inicial
#       self.nombre = nombre
#       self.valor = valor
#       print('Soy el número', nombre)
      
#   def siguiente(self):
#       self.valor += 1
#       print('Ya no soy el número', self.nombre, 'ahora soy', self.valor)

#   def paridad(self):
#       if self.valor%2==0:
#         print('soy un número par')
#       else:
#         print('Soy un número impar')
  
# numero = NumeroNatural('tres', 3) #instacia de la clase número natural
# #a una instacia le podemos asociar atributos(Caracteristicas) y métodos(Cosas que puede hacer).
# #EJECUTAR UN MÉTODO
# numero.paridad()
# numero.siguiente()
# numero.paridad()


#CLASE DE MASCOTA -- Conjunto de mascotas
#ATRIBUTOS: Especie, Edad, Dueño, Tamaño
#MÉTODOS: ¿Qué especie es?, Cambiar de dueño, Cambiar tamaño 
class mascota:
    def __init__(self, especie, edad, dueño, tamaño): #método inicial
      self.especie = especie                           #Definicion de atributos
      self.edad = edad
      self.dueño = dueño
      self.tamaño = tamaño

mascota1 = mascota('perro', 3, 'Juan', 30) #instancia que tiene atributos.
