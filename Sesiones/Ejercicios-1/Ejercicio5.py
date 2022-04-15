# 5. Una empresa constructora vende terrenos con la forma que se muestra,
# donde los lados A y B son perpendiculares al igual que los lados C y B, y
# además la medida del lado A es mayor a la medida del lado C. Realice un
# programa que pida al usuario ingresar la medida de los lados A, B y C en
# metros y que muestre el valor del área y el perímetro del terreno.
# (Ejemplo de prueba: Si el lado A mide 5 m, el lado B mide 4 m y el lado C
# mide 2 m, entonces el perímetro es 16 m y el área es 14 m2.)

#los lados A y B son perpendiculares
#los lados C y B son perpendiculares
#la medida del lado A es mayor a la medida del lado C.

#Mostrar el perímetro = A+B+C El perimetro es la suma de todos sus lados.
#Mostrar el área = a = (b*h) / 2

print('Hola, ingresar los valores de A, B, C en metros\n')
while True:
    try:
      a, b, c = [int(input(f'Ingrese el valor para {value}: ')) for value in ('a', 'b', 'c')]
    except ValueError:
      print('\nEl valor ingresado no es valido')
    else:
      break

#-pendiente para resolución de este problema no lo veo claro.