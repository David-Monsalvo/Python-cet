from math import sqrt
# ax2 + bx + c = 0.
# 1. Se calcula el descriminante:
    # disc = b * b - 4 * a * c
# 2.Si disc es NEGATIVO la ecuación no tienen solución.
# 3.Si disc No es NEGATIVO, calcula su raíz:
  # raiz = srqt(disc)
# 4.  calculamos la solución: X_1 = (-b + raiz) / (2 * a) y x_2 = (-b - raiz) / (2 * a)

# Solicitar los valore a, b, b al usuario
print('Vamos a resolver una ecuación de segundo grado: \n ax² + bx + c = 0\n')
while True:
  try:
   a, b, c = [float(input(f'Dame el coeficiente para {coef}: ')) for coef in ('a', 'b', 'c')]
  except ValueError:
    print('El valor indicado no es valido\n')
  else:
    break

discriminante = b ** 2 - 4 * a * c

#Hay ecuaciones de segundo grado que no tienen solución, esto se debe al que el discriminante es negativo
# por lo tanto no tiene una solución REAL, solo la puede tener en el campo de los número complejos.

if discriminante < 0 :
  print('\nLa ecuación no tienen soluciones reales.')
else:
# Suele suceder que a veces si el discriminante es 0 tendremos la misma solución para ambas ecuación, tanto positiva
#Como negativas en este caso realizamos una validación para realizar la segunda ecuación si el valor de la discriminante  es diferente a cero.
    raiz = sqrt(discriminante)
    ecuation_plus = (-b + raiz) / (2 * a)
    if discriminante != 0:
      ecuation_minimus = (-b - raiz) / (2 * a)
      print(f'\nEl discriminate es: {discriminante} y las soluciones de las ecuaciónes son {ecuation_plus} y {ecuation_minimus}  ')
    else:
      print(f'\nLa única solución es x = {ecuation_plus}')