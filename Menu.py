from Funciones import *
from Tp_PRINCIPAL import *
#Por default existe un usuario "invisible" con nombre de usuario "admin" y contrasena "admin" para que pueda crear el resto de cuentas de personal.

listaClientes = []
listaPersonal = []

hoy = fecha_actual()
clientesArchivo(listaClientes,"descarga")
personalArchivo(listaPersonal,"descarga")
ocupActual = ocupacion_actual(hoy)
ocupBas , ocupMed , ocupPrem = ocupacion_segun_tipo(hoy)
tipo_menu = None

menu_general = True
while menu_general:
    menu_general = input("1: Crear cuenta \n2: Ingresar a su cuenta \n0: Salir del programa \n ->")
    menu_general = checkNro(menu_general,2)
    listaUsuarios = listaClientes + listaPersonal

    if menu_general == 1: #Crear cuenta
        signIn(listaClientes)

    elif menu_general == 2: #Ingresar a cuenta
        cuenta = logIn(listaUsuarios)
        if type(cuenta) == Cliente:
            tipo_menu = "Cliente"
        elif type(cuenta) == Administrativo:
            tipo_menu = "Administrador"
        elif type(cuenta) == Limpieza:
            tipo_menu = "Limpieza"
        elif type(cuenta) == Mantenimiento:
            tipo_menu = "Mantenimiento"
        elif cuenta == None:
            tipo_menu = None
            
   
    if tipo_menu == "Administrador":
        cuenta.ingreso()
        '''La funcion esta detallada en Funciones.py'''
        menu_Administrativo(listaPersonal,ocupActual,ocupBas,ocupMed,ocupPrem,cuenta,hoy)

    if tipo_menu == "Mantenimiento":
        cuenta.ingreso()
        '''La funcion esta detallada en Funciones.py'''
        menu_Limpieza_Mantenimiento(cuenta)

    if tipo_menu == "Limpieza":
        cuenta.ingreso()
        '''La funcion esta detallada en Funciones.py'''
        menu_Limpieza_Mantenimiento(cuenta)
    
    if tipo_menu=="Cliente":
        menu_cliente(cuenta)
        

clientesArchivo(listaClientes,"carga")
personalArchivo(listaPersonal,"carga")