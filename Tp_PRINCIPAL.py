import datetime
import csv


class Usuario:
    def __init__(self,nombre,apellido,nombreusuario,dni,contrasena):
        self.nombre=nombre
        self.apellido=apellido
        self.nombreusuario=nombreusuario
        self.dni=dni
        self.contrasena=contrasena

class Cliente(Usuario):
    def __init__(self, nombre, apellido, nombreusuario, dni, contrasena ,nro_cliente):
        super().__init__(nombre, apellido, nombreusuario, dni, contrasena)
        self.nro_cliente=nro_cliente
    def check_in(self):
        try:
            archivo_cliente = str(self.dni) + '_historial.csv'
            fd = open(archivo_cliente,'x', encoding='utf-8') as archivo
            
        
class Personal(Usuario):
    def __init__(self, nombre, apellido, nombreusuario, dni, contraseña,nro_personal,sueldo,fecha_alta=datetime.date):
        super().__init__(nombre, apellido, nombreusuario, dni, contraseña)
        self.nro_personal=nro_personal
        self.sueldo=sueldo
    

class Administrativo(Personal):
    def __init__(self, nombre, apellido, nombreusuario, dni, contraseña, nro_personal, sueldo, fecha_alta=datetime.date):
        super().__init__(nombre, apellido, nombreusuario, dni, contraseña, nro_personal, sueldo, fecha_alta)

class Limpieza(Personal):
    def __init__(self, nombre, apellido, nombreusuario, dni, contraseña, nro_personal, sueldo, fecha_alta=datetime.date):
        super().__init__(nombre, apellido, nombreusuario, dni, contraseña, nro_personal, sueldo, fecha_alta)

class Mantenimiento(Personal):
    def __init__(self, nombre, apellido, nombreusuario, dni, contraseña, nro_personal, sueldo, fecha_alta=datetime.date):
        super().__init__(nombre, apellido, nombreusuario, dni, contraseña, nro_personal, sueldo, fecha_alta)
    

def jj ():
    
    pass

dni = 45014484
archivo_cliente = str(dni) + '_historial.csv'
print(archivo_cliente)