import sqlite3

class conexionDB:
  def __init__(self):
    self.database = 'database/clientes.db'
    self.conexion = sqlite3.connect(self.database)
    self.cursor =  self.conexion.cursor()
  def closeDB(self):
    self.conexion.commit()
    self.conexion.close()