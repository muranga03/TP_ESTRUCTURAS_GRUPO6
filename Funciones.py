def logIn(lista,usuario):
    '''Esta funcion toma como parametro una lista con todos los usuarios creados y un nombre de usuario ingresado por el usuario
    y verifica si este nombre de usuario existe dentro de la lista al mismo tiempo verifica si la contraseña que ingresa el usuario
    coincide con el nombre de usuario. Si ingresa un usuario que no existe o si ingresa una contraseña erronea se devuelve FALSE, si la contraseña
    es la vinculada con el usuario entonces se devuelve TRUE'''
    for usr in lista:
        if usr.nombredeusuario == usuario:
            contra = input("ingrese su contraseña")
            if contra == usr.contraseña:
                return True
            else:
                print("La contraseña es incorrecta")
                return False
    print("El usuario ingresado no existe")
    return False
    
def signIn(lista):
    '''Esta funcion recibe como parametro una lista con todos los usuarios creados y pide un nombre de usuario y una contraseña para
    asociar a este nuevo usuario. En caso de que ya exista el usuario imprime que ese nombre de usuario ya esta siendo usado y pide uno nuevo'''
    usuario = input("Ingrese su nombre de usuario, no puede tener espacios ni comas")
    if " " in usuario or "," in usuario:
        print("Su nombre de usuario no debe contener ni espacios ni comas, ingrese un nombre nuevo")
    else:
        for usr in lista:
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
                nuevoUsuario = Usuario(nombre,apellido,usuario,dni,contra)
                lista.append(nuevoUsuario)
        

