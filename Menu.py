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
opcion = True

opcion = True
while opcion:
    opcion = input("1: Crear cuenta \n2: Ingresar a su cuenta \n0: Salir del programa \n ->")
    opcion = checkNro(opcion)
    listaUsuarios = listaClientes + listaPersonal

    if opcion == 1: #Crear cuenta
        signIn(listaClientes)

    elif opcion == 2: #Ingresar a cuenta
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
        while menu==1:
            opcion = input("1: Crear una cuenta de Personal \n2: Ver porcentaje de ocupacion actual de habitaciones \n3: Ver Porcentaje de ocupacion actual de habitaciones segun su categoria \n4: Ver recaudacion de hoy \n5: Crear tarea \n6: Eliminar primer tarea \n7: Eliminar ultima queja \n0: Cerrar Menu Administrativo \n ->")
            opcion = checkNro(opcion)
            
            if opcion == 1:
                tipo = input("Seleccione el tipo de cuenta que desea crear:\n1: Cuenta Administrador \n2: Cuenta Limpieza \n3: Cuenta Mantenimiento \n0: Si desea regresar al menu \n ->")
                tipo = checkNro(tipo)
                crearPersonal(tipo,listaPersonal)

            elif opcion == 2:
                print("El porcentaje de ocupacion de habitaciones actual es: " + ocupActual +'%')

            elif opcion == 3:
                print("El porcentaje de ocupacion de habitaciones de tipo basico actual es: " + ocupBas +'%' + "\nEl porcentaje de ocupacion de habitaciones de tipo medio actual es: " + ocupMed +'%' + "\nEl porcentaje de ocupacion de habitaciones de tipo medio actual es: " + ocupPrem +'%')
            
            elif opcion == 4:
                cuenta.ver_recaudacion_diaria(hoy)
            
            elif opcion == 5:
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
                tarea = checkNro(tarea)
                cuenta.asignar_tarea(tarea,tipo)

            elif opcion == 6:
                cuenta.borrar_primera_tarea()

            elif opcion == 7:
                cuenta.eliminar_ultima_queja()

    if menu == "Mantenimiento":
        '''La funcion esta detallada en Funciones.py'''
        menu_Limpieza_Mantenimiento(cuenta)

    if menu == "Mantenimiento":
        '''La funcion esta detallada en Funciones.py'''
        menu_Limpieza_Mantenimiento(cuenta)



clientesArchivo(listaClientes,"carga")
personalArchivo(listaPersonal,"carga")