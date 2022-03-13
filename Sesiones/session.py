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