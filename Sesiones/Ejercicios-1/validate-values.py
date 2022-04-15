# # Validar si los datos que ingresa el usuario son validos

# # variable que indica el valor es valido
# # al principio no lo va hacer
# success = False

# # Creamos una función para validar el dato
# def validate(value):
#   entero = int(value)
#   return entero >= 0 and entero <= 100 #Como no hay implementación, por lo tanto devovelmos simepre false

# # Solicitamos ingreso de datos a el usuario
# print('Indroduzca un valor de 0 a 100, por favor:') #no se a que se refiere con end=''

# #Bucle para validar los valores que ingrese el usuario
# while not success:
#   value  = input()
#   success = validate(value)
#   if not success:
#     print('El valor ingresado no es valido, ingrese un valor valido:')

# #si el valor es VALIDO ya podemos realizar las respectivas validaciónes
# print(f'El valor ingresado es valido {value}.')

# # ESTE PROGRAMA SOLO VALIDA SI ÚTILIZAMOS VALORES ENTEROS

# #pedimos un valor al usuario
# valor = input()

# try:
# 	entero = float(valor) #intentamos la conversión
# except (ValueError):
# 	print('Error: valor no es un número decimal') #gestionamos el error

#Programa que le solicita al usuario solo dato númerico

while True:
  try:
    a = int(input('Número: '))
    
  except ValueError:
      print('el valor indicado no es valido')
  else:
      break
print('El programa Continua')