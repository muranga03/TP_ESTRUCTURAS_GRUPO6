import csv
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

persona = Cliente("Pedro","Massalin","Pedrom",45617662,"massa123",1)
persona2 = Cliente("Mato","U","matiu",45617663,"matiu123",2)
lista = [persona,persona2]
clientesArchivo(lista,"carga")