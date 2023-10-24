import datetime as dt
import csv
from datetime import datetime

def ingreso_archivo (legajo, fecha, var):
    if var :
        # Utilizo esta parte de la funcion para ingresar los datos del ingreso del personal a un archivo
        try:
            fd= open("ingreso.txt", "a")
            fd.write("El legajo, ")
            fd.write(str(legajo)+ ", ingreso ")
            fd.write(str(fecha))
            fd.write('\n')
            fd.close()
        except FileNotFoundError:
            fd= open("ingreso.txt", "x")
            fd.write(str(legajo)+ " ")
            fd.write(str(fecha))
            fd.write('\n')
            fd.close()
    # Utilizo esta parte de la funcion para ingresar los datos del egreso del personal a un archivo
    elif var == False:
        try:
            fd= open("egreso.txt", "a")
            fd.write("El legajo, ")
            fd.write(str(legajo)+ ", egreso ")
            fd.write(str(fecha))
            fd.write('\n')
            fd.close()
        except FileNotFoundError:
            fd= open("egreso.txt", "x")
            fd.write(str(legajo)+ " ")
            fd.write(str(fecha))
            fd.write('\n')
            fd.close()


        
def egreso_archivo(legajo, fecha_egreso):
# traigo el archivo de ingreso y verifico que la fecha de egreso sea posterior a la de ingreso de un legajo

    lista=[]
    FILE= "ingreso.txt"
    try:
        with open(FILE, 'r', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                lista.append(fila)
        
        
    except FileNotFoundError:  
        print("El archivo", FILE, "no existe.")
    fecha= None
    for i in range(len(lista)):
        if int(lista[i][1])== int(legajo):
            var=lista[i][-1].split(".")[0]
    fechanueva=datetime.strptime(var, ' ingreso %Y-%m-%d %H:%M:%S')
    if fecha_egreso>=fechanueva:
        ingreso_archivo(legajo,fecha_egreso,False)
    else:
        print("La fecha de egreso es menor que la fecha de ingreso")   




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
        FILE = str(self.dni) + '_historial.csv'
        lista = []
        try:
            with open(FILE, 'r', encoding='utf-8') as archivo:
                lector = csv.reader(archivo)
                for fila in lector:
                    lista.append(fila)
        except FileNotFoundError:  
            print("El archivo", FILE, "no existe. Se creará el archivo", FILE)
            with open(FILE,'a', encoding = 'utf-8') as archivo:
                lista.append(['DNI','Habitacion','Fecha Check-in','Fecha Check-Out'])
                escritor = csv.writer(archivo)
                for fila in lista:
                    escritor.writerow(fila)
        nrohab = int(input('Ingrese la habitacion deseada'))
        fci = dt.datetime.today().date()
        fco = None
        lista_reserva = [self.dni, nrohab, fci, fco]
        lista.append(lista_reserva)
        with open(FILE, 'w', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            for reserva in lista:
                escritor.writerow(reserva)
    def check_out(self,dias):
        FILE = str(self.dni) + '_historial.csv'
        lista = []
        try: 
            with open(FILE, 'r', encoding='utf-8') as archivo:
                lector = csv.reader(archivo)
                for fila in lector:
                    lista.append(fila)
        except FileNotFoundError:  
            print("El archivo", FILE, "no existe. Se creará el archivo", FILE)
            with open(FILE,'a', encoding = 'utf-8') as archivo:
                lista.append(['DNI','Habitacion','Fecha Check-in','Fecha Check-Out'])
                escritor = csv.writer(archivo)
                for fila in lista:
                    escritor.writerow(fila)
        if len(lista)>1 and lista[len(lista)-1][3] == '':
            fcistr = lista[1][2]
            fci = dt.datetime.strptime(fcistr, '%Y-%m-%d').date()
            fco = fci + dt.timedelta(days=dias)
            lista[len(lista)-1][3] = fco
            with open(FILE, 'w', newline='', encoding='utf-8') as archivo:
                escritor = csv.writer(archivo)
                for reserva in lista:
                    escritor.writerow(reserva)
        else: 
            if len(lista)==1: 
                print('Aún no ha hecho reservas')
            if lista[len(lista)-1][3] != '':
                print('Usted ya ha terminado todas sus reservas')
    def buffet():
        pass
    
class habitacion():
    def _init_(self,nro, capacidad,precio):
        self.nro = nro
        self.capacidad = capacidad
        self.precio = precio
        
class hab_prem(habitacion): #Habitacion Suite/Familiar
    def _init_(self,nro, capacidad,precio, categoria = 'Premium', balcon = True, banopriv= True):
        super()._init_(nro, capacidad,precio)
        self.categoria = categoria
        self.balcon = balcon
        self. banopriv = banopriv
        self.listahab = [self.nro,self.capacidad,self.precio,self.categoria,self.balcon,self.banopriv]
        
class hab_med(habitacion): #Habitacion media
    def _init_(self,nro, capacidad,precio, categoria = 'Intermedia', balcon = False, banopriv= True):
        super()._init_(nro, capacidad,precio)
        self.categoria = categoria
        self.balcon = balcon
        self. banopriv = banopriv
        self.listahab = [self.nro,self.capacidad,self.precio,self.categoria,self.balcon,self.banopriv]

class hab_bas(habitacion): #Habitacion basica
    def _init_(self,nro, capacidad,precio, categoria = 'Basica', balcon = False, banopriv= False):
            super()._init_(nro, capacidad,precio)
            self.categoria = categoria
            self.balcon = balcon
            self. banopriv = banopriv
            self.listahab = [self.nro,self.capacidad,self.precio,self.categoria,self.balcon,self.banopriv]

class Personal(Usuario):

    def __init__(self, nombre, apellido, nombreusuario, dni, contraseña,nro_personal,sueldo,fecha_alta=dt.date):
        super().__init__(nombre, apellido, nombreusuario, dni, contraseña)
        self.nro_personal=nro_personal
        self.sueldo=sueldo
    
    def ingreso (self):
        legajo =self.nro_personal
        fecha=dt.datetime.now()
        ingreso_archivo(legajo,fecha,True)

    def egreso(self):
        legajo =self.nro_personal
        fecha=dt.datetime.now()
        egreso_archivo(legajo,fecha)
        


class Administrativo(Personal):
    def __init__(self, nombre, apellido, nombreusuario, dni, contraseña, nro_personal, sueldo, fecha_alta=dt.date):
        super().__init__(nombre, apellido, nombreusuario, dni, contraseña, nro_personal, sueldo, fecha_alta)

class Limpieza(Personal):
    def __init__(self, nombre, apellido, nombreusuario, dni, contraseña, nro_personal, sueldo, fecha_alta=dt.date):
        super().__init__(nombre, apellido, nombreusuario, dni, contraseña, nro_personal, sueldo, fecha_alta)

class Mantenimiento(Personal):
    def __init__(self, nombre, apellido, nombreusuario, dni, contraseña, nro_personal, sueldo, fecha_alta=dt.date):
        super().__init__(nombre, apellido, nombreusuario, dni, contraseña, nro_personal, sueldo, fecha_alta)
 
