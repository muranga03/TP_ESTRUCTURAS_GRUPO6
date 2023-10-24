class Usuario:
    def __init__(self,nombre,apellido,nombreusuario,dni,contraseña):
        self.nombre=nombre
        self.apellido=apellido
        self.nombreusuario=nombreusuario
        self.dni=dni
        self.contraseña=contraseña

    def __str__(self):
        return "hola soy {} mi apellido es {} y mi usuario {}".format(self.nombre,self.apellido,self.nombreusuario)

class Cliente(Usuario):  #para que se ponga solo el numero de cliente
    numero = 1
    def __init__(self, nombre, apellido, nombreusuario, dni, contraseña,):
        super().__init__(nombre, apellido, nombreusuario, dni, contraseña)
        self.nro_cliente=Cliente.numero
        Cliente.numero+=1



lista=[]
prueba = Usuario("pedro","massalin","PedroM",45617662,"massa123")
lista.append(prueba)
prueba = Usuario("pedro2","massalin2","PedroM2",456176622,"massa1232")
lista.append(prueba)
print(lista[0])
print(lista[1])
print(lista)