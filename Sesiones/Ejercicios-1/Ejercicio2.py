# 2. Realice un programa que pida al usuario ingresar dos palabras de cinco letras. 
# El programa debe indicar cuál palabra tiene más vocales o si ambas
# tienen la misma cantidad de vocales.
# (Ejemplo de prueba: Si el usuario ingresa las palabras “ratón” y “menta”,
# entonces el programa muestra “Las dos palabras tienen la misma cantidad
# de vocales”.)
print('----------------------------------------')
print('| Ingrese dos palabras de cinco letras |')
print('----------------------------------------')

word1 = input("Ingrese una palabra: ")
word2 = input("Ingrese una palabra: ")

CharacterNumber = len(word1)
CharacterNumber2 = len(word2)

if CharacterNumber and CharacterNumber2 <= 5 :    
    
    def count_vocales_1(word1):
        count = 0
        for letter in word1:
            if letter.lower() in 'aeiouáéíóú':
                count = count + 1                
        return count
    
    def count_vocales_2(word2):
        count = 0
        for letter in word2:
            if letter.lower() in 'aeiouáéíóú':
                count = count + 1
        return count
    
    cantidad = count_vocales_1(word1)
    cantidad2 = count_vocales_2(word2)
    
    if cantidad != cantidad2:
        print("\n\t En la cadena", word1,  "hay", cantidad, "vocales")
        print("\t En la cadena", word2,  "hay", cantidad2, "vocales")
        
    else:        
        print('\nLas dos palabras tienen la misma cantidad de vocales')        
else:    
    print('\nIngresaste un valor mayor a cinco caracteres')