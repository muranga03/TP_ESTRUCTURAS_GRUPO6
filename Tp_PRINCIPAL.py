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

#Creacion de las habitaciones
basica1 = hab_bas(101, 4, 1000)
intermedia1 = hab_med(201, 2, 2000)
premium1 = hab_prem(301, 2, 5000)
basica2 = hab_bas(102, 3, 800)
intermedia2 = hab_med(202, 4, 3000)
premium2 = hab_prem(302, 2, 5000)
basica3 = hab_bas(103, 6, 1500)
intermedia3 = hab_med(203, 4, 3500)
premium3 = hab_prem(303, 2, 5000)
basica4 = hab_bas(104, 3, 800)

listahab = [] #Lista de todas las habitaciones(libres)
listahab.append(basica1)
listahab.append(intermedia1)
listahab.append(premium1)
listahab.append(basica2)
listahab.append(intermedia2)
listahab.append(premium2)
listahab.append(basica3)
listahab.append(intermedia3)
listahab.append(premium3)
listahab.append(basica4)

listahabocupadas = [] #lista donde se meten todas las habitaciones ocupadas


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
        existe = False
        ocupado = False
        while existe == False and ocupado == False:
            nrohab = int(input('Ingrese la habitacion deseada'))
            for i in listahab:
                if i.nro == nrohab:
                    existe = True
            for i in listahabocupadas:
                if i.nro ==nrohab:
                    ocupado = True
                    print('Esa habitación esta ocupada')
        if existe ==False:
            print('Esa habitación no existe')
        
        for i in listahab:
            if i.nro == nrohab:
                listahabocupadas.append(i)
                listahab.remove(i)
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
            fcistr = lista[len(lista)-1][2]
            fci = dt.datetime.strptime(fcistr, '%Y-%m-%d').date()
            fco = fci + dt.timedelta(days=dias)
            lista[len(lista)-1][3] = fco
            nrohab = lista[len(lista)-1][1]
            for i in listahabocupadas:
                if i.nro == nrohab:
                    listahab.append(i)
                    listahabocupadas.remove(i)
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
 