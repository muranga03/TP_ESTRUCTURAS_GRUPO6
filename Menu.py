from Funciones import *
from Tp_PRINCIPAL import *


listaClientes = []
listaPersonal = []

clientesArchivo(listaClientes,"descarga")
personalArchivo(listaPersonal,"descarga")

opcion = False
while opcion:
    opcion = input("1: Crear cuenta \n2: Ingresar a su cuenta \n0: Salir del programa \n ->")
    opcion = checkNro(opcion)
    listaUsuarios = listaClientes + listaPersonal

    if opcion == 1: #Crear cuenta
        signIn(listaClientes)

    if opcion == 2: #Ingresar a cuenta
        cuenta = logIn(listaUsuarios)
        if type(cuenta) == Cliente:
            menu = "Cliente"
        elif type(cuenta) == Administrativo:
            menu = "Administrador"
        elif type(cuenta) == Limpieza:
            menu = "Limpieza"
        elif type(cuenta) == Mantenimiento:
            menu = "Mantenimiento"
        
    if menu == "Administrador":
        menu = input("1: Menu Administrativo \n2: Menu Cliente \n3: Menu Limpieza \n4: Menu Mantenimiento \n0: Cerrar sesion \n ->")
        menu = checkNro(menu)
        if menu == 1:
            opcion = input("1: Crear una cuenta de Personal \n2:  \n3:  \n4:  \n5:  \n6:  \n0:  \n ->")
            opcion = checkNro(opcion)
            if opcion == 1:
                tipo = input("Seleccione el tipo de cuenta que desea crear:\n1: Cuenta Administrador \n2: Cuenta Limpieza \n3: Cuenta Mantenimiento \n0: Si desea regresar al menu \n ->")
                tipo = checkNro(tipo)
                crearPersonal(tipo,listaPersonal)


clientesArchivo(listaClientes,"carga")
personalArchivo(listaPersonal,"carga")