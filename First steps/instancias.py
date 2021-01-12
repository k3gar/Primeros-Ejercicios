#Estoy viendo por primera vez la POO y en este caso estoy aplicando lo correspondiente al uso de clases e instancias
#Intentaré explicar mi código

class human(): #Defino mi clase human
    def __init__(self, edad, nombre, ocupacion): #Defino los parametros de los objetos que se crearan
        self.edad = edad
        self.nombre = nombre
        self.ocupacion = ocupacion

    def presentar(self): #Se crea el metodo presentar
        presentacion = ("Hola soy {}, mi edad es {} y mi ocupación es {}")
        print(presentacion.format(self.nombre, self.edad, self.ocupacion))

    def contratar(self, puesto): #Se crea el metodo contratar. Este metodo hará cambios en los datos almacenados en persona1
        self.puesto = puesto
        print("{} ha sido contratado como {}".format(self.nombre, self.puesto))
        self.ocupacion = puesto #Reescribira el valor "Informatico" por el valor "doctor" (segun línea 24)



persona1 = human(18, "Kevin", "Informatico")

persona1.presentar()
persona1.contratar("doctor")
persona1.presentar()

