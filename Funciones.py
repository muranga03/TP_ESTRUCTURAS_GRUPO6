import csv
import matplotlib.pyplot as pplt
from Tp_PRINCIPAL import *

def logIn(listaUsuarios,usuario):
    '''Esta funcion toma como parametro una lista con todos los usuarios creados y un nombre de usuario ingresado por el usuario
    y verifica si este nombre de usuario existe dentro de la lista al mismo tiempo verifica si la contraseña que ingresa el usuario
    coincide con el nombre de usuario. Si ingresa un usuario que no existe o si ingresa una contraseña erronea se devuelve FALSE, si la contraseña
    es la vinculada con el usuario entonces se devuelve TRUE. Esta funcion sirve tanto para Clientes como para el Personal'''
    for usr in listaUsuarios:
        if usr.nombreusuario == usuario:
            contra = input("ingrese su contraseña")
            if contra == usr.contrasena:
                return True
            else:
                print("La contraseña es incorrecta")
                return False
    print("El usuario ingresado no existe")
    return False
    
def signIn(listaClientes):
    '''Esta funcion recibe como parametro una lista con todos los usuarios creados y pide los datos necesarios para
    generar un nuevo usuario. En caso de que ya exista el usuario imprime que ese nombre de usuario ya esta siendo usado y pide uno nuevo.
    Esta funcion solo puede usarse para crear un cliente. El personal lo genera el Administrador'''
    usuario = input("Ingrese su nombre de usuario, no puede tener espacios ni comas")
    while " " in usuario or "," in usuario:
        print("Su nombre de usuario no debe contener ni espacios ni comas, ingrese un nombre nuevo. Si desea salir ingrese 'quit'")
        usuario = input("Ingrese su nombre de usuario, no puede tener espacios ni comas")
        if usuario == "quit":
            return
    for usr in listaClientes:
        if usr.nombreusuario == usuario:
            print("El usuario: " + usuario + " ya existe")
            return
        else:
            nombre = input("Ingrese su nombre")
            while nombre.isalpha()==False:
                nombre = input("Ingrese su nombre solo con letras")
            nombre = nombre.upper()
            apellido = input("Ingrese su apellido")
            while apellido.isalpha()==False:
                apellido = input("Ingrese su apellido solo con letras")
            apellido = nombre.upper()
            dni = input("Ingrese su DNI")
            while dni.isnumeric()==False or len(dni)!=8:
                dni = input("Ingrese su DNI solo con numeros, debe tener 8 caracteres")
            contra = input("Ingrese su contraseña, debe tener mas de 5 caracteres sin espacios ni comas")
            while len(contra)<5 or ' ' in contra or ',' in contra:
                contra = input("Ingrese su contraseña denuevo, debe contener al menos 5 caracteres y no puede contener espacios ni comas")
            nuevoUsuario = Cliente(nombre,apellido,usuario,dni,contra)
            listaClientes.append(nuevoUsuario)
    
def clientesArchivo(listaClientes,instancia):
    '''Esta funcion toma como parametros la lista de los clientes para poder cargar los clientes creados en un archivo al finalizar la ejecucion
    y para poder descargar estos usuarios cuando termine la ejecucion del programa. La variable 'instancia' sirve para poder definir si esta funcion se esta corriendo
    para cargar datos o para descargarlos. Se escribe 'carga' o 'descarga' para cuando se inicia el programa o para cuando se cierra respectivamente.'''
    file_path = "Clientes.csv"

    if instancia == 'descarga':
        try:    
            with open(file_path,'r',encoding="utf-8") as archivo:
                lector = csv.reader(archivo)
                for persona in lector:
                    cliente = Cliente(persona[0],persona[1],persona[2],persona[3],persona[4])
                    listaClientes.append(cliente)
                return listaClientes
        except FileNotFoundError:
            return

    elif instancia == 'carga':
        lista = []
        for i in listaClientes:
            clientes = [i.nombre,i.apellido,i.nombreusuario,i.dni,i.contrasena]
            lista.append(clientes)
        with open(file_path, 'w', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerows(lista)

def personalArchivo(listaPersonal,instancia):
    '''Esta funcion toma como parametros la lista del personal para poder cargar al personal creado en un archivo al finalizar la ejecucion
    y para poder descargar estos usuarios cuando termine la ejecucion del programa. La variable 'instancia' sirve para poder definir si esta funcion se esta corriendo
    para cargar datos o para descargarlos. Se escribe 'carga' o 'descarga' para cuando se inicia el programa o para cuando se cierra respectivamente. Esta funcion en instancia 'descarga' devuelve una lista
    con todo el personal instanciado por tipo'''
    file_path = "Personal.csv"
    if instancia == 'descarga':
        try:    
            with open(file_path,'r',encoding="utf-8") as archivo:
                lector = csv.reader(archivo)
                for persona in lector:
                    if persona[0] == "Administrador":
                        personal = Administrativo(persona[1],persona[2],persona[3],persona[4],persona[5],persona[6])
                    elif persona[0] == "Limpiador":
                        personal = Limpieza(persona[1],persona[2],persona[3],persona[4],persona[5],persona[6])
                    elif persona[0] == "Mantenimiento":
                        personal = Mantenimiento(persona[1],persona[2],persona[3],persona[4],persona[5],persona[6])
                    listaPersonal.append(personal)
                return listaPersonal
        except FileNotFoundError:
            return

    elif instancia == 'carga':
        lista = []
        for i in listaPersonal:
            personal = [i.tipo,i.nombre,i.apellido,i.nombreusuario,i.dni,i.contrasena,i.sueldo]
            lista.append(personal)
        with open(file_path, 'w', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerows(lista)
            
def ocupacion_actual(): #Obtiene y procesa los datos desde la lista de habitaciones ocupadas, luego lo transfiere a un archivo de registro
    listahabocupadas = habitaciones_ocupadas()
    listahab = cargar_habitaciones()
    cap_tot = 0
    ocu_actual = 0
    for i in listahab:
        cap_tot += i.capacidad
    for j in listahabocupadas:
        ocu_actual += j.capacidad
    porcentaje_ocupado = (ocu_actual/cap_tot)*100
    hoy = fecha_actual()
    fn = 'ocupacion_diaria.csv'
    info = [hoy, porcentaje_ocupado]
    with open(fn, 'a',newline = '', encoding = 'utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(info)
    return porcentaje_ocupado
   
def ocupacion_segun_tipo(): #Obtiene y procesa los datos desde la lista de habitaciones ocupadas, luego lo transfiere a un archivo de registro
    listahabocupadas = habitaciones_ocupadas()
    listahab = cargar_habitaciones()
    hoy = fecha_actual()
    cap_bas= 0
    ocu_bas = 0
    cap_med = 0
    ocu_med = 0
    cap_prem = 0
    ocu_prem = 0
    for i in listahab:
        if i.categoria == 'Premium':
            cap_prem += i.capacidad
        elif i.categoria == 'Intermedia':
            cap_med += i.capacidad
        elif i.categoria == 'Basica':
            cap_bas += i.capacidad
        
    for j in listahabocupadas:
        if j.categoria == 'Premium':
            ocu_prem += j.capacidad
        elif j.categoria == 'Intermedia':
            ocu_med += j.capacidad
        elif j.categoria == 'Basica':
            ocu_bas += j.capacidad
        
    por_ocup_bas = (ocu_bas/cap_bas)*100
    por_ocup_med = (ocu_med/cap_med)*100
    por_ocup_prem = (ocu_prem/cap_prem)*100
    fb = 'porcentaje_bas.csv'
    info_bas = [hoy, por_ocup_bas]
    with open(fb, 'a',newline = '', encoding = 'utf-8') as arch:
        escritor = csv.writer(arch)
        escritor.writerow(info_bas)
    fm = 'porcentaje_med.csv'
    info_med = [hoy, por_ocup_med]
    with open(fm, 'a',newline = '',encoding = 'utf-8') as arc:
        escritor = csv.writer(arc)
        escritor.writerow(info_med)
    fp = 'porcentaje_prem.csv'
    info_prem = [hoy, por_ocup_prem]
    with open(fp, 'a',newline = '', encoding = 'utf-8') as archiv:
        escritor = csv.writer(archiv)
        escritor.writerow(info_prem)
    return por_ocup_bas, por_ocup_med, por_ocup_prem

def analisis_ocupacion(): #Genera un grafico de la ocupacion del hotel a lo largo del tiempo, si no hay informacion, devuelve la ocupacion actual
    file = 'ocupacion_diaria.csv'
    lista = []
    hoy = fecha_actual
    lista_y = [] #Datos que en graficos iran en eje y
    lista_x = []#Datos que en graficos iran en eje x
    try:
        with open(file, 'r',encoding = 'utf-8') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                lista.append(fila)
        for i in lista:#Paso datos a listas
            if len(i) == 2:
                i[1] = float(i[1])
                lista_y.append(i[1])
                dia = i[0][5:]
                lista_x.append(dia)
        pplt.plot(lista_x,lista_y)
        pplt.xlabel('Fecha')
        pplt.ylabel('Porcentaje de Ocupacion (%)')
        pplt.show()
    except  FileNotFoundError:
        ocupacion = ocupacion_actual()
        with open(file, 'w',newline = '',encoding = 'utf-8') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow([hoy, ocupacion])
        print('Solo se encontró un registro de la ocupación diaria')
        print('El porcentaje de ocupacion de la fecha: ', hoy, 'fue del :', ocupacion, '%')



marcos = Cliente('marcos','viegener', 'marcosvieg', 45014484, 'menemalreves',1)
juan = Cliente('Juan', 'Perez','Juanperez', 12345684, 'milei2023',2)
quito = Cliente('Quito', 'nemen','quinem', 13429534, 'ninfa123',3)


persona = Cliente("Pedro","Massalin","Pedrom",45617662,"massa123",1)
persona2 = Cliente("Mato","U","matiu",45617663,"matiu123",2)
lista = [persona,persona2]
clientesArchivo(lista,"carga")