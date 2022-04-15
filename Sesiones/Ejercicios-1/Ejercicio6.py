# 6. Almacenes “El harapiento distinguido” vende dos tipos de trajes A y B que
# cuestan $250000 y los trajes tipo $175000 respectivamente. Para estos
# precios hay una promoción dependiendo del día de la semana. 
# 
# Si se adquiere un traje un día viernes, a cualquier tipo de traje se 
# le aplica un descuento de 5%. 
# 
# Si se compra un sábado o un domingo, los trajes tipo A tienen un
# descuento del 15% y los trajes tipo B tienen un descuento del 8%. 
# 
# Realice un programa que pida al usuario ingresar el día de la semana, la cantidad de
# trajes tipo A y tipo B comprados, y luego muestre el precio total a pagar.

# (Ejemplo de prueba: Si se compran 3 trajes tipo A y 2 trajes tipo B un sábado,
# entonces se debe pagar $959500.)
while True:
    try:
        WeeklyDay = input('Ingrese el día de la semana de la compra del traje: ').lower()
        TotalSuitTypeA = int(input('Ingrese el total de trajes tipo A comprados: '))
        TotalSuitTypeB = int(input('Ingrese el total de trajes tipo B comprados: '))
    except ValueError:
        print('El valor ingresado no es valido.')
    else:
        break
TypeSuitA = 250000
TypeSuitB = 175000

DiscountFriday = 0.05 #descuento de 5% en los 2 tipos de traje
DiscountTypeA = 0.15 #TipoA 15% de descuento | Sabado - Domingo
DiscountTypeB = 0.08 #TipoB es de 8% de descuento | Sabado - Domingo

if WeeklyDay == "viernes":
    #Tipo A
    MultCantidadA = TypeSuitA * TotalSuitTypeA
    MultDiscoutA = int(MultCantidadA * DiscountFriday)
    DiscountTotalA = MultCantidadA - MultDiscoutA
    
    #Tipo B
    MultCantidadB = TypeSuitB * TotalSuitTypeB
    MultDiscoutB = int(MultCantidadB * DiscountFriday)
    DiscountTotalB = MultCantidadB - MultDiscoutB
    
    TotalFriday = DiscountTotalA + DiscountTotalB

    print("\nEl total a pagar es de",TotalFriday, 'Mil Pesos')
  
elif WeeklyDay == "sabado" or WeeklyDay == "domingo":         
    #Tipo A
    MultCantidadA = TypeSuitA * TotalSuitTypeA
    MultDiscoutA = int(MultCantidadA * DiscountTypeA)
    DiscountTotalA = MultCantidadA - MultDiscoutA

    #Tipo B
    MultCantidadB = TypeSuitB * TotalSuitTypeB
    MultDiscoutB = int(MultCantidadB * DiscountTypeB)
    DiscountTotalB = MultCantidadB - MultDiscoutB

    TotalWeekend = DiscountTotalA + DiscountTotalB
    
    print("\nEl total a pagar es de",TotalWeekend, 'Mil Pesos')
else:
     #Tipo A
    MultCantidadA = TypeSuitA * TotalSuitTypeA
    
    #Tipo B
    MultCantidadB = TypeSuitB * TotalSuitTypeB
    
    TotalPay = MultCantidadA + MultCantidadB

    print("\nEl total a pagar es de",TotalPay, 'Mil Pesos') 

