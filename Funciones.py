import csv
# import matplotlib.pyplot as pplt
from Tp_PRINCIPAL import *

def logIn(listaUsuarios):
    '''Esta funcion toma como parametro una lista con todos los usuarios creados y un nombre de usuario ingresado por el usuario
    y verifica si este nombre de usuario existe dentro de la lista al mismo tiempo verifica si la contraseña que ingresa el usuario
    coincide con el nombre de usuario. Si ingresa un usuario que no existe o si ingresa una contraseña erronea se devuelve FALSE, si la contraseña
    es la vinculada con el usuario entonces se devuelve TRUE. Esta funcion sirve tanto para Clientes como para el Personal'''
    usuario = input("Ingrese su nombre de usuario\n ->")
    if usuario == "admin":
        contra = input("Ingrese su contraseña\n ->")
        if contra == "admin":
            admin = Administrativo("","","","","","")
            return admin
        else:
            print("La contraseña es incorrecta\n")
            return None
    for usr in listaUsuarios:
        if usr.nombreusuario == usuario:
            contra = input("Ingrese su contraseña\n ->")
            if contra == usr.contrasena:
                return usr
            else:
                print("La contraseña es incorrecta\n")
                return None
    print("El usuario ingresado no existe\n")
    return None
    
def signIn(listaClientes):
    '''Esta funcion recibe como parametro una lista con todos los usuarios creados y pide los datos necesarios para
    generar un nuevo usuario. En caso de que ya exista el usuario imprime que ese nombre de usuario ya esta siendo usado y pide uno nuevo.
    Esta funcion solo puede usarse para crear un cliente. El personal lo genera el Administrador'''
    usuario = input("Ingrese su nombre de usuario, no puede tener espacios ni comas. Si desea salir ingrese 'quit'\n ->")
    while " " in usuario or "," in usuario:
        usuario = input("Ingrese su nombre de usuario, no puede tener espacios ni comas. Si desea salir ingrese 'quit'\n ->")
        if usuario == "quit":
            return
    if listaClientes != []:    
        for usr in listaClientes:
            if usr.nombreusuario == usuario:
                print("El usuario: " + usuario + " ya existe\n")
                return     
    nombre = input("Ingrese su nombre\n ->")
    while nombre.isalpha()==False:
        nombre = input("Ingrese su nombre solo con letras\n ->")
    nombre = nombre.upper()
    apellido = input("Ingrese su apellido\n ->")
    while apellido.isalpha()==False:
        apellido = input("Ingrese su apellido solo con letras\n ->")
    apellido = nombre.upper()
    dni = input("Ingrese su DNI\n ->")
    dni = checkNro(dni,8,8)
    contra = input("Ingrese su contraseña, debe tener mas de 5 caracteres sin espacios ni comas\n ->")
    while len(contra)<5 or ' ' in contra or ',' in contra:
        contra = input("Ingrese su contraseña denuevo, debe contener al menos 5 caracteres y no puede contener espacios ni comas\n ->")
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
            return listaClientes

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
            return listaPersonal

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

# def analisis_ocupacion(): #Genera un grafico de la ocupacion del hotel a lo largo del tiempo, si no hay informacion, devuelve la ocupacion actual
#     file = 'ocupacion_diaria.csv'
#     lista = []
#     hoy = fecha_actual
#     lista_y = [] #Datos que en graficos iran en eje y
#     lista_x = []#Datos que en graficos iran en eje x
#     try:
#         with open(file, 'r',encoding = 'utf-8') as archivo:
#             lector = csv.reader(archivo)
#             for fila in lector:
#                 lista.append(fila)
#         for i in lista:#Paso datos a listas
#             if len(i) == 2:
#                 i[1] = float(i[1])
#                 lista_y.append(i[1])
#                 dia = i[0][5:]
#                 lista_x.append(dia)
#         pplt.plot(lista_x,lista_y)
#         pplt.xlabel('Fecha')
#         pplt.ylabel('Porcentaje de Ocupacion (%)')
#         pplt.show()
#     except  FileNotFoundError:
#         ocupacion = ocupacion_actual()
#         with open(file, 'w',newline = '',encoding = 'utf-8') as archivo:
#             escritor = csv.writer(archivo)
#             escritor.writerow([hoy, ocupacion])
#         print('Solo se encontró un registro de la ocupación diaria')
#         print('El porcentaje de ocupacion de la fecha: ', hoy, 'fue del :', ocupacion, '%')

def checkNro(numero,maximo=False,minimo=0):
    '''Se fija si la variable numero pedida es un numero y si esta entre los valores minimo y maximo incluidos. En caso de no ingresar un minimo
    este es 0 por default'''
    intervalo = False
    while numero.isnumeric()==False or intervalo==False:
        if maximo:
            try:
                if minimo<=int(numero)<=maximo:
                    intervalo = True
                    break
                else:
                    numero = input("Debe estar entre {} y {}".format(minimo,maximo))
            except ValueError:
                numero = input("Solo debe contener numeros\n ->")          
        else:
            intervalo = True
            numero = input("Solo debe contener numeros\n ->")  
    numero = int(numero)
    return numero

def crearPersonal(tipo,listaPersonal):
    '''Toma como parametro "Tipo" que es un numero del 0 - 3 y pide las variables necesarias para poder crear
    una nueva cuenta de personal. Tambien toma listaPersonal para poder agregarle la nueva cuenta.
            0 : Salir
            1 : Cuenta de Administrador
            2 : Cuenta de Limpieza
            3 : Cuenta de Mantenimiento'''
    if tipo != 0:
        usuario = input("Ingrese su nombre de usuario, no puede tener espacios ni comas. Si desea salir ingrese 'quit'\n ->")
        while " " in usuario or "," in usuario:
            usuario = input("Ingrese su nombre de usuario, no puede tener espacios ni comas. Si desea salir ingrese 'quit'\n ->")
            if usuario == "quit":
                return
        if listaPersonal != []:    
            for usr in listaPersonal:
                if usr.nombreusuario == usuario:
                    print("El usuario: " + usuario + " ya existe")
                    return     
        nombre = input("Ingrese el nombre\n ->")
        while nombre.isalpha()==False:
            nombre = input("Ingrese el nombre solo con letras\n ->")
        nombre = nombre.upper()
        apellido = input("Ingrese el apellido\n ->")
        while apellido.isalpha()==False:
            apellido = input("Ingrese el apellido solo con letras\n ->")
        apellido = nombre.upper()
        dni = input("Ingrese el DNI\n ->")
        dni = checkNro(dni,8,8)
        contra = input("Ingrese la contraseña, debe tener mas de 5 caracteres sin espacios ni comas\n ->")
        while len(contra)<5 or ' ' in contra or ',' in contra:
            contra = input("Ingrese la contraseña denuevo, debe contener al menos 5 caracteres y no puede contener espacios ni comas\n ->")
        sueldo = input("Ingrese el sueldo\n ->")
        while sueldo.isnumeric()==False or sueldo <= 0:
            sueldo = input("Ingrese el sueldo solo con numeros, debe ser positivo\n ->")
        if tipo == 1:
            nuevoPersonal = Administrativo(nombre,apellido,usuario,dni,contra,sueldo)
        if tipo == 2:
            nuevoPersonal = Limpieza(nombre,apellido,usuario,dni,contra,sueldo)
        if tipo == 3:
            nuevoPersonal = Mantenimiento(nombre,apellido,usuario,dni,contra,sueldo)
        listaPersonal.append(nuevoPersonal)

def menu_Limpieza_Mantenimiento(cuenta):
    '''Esta funcion sirve para el menu de limpieza y mantenimiento. Cuando el usuario ingresa le aparecen la siguientes 3 opciones.
      Si elige la opcion 1 entonces se ejecuta otra funcion llamada realizar_tarea, metodo de la clase personal. 
      En las otras dos opciones sale del programa mediante un break'''
    while True:
        print("\nMenú:")
        print("1. Realizar Primer Tarea")
        print("2. Renunciar")
        print("3. Salir del programa")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            cuenta.realizar_tarea()
        elif opcion == "2":
            cuenta.baja()
            print("Usted ha renunciado. Muchas gracias por su trabajo realizado durante todo este tiempo")
            break
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

def menu_Administrativo(listaPersonal,ocupActual,ocupBas,ocupMed,ocupPrem,cuenta,hoy):
        '''Esta funcion sirve como menu para el personal de clase Administrativo. Permite realizar cada funcion que cumple un administrador mediante numeros que ingresa el usuario'''
        
        opcion = input("\n1: Crear una cuenta de Personal \n2: Ver porcentaje de ocupacion actual de habitaciones \n3: Ver Porcentaje de ocupacion actual de habitaciones segun su categoria \n4: Ver recaudacion de hoy \n5: Crear tarea \n6: Eliminar primer tarea \n7: Eliminar ultima queja \n0: Cerrar cuenta \n ->")
        opcion = checkNro(opcion,7)
        while True:    
            if opcion == 1:
                tipo = input("Seleccione el tipo de cuenta que desea crear:\n1: Cuenta Administrador \n2: Cuenta Limpieza \n3: Cuenta Mantenimiento \n0: Si desea regresar al menu \n ->")
                tipo = checkNro(tipo,3)
                crearPersonal(tipo,listaPersonal)

            elif opcion == 2:
                print("El porcentaje de ocupacion de habitaciones actual es: " + ocupActual +'%')

            elif opcion == 3:
                print("El porcentaje de ocupacion de habitaciones de tipo basico actual es: " + ocupBas +'%' + "\nEl porcentaje de ocupacion de habitaciones de tipo medio actual es: " + ocupMed +'%' + "\nEl porcentaje de ocupacion de habitaciones de tipo medio actual es: " + ocupPrem +'%')
                
            elif opcion == 4:
                cuenta.ver_recaudacion_diaria(hoy)
                
            elif opcion == 5:
                tipo == input("Ingrese a que personal quiere agregarle la tarea: \n1: Administrador \n2: Limpieza \n3: Mantenimiento")
                tipo = checkNro(tipo,3,1)
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

            elif opcion == 6:
                cuenta.realizar_tarea()

            elif opcion == 7:
                cuenta.eliminar_ultima_queja()
            
            elif opcion == 0:
                break