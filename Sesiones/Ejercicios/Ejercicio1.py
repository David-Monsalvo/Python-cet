# 1. Realice un programa que pida al usuario tres números enteros diferentes
# (que llamaremos 𝑎, 𝑏 y 𝑐). El programa debe ordenarlos y mostrar la siguiente
# desigualdad correcta
# 𝑎 < 𝑏 < 𝑐
# (Ejemplo de prueba: Si el usuario ingresa -4, 7 y -10, el programa debe
# mostrar -10<-4<7.)

while True:
    try:
      a = int(input('Ingrese un número: '))
      b = int(input('Ingrese un número: '))
      c = int(input('Ingrese un número: '))
      
    except ValueError:
        print("El valor indicado no es valido")
        continue
    else:
        break
#ordenar los datos de menor a mayor
numeros = [a,b,c]
numeros.sort()

def mostrar_lista(numeros):
  texto = ""
  n = len(numeros)
  for c in range(0, n):
    texto = texto + str(numeros[c]) + ' < '
  ftexto = texto[:-2] #Quitamos los dos últimos indices del String
  print(ftexto) 
mostrar_lista(numeros)