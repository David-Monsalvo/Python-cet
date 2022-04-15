# 3. Una empresa alquila autos a 250 mil pesos el día siempre que el número
# de kilómetros recorridos sea menor a 40 km. Hay un cargo extra de 10 mil
# pesos por cada kilómetro recorrido. Realice un programa que pida al usuario
# ingresar la cantidad de kilómetros recorridos y que muestre el precio que
# debe pagar por el alquiler del auto.
# (Ejemplo de prueba: Si el usuario ingresa 50 km, el precio que debe es 350
# mil pesos.)
while True:
    try:
      km_tour = int(input('Ingrese los Kilómetros recorridos: '))
      
    except ValueError:
        print("\tEl valor indicado no es valido\n")
        continue
    else:
        break

PRICE_DAY = 250 
KM_MINIMUM = 40

if km_tour > KM_MINIMUM:
  
  def total_price_km(price):
    Subtraction = price - KM_MINIMUM
    Multiplication = Subtraction * 10
    Sum = Multiplication + 250
    return Sum

  total = total_price_km(km_tour)
  print('\n\tEl valor a pagar es de', total, 'Mil pesos')
else:
  print('\n\tEl valor a pagar es de 250 Mil pesos')