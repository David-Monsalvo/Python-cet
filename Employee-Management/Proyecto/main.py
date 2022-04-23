# # Fase 1: 
# # La empresa desea administrar los datos de sus empleados, los cuales son: 
# # Número de Identificación, Nombres, Apellidos, Dirección, Teléfono, Edad, Género, 
# # Estado Civil, Número de hijos, Estatura en metros, fecha de contratación (Día, mes 
# # y año), Sueldo básico y Días Laborados. 
# # Gestionar de la siguiente manera: 
# # 1. Obtener los datos por teclado  para un único empleado (Tener en cuenta el 
# # tipo de dato adecuado para cada dato) 
# # 2. Imprimir  o  mostrar  los  datos  obtenidos  por  pantalla  (mostrar  la  fecha  de 
# # contratación en un formato de fecha adecuado)

# #Nombre de la empresa es : Employee Management

# # ID = único - Int
# # FirstName = String
# # LastName = String
# # Adress = String
# # PhoneNumber = int
# # Age = int
# # Gender = String
# # CivilStatus = String
# # ChildrenNumber = int
# # Height = Float
# # InitialHireDate = date (dd/mm/yyyy)
# # BasicSalary = int
# # WorkingDays = int

# #https://docs.python.org/es/3/tutorial/venv.html
# #Se Importa la libreria para realizar componentes de ventana https://docs.python.org/es/3/library/tk.html

import tkinter as tk
from tkinter import ttk
from client.gui_app import Frame, barra_menu

# Definición de función principal
def main():
    app = tk.Tk()
    app.title("Employee Management - 1990 - CET")
    app.iconbitmap("assets/images/employee.ico")
    app.resizable(1,1) #valores boolean
    app.geometry('1000x820')
    
    barra_menu(app)
    root_app = Frame(app = app)   
    
    app.mainloop()
        
#Entry Point    
if __name__ == '__main__':
    main()