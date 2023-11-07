from Funciones import *
from Tp_PRINCIPAL import *

opcion = input("1: Ingresar a su cuenta \n 2: Crear cuenta \n 0: Salir del programa")
opcion = checkNro(opcion)
while opcion != 0:
    if opcion == 1:
        logIn(listaUsuarios,usuario)