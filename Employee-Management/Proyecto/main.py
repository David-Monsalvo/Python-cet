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

from sre_parse import State
import tkinter as tk
from tkinter import ttk

# Definición de función principal
def main():
    app = tk.Tk()
    app.title("Employee Management - 1990 - CET")
    app.iconbitmap("assets/images/employee.ico")
    app.resizable(1,1) #valores boolean
    app.geometry('1000x720')
    app.config(bg = '#0e1217')

    barra_menu = tk.Menu(app)
    app.config(menu=barra_menu, width=300, height=300, bg='#0e1217') #deberia tener configuracion de ancho y alto, pero no lo esta tomando
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
    EmployeeId.config(width = 30, font=('Arial', 12, 'bold'), bg = '#0e1217', fg = '#a0bcdf')
    EmployeeId.grid(row = 0, column = 0, padx = (20, 0), pady = (15,0))
    
    #Entry ID
    EntryEmployeeId = tk.Entry(app)
    EntryEmployeeId.config(width = 24, font = ('Arial', 12))
    EntryEmployeeId.grid(row = 1, column = 0, padx = (20, 0), pady = 0, ipady = 3, sticky='w')
    
    #Label FirstName
    EmployeeFirstName = tk.Label(app, text='Nombre: ', justify='left', anchor='w')
    EmployeeFirstName.config(width = 30, font=('Arial', 12, 'bold'), bg = '#0e1217', fg = '#a0bcdf')
    EmployeeFirstName.grid(row = 2, column = 0, padx = (20, 0), pady = (20,0))
    
    #Entry FirstName
    EntryEmployeeFirstName = tk.Entry(app)
    EntryEmployeeFirstName.config(width = 24, font = ('Arial', 12))
    EntryEmployeeFirstName.grid(row = 3, column = 0, padx = (20, 0), pady = 0, ipady = 3, sticky='w')
    
    #Label LastName
    EmployeeLastName = tk.Label(app, text='Apellidos: ', justify='left', anchor='w')
    EmployeeLastName.config(width = 30, font=('Arial', 12, 'bold'), bg = '#0e1217', fg = '#a0bcdf')
    EmployeeLastName.grid(row = 4, column = 0, padx = (20, 0), pady = (20,0))
    
    #Entry LastName
    EntryEmployeeLastName = tk.Entry(app)
    EntryEmployeeLastName.config(width = 24, font = ('Arial', 12))
    EntryEmployeeLastName.grid(row = 5, column = 0, padx = (20, 0), pady = 0, ipady = 3, sticky='w')
    
    #Label Adress
    EmployeeAdress = tk.Label(app, text='Dirección: ', justify='left', anchor='w')
    EmployeeAdress.config(width = 30, font=('Arial', 12, 'bold'), bg = '#0e1217', fg = '#a0bcdf')
    EmployeeAdress.grid(row = 6, column = 0, padx = (20, 0), pady = (20,0))
    
    #Entry Adress
    EntryEmployeeAdress = tk.Entry(app)
    EntryEmployeeAdress.config(width = 30, font = ('Arial', 12))
    EntryEmployeeAdress.grid(row = 7, column = 0, padx = (20, 0), pady = 0, ipady = 3, sticky='w')
    
   
    #Label PhoneNumber
    EmployeePhoneNumber = tk.Label(app, text='Número de Teléfono: ', justify='left', anchor='w')
    EmployeePhoneNumber.config(width = 30, font=('Arial', 12, 'bold'), bg = '#0e1217', fg = '#a0bcdf')
    EmployeePhoneNumber.grid(row = 0, column = 1, padx = (20, 0), pady = (15,0))
    
    #Entry PhoneNumber
    EntryEmployeePhoneNumber = tk.Entry(app)
    EntryEmployeePhoneNumber.config(width = 26, font = ('Arial', 12))
    EntryEmployeePhoneNumber.grid(row = 1, column = 1, padx = (20, 0), pady = 0, ipady = 3, sticky='w')
   
    #Label Age
    EmployeeAge = tk.Label(app, text='Edad: ', justify='left', anchor='w')
    EmployeeAge.config(width = 30, font=('Arial', 12, 'bold'), bg = '#0e1217', fg = '#a0bcdf')
    EmployeeAge.grid(row = 2, column = 1, padx = (20, 0), pady = (15,0))
    
    #Entry Age
    EntryEmployeeAge = tk.Entry(app)
    EntryEmployeeAge.config(width = 6, font = ('Arial', 12))
    EntryEmployeeAge.grid(row = 3, column = 1, padx = (20, 0), pady = 0, ipady = 3, sticky='w')
    
    # #Label Gender
    EmployeeGender = tk.Label(app, text = 'Género: ', justify='left', anchor='w')
    EmployeeGender.config(width = 10, font=('Arial', 12, 'bold'), bg = '#0e1217', fg = '#a0bcdf')
    EmployeeGender.grid(row = 2, column = 1, padx = 0, pady = (15,0))
    
    #Entry Gender
    EntryEmployeeGender = ttk.Combobox(app, values=[' ','Masculino', 'Femenino', 'Otros'],  state="readonly")
    EntryEmployeeGender.grid(row = 3, column = 1, padx = (110, 0), pady = 0, ipady = 3, sticky='w')
    EntryEmployeeGender.config(width = 12, font = ('Arial', 12))
    EntryEmployeeGender.current(0)

    #Label CivilStatus
    EmployeeCivilStatus = tk.Label(app, text='Estado Civil: ', justify='left', anchor='w')
    EmployeeCivilStatus.config(width = 30, font=('Arial', 12, 'bold'), bg = '#0e1217', fg = '#a0bcdf')
    EmployeeCivilStatus.grid(row = 4, column = 1, padx = (20, 0), pady = (15,0))
    
    #Entry CivilStatus
    EntryEmployeeCivilStatus = ttk.Combobox(app, values=[' ','Soltero/a', 'Casado/a', 'Viudo/a', 'Divorciado/a'],  state="readonly")
    EntryEmployeeCivilStatus.config(width = 24, font = ('Arial', 12))
    EntryEmployeeCivilStatus.grid(row = 5, column = 1, padx = (20, 0), pady = 0, ipady = 3, sticky='w')   
    
    #Label ChildrenNumber
    EmployeeChildrenNumber = tk.Label(app, text='N° Hijos: ', justify='left', anchor='w')
    EmployeeChildrenNumber.config(width = 30, font=('Arial', 12, 'bold'), bg = '#0e1217', fg = '#a0bcdf')
    EmployeeChildrenNumber.grid(row = 6, column = 1, padx = (20, 0), pady = (15,0))
    
    #Entry ChildrenNumber
    EntryEmployeeChildrenNumber = tk.Entry(app)
    EntryEmployeeChildrenNumber.config(width = 8, font = ('Arial', 12))
    EntryEmployeeChildrenNumber.grid(row = 7, column = 1, padx = (20, 0), pady = 0, ipady = 3, sticky='w')
    
    # #Label Height
    EmployeeHeight = tk.Label(app, text = 'Estatura (CM): ', justify='left', anchor='w')
    EmployeeHeight.config(width = 11, font=('Arial', 12, 'bold'), bg = '#0e1217', fg = '#a0bcdf')
    EmployeeHeight.grid(row = 6, column = 1, padx = (52,0), pady = (15,0))
    
    #Entry Height
    EntryEmployeeHeight = tk.Entry(app)
    EntryEmployeeHeight.config(width = 13, font = ('Arial', 12))
    EntryEmployeeHeight.grid(row = 7, column = 1, padx = (135, 0), pady = 0, ipady = 3, sticky='w') 

    #Label InitialHireDate
    EmployeeInitialHireDate = tk.Label(app, text='Fecha de contratación: ', justify='left', anchor='w')
    EmployeeInitialHireDate.config(width = 30, font=('Arial', 12, 'bold'), bg = '#0e1217', fg = '#a0bcdf')
    EmployeeInitialHireDate.grid(row = 0, column = 2, padx = (20, 0), pady = (15,0))
    
    #Entry InitialHireDate
    EntryEmployeeInitialHireDate = tk.Entry(app)
    EntryEmployeeInitialHireDate.config(width = 26, font = ('Arial', 12))
    EntryEmployeeInitialHireDate.grid(row = 1, column = 2, padx = (20, 0), pady = 0, ipady = 3, sticky='w')
    
    #Label BasicSalary
    EmployeeBasicSalary = tk.Label(app, text='Sueldo básico: ', justify='left', anchor='w')
    EmployeeBasicSalary.config(width = 30, font=('Arial', 12, 'bold'), bg = '#0e1217', fg = '#a0bcdf')
    EmployeeBasicSalary.grid(row = 2, column = 2, padx = (20, 0), pady = (15,0))
    
    #Entry BasicSalary
    EntryEmployeeBasicSalary = tk.Entry(app)
    EntryEmployeeBasicSalary.config(width = 26, font = ('Arial', 12))
    EntryEmployeeBasicSalary.grid(row = 3, column = 2, padx = (20, 0), pady = 0, ipady = 3, sticky='w')
    
    #Label WorkingDays
    EmployeeWorkingDays = tk.Label(app, text='Días Trabajados: ', justify='left', anchor='w')
    EmployeeWorkingDays.config(width = 30, font=('Arial', 12, 'bold'), bg = '#0e1217', fg = '#a0bcdf')
    EmployeeWorkingDays.grid(row = 4, column = 2, padx = (20, 0), pady = (15,0))
    
    #Entry WorkingDays
    EntryEmployeeWorkingDays = tk.Entry(app)
    EntryEmployeeWorkingDays.config(width = 26, font = ('Arial', 12))
    EntryEmployeeWorkingDays.grid(row = 5, column = 2, padx = (20, 0), pady = 0, ipady = 3, sticky='w')
    
    #Botones
    BottonNew = tk.Button(app, text = 'Nuevo')
    BottonNew.config(width = 25, font = ('Arial', 12, 'bold'), fg = '#fff',bg = '#00cc88', cursor = 'hand2', activebackground = '#82d4bb', 
                      activeforeground = '#fff' )
    BottonNew.grid( row = 8, column = 0, pady= (30, 0), padx = (20, 0), ipady = 5, sticky = 'w')
 
    BottonSave = tk.Button(app, text = 'Guardar')
    BottonSave.config(width = 25, font = ('Arial', 12, 'bold'), fg = '#fff',bg = '#f9c22e', cursor = 'hand2', activebackground = '#f0a202', 
                      activeforeground = '#fff' )
    BottonSave.grid( row = 8, column = 1, pady= (30, 0), padx = (20, 0), ipady = 5, sticky = 'w')   
    
    BottonCancel = tk.Button(app, text = 'Cancelar')
    BottonCancel.config(width = 25, font = ('Arial', 12, 'bold'), fg = '#fff',bg = '#e01a4f', cursor = 'hand2', activebackground = '#f15946', 
                      activeforeground = '#fff' )
    BottonCancel.grid( row = 8, column = 2, pady= (30, 0), padx = (20, 0), ipady = 5, sticky = 'w')

   
    
    app.mainloop()
    
    return app

def EnableEntrys():
    pass

def DisabledEntrys():    
    l = main()
    l.BottonCancel.config(State = 'disabled')
    

        
    

    
            
    

#Entry Point - Punto de entrada    
if __name__ == '__main__':
    main()
    EnableEntrys()
    DisabledEntrys()