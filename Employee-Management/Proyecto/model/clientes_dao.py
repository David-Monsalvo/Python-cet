from .conexiondb import conexionDB
from tkinter import messagebox

def createTable():
  conexion = conexionDB()
  sql = '''
  CREATE TABLE clientes(
    id INTEGER,
    Number_of_Identification VARCHAR(100),
    FirstName VARCHAR(100),
    LastName VARCHAR(255),
    Adress VARCHAR(200),
    Phone_Number VARCHAR(255),
    Age VARCHAR(255), 
    Gender VARCHAR(100),
    Civil_Status VARCHAR(100), 
    Children_Number VARCHAR(255),
    Height VARCHAR(255),
    Initial_Hire_Date VARCHAR(100),
    Basic_Salary VARCHAR(255),
    Working_Days VARCHAR(255),
    
  
    PRIMARY KEY (id AUTOINCREMENT)
    
  )
  '''
  try:
    conexion.cursor.execute(sql)
    conexion.closeDB()
    title = 'CREACIÓN DE TABLA'
    description = 'Se creo la tabla correctamente.'
    messagebox.showinfo(title, description)
    
  except:
    title = 'ERROR CRACIÓN DE TABLA'
    description = 'La tabla ya se encuentra creada.'
    messagebox.showerror(title, description)
    
def deleteTable():
  conexion = conexionDB()
  sql = 'DROP TABLE clientes'
  try:
    conexion.cursor.execute(sql)
    conexion.closeDB()
    title = 'TABLA ELIMINADA'
    description = 'Se elimino la tabla correctamente.'
    messagebox.showinfo(title, description)
  except:
    title = 'TABLA ERROR'
    description = 'La tabla ya se encuentre eliminada.'
    messagebox.showerror(title, description)
    
class ClientsInsert:
  
  def __init__(self, Number_of_Identification,FirstName,LastName,Adress,Phone_Number, Age, Gender, Civil_Status, Children_Number, Height, Initial_Hire_Date, Basic_Salary, Working_Days):
    
    self.id = None
    self.Number_of_Identification = Number_of_Identification
    self.FirstName = FirstName
    self.LastName = LastName
    self.Adress = Adress
    self.Phone_Number = Phone_Number
    self.Age = Age
    self.Gender = Gender
    self.Civil_Status = Civil_Status
    self.Children_Number = Children_Number
    self.Height = Height
    self.Initial_Hire_Date = Initial_Hire_Date
    self.Basic_Salary = Basic_Salary
    self.Working_Days = Working_Days

  def __str__(self):
    return f'ClientsInsert[{self.Number_of_Identification}, {self.FirstName}, {self.LastName}, {self.Adress}, {self.Phone_Number}, {self.Age}, {self.Gender}, {self.Civil_Status}, {self.Children_Number}, {self.Height}, {self.Initial_Hire_Date}, {self.Basic_Salary}, {self.Working_Days}]'
  
def insertDB(clientValues):
  
  conexion = conexionDB()
  sql = f"""INSERT INTO clientes (Number_of_Identification, FirstName, LastName,  Adress, Phone_Number, Age, Gender, Civil_Status, Children_Number, Height, Initial_Hire_Date, Basic_Salary, Working_Days)
  VALUES('{clientValues.Number_of_Identification}', '{clientValues.FirstName}', '{clientValues.LastName}', '{clientValues.Adress}', '{clientValues.Phone_Number}', '{clientValues.Age}', '{clientValues.Gender}', '{clientValues.Civil_Status}', '{clientValues.Children_Number}', '{clientValues.Height}', '{clientValues.Initial_Hire_Date}', '{clientValues.Basic_Salary}', '{clientValues.Working_Days}')"""
    
  try:
    conexion.cursor.execute(sql)
    conexion.closeDB()
    
  except:
    title = 'ERROR EN GUARDAR REGISTRO'
    description = 'La tabla de clientes no se encuentra creada'
    messagebox.showerror(title, description)
    
def listar():
  conexion  = conexionDB()
  lista_clientes = []
  
  sql = 'SELECT * FROM clientes'
  
  try:
    conexion.cursor.execute(sql)
    lista_clientes = conexion.cursor.fetchall()
    conexion.closeDB()
  except:
    title = 'ERROR LISTAR'
    description = 'No se encontraron datos en la tabla, por favor validar'
    messagebox.showerror(title, description)
    
  return lista_clientes
    
def EditValues(clientValues, idClients):
  
  conexion = conexionDB()
  sql = f"""UPDATE clientes
  SET Number_of_Identification = '{clientValues.Number_of_Identification}',
  FirstName = '{clientValues.FirstName}',
  LastName = '{clientValues.LastName}',
  Adress = '{clientValues.Adress}',
  Phone_Number = '{clientValues.Phone_Number}',
  Age = '{clientValues.Age}',
  Gender = '{clientValues.Gender}',
  Civil_Status = '{clientValues.Civil_Status}',
  Children_Number = '{clientValues.Children_Number}',
  Height = '{clientValues.Height}',
  Initial_Hire_Date = '{clientValues.Initial_Hire_Date}',
  Basic_Salary = '{clientValues.Basic_Salary}',
  Working_Days = '{clientValues.Working_Days}'
  WHERE id = {idClients}"""   
  try:
    conexion.cursor.execute(sql)
    conexion.closeDB()
  except:
    title = 'EDITAR USUARIO'
    description = 'No se puede realizar la actualización de usuarios, por favor validar'
    messagebox.showerror(title, description)
    
def DeleteValues(idClients):
  conexion = conexionDB()
  
  sql = f'DELETE FROM clientes WHERE id = {idClients}'
  try:
    conexion.cursor.execute(sql)
    conexion.closeDB()
  except:
    title = 'ELIMINAR USUARIO'
    description = 'Error al momento de eliminar contacto'
    messagebox.showerror(title, description)