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
    
def signIn(listaClientes,listaUsuarios):
    '''Esta funcion recibe como parametro una lista con todos los usuarios creados y pide los datos necesarios para
    generar un nuevo usuario. En caso de que ya exista el usuario imprime que ese nombre de usuario ya esta siendo usado y pide uno nuevo.
    Esta funcion solo puede usarse para crear un cliente. El personal lo genera el Administrador'''
    usuario = input("Ingrese su nombre de usuario, no puede tener espacios ni comas. Si desea salir ingrese 'quit'\n ->")
    while " " in usuario or "," in usuario:
        usuario = input("Ingrese su nombre de usuario, no puede tener espacios ni comas. Si desea salir ingrese 'quit'\n ->")
        if usuario == "quit":
            return
    if listaClientes != []:    
        for usr in listaUsuarios:
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
    apellido = apellido.upper()
    dni = input("Ingrese su DNI\n ->")
    while dni.isnumeric()==False or len(dni)!=8:
        dni = input("Ingrese su dni solo con numeros y con 8 digitos\n ->")
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

def mostrar_habitaciones():
    listahab = cargar_habitaciones()
    print('Desea visualizar las habitaciones con algun filtro?')
    rta = input('Si no desea utilizar un filtro, inserte el caracter n, si desea utilizar algun filtro, ingrese cualquier otro caracter')
    if rta ==  'n' or rta == 'N':
        print('Las habitaciones son:')
        for i in listahab:
            print(i)
    else:
        correcto = False
        while correcto == False:
            filtro1 = input('Ingrese que tipo de filtro quiere aplicar: categoria, capacidad, precio')
            filtro1 = filtro1.lower()
            if filtro1 ==  'categoria' or filtro1 == 'capacidad' or filtro1 == 'precio':
                correcto = True
        if filtro1 == 'categoria':
            bien = False
            while bien == False:
                cat = input('ingrese la categoria elegida: premium, intermedia, basica')
                cat = cat.lower()
                cat= cat.capitalize()
                if cat == 'Premium' or cat =='Intermedia' or cat == 'Basica':
                    bien = True
            rta = input('Si no desea utilizar otro filtro, inserte el caracter n, si desea utilizar algun filtro, ingrese cualquier otro caracter')
            if rta ==  'n' or rta == 'N':
                print('Las habitaciones de la categoria ', cat, 'son:')
                for i in listahab:
                    if i.categoria == cat:
                        print(i)
            else: 
                correcto = False
                while correcto == False:
                    filtro2 = input('Ingrese que tipo de filtro quiere aplicar:capacidad, precio')
                    filtro2  = filtro2.lower()
                    if filtro2 == 'capacidad' or filtro2 =='precio':
                        correcto = True
                if filtro2 == 'capacidad':
                    aprobado = False
                    while aprobado == False:
                        numero = input('ingrese la capacidad minima con la que desea filtrar')
                        if numero.isdigit():
                            aprobado = True
                            numero = int(numero)
                    print('Las habitaciones de la categoria ', cat, 'y capacidad mayor a', numero,  'son:')
                    imprimio = False
                    for i in listahab:
                        if i.categoria == cat and i.capacidad >= numero:
                            print(i)
                            imprimio = True
                    if imprimio == False:
                        print('No hay habitaciones con estos requerimientos')
                        
                else:
                    aprobado = False
                    while aprobado== False:
                        numero = input('ingrese el precio maximo con el que desea filtrar')
                        if numero.isdigit():
                            aprobado = True
                            numero = int(numero)
                    print('Las habitaciones de la categoria ', cat, 'y precio menor a', numero,  'son:')
                    imprimio = False
                    for i in listahab:
                        if i.categoria == cat and i.precio <=numero:
                            print(i)
                            imprimio == True
                        if imprimio == False:
                            print('No hay habitaciones con estos requerimientos')
                        
        elif filtro1 == 'capacidad':
            bien = False
            while bien == False:
                numero = input('ingrese la capacidad minima con la que desea filtrar')
                if numero.isdigit():
                    bien = True
                    numero = int(numero)
            rta = input('Si no desea utilizar otro filtro, inserte el caracter n, si desea utilizar algun filtro, ingrese cualquier otro caracter')
            if rta ==  'n' or rta == 'N':
                print('Las habitaciones con capacidad mayor a', numero, 'son:')
                for i in listahab:
                    if i.capacidad >=numero:
                        print(i)
            else:
                correcto = False
                while correcto == False:
                    filtro2 = input('Ingrese que tipo de filtro quiere aplicar:categoria, precio')
                    filtro2  = filtro2.lower()
                    if filtro2 == 'categoria' or filtro2 =='precio':
                        correcto = True
                if filtro2 == 'categoria':
                    bien = False
                    while bien == False:
                        cat = input('ingrese la categoria elegida: premium, intermedia, basica')
                        cat = cat.lower()
                        cat= cat.capitalize()
                        if cat == 'Premium' or cat =='Intermedia' or cat == 'Basica':
                            bien = True
                    print('Las habitaciones de la categoria ', cat, 'y capacidad mayor a', numero,  'son:')
                    imprimio = False
                    for i in listahab:
                        if i.capacidad >= numero and i.categoria == cat:
                            print(i)
                            imprimio == True
                    if imprimio == False:
                        print('No hay habitaciones con estos requerimientos')
                else:
                    aprobado = False
                    while aprobado== False:
                        precio = input('ingrese el precio maximo con el que desea filtrar')
                        if precio.isdigit():
                            aprobado = True
                            precio = int(precio)
                    print('Las habitaciones con capacidad mayor a ', numero, 'y precio menor a', precio,  'son:')
                    imprimio = False
                    for i in listahab:
                        if i.capacidad >= numero and i.precio <=precio:
                            print(i)
                            imprimio == True
                    if imprimio == False:
                        print('No hay habitaciones con estos requerimientos')
        elif filtro1 == 'precio':
            bien = False
            while bien == False:
                precio = input('ingrese el precio maximo con el que desea filtrar')
                if precio.isdigit():
                    bien = True
                    precio = int(precio)
            rta = input('Si no desea utilizar otro filtro, inserte el caracter n, si desea utilizar algun filtro, ingrese cualquier otro caracter')
            if rta ==  'n' or rta == 'N':
                print('Las habitaciones con precio menor a', precio, 'son:')
                imprimio = True
                for i in listahab:
                    if i.precio <= precio:
                        print(i)  
                        imprimio == True
                if imprimio == False:
                    print('No hay habitaciones con estos requerimientos')
            else:
                correcto = False
                while correcto == False:
                    filtro2 = input('Ingrese que tipo de filtro quiere aplicar:categoria, capacidad')
                    filtro2  = filtro2.lower()
                    if filtro2 == 'categoria' or filtro2 =='capacidad':
                        correcto = True
                if filtro2 == 'categoria':
                    bien = False
                    while bien == False:
                        cat = input('ingrese la categoria elegida: premium, intermedia, basica')
                        cat = cat.lower()
                        cat= cat.capitalize()
                        if cat == 'Premium' or cat =='Intermedia' or cat == 'Basica':
                            bien = True
                    print('Las habitaciones de la categoria ', cat, 'y precio menor a', precio,  'son:')
                    imprimio = False
                    for i in listahab:
                        if i.precio <= precio and i.categoria == cat:
                            print(i)
                            imprimio == True
                    if imprimio == False:
                        print('No hay habitaciones con estos requerimientos')
                else:
                    aprobado = False
                    while aprobado== False:
                        numero = input('ingrese la capacidad minima con el que desea filtrar')
                        if numero.isdigit():
                            aprobado = True
                            numero = int(numero)
                    print('Las habitaciones con precio menor a  ', precio, 'y capacidad mayor a', numero,  'son:')
                    imprimio = False
                    for i in listahab:
                        if i.capacidad >=  numero and i.precio <=precio:
                            print(i)
                            imprimio == True
                    if imprimio == False:
                        print('No hay habitaciones con estos requerimientos')

def ocupacion_actual(hoy): #Obtiene y procesa los datos desde la lista de habitaciones ocupadas, luego lo transfiere a un archivo de registro
    listahabocupadas = habitaciones_ocupadas()
    listahab = cargar_habitaciones()
    cap_tot = 0
    ocu_actual = 0
    for i in listahab:
        cap_tot += i.capacidad
    for j in listahabocupadas:
        ocu_actual += j.capacidad
    porcentaje_ocupado = (ocu_actual/cap_tot)*100
    fn = 'ocupacion_diaria.csv'
    info = [hoy, porcentaje_ocupado]
    with open(fn, 'a',newline = '', encoding = 'utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(info)
    return porcentaje_ocupado
   
def ocupacion_segun_tipo(hoy): #Obtiene y procesa los datos desde la lista de habitaciones ocupadas, luego lo transfiere a un archivo de registro
    listahabocupadas = habitaciones_ocupadas()
    listahab = cargar_habitaciones()
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
            usuario = input("Ingrese el nombre de usuario, no puede tener espacios ni comas. Si desea salir ingrese 'quit'\n ->")
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
        apellido = apellido.upper()
        dni = input("Ingrese el DNI\n ->")
        while dni.isnumeric()==False or len(dni)!=8:
            dni = input("Ingrese su dni solo con numeros y con 8 digitos\n ->")
        contra = input("Ingrese la contraseña, debe tener mas de 5 caracteres sin espacios ni comas\n ->")
        while len(contra)<5 or ' ' in contra or ',' in contra:
            contra = input("Ingrese la contraseña denuevo, debe contener al menos 5 caracteres y no puede contener espacios ni comas\n ->")
        sueldo = input("Ingrese el sueldo\n ->")
        negativo = True
        while sueldo.isnumeric()==False or negativo:
            try:
                if int(sueldo)>=0:
                    break
                else:
                    sueldo = input("Ingrese el sueldo solo con numeros, debe ser positivo\n ->")
            except ValueError:
                sueldo = input("Ingrese el sueldo solo con numeros, debe ser positivo\n ->")
        print("se creo bien")
        if tipo == 1:
            nuevoPersonal = Administrativo(nombre,apellido,usuario,dni,contra,sueldo)
        elif tipo == 2:
            nuevoPersonal = Limpieza(nombre,apellido,usuario,dni,contra,sueldo)
        elif tipo == 3:
            nuevoPersonal = Mantenimiento(nombre,apellido,usuario,dni,contra,sueldo)
        listaPersonal.append(nuevoPersonal)


def menu_Limpieza_Mantenimiento(cuenta,listaPersonal,listaClientes,listaUsuarios):
    '''Esta funcion sirve para el menu de limpieza y mantenimiento. Cuando el usuario ingresa le aparecen la siguientes 3 opciones.
      Si elige la opcion 1 entonces se ejecuta otra funcion llamada realizar_tarea, metodo de la clase personal. 
      En las otras dos opciones sale del programa mediante un break'''
    while True:
        print("\nMenú:")
        print("1. Realizar Primer Tarea")
        print("2. Renunciar")
        print("0. Salir del programa")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            cuenta.realizar_tarea()
        elif opcion == "2":
            cuenta.renunciar()
            print("Usted ha renunciado. Muchas gracias por su trabajo realizado durante todo este tiempo")
            cont = 0
            for usr in listaPersonal:
                if usr == cuenta:
                    listaPersonal.pop(cont)
                cont+=1
            listaUsuarios = listaPersonal+listaClientes
            return listaUsuarios
        elif opcion == "0":
            cuenta.egreso()
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

def menu_Administrativo(listaPersonal,ocupActual,ocupBas,ocupMed,ocupPrem,cuenta,hoy):
        '''Esta funcion sirve como menu para el personal de clase Administrativo. Permite realizar cada funcion que cumple un administrador mediante numeros que ingresa el usuario'''

        while True:    
            opcion = input("\n1: Crear una cuenta de Personal \n2: Ver porcentaje de ocupacion actual de habitaciones \n3: Ver Porcentaje de ocupacion actual de habitaciones segun su categoria \n4: Ver recaudacion de hoy \n5: Crear tarea \n6: Eliminar primer tarea \n7: Eliminar ultima queja \n0: Cerrar cuenta \n ->")
            opcion = checkNro(opcion,7)
            if opcion == 1:
                tipo = input("Seleccione el tipo de cuenta que desea crear:\n1: Cuenta Administrador \n2: Cuenta Limpieza \n3: Cuenta Mantenimiento \n0: Si desea regresar al menu \n ->")
                tipo = checkNro(tipo,3)
                crearPersonal(tipo,listaPersonal)

            elif opcion == 2:
                print("El porcentaje de ocupacion de habitaciones actual es: " + ocupActual +'%')

            elif opcion == 3:
                print("El porcentaje de ocupacion de habitaciones de tipo basico actual es: " + ocupBas +'%' + "\nEl porcentaje de ocupacion de habitaciones de tipo medio actual es: " + ocupMed +'%' + "\nEl porcentaje de ocupacion de habitaciones de tipo medio actual es: " + ocupPrem +'%')
                
            elif opcion == 4:
                cuenta.ver_recaudacion_diaria(hoy,True)
                
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
                cuenta.egreso()
                break
            
def menu_cliente(cuenta,lista_reservas,hoy):
    opcion = input("1: Reservar habitacion \n2: Buffet \n3: Presentar queja \n4: Eliminar reserva \n0: Cerrar sesion \n ->")
    opcion = checkNro(opcion,4,0)
    while opcion!=0:
        if opcion==1:
            try:
                fd= open(f"{cuenta.nombreusuario}_historial.csv", "r")
                print("Usted ya tiene una reserva")
                opcion = input("2: Buffet \n3: Presentar queja \n4: Eliminar reserva \n0: Cerrar sesion \n ->")
                opcion = checkNro(opcion,4,0)
            except FileNotFoundError: 
                cuenta.check_in(hoy)
                opcion = input("2: Buffet \n3: Presentar queja \n4: Eliminar reserva \n0: Cerrar sesion \n ->")
                opcion = checkNro(opcion,4,0)
        else:
            try:
                fd= open(f"{cuenta.nombreusuario}_historial.csv", "r")
                if opcion==2:
                    cuenta.buffet()
                    opcion = input("2: Buffet \n3: Presentar queja \n4: Eliminar reserva \n0: Cerrar sesion \n ->")
                    opcion = checkNro(opcion,4,0)
                elif opcion ==3:
                    queja= input("Escriba la queja que quiere presentar")
                    cuenta.presentar_queja(queja)
                    opcion = input("2: Buffet \n3: Presentar queja \n4: Eliminar reserva \n0: Cerrar sesion \n ->")
                    opcion = checkNro(opcion,4,0)
                elif opcion ==4:
                    cuenta.check_out(hoy)
                    cuenta = None
                    return

            except FileNotFoundError:
                print("Usted no hizo el check in. Ingrese nuevamente una opcion")
                opcion = input("1: Reservar habitacion \n2: Buffet \n3: Presentar queja \n4: Eliminar reserva \n0: Cerrar sesion \n ->")
                opcion = checkNro(opcion,4,0)

def cant_clientes_x_categoria(listaClientes):
    cliente_sin_gastos=0
    premium=0
    standar=0
    for item in listaClientes:
        nombre_archivo = f"{item}_gastos.csv"

        try:
            with open(nombre_archivo, 'r') as file:
                lector_csv = csv.reader(file)
                suma = sum(int(fila[0]) for fila in lector_csv)
                print(suma)
            if suma <50000:
                standar+=1
            elif suma>50000:
                premium+=1

        except FileNotFoundError:
            cliente_sin_gastos+=1
    print(f"La cantidad de clientes sin gastos es: {cliente_sin_gastos}\nLa cantidad de clientes categoria Standar es: {standar}\nLa cantidad de clientes premium es: {premium}")
