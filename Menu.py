from Funciones import *
from Tp_PRINCIPAL import *
#Por default existe un usuario "invisible" con nombre de usuario "admin" y contrasena "admin" para que pueda crear el resto de cuentas de personal.

listaClientes = []
listaPersonal = []

hoy = fecha_actual()
clientesArchivo(listaClientes,"descarga")
personalArchivo(listaPersonal,"descarga")
ocupActual = ocupacion_actual()
ocupBas , ocupMed , ocupPrem = ocupacion_segun_tipo()

menu_general = True
while menu_general:
    menu_general = input("1: Crear cuenta \n2: Ingresar a su cuenta \n0: Salir del programa \n ->")
    menu_general = checkNro(menu_general)
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
        
    if tipo_menu == "Administrador":
        menu_admin = input("1: Crear una cuenta de Personal \n2: Ver porcentaje de ocupacion actual de habitaciones \n3: Ver Porcentaje de ocupacion actual de habitaciones segun su categoria \n4: Ver recaudacion de hoy \n5: Crear tarea \n6: Eliminar primer tarea \n7: Eliminar ultima queja \n0: Cerrar Menu Administrativo \n ->")
        menu_admin = checkNro(menu_admin,7)
            
        if menu_admin == 1:
            tipo = input("Seleccione el tipo de cuenta que desea crear:\n1: Cuenta Administrador \n2: Cuenta Limpieza \n3: Cuenta Mantenimiento \n0: Si desea regresar al menu \n ->")
            tipo = checkNro(tipo,3)
            crearPersonal(tipo,listaPersonal)

        elif menu_admin == 2:
            print("El porcentaje de ocupacion de habitaciones actual es: " + ocupActual +'%')

        elif menu_admin == 3:
            print("El porcentaje de ocupacion de habitaciones de tipo basico actual es: " + ocupBas +'%' + "\nEl porcentaje de ocupacion de habitaciones de tipo medio actual es: " + ocupMed +'%' + "\nEl porcentaje de ocupacion de habitaciones de tipo medio actual es: " + ocupPrem +'%')
            
        elif menu_admin == 4:
            cuenta.ver_recaudacion_diaria(hoy)
            
        elif menu_admin == 5:
            tipo == input("Ingrese a que personal quiere agregarle la tarea: \n1: Administrador \n2: Limpieza \n3: Mantenimiento")
            tipo = checkNro(tipo)
            print("Los trabajos disponibles para el tipo de personal elegido son los siguientes: ")
            if tipo == 1:
                clase =  Administrativo
            if tipo == 2:
                clase = Limpieza
            if tipo == 3:
                clase = Mantenimiento
            cont=0
            for i in clase.trabajos:
                print(cont + ": " + i)
                cont=+1
            tarea = input("Ingrese la opcion deseada")
            tarea = checkNro(tarea,len(clase.trabajos))
            cuenta.asignar_tarea(clase.trabajos[tarea],tipo)

        elif menu_admin == 6:
            cuenta.realizar_tarea()

        elif menu_admin == 7:
            cuenta.eliminar_ultima_queja()

    if tipo_menu == "Mantenimiento":
        '''La funcion esta detallada en Funciones.py'''
        menu_Limpieza_Mantenimiento(cuenta)

    if tipo_menu == "Mantenimiento":
        '''La funcion esta detallada en Funciones.py'''
        menu_Limpieza_Mantenimiento(cuenta)



clientesArchivo(listaClientes,"carga")
personalArchivo(listaPersonal,"carga")