# 3. Una empresa alquila autos a 250 mil pesos el día siempre que el número
# de kilómetros recorridos sea menor a 40 km. Hay un cargo extra de 10 mil
# pesos por cada kilómetro recorrido. Realice un programa que pida al usuario
# ingresar la cantidad de kilómetros recorridos y que muestre el precio que
# debe pagar por el alquiler del auto.
# (Ejemplo de prueba: Si el usuario ingresa 50 km, el precio que debe es 350
# mil pesos.)

# 39 = 250 + 10mil pesos 48 = 12

PRICE_DAY = 250 
KM_MINIMUM = 40

km_tour = int(input('Ingrese los Kilometros recorrido: '))


def total_price_km(price):
  if price == 40:
    print('El precio a pagar es de 250 Mil pesos')
  else:
    pass 