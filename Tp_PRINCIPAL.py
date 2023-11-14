import datetime as dt
import csv
from Funciones import *
              
class Reserva:
    def __init__(self, habit, usuario, entrada, salida):
        self.habit = habit
        self.usuario = usuario
        self.entrada = entrada
        self.salida = salida
        self.prox = None

class Lista_reservas:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head is None
    def subir_lista_reservas(self): #Sube los cambios a un archivo, para guardar la información
        FILE = 'lista_reservas.csv'
        with open(FILE, 'w', newline = '', encoding = 'utf-8') as archivo:
            escritor = csv.writer(archivo)
            if self.is_empty():
                return
            current = self.head
            while current:
                lista = []
                lista.append(current.usuario.nombreusuario)
                lista.append(current.habit.nro)
                lista.append(current.entrada)
                lista.append(current.salida)
                escritor.writerow(lista)
                current = current.prox
        return
    

    def agregar_reserva(self,habit, usuario, fecha_ent, fecha_sal):
        new_node=Reserva(habit, usuario, fecha_ent, fecha_sal)
        if self.is_empty():
            self.head = new_node
            return
        current = self.head
        while current.prox:
            current = current.prox
        current.prox = new_node

    def eliminar_reserva(self,hoy, nombreusuario):
        '''
        Este método busca el primer nodo cuyo valor se corresponde al argumento y lo desenlaza. 
        
        '''
        if self.is_empty():
            return

        if self.head.usuario.nombreusuario == nombreusuario:
            if self.head.entrada > hoy:
                self.head = self.head.prox
                print('Usted ha eliminado su reserva')
            else:
                print('No puede eliminar una reserva que ya ha hecho el check in')
            return

        current = self.head
        while current.prox:
            if current.prox.usuario.nombreusuario == nombreusuario:
                current.prox = current.prox.prox
                return
            else: 
                current = current.prox
        self.subir_lista_reservas()
        
    def buscar_cuarto(self, nrohab): #Si el valor de encontrado es False, esta funcion me deja directamente hacer la reserva para ese cuarto 
        current = self.head
        encontrado = False
        if self.is_empty():
            return encontrado
        while current:
            if current.habit.nro == nrohab:
                encontrado = True
            current = current.prox
        return encontrado
    def buscar_cliente(self, nombreusuario):#Funcion que me sirve para ver si el cliente tiene o no reservas hechas, (el cliente solo puede tener una reserva a la vez)
        current = self.head
        encontrado = False
        if self.is_empty():
            print('No hay reservas, está habilitado a hacer reservas')
            return encontrado
        while current:
            if current.usuario.nombreusuario == nombreusuario:
                encontrado = True 
            current = current.prox
        return encontrado
    def buscar_cliente_activo(self, nombreusuario,hoy):#Funcion que me sirve para ver si el cliente tiene o no reservas hechas, (el cliente solo puede tener una reserva a la vez)
        current = self.head
        if self.is_empty():
            print('No hay reservas, está habilitado a hacer reservas')
            return False
        while current:
            if current.usuario.nombreusuario == nombreusuario:
                if current.entrada < hoy:
                    return True
            current = current.prox
        return False
    def confirmar_entrada(self,nrohab,entrada, salida): #entrada y salida son las fechas de reserva que pide el usuario
        current = self.head
        habilitado = True #Decide si esta bien pedida esta reserva, si es False no esta bien, si es True, si
        if self.is_empty():
            return habilitado
        while current: #Checkeo para todas las reservas, que cambie el valor de habilitado, cuando se termine de verificar me dira si esta bien o no
            if current.habit.nro == nrohab:
                if current.entrada > entrada: #si la fecha de entrada de reserva es mayor a la pedida, tengo que checkear que la fecha de salida pedida sea menor a la entrada de la reserva
                    if current.entrada > salida:
                        habilitado = True#Como las fechas de entrada y salida son menores a la de entrada y reserva, se puede hacer la reserva (con la informacion que tenemos, despues hay que seguir checkeando el resto de las reservas)
                        return habilitado
                    else: 
                        habilitado = False
                        return habilitado
                elif current.entrada < entrada < current.salida: #La entrada no puede pisarse con otra estadia
                    habilitado = False
                    return habilitado
                elif current.salida < entrada: #Si la fecha de entrada pedida, es mayor a la de salida de la resrva, todo ok
                    habilitado = True
                    return habilitado
            current = current.prox
        return habilitado
    def recorrer_para_check_in(self,hoy): #Funcion que recorre la lista todos los dias, para hacer 'entrar' a los clientes
        current = self.head
        encontrado = False
        if self.is_empty():
            return encontrado
        while current:
            if current.entrada == hoy:
                nrohabit = current.habit.nro
                entrada = current.entrada
                current.usuario.check_in(nrohabit,entrada,hoy)
            current = current.prox
    def recorrer_para_check_out(self,hoy):
        '''
        Este metodo recorre la lista, y le hace el checkout a las reservas cuya fecha es igual a la fecha actual
        '''
        if self.is_empty():
            return

        elif self.head.salida == hoy:
            self.head = self.head.prox
            return

        current = self.head
        while current.prox:
            if current.prox.salida == hoy:
                nrohabit = current.habit.nro
                entrada = current.entrada
                salida = current.salida
                current.prox.usuario.check_out(nrohabit,entrada,salida,hoy)
                current.prox = current.prox.prox
                return
            else: 
                current = current.prox
    def habitaciones_con_reservas(self): #Funcion que sirve para directamente mostrar las habitaciones que estan ocupadas
        habitaciones_con_reservas = set() #Se utilizan sets, para mostrarle directamente al cliente que habitaciones estan disponibles, asi ayuda a la seleccion de la habtiacion
        if self.is_empty():
            print('No hay habitaciones con reservas hechas')
            return 
        else:
            current = self.head
            while current:
                habitaciones_con_reservas.add(current.habit.nro)
                current = current.prox
            print('Las habtiaciones con reservas son:')
            for i in habitaciones_con_reservas:
                print(i)
    def quesoy(self):
        if self.is_empty():
            print('La lista esta vacia')
            return
        else:
            current = self.head
            while current:
                print(current.habit.nro)
                current = current.prox

class Recaudaciones:
    '''Clase creada especialmente para el manejo de las recaudaciones diarias'''
    def __init__(self, nombre_archivo):
        self.total_diario = {}  # Utilizamos un diccionario para almaceral las recaudaciones diarias
        self.nombre_archivo = nombre_archivo
        self.bajar_de_archivo()

    def guardar_recaudacion(self, fecha, cant):
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

class habitacion():

    def __init__(self,nro,capacidad,precio):
        self.nro=nro
        self.capacidad = capacidad
        self.precio = precio
        
class hab_prem(habitacion): #Habitacion Suite/Familiar
    def __init__(self,nro, capacidad,precio, categoria = 'Premium', balcon = True, banopriv= True):
        super().__init__(nro, capacidad,precio)
        self.categoria = categoria
        self.balcon = balcon
        self. banopriv = banopriv
        self.listahab = [self.nro,self.capacidad,self.precio,self.categoria,self.balcon,self.banopriv]
    def __str__(self):
        return("La habitacion numero {}, tiene una capacidad para {} personas y un precio {} pesos, pertenece a la categoria {} que tiene baño privado y balcon".
               format(self.nro, self.capacidad, self.precio, self.categoria))
          
class hab_med(habitacion): #Habitacion media
    def __init__(self,nro, capacidad,precio, categoria = 'Intermedia', balcon = False, banopriv= True):
        super().__init__(nro, capacidad,precio)
        self.categoria = categoria
        self.balcon = balcon
        self. banopriv = banopriv
        self.listahab = [self.nro,self.capacidad,self.precio,self.categoria,self.balcon,self.banopriv]
    def __str__(self):
        return("La habitacion numero {}, tiene una capacidad para {} personas y un precio {} pesos, pertenece a la categoria {} que tiene baño privado y no tiene balcon".
               format(self.nro, self.capacidad, self.precio, self.categoria))

class hab_bas(habitacion): #Habitacion basica
    def __init__(self,nro, capacidad,precio, categoria = 'Basica', balcon = False, banopriv= False):
            super().__init__(nro, capacidad,precio)
            self.categoria = categoria
            self.balcon = balcon
            self. banopriv = banopriv
            self.listahab = [self.nro,self.capacidad,self.precio,self.categoria,self.balcon,self.banopriv]
    def __str__(self):
        return("La habitacion numero {}, tiene una capacidad para {} personas y un precio {} pesos, pertenece a la categoria {} que no tiene baño privado ni balcon".
               format(self.nro, self.capacidad, self.precio, self.categoria))
                
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
    def check_in(self,nrohabit,entrada,hoy): #Mete al usuario al hotel, al hacerlo, se agrega la informacion al archvo del cliente
        FILE = str(self.nombreusuario) + '_historial.txt'
        hora = dt.datetime.now().strftime("%H:%M")
        lista = []
        multa = 0
        listahab = cargar_habitaciones()
        listahabocupadas = habitaciones_ocupadas()
        escribo = str(self.dni)+ ', ' + str(nrohabit) + ', ' + str(entrada)
        
        
        try: # Probamos el siguiente código
            with open(FILE, 'r', encoding='utf-8') as archivo:
                archivo.readlines()
            
            with open(FILE, 'r', encoding='utf-8') as archivo:
                archivo.write(escribo)
        except FileNotFoundError:  # Si se encuentra un error se ejecuta esta parte
            with open(FILE,'a', encoding = 'utf-8') as archivo:
                archivo.write('DNI, Habitacion, Fecha Check-in, Fecha Check-Out')
                
        fp = 'habitaciones_ocupadas.csv'
        for i in listahab:
            if i.nro == nrohabit:
                listahabocupadas.append(i)
                noc = i.nro
                co = i.capacidad
                po = i.precio
                cato = i.categoria
                bo = i.balcon
                bpo = i.banopriv
                habo = [noc, co, po, cato, bo, bpo]
                print('El usuario,',self.nombreusuario, 'ha ingresado a la habitación', noc)
        with open (fp, 'a', newline = '', encoding = 'utf-8')as arc:
            escritor = csv.writer(arc)
            escritor.writerow(habo)
        if hora < '09:00' or hora > '18:00':
            multa = 500
            descripcionmulta = 'Multa por check in fuera de horario establecido'
        fci = entrada
        fco = None
        lista_registro =[self.dni, nrohabit, fci, fco]
        lista.append(lista_registro)
        with open(FILE, 'w', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            for reserva in lista:
                escritor.writerow(reserva)
        file2 =   str(self.nombreusuario) + '_gastos.csv'
        if multa > 0:
            with open(file2,'a', newline = '', encoding = 'utf-8') as registro:
                writer =csv.writer(registro)
                gasto = [multa, descripcionmulta]
                writer.writerow(gasto)
                recaudacion_diaria(multa,hoy)
            

    def check_out(self,nrohabit,entrada,salida,hoy):
        FILE = str(self.nombreusuario) + '_historial.txt'
        lista = []
        multa = 0
        hora = dt.datetime.now().strftime("%H:%M")
        listahabocupadas = habitaciones_ocupadas()
        listahab = cargar_habitaciones()
        rescribo = str(self.dni)+ ', ' + str(nrohabit) + ', ' + str(entrada) + ', ' + str(salida)
        try: # Probamos el siguiente código
            with open(FILE, 'r', encoding='utf-8') as archivo:
                lineas= archivo.readlines()
            if lineas:
                lineas[-1] = rescribo
            with open(FILE, 'w', encoding='utf-8') as archivo:
                archivo.writelines(lineas)
                
            duracion = str(salida - entrada)
            digito = ''
            for i in duracion:
                if i.isdigit() and listo == False:
                    digito += i
                if i == ' ':
                    listo = True
            dias = int(digito)
            rescribo = str(self.dni)+ ', ' + str(nrohabit) + ', ' + str(entrada) + ', ' + str(salida)
            
            for i in listahab:
                if i == nrohabit:
                    montodiario = i.precio
            with open(FILE, 'w', newline='', encoding='utf-8') as archivo:
                escritor = csv.writer(archivo)
                for reserva in lista:
                    escritor.writerow(reserva)
            if hora < '09:00' or hora > '18:00':
                multa = 500
                descripcionmulta = 'Multa por check out fuera de horario establecido'
            montotot = dias*montodiario
            recaudacion_diaria(montotot,hoy)
            descripcion = 'Estadia desde ' + str(entrada) + ' hasta ' + str(salida)
            file2 =   str(self.nombreusuario) + '_gastos.csv'
            with open(file2,'a', newline = '', encoding = 'utf-8') as registro:
                writer =csv.writer(registro)
                gasto = [montotot, descripcion]
                writer.writerow(gasto)
                if multa > 0:
                    gasto2 = [multa, descripcionmulta]
                    writer.writerow(gasto2) 
                    recaudacion_diaria(multa)
    
            fp = 'habitaciones_ocupadas.csv'
            with open (fp, 'w', newline = '', encoding = 'utf-8')as arc:
                escritor = csv.writer(arc)
                for i in listahabocupadas:
                    noc = i.nro
                    co = i.capacidad
                    po = i.precio
                    cato = i.categoria
                    bo = i.balcon
                    bpo = i.banopriv
                    habo = [noc, co, po, cato, bo, bpo]
                    escritor.writerow(habo) 
        except FileNotFoundError:
            return
    
    def buffet(self,hoy):
        ''' Este metodo al ser ejecutado te presenta el menu con sus distintas opciones, permitiendote elegir una opcion a la vez.
        Una vez terminado tu pedido hace la suma del total y lo agrega a tus historial de gastos como cliente y a la recaudacion diaria. Esta funcion utiliza un diccionario en buffet_menu'''
        buffet_menu = {
            "1) Desayuno": 220,
            "2) Almuerzo": 400,
            "3) Merienda": 200,
            "4) Cena": 450,
            "5) Refresco": 50,
            "6) Agua": 40,
        }

        orden = []

        while True:
            print_menu(buffet_menu)
            opcion = input("Ingrese el numero de las opciones que te gustaria agregar a tu pedido, o '0' para terminar la orden.\n ->")
            opcion = checkNro(opcion,len(buffet_menu))
            orden.append(list(buffet_menu.keys())[opcion - 1])
            if opcion == 0:
                break

        if not orden:
            print("No hay items en tu orden.")
        else:
            costo_total = calcular_total(orden, buffet_menu)
            print("Tu orden:")
            for item in orden:
                print(item)
            print(f"Costo total: ${costo_total:.2f}")
            recaudacion_diaria(costo_total,hoy)
            file2 =   str(self.nombreusuario) + '_gastos.csv'
            descripcion = 'Compra en el buffet'
            with open(file2,'a', newline = '', encoding = 'utf-8') as registro:
                writer =csv.writer(registro)
                gasto = [costo_total, descripcion]
                writer.writerow(gasto)
            

    def presentar_queja(self, queja):
        '''Cuando llamas este metodo del cliente, agrega tu queja a un archivo que acumula todas las quejas de los distintos clientes.
          Luego el administrador tiene la posibilidad de resolver la queja, mediante un metodo propio de su clase'''
        try:
            with open("quejas.txt", "a") as file:
                file.write(f"Cliente: {self.nro_cliente}, ")
                file.write(f"Queja: {queja}\n")
                file.write("-" * 20 + "\n")  # Separador
            print("Tu queja ha sido registrada con éxito. Gracias por tu retroalimentación.")
        except IOError as e:
            print(f"Error al guardar la queja: {e}")    
    
    def crear_reserva(self, lista_reservas,hoy):
        listahab = cargar_habitaciones()
        listahabocupadas = habitaciones_ocupadas()
        nombreusuario = self.nombreusuario
        encontrado = lista_reservas.buscar_cliente(nombreusuario)#Esta variable me dice si el cliente tiene o no una reserva
        if encontrado == False: 
            existe = False
            mostrar_habitaciones()
            while existe == False:
                nrohab = (input('Ingrese la habitacion deseada'))
                try:
                    existe = False
                    nrohab = int(nrohab)
                    for i in listahab:
                        if i.nro == nrohab:
                            print(i.nro)
                            existe = True
                    print(existe)
                    if existe == False:
                        print('Esta habitacion no existe')
                except ValueError:
                    print('Escriba el numero de habitacion Correctamente')
            for i in listahab:
                if i.nro == nrohab:
                    habitacion = i
            
            if lista_reservas.buscar_cuarto(habitacion.nro) == False: #Busca en la lista de reservas, si no esta el cuarto, puede directamente hacer la reserva
                fechabien = False
                while fechabien == False: #Ojo fijarse en archivo fecha actual ya que los dias corren cada vez que se ejecuta el programa
                    try:
                        fci =input('ingrese la fecha en la que quiere reservar en el formato: yyyy-mm-dd')
                        entrada = dt.datetime.strptime(fci, '%Y-%m-%d').date()
                        if entrada > hoy:
                            fechabien = True
                    except ValueError:
                        print('inserte la fecha en el formato pedido')
                diasbien = False
                while diasbien == False:
                    try:
                        dias = input('Ingrese la cantidad de dias que se quiere quedar')
                        dias = int(dias)
                        diasbien = True
                    except ValueError:
                        print('Inserte un valor unitario de dias')
                salida = entrada + dt.timedelta(days = dias)
                lista_reservas.agregar_reserva(habitacion,self,entrada,salida)
                lista_reservas.subir_lista_reservas()
                print('Se hizo la reserva exitosamente')
            else:
                loop = True
                while loop:
                    fechabien = False
                    while fechabien == False:
                        try:
                            fci =input('ingrese la fecha en la que quiere reservar en el formato: yyyy-mm-dd')
                            entrada = dt.datetime.strptime(fci, '%Y-%m-%d').date()
                            if entrada > hoy:
                                fechabien = True
                        except ValueError:
                            print('inserte la fecha en el formato pedido')
                    diasbien = False
                    while diasbien == False:
                        try:
                            dias = input('Ingrese la cantidad de dias que se quiere quedar')
                            dias = int(dias)
                            diasbien = True
                        except ValueError:
                            print('Inserte un valor unitario de dias')
                    salida = entrada + dt.timedelta(days = dias)
                    confirmado = lista_reservas.confirmar_entrada(habitacion.nro,entrada, salida)
                    if confirmado == True:
                        lista_reservas.agregar_reserva(habitacion,self,entrada,salida)
                        print('Se hizo la reserva exitosamente')
                        lista_reservas.subir_lista_reservas()
                        loop = False
                    else:
                        print('\nEsa habitacion está reservada en el rango de las fechas pedidas\n')
                        loop = True
        else: 
            print('Usted ya esta ocupando una habitación, por politica del hotel no puede hacer una reserva')
    def cancelar_reserva(self,lista_reservas,hoy,nombreusuario):
        nombreusuario = self.nombreusuario
        presente = lista_reservas.buscar_cliente(nombreusuario)
        if presente == False:
            print('Usted no tiene reservas hechas')
        else: 
            lista_reservas.eliminar_reserva(hoy,nombreusuario)

class Personal(Usuario):
    numero=1
    def __init__(self, nombre, apellido, nombreusuario, dni, contraseña,sueldo):
        super().__init__(nombre, apellido, nombreusuario, dni, contraseña)
        self.nro_personal=Personal.numero
        Personal.numero+=1
        self.sueldo=sueldo
    
    def ingreso (self,hoy):
        nombre=self.nombreusuario
        ingreso_y_egreso(nombre,hoy,False,True)

    def egreso(self,hoy):
        nombre=self.nombreusuario
        ingreso_y_egreso(nombre,hoy,False,False)

    def renunciar(self,hoy):
        nombre=self.nombreusuario
        ingreso_y_egreso(nombre,hoy,True,False)

    def realizar_tarea(self): # En este metodo utilizamos una cola ya que la primer tarea en ser ingresada es la primera en ser realizada
        nombre_archivo = f"tareas_{self.tipo}.txt"  
        try:
            with open(nombre_archivo, "r") as file:
                tareas = file.readlines()

            if not tareas:
                print(f"No hay tareas en el archivo '{nombre_archivo}'.")
                return
            
            tareas.pop(0)  # Elimina la primera tarea

            with open(nombre_archivo, "w") as file:
                file.writelines(tareas)

            print("La primera tarea ha sido eliminada con éxito.")
        except FileNotFoundError:
            print(f"No existe el archivo: {nombre_archivo}")
    
class Administrativo(Personal):
    tipo="Administrativo"
    trabajos=["Organizar un evento","Coordinar el transporte","Recibir al cliente"]
    
    def __init__(self, nombre, apellido, nombreusuario, dni, contraseña, sueldo):
        super().__init__(nombre, apellido, nombreusuario, dni, contraseña, sueldo)
    
    def ver_recaudacion_diaria(self,fecha):
        self.fecha=fecha
        fundraiser = Recaudaciones("Recaudaciones.txt")
        total=fundraiser.obtener_total_diario(fecha)
        print(f"Total recaudado en {fecha}: ${total}")
    
    def eliminar_ultima_queja(self):        # Implemento una pila, siendo la ultima queja la primera en resolverse
        try:
            with open("quejas.txt", "r") as file:
                lines = file.readlines()

            if not lines:
                print("No hay quejas registradas para eliminar.")
                return

            while lines and lines[-1].strip() == "-" * 20:
                lines.pop()  
                if not lines:
                    print("No hay quejas registradas para eliminar.")
                    return

            lines.pop()  # Elimina la última queja

            with open("quejas.txt", "w") as file:
                file.writelines(lines)

            print("La última queja ha sido eliminada con éxito.")

        except FileNotFoundError:
            print("El archivo quejas.txt no existe")
    
    def asignar_tarea (self,tarea,tipo):
        if tipo == 1:
            
            nombre="Administrativo"
        elif tipo ==2:
            
            nombre="Limpieza"
        elif tipo ==3:
            
            nombre="Mantenimiento"
        
        nombre_archivo = f"tareas_{nombre}.txt"  
        try:
            with open(nombre_archivo, "a") as file:
                file.write(tarea + "\n")  
            print(f"La tarea se ha guardado en el archivo '{nombre_archivo}' con éxito.")
        except IOError as e:
            print(f"Error al guardar la tarea en el archivo: {e}")
    
class Limpieza(Personal):
    tipo="Limpieza"
    trabajos=["Lavar la cocina","Limpiarlos cuartos","Limpiar el lobby"]

    def __init__(self, nombre, apellido, nombreusuario, dni, contraseña, sueldo):
        super().__init__(nombre, apellido, nombreusuario, dni, contraseña, sueldo)

class Mantenimiento(Personal):
    tipo="Mantenimiento"
    trabajos=["Cortar el pasto", "Limpiar la pileta","Podar las plantas"]

    def __init__(self, nombre, apellido, nombreusuario, dni, contraseña,sueldo):
        super().__init__(nombre, apellido, nombreusuario, dni, contraseña, sueldo)
