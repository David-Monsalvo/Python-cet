# 2. Realice un programa que pida al usuario ingresar dos palabras de cinco letras. 
# El programa debe indicar cuál palabra tiene más vocales o si ambas
# tienen la misma cantidad de vocales.
# (Ejemplo de prueba: Si el usuario ingresa las palabras “ratón” y “menta”,
# entonces el programa muestra “Las dos palabras tienen la misma cantidad
# de vocales”.)



# leer el tamaño de cada word y si es > al indice 6 se indica que la palabra ingresada no es valida
#validar si es número o letras





# Validate1 = word1.isnumeric()
# Validate2 = word2.isnumeric() 

# if Validate1 and Validate2 == True:
#   print('Hola')
# else:
word1 = input("Ingrese una palabra: ")
word2 = input("Ingrese una palabra: ")
Validate1 = word1.isalpha()
Validate2 = word2.isalpha() 

print(Validate1, Validate2)    
    
while Validate1 and Validate2 == True:
    try:
        print('código correcto')

    except ValueError:
        print("El valor indicado no es valido")
        continue
    else:
        break
print('Other')