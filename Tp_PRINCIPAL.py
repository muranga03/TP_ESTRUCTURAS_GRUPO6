import datetime

class Usuario:
    def __init__(self,nombre,apellido,nombreusuario,dni,contraseña):
        self.nombre=nombre
        self.apellido=apellido
        self.nombreusuario=nombreusuario
        self.dni=dni
        self.contraseña=contraseña

class Cliente(Usuario):
    def __init__(self, nombre, apellido, nombreusuario, dni, contraseña,nro_cliente):
        super().__init__(nombre, apellido, nombreusuario, dni, contraseña)
        self.nro_cliente=nro_cliente

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
    


