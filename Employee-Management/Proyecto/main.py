# Fase 1: 
# La empresa desea administrar los datos de sus empleados, los cuales son: 
# Número de Identificación, Nombres, Apellidos, Dirección, Teléfono, Edad, Género, 
# Estado Civil, Número de hijos, Estatura en metros, fecha de contratación (Día, mes 
# y año), Sueldo básico y Días Laborados. 
# Gestionar de la siguiente manera: 
# 1. Obtener los datos por teclado  para un único empleado (Tener en cuenta el 
# tipo de dato adecuado para cada dato) 
# 2. Imprimir  o  mostrar  los  datos  obtenidos  por  pantalla  (mostrar  la  fecha  de 
# contratación en un formato de fecha adecuado)

#Nombre de la empresa es : Employee Management

# ID = único - Int
# FirstName = String
# LastName = String
# Adress = String
# PhoneNumber = int
# Age = int
# Gender = String
# CivilStatus = String
# ChildrenNumber = int
# Height = Float
# InitialHireDate = date (dd/mm/yyyy)
# BasicSalary = int
# WorkingDays = int

#https://docs.python.org/es/3/tutorial/venv.html
#Se Importa la libreria para realizar componentes de ventana https://docs.python.org/es/3/library/tk.html

import tkinter as tk
from tkinter import ttk
# Definición de función principal
def main():
    app = tk.Tk()
    app.title("Employee Management - 1990 - CET")
    app.iconbitmap("assets/images/employee.ico")
    app.resizable(1,1) #valores boolean
    app.geometry('1000x720')

    barra_menu = tk.Menu(app)
    app.config(menu=barra_menu, width=300, height=300) #deberia tener configuracion de ancho y alto, pero no lo esta tomando
    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    
    barra_menu.add_cascade(label='Inicio', menu=menu_inicio)
    menu_inicio.add_command(label='Crear un registro en la base de datos')
    menu_inicio.add_command(label='Eliminar un registro en la base de datos')
    menu_inicio.add_command(label='Salir', command = app.destroy)
    #Forma de Agregar más datos 
    barra_menu.add_cascade(label='Consultas')
    barra_menu.add_cascade(label='Configuración')
    barra_menu.add_cascade(label='Ayuda')
    
    #Column 0
    #Label ID
    EmployeeId = tk.Label(app, text='Número de Identificación: ', justify='left', anchor='w')
    EmployeeId.config(width = 30, font=('Arial', 12, 'bold'))
    EmployeeId.grid(row = 0, column = 0, padx = (20, 0), pady = (15,0))
    
    #Entry ID
    EntryEmployeeId = tk.Entry(app)
    EntryEmployeeId.config(width = 24, font = ('Arial', 12))
    EntryEmployeeId.grid(row = 1, column = 0, padx = (20, 0), pady = 0, ipady = 3, sticky='w')
    
    #Label FirstName
    EmployeeFirstName = tk.Label(app, text='Nombre: ', justify='left', anchor='w')
    EmployeeFirstName.config(width = 30, font=('Arial', 12, 'bold'))
    EmployeeFirstName.grid(row = 2, column = 0, padx = (20, 0), pady = (20,0))
    
    #Entry FirstName
    EntryEmployeeFirstName = tk.Entry(app)
    EntryEmployeeFirstName.config(width = 24, font = ('Arial', 12))
    EntryEmployeeFirstName.grid(row = 3, column = 0, padx = (20, 0), pady = 0, ipady = 3, sticky='w')
    
    #Label LastName
    EmployeeLastName = tk.Label(app, text='Apellido: ', justify='left', anchor='w')
    EmployeeLastName.config(width = 30, font=('Arial', 12, 'bold'))
    EmployeeLastName.grid(row = 4, column = 0, padx = (20, 0), pady = (20,0))
    
    #Entry LastName
    EntryEmployeeLastName = tk.Entry(app)
    EntryEmployeeLastName.config(width = 24, font = ('Arial', 12))
    EntryEmployeeLastName.grid(row = 5, column = 0, padx = (20, 0), pady = 0, ipady = 3, sticky='w')
    
    #Label Adress
    EmployeeAdress = tk.Label(app, text='Dirección: ', justify='left', anchor='w')
    EmployeeAdress.config(width = 30, font=('Arial', 12, 'bold'))
    EmployeeAdress.grid(row = 6, column = 0, padx = (20, 0), pady = (20,0))
    
    #Entry Adress
    EntryEmployeeAdress = tk.Entry(app)
    EntryEmployeeAdress.config(width = 30, font = ('Arial', 12))
    EntryEmployeeAdress.grid(row = 7, column = 0, padx = (20, 0), pady = 0, ipady = 3, sticky='w')
    
   
    #Label PhoneNumber
    EmployeePhoneNumber = tk.Label(app, text='Número de Teléfono: ', justify='left', anchor='w')
    EmployeePhoneNumber.config(width = 30, font=('Arial', 12, 'bold'))
    EmployeePhoneNumber.grid(row = 0, column = 1, padx = (20, 0), pady = (15,0))
    
    #Entry PhoneNumber
    EntryEmployeePhoneNumber = tk.Entry(app)
    EntryEmployeePhoneNumber.config(width = 25, font = ('Arial', 12))
    EntryEmployeePhoneNumber.grid(row = 1, column = 1, padx = (20, 0), pady = 0, ipady = 3, sticky='w')
   
    #Label Age
    EmployeeAge = tk.Label(app, text='Edad: ', justify='left', anchor='w')
    EmployeeAge.config(width = 30, font=('Arial', 12, 'bold'))
    EmployeeAge.grid(row = 2, column = 1, padx = (20, 0), pady = (15,0))
    
    #Entry Age
    EntryEmployeeAge = tk.Entry(app)
    EntryEmployeeAge.config(width = 6, font = ('Arial', 12))
    EntryEmployeeAge.grid(row = 3, column = 1, padx = (20, 0), pady = 0, ipady = 3, sticky='w')
    
    # #Label Gender
    EmployeeGender = tk.Label(app, text = 'Género: ', justify='left', anchor='w')
    EmployeeGender.config(width = 10, font=('Arial', 12, 'bold'))
    EmployeeGender.grid(row = 2, column = 1, padx = 0, pady = (15,0))
    
    #Entry Gender
    EntryEmployeeGender = ttk.Combobox(app, values=[' ','Masculino', 'Femenino', 'Otros'],  state="readonly")
    EntryEmployeeGender.grid(row = 3, column = 1, padx = (110, 0), pady = 0, ipady = 3, sticky='w')
    EntryEmployeeGender.config(width = 12, font = ('Arial', 12))
    EntryEmployeeGender.current(0)

    #Label CivilStatus
    EmployeeCivilStatus = tk.Label(app, text='Estado Civil: ', justify='left', anchor='w')
    EmployeeCivilStatus.config(width = 30, font=('Arial', 12, 'bold'))
    EmployeeCivilStatus.grid(row = 4, column = 1, padx = (20, 0), pady = (15,0))
    
    #Entry CivilStatus
    EntryEmployeeCivilStatus = ttk.Combobox(app, values=[' ','Soltero/a', 'Casado/a', 'Viudo/a', 'Divorciado/a'],  state="readonly")
    EntryEmployeeCivilStatus.config(width = 24, font = ('Arial', 12))
    EntryEmployeeCivilStatus.grid(row = 5, column = 1, padx = (20, 0), pady = 0, ipady = 3, sticky='w')   
    

    app.mainloop()

#Entry Point - Punto de entrada    
if __name__ == '__main__':
    main()