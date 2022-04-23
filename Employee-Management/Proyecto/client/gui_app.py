from pydoc import describe
import tkinter as tk
from tkinter import StringVar, ttk, messagebox
from model.clientes_dao import createTable, deleteTable, ClientsInsert, insertDB, listar, EditValues, DeleteValues


def barra_menu(app):
  barra_menu = tk.Menu(app)
  app.config(menu=barra_menu, width=300, height=300, bg='#0e1217')
  menu_inicio = tk.Menu(barra_menu, tearoff=0)
  
  barra_menu.add_cascade(label='Inicio', menu=menu_inicio)
  menu_inicio.add_command(label='Crear una tabla en la base de datos', command=createTable)
  menu_inicio.add_command(label='Eliminar una tabla en la base de datos', command=deleteTable)
  menu_inicio.add_command(label='Salir', command = app.destroy)
  #Forma de Agregar más datos 
  barra_menu.add_cascade(label='Consultas')
  barra_menu.add_cascade(label='Configuración')
  barra_menu.add_cascade(label='Ayuda')

#Clase padre
class Frame(tk.Frame):
  #Crear el constructor
  def __init__(self, app = None):
    super().__init__(app)
    self.app = app
    self.pack()
    self.config(bg="#0e1217")
    self.idClients = None
    self.campos_app()
    self.EnableFields()
    self.DisabledFields()
    self.InformationEmployeeTable()
 
    self.CrudDBTable()
    
  def campos_app(self): 
    
    #Label ID
    self.EmployeeId = tk.Label(self, text='Número de Identificación: ', justify='left', anchor='w')
    self.EmployeeId.config(width = 30, font=('Arial', 12, 'bold'), bg = '#0e1217', fg = '#a0bcdf')
    self.EmployeeId.grid(row = 0, column = 0, padx = (20, 0), pady = (15,0))
    
    #Entry ID
    self.Mi_Number_of_Identification = tk.StringVar()
    
    self.EntryEmployeeId = tk.Entry(self, textvariable = self.Mi_Number_of_Identification)
    self.EntryEmployeeId.config(width = 24, font = ('Arial', 12))
    self.EntryEmployeeId.grid(row = 1, column = 0, padx = (20, 0), pady = 0, ipady = 3, sticky='w')
    
    #Label FirstName
    self.EmployeeFirstName = tk.Label(self, text='Nombre: ', justify='left', anchor='w')
    self.EmployeeFirstName.config(width = 30, font=('Arial', 12, 'bold'), bg = '#0e1217', fg = '#a0bcdf')
    self.EmployeeFirstName.grid(row = 2, column = 0, padx = (20, 0), pady = (20,0))
    
    #Entry FirstName
    self.Mi_FirstName = tk.StringVar()
    self.EntryEmployeeFirstName = tk.Entry(self, textvariable=self.Mi_FirstName)
    self.EntryEmployeeFirstName.config(width = 24, font = ('Arial', 12))
    self.EntryEmployeeFirstName.grid(row = 3, column = 0, padx = (20, 0), pady = 0, ipady = 3, sticky='w')
    
    #Label LastName
    self.EmployeeLastName = tk.Label(self, text='Apellidos: ', justify='left', anchor='w')
    self.EmployeeLastName.config(width = 30, font=('Arial', 12, 'bold'), bg = '#0e1217', fg = '#a0bcdf')
    self.EmployeeLastName.grid(row = 4, column = 0, padx = (20, 0), pady = (20,0))
    
    #Entry LastName
    self.Mi_LastName = tk.StringVar()
    self.EntryEmployeeLastName = tk.Entry(self, textvariable=self.Mi_LastName)
    self.EntryEmployeeLastName.config(width = 24, font = ('Arial', 12))
    self.EntryEmployeeLastName.grid(row = 5, column = 0, padx = (20, 0), pady = 0, ipady = 3, sticky='w')
    
    #Label Adress
    self.EmployeeAdress = tk.Label(self, text='Dirección: ', justify='left', anchor='w')
    self.EmployeeAdress.config(width = 30, font=('Arial', 12, 'bold'), bg = '#0e1217', fg = '#a0bcdf')
    self.EmployeeAdress.grid(row = 6, column = 0, padx = (20, 0), pady = (20,0))
    
    #Entry Adress
    self.Mi_Adress = tk.StringVar()
    self.EntryEmployeeAdress = tk.Entry(self, textvariable=self.Mi_Adress)
    self.EntryEmployeeAdress.config(width = 30, font = ('Arial', 12))
    self.EntryEmployeeAdress.grid(row = 7, column = 0, padx = (20, 0), pady = 0, ipady = 3, sticky='w')
    
   
    #Label PhoneNumber
    self.EmployeePhoneNumber = tk.Label(self, text='Número de Teléfono: ', justify='left', anchor='w')
    self.EmployeePhoneNumber.config(width = 30, font=('Arial', 12, 'bold'), bg = '#0e1217', fg = '#a0bcdf')
    self.EmployeePhoneNumber.grid(row = 0, column = 1, padx = (20, 0), pady = (15,0))
    
    #Entry PhoneNumber
    self.Mi_Phone_Number = tk.StringVar()
    self.EntryEmployeePhoneNumber = tk.Entry(self, textvariable=self.Mi_Phone_Number)
    self.EntryEmployeePhoneNumber.config(width = 26, font = ('Arial', 12))
    self.EntryEmployeePhoneNumber.grid(row = 1, column = 1, padx = (20, 0), pady = 0, ipady = 3, sticky='w')
   
    #Label Age
    self.EmployeeAge = tk.Label(self, text='Edad: ', justify='left', anchor='w')
    self.EmployeeAge.config(width = 30, font=('Arial', 12, 'bold'), bg = '#0e1217', fg = '#a0bcdf')
    self.EmployeeAge.grid(row = 2, column = 1, padx = (20, 0), pady = (15,0))
    
    #Entry Age
    self.Mi_Age = tk.StringVar()
    self.EntryEmployeeAge = tk.Entry(self, textvariable=self.Mi_Age)
    self.EntryEmployeeAge.config(width = 6, font = ('Arial', 12))
    self.EntryEmployeeAge.grid(row = 3, column = 1, padx = (20, 0), pady = 0, ipady = 3, sticky='w')
    
    # #Label Gender
    self.EmployeeGender = tk.Label(self, text = 'Género: ', justify='left', anchor='w')
    self.EmployeeGender.config(width = 10, font=('Arial', 12, 'bold'), bg = '#0e1217', fg = '#a0bcdf')
    self.EmployeeGender.grid(row = 2, column = 1, padx = 0, pady = (15,0))
    
    #Entry Gender
    self.Mi_Gender = tk.StringVar()
    self.EntryEmployeeGender = ttk.Combobox(self, values=[' ','Masculino', 'Femenino', 'Otros'],  state="readonly", textvariable=self.Mi_Gender)
    self.EntryEmployeeGender.grid(row = 3, column = 1, padx = (110, 0), pady = 0, ipady = 3, sticky='w')
    self.EntryEmployeeGender.config(width = 12, font = ('Arial', 12))
    self.EntryEmployeeGender.current(0)

    #Label CivilStatus
    self.EmployeeCivilStatus = tk.Label(self, text='Estado Civil: ', justify='left', anchor='w')
    self.EmployeeCivilStatus.config(width = 30, font=('Arial', 12, 'bold'), bg = '#0e1217', fg = '#a0bcdf')
    self.EmployeeCivilStatus.grid(row = 4, column = 1, padx = (20, 0), pady = (15,0))
    
    #Entry CivilStatus
    self.Mi_Civil_Status = tk.StringVar()
    self.EntryEmployeeCivilStatus = ttk.Combobox(self, values=[' ','Soltero/a', 'Casado/a', 'Viudo/a', 'Divorciado/a'],  state="readonly", textvariable=self.Mi_Civil_Status)
    self.EntryEmployeeCivilStatus.config(width = 24, font = ('Arial', 12))
    self.EntryEmployeeCivilStatus.grid(row = 5, column = 1, padx = (20, 0), pady = 0, ipady = 3, sticky='w')   
    
    #Label ChildrenNumber
    self.EmployeeChildrenNumber = tk.Label(self, text='N° Hijos: ', justify='left', anchor='w')
    self.EmployeeChildrenNumber.config(width = 30, font=('Arial', 12, 'bold'), bg = '#0e1217', fg = '#a0bcdf')
    self.EmployeeChildrenNumber.grid(row = 6, column = 1, padx = (20, 0), pady = (15,0))
    
    #Entry ChildrenNumber
    self.Mi_Children_Number = tk.StringVar()
    self.EntryEmployeeChildrenNumber = tk.Entry(self, textvariable=self.Mi_Children_Number)
    self.EntryEmployeeChildrenNumber.config(width = 8, font = ('Arial', 12))
    self.EntryEmployeeChildrenNumber.grid(row = 7, column = 1, padx = (20, 0), pady = 0, ipady = 3, sticky='w')
    
    # #Label Height
    self.EmployeeHeight = tk.Label(self, text = 'Estatura (CM): ', justify='left', anchor='w')
    self.EmployeeHeight.config(width = 11, font=('Arial', 12, 'bold'), bg = '#0e1217', fg = '#a0bcdf')
    self.EmployeeHeight.grid(row = 6, column = 1, padx = (52,0), pady = (15,0))
    
    #Entry Height
    self.Mi_Height = tk.StringVar()
    self.EntryEmployeeHeight = tk.Entry(self, textvariable=self.Mi_Height)
    self.EntryEmployeeHeight.config(width = 13, font = ('Arial', 12))
    self.EntryEmployeeHeight.grid(row = 7, column = 1, padx = (135, 0), pady = 0, ipady = 3, sticky='w') 

    #Label InitialHireDate
    self.EmployeeInitialHireDate = tk.Label(self, text='Fecha de contratación: ', justify='left', anchor='w')
    self.EmployeeInitialHireDate.config(width = 30, font=('Arial', 12, 'bold'), bg = '#0e1217', fg = '#a0bcdf')
    self.EmployeeInitialHireDate.grid(row = 0, column = 2, padx = (20, 0), pady = (15,0))
    
    #Entry InitialHireDate
    self.Mi_Initial_Hire_Date = tk.StringVar()
    self.EntryEmployeeInitialHireDate = tk.Entry(self, textvariable=self.Mi_Initial_Hire_Date)
    self.EntryEmployeeInitialHireDate.config(width = 26, font = ('Arial', 12))
    self.EntryEmployeeInitialHireDate.grid(row = 1, column = 2, padx = (20, 0), pady = 0, ipady = 3, sticky='w')
    
    #Label BasicSalary
    self.EmployeeBasicSalary = tk.Label(self, text='Sueldo básico: ', justify='left', anchor='w')
    self.EmployeeBasicSalary.config(width = 30, font=('Arial', 12, 'bold'), bg = '#0e1217', fg = '#a0bcdf')
    self.EmployeeBasicSalary.grid(row = 2, column = 2, padx = (20, 0), pady = (15,0))
    
    #Entry BasicSalary
    self.Mi_Basic_Salary = tk.StringVar()
    self.EntryEmployeeBasicSalary = tk.Entry(self, textvariable=self.Mi_Basic_Salary)
    self.EntryEmployeeBasicSalary.config(width = 26, font = ('Arial', 12))
    self.EntryEmployeeBasicSalary.grid(row = 3, column = 2, padx = (20, 0), pady = 0, ipady = 3, sticky='w')
    
    #Label WorkingDays
    self.EmployeeWorkingDays = tk.Label(self, text='Días Trabajados: ', justify='left', anchor='w')
    self.EmployeeWorkingDays.config(width = 30, font=('Arial', 12, 'bold'), bg = '#0e1217', fg = '#a0bcdf')
    self.EmployeeWorkingDays.grid(row = 4, column = 2, padx = (20, 0), pady = (15,0))
    
    #Entry WorkingDays
    self.Mi_Working_Days = tk.StringVar()
    self.EntryEmployeeWorkingDays = tk.Entry(self, textvariable=self.Mi_Working_Days)
    self.EntryEmployeeWorkingDays.config(width = 26, font = ('Arial', 12))
    self.EntryEmployeeWorkingDays.grid(row = 5, column = 2, padx = (20, 0), pady = 0, ipady = 3, sticky='w')
    
    #Botones
    self.BottonNew = tk.Button(self, text = 'Nuevo', command = self.EnableFields)
    self.BottonNew.config(width = 25, font = ('Arial', 12, 'bold'), fg = '#fff',bg = '#00cc88', cursor = 'hand2', activebackground = '#82d4bb', 
                      activeforeground = '#fff' )
    self.BottonNew.grid( row = 8, column = 0, pady= (30, 30), padx = (20, 0), ipady = 5, sticky = 'w')

    self.BottonSave = tk.Button(self, text = 'Guardar', command = self.SaveEntrys)
    self.BottonSave.config( width = 25, font = ('Arial', 12, 'bold'), fg = '#fff',bg = '#f9c22e', cursor = 'hand2', activebackground = '#f0a202', 
                      activeforeground = '#fff' )
    self.BottonSave.grid( row = 8, column = 1, pady= (30, 30), padx = (20, 0), ipady = 5, sticky = 'w')   
    
    self.BottonCancel = tk.Button(self, text = 'Cancelar', command = self.DisabledFields)
    self.BottonCancel.config(width = 25, font = ('Arial', 12, 'bold'), fg = '#fff',bg = '#e01a4f', cursor = 'hand2', activebackground = '#f15946', 
                      activeforeground = '#fff' )
    self.BottonCancel.grid( row = 8, column = 2, pady= (30, 30), padx = (20, 0), ipady = 5, sticky = 'w')
  
  def EnableFields(self):
    
    #Campos
    self.EntryEmployeeId.config(state = 'normal')
    self.EntryEmployeeFirstName.config(state = 'normal')
    self.EntryEmployeeLastName.config(state = 'normal')
    self.EntryEmployeeAdress.config(state = 'normal')
    self.EntryEmployeePhoneNumber.config(state = 'normal')
    self.EntryEmployeeAge.config(state = 'normal')
    self.EntryEmployeeGender.config(state = 'normal')
    self.EntryEmployeeCivilStatus.config(state = 'normal')
    self.EntryEmployeeChildrenNumber.config(state = 'normal')
    self.EntryEmployeeHeight.config(state = 'normal')
    self.EntryEmployeeInitialHireDate.config(state = 'normal')
    self.EntryEmployeeBasicSalary.config(state = 'normal')
    self.EntryEmployeeWorkingDays.config(state = 'normal')
    
    #Botones
    self.BottonSave.config(state = 'normal')
    self.BottonCancel.config(state = 'normal')
    
  def DisabledFields(self):
    self.idClients = None
    
    self.EntryEmployeeId.delete(0, 'end')
    self.EntryEmployeeFirstName.delete(0, 'end')
    self.EntryEmployeeLastName.delete(0, 'end')
    self.EntryEmployeeAdress.delete(0, 'end')
    self.EntryEmployeePhoneNumber.delete(0, 'end')
    self.EntryEmployeeAge.delete(0, 'end')
    self.EntryEmployeeGender.delete(0, 'end')
    self.EntryEmployeeCivilStatus.delete(0, 'end')
    self.EntryEmployeeChildrenNumber.delete(0, 'end')
    self.EntryEmployeeHeight.delete(0, 'end')
    self.EntryEmployeeInitialHireDate.delete(0, 'end')
    self.EntryEmployeeBasicSalary.delete(0, 'end')
    self.EntryEmployeeWorkingDays.delete(0, 'end')
    #Campos
    self.EntryEmployeeId.config(state = 'disabled')
    self.EntryEmployeeFirstName.config(state = 'disabled')
    self.EntryEmployeeLastName.config(state = 'disabled')
    self.EntryEmployeeAdress.config(state = 'disabled')
    self.EntryEmployeePhoneNumber.config(state = 'disabled')
    self.EntryEmployeeAge.config(state = 'disabled')
    self.EntryEmployeeGender.config(state = 'disabled')
    self.EntryEmployeeCivilStatus.config(state = 'disabled')
    self.EntryEmployeeChildrenNumber.config(state = 'disabled')
    self.EntryEmployeeHeight.config(state = 'disabled')
    self.EntryEmployeeInitialHireDate.config(state = 'disabled')
    self.EntryEmployeeBasicSalary.config(state = 'disabled')
    self.EntryEmployeeWorkingDays.config(state = 'disabled')
    
    #Botones
    self.BottonSave.config(state = 'disabled')
    self.BottonCancel.config(state = 'disabled')
    
  def SaveEntrys(self): 
    
    clientValues = ClientsInsert(
      
      self.Mi_Number_of_Identification.get(),
      self.Mi_FirstName.get(),
      self.Mi_LastName.get(),
      self.Mi_Adress.get(),
      self.Mi_Phone_Number.get(),
      self.Mi_Age.get(),
      self.Mi_Gender.get(),
      self.Mi_Civil_Status.get(), 
      self.Mi_Children_Number.get(),
      self.Mi_Height.get(),
      self.Mi_Initial_Hire_Date.get(),
      self.Mi_Basic_Salary.get(),
      self.Mi_Working_Days.get()
      
    )
    if self.idClients == None:
      insertDB(clientValues)
    else:
      EditValues(clientValues, self.idClients)
    
    self.RefreshValuesDB()
    
    self.DisabledFields()
    
  def InformationEmployeeTable(self):
    
    
    self.informationTable = tk.Frame(self.app)
    self.informationTable.pack()

    #scrollbar
    self.scrollTableY = tk.Scrollbar(self.informationTable)
    self.scrollTableY.pack(side='right', fill='y')
    self.scrollTableX = tk.Scrollbar(self.informationTable,orient='horizontal')
    self.scrollTableX.pack(side='bottom',fill='x')
    
    self.table = ttk.Treeview(self.informationTable,yscrollcommand=self.scrollTableY.set, xscrollcommand =self.scrollTableX.set)
    self.table.pack()

    self.scrollTableY.config(command=self.table.yview)
    self.scrollTableX.config(command=self.table.xview)

    #define our column
    self.table['columns'] = ('','Número de Identificación', 'Nombres', 'Apellidos', 'Dirección', 'Teléfono', 'Edad',
                        'Género', 'Estado Civil', 'Número de hijos', 'Estatura en metros', 'Fecha de contratación', 'Sueldo básico', 'Días Laborados' )

    # format our column
    self.table.column("#0", width=0,  stretch=tk.NO)
    self.table.column("#1",anchor=tk.CENTER, width=50)
    self.table.column("#2",anchor=tk.CENTER,width=85)
    self.table.column("#3",anchor=tk.CENTER,width=85)
    self.table.column("#4",anchor=tk.CENTER,width=85)
    self.table.column("#5",anchor=tk.CENTER,width=85)
    self.table.column("#6",anchor=tk.CENTER,width=85)
    self.table.column("#7",anchor=tk.CENTER,width=85)
    self.table.column("#8",anchor=tk.CENTER,width=85)
    self.table.column("#9",anchor=tk.CENTER,width=85)
    self.table.column("#10",anchor=tk.CENTER,width=85)
    self.table.column("#11",anchor=tk.CENTER,width=85)
    self.table.column("#12",anchor=tk.CENTER,width=85)
    self.table.column("#13",anchor=tk.CENTER,width=85)
    self.table.column("#14",anchor=tk.CENTER,width=95)
    

    #Create Headings 
    self.table.heading("#0",text="",anchor=tk.CENTER)
    self.table.heading("#1",text="ID",anchor=tk.CENTER)
    self.table.heading("#2",text="Número de Identificación",anchor=tk.CENTER)
    self.table.heading("#3",text="Nombres",anchor=tk.CENTER)
    self.table.heading("#4",text="Apellidos",anchor=tk.CENTER)
    self.table.heading("#5",text="Dirección",anchor=tk.CENTER)
    self.table.heading("#6",text="Teléfono",anchor=tk.CENTER)
    self.table.heading("#7",text="Edad",anchor=tk.CENTER)
    self.table.heading("#8",text="Género",anchor=tk.CENTER)
    self.table.heading("#9",text="Estado Civil",anchor=tk.CENTER)
    self.table.heading("#10",text="Número de hijos",anchor=tk.CENTER)
    self.table.heading("#11",text="Estatura en metros",anchor=tk.CENTER)
    self.table.heading("#12",text="Fecha de contratación",anchor=tk.CENTER)
    self.table.heading("#13",text="Sueldo básico",anchor=tk.CENTER)
    self.table.heading("#14",text="Días Laborados",anchor=tk.CENTER)
    #Recuperar los datos de la DB
    self.lista_clientes = listar()   
    #iterar la lista de clientes
    for p in self.lista_clientes:
      #add data 
      self.table.insert(parent='',index='end',text='',values=(p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11], p[12], p[13]))
      
  def RefreshValuesDB(self):
    if self.idClients == None:
      # # #Recuperar los datos de la DB
      self.lista_clientes = listar()
      lastItemTuple = self.lista_clientes[-1]
      p = lastItemTuple

      #add data 
      self.table.insert(parent='',index='end',text='',values=(p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11], p[12], p[13]))
    else:
      pass
      # # # #Recuperar los datos de la DB
      # self.lista_clientes = listar()
      # for p in self.lista_clientes:
      #   #add data 
      #   self.table.update(parent='',index='end',text='',values=(self.idClients, p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11], p[12], p[13]))
    
  def CrudDBTable(self):
    bottomTable = tk.Frame(self.app)
    bottomTable.config(bg='#0e1217')
    bottomTable.pack()
    
    self.BottonEdit = tk.Button(bottomTable, text = 'Editar', command=self.EditValues )
    self.BottonEdit.config(width = 25, font = ('Arial', 12, 'bold'), fg = '#fff',bg = '#00cc88', cursor = 'hand2', activebackground = '#82d4bb', 
                      activeforeground = '#fff' )
    self.BottonEdit.grid( row = 0, column = 0, pady= (30, 30), padx = (20, 0), ipady = 5, sticky = 'w')  
    
    self.BottonDelete = tk.Button(bottomTable, text = 'Eliminar', command=self.DeleteValues)
    self.BottonDelete.config(width = 25, font = ('Arial', 12, 'bold'), fg = '#fff',bg = '#e01a4f', cursor = 'hand2', activebackground = '#f15946', 
                      activeforeground = '#fff' )
    self.BottonDelete.grid( row = 0, column= 1,  pady= (30, 30), padx = (20, 0), ipady = 5, sticky = 'w')
    
  def EditValues(self):
    try:
      self.idClients = self.table.item(self.table.selection())['values'][0]
      self.Identificacion = self.table.item(self.table.selection())['values'][1]
      self.Nombre = self.table.item(self.table.selection())['values'][2]
      self.Apellido = self.table.item(self.table.selection())['values'][3]
      self.Direccion = self.table.item(self.table.selection())['values'][4]
      self.NumeroTelefono = self.table.item(self.table.selection())['values'][5]
      self.Edad = self.table.item(self.table.selection())['values'][6]
      self.Genero = self.table.item(self.table.selection())['values'][7]
      self.EstadoCivil = self.table.item(self.table.selection())['values'][8]
      self.NHijos = self.table.item(self.table.selection())['values'][9]
      self.Estatura = self.table.item(self.table.selection())['values'][10]
      self.FechaContratacion = self.table.item(self.table.selection())['values'][11]
      self.SueldoBasico = self.table.item(self.table.selection())['values'][12]
      self.DiasTrabajados = self.table.item(self.table.selection())['values'][13]

      
      self.EnableFields()
      
      self.EntryEmployeeId.insert(0, self.Identificacion)
      self.EntryEmployeeFirstName.insert(0, self.Nombre)
      self.EntryEmployeeLastName.insert(0, self.Apellido)
      self.EntryEmployeeAdress.insert(0, self.Direccion)
      self.EntryEmployeePhoneNumber.insert(0, self.NumeroTelefono)
      self.EntryEmployeeAge.insert(0, self.Edad)
      self.EntryEmployeeGender.insert(0, self.Genero)
      self.EntryEmployeeCivilStatus.insert(0, self.EstadoCivil)
      self.EntryEmployeeChildrenNumber.insert(0, self.NHijos)
      self.EntryEmployeeHeight.insert(0, self.Estatura)
      self.EntryEmployeeInitialHireDate.insert(0, self.FechaContratacion)
      self.EntryEmployeeBasicSalary.insert(0, self.SueldoBasico)
      self.EntryEmployeeWorkingDays.insert(0, self.DiasTrabajados)
    except:
      title = 'Edición de Datos'
      description = 'No has seleccionado ningún registro'
      messagebox.showerror(title, description)
    
  def DeleteValues(self):
    try:
      self.idClients = self.table.item(self.table.selection())['values'][0]
      DeleteValues(self.idClients)
      self.idClients = None
      
    except:
      title = 'ELIMINAR REGISTRO'
      description = 'No has selecionado a ningún registro'
      messagebox.showerror(title, description)
      


    
    
    


