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
    
    for i in range(len(lista)):
        if int(lista[i][1])== int(legajo):
            var=lista[i][-1].split(".")[0]
    fechanueva=datetime.strptime(var, ' ingreso %Y-%m-%d %H:%M:%S')
    if fecha_egreso>=fechanueva:
        ingreso_archivo(legajo,fecha_egreso,False)
    else:
        print("La fecha de egreso es menor que la fecha de ingreso")   

def historial_personal (legajo, nombre,apellido ,fecha,tipo):
    # Utilizo esta funcion para crear el archivo con el historial de fecha de altas y bajas de cada empleado
    try:
        fd= open("Historial_del_personal.txt", "a")
        fd.write("La persona, ")
        fd.write(str(nombre) + " " +str(apellido))
        fd.write(" de legajo, ")
        fd.write(str(legajo)+ ", empezo a trabajar ")
        fd.write(str(fecha))
        fd.write("  como  ")
        fd.write(str(tipo))
        fd.write('\n')
        fd.close()
    except FileNotFoundError:
        fd= open("Historial_del_personal.txt", "x")
        fd.write("La persona, ")
        fd.write(str(nombre) + " " +str(apellido))
        fd.write(" de legajo, ")
        fd.write(str(legajo)+ ", empezo a trabajar ")
        fd.write(str(fecha))   
        fd.write("  como  ")
        fd.write(str(tipo))
        fd.write('\n')
        fd.close()

def asignar_tarea(legajo,tarea):
# Bajo el archivo con el historial del personal en una lista de listas
    lista=[]
    FILE= "Historial_del_personal.txt"
    try:
        with open(FILE, 'r', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                lista.append(fila)
        
        
    except FileNotFoundError:  
        print("El archivo", FILE, "no existe.")
    contador=0
    for i in range(len(lista)):
# Me fijo si el legajo ingresado para asignar la tarea pertenece a un personal en servicio       
        if contador==0:
            if int(legajo)==int(lista[i][2]):
                try:
                    fd= open("tareas.txt", "a")
                    fd.write("El legajo, ")
                    fd.write(str(legajo)+ ", tiene la siguiente asignatura:  ")
                    fd.write(str(tarea))
                    fd.write('\n')
                    fd.close()
                except FileNotFoundError:
                    fd= open("tareas.txt", "x")
                    fd.write(str(legajo)+ ", tiene la siguiente asignatura:  ")
                    fd.write(str(tarea))
                    fd.write('\n')
                    fd.close()
                contador+=1
            else:
                print("El legajo ingresado no es de un personal en servicio")
                contador+=1

def dar_baja_personal(legajo):
    lista=[]
    FILE= "Historial_del_personal.txt"
    try:
        with open(FILE, 'r', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                lista.append(fila)
        
        
    except FileNotFoundError:  
        print("El archivo", FILE, "no existe.")
    for i in range(len(lista)):
        if int(lista[i][2])== int(legajo):
            lista[i].append(" y la fecha de baja es ")
            fecha=dt.date.today()
            lista[i].append(str(fecha))
    with open(FILE, 'w', newline='', encoding='utf-8') as archivo:
                escritor = csv.writer(archivo)
                for reserva in lista:
                    escritor.writerow(reserva)

class Recaudaciones:
    def __init__(self, nombre_archivo):
        self.total_diario = {}  # Dictionary to store daily fundraising totals
        self.nombre_archivo = nombre_archivo
        self.bajar_de_archivo()

    def guardar_donaciones(self, fecha, cant):
        if fecha in self.total_diario:
            self.total_diario[fecha] += cant
        else:
            self.total_diario[fecha] = cant

    def obtener_total_diario(self, fecha):
        if fecha in self.total_diario:
            return self.total_diario[fecha]
        else:
            return 0

    def guardar_en_archivo(self):
        with open(self.nombre_archivo, 'w') as file:
            for fecha, total in self.total_diario.items():
                file.write(f"{fecha}: {total}\n")

    def bajar_de_archivo(self):
        self.total_diario = {}
        try:
            with open(self.nombre_archivo, 'r') as file:
                for line in file:
                    fecha, total = line.strip().split(": ")
                    self.total_diario[fecha] = int(total)
        except FileNotFoundError:
            print(f"Creando archivo {self.nombre_archivo}")

def recaudacion_diaria(recaudado,fecha):
    fundraiser = Recaudaciones("Recaudaciones.txt")
    
    if type(fecha)==dt.date:
        fecha_2 = fecha.strftime('%Y-%m-%d')
        fecha=fecha_2
        
    # Registrar donaciones diarias
    fundraiser.guardar_donaciones(fecha, recaudado)

    # Guardar data en el archivo
    fundraiser.guardar_en_archivo()

    # Obtener totales diarios
    total_1 = fundraiser.obtener_total_diario(fecha)
    

    print(f"Total recaudado en {fecha}: ${total_1}")

def print_menu(menu):
    print("Menu:")
    for item, precio in menu.items():
        print(f"{item}: ${precio:.2f}")

def calcular_total(orden, menu):
    costo_total = sum(menu[item] for item in orden)
    return costo_total

def buffet():
    buffet_menu = {
        "1) Desayuno": 2200,
        "2) Almuerzo": 4000,
        "3) Merienda": 2000,
        "4) Cena": 4500,
        "5) Refresco": 500,
        "6) Agua": 400,
    }

    orden = []

    while True:
        print_menu(buffet_menu)
        print("Ingrese el numerode las opciones que te gustaria agregar a tu pedido, o '0' para terminar la orden.")
        opcion = input("Ingrese el numero de la opcion: ")

        if opcion == '0':
            break

        try:
            opcion = int(opcion)
            if 1 <= opcion <= len(buffet_menu):
                orden.append(list(buffet_menu.keys())[opcion - 1])
            else:
                print("Opcion invalida. Por favor ingrese el numero de vuelta")
        except ValueError:
            print("Input invalido. Ingrese el numero")

    if not orden:
        print("No hay items en tu orden.")
    else:
        costo_total = calcular_total(orden, buffet_menu)
        print("Tu orden:")
        for item in orden:
            print(item)
        print(f"Costo total: ${costo_total:.2f}")
        recaudacion_diaria(costo_total,dt.date.today())

class habitacion():

    def _init_(self,nro,capacidad,precio):
        self.nro=nro
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

# Creacion de las habitaciones
# basica1 = hab_bas(101, 4, 1000)
# intermedia1 = hab_med(201, 2, 2000)
# premium1 = hab_prem(301, 2, 5000)
# basica2 = hab_bas(102, 3, 800)
# intermedia2 = hab_med(202, 4, 3000)
# premium2 = hab_prem(302, 2, 5000)
# basica3 = hab_bas(103, 6, 1500)
# intermedia3 = hab_med(203, 4, 3500)
# premium3 = hab_prem(303, 2, 5000)
# basica4 = hab_bas(104, 3, 800)

# listahab = [] #Lista de todas las habitaciones(libres)
# listahab.append(basica1)
# listahab.append(intermedia1)
# listahab.append(premium1)
# listahab.append(basica2)
# listahab.append(intermedia2)
# listahab.append(premium2)
# listahab.append(basica3)
# listahab.append(intermedia3)
# listahab.append(premium3)
# listahab.append(basica4)

listahabocupadas = [] #lista donde se meten todas las habitaciones ocupadas


class Usuario:
    def __init__(self,nombre,apellido,nombreusuario,dni,contrasena):
        self.nombre=nombre
        self.apellido=apellido
        self.nombreusuario=nombreusuario
        self.dni=dni
        self.contrasena=contrasena

class Cliente(Usuario):
    numero = 1
    def __init__(self, nombre, apellido, nombreusuario, dni, contraseña):
        super().__init__(nombre, apellido, nombreusuario, dni, contraseña)
        self.nro_cliente=Cliente.numero
        Cliente.numero+=1
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
    numero=1
    def __init__(self, nombre, apellido, nombreusuario, dni, contraseña,sueldo):
        super().__init__(nombre, apellido, nombreusuario, dni, contraseña)
        self.nro_personal=Personal.numero
        Personal.numero+=1
        self.sueldo=sueldo
    
    def ingreso (self):
        legajo =self.nro_personal
        fecha=dt.datetime.now()
        ingreso_archivo(legajo,fecha,True)

    def egreso(self):
        legajo =self.nro_personal
        fecha=dt.datetime.now()
        egreso_archivo(legajo,fecha)
        
    def alta(self):
        legajo=self.nro_personal
        nombre=self.nombre
        apellido=self.apellido
        tipo=self.tipo
        fecha_alta=dt.date.today()
        historial_personal (legajo, nombre,apellido ,fecha_alta,tipo)
    
    def baja (self):
        legajo=self.nro_personal
        dar_baja_personal(legajo)
    
    def asignar_tarea (self,tarea):
        legajo=self.nro_personal
        trabajos = self.trabajos
        if tarea.lower() in trabajos:
            asignar_tarea(legajo,tarea)
        else:
            print("La tarea no corresponde al tipo de empleado")



class Administrativo(Personal):
    tipo="Administrador"
    trabajos=["organizar evento","coordinar transporte","recibir al cliente"]

    def __init__(self, nombre, apellido, nombreusuario, dni, contraseña, sueldo):
        super().__init__(nombre, apellido, nombreusuario, dni, contraseña, sueldo)
    
    
        

class Limpieza(Personal):
    tipo="Limpiador"
    trabajos=["lavar cocina","limpiar cuartos","limpiar lobby"]

    def __init__(self, nombre, apellido, nombreusuario, dni, contraseña, sueldo):
        super().__init__(nombre, apellido, nombreusuario, dni, contraseña, sueldo)


class Mantenimiento(Personal):
    tipo="Mantenimiento"
    trabajos=["cortar pasto", "limpiar pileta","podar plantas"]

    def __init__(self, nombre, apellido, nombreusuario, dni, contraseña,sueldo):
        super().__init__(nombre, apellido, nombreusuario, dni, contraseña, sueldo)

# persona=Mantenimiento("ma","u","man","23","ma",12)
# persona1=Limpieza("oeter","u","man","23","ma",12)

# print(persona.nro_personal)
# print(persona1.nro_personal)
