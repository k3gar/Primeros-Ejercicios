class human():
    def __init__(self, edad, nombre, ocupacion):
        self.edad = edad
        self.nombre = nombre
        self.ocupacion = ocupacion

    def presentar(self):
        presentacion = ("Hola soy {}, mi edad es {} y mi ocupación es {}")
        print(presentacion.format(self.nombre, self.edad, self.ocupacion))

    def contratar(self, puesto):
        self.puesto = puesto
        print("{} ha sido contratado como {}".format(self.nombre, self.puesto))
        self.ocupacion = puesto



persona1 = human(18, "Kevin", "Informatico")

persona1.presentar()
persona1.contratar("doctor")
persona1.presentar()