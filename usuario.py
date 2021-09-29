"""clase usuario que recibe dos parametros y un método, id, nombre como parametro: saludar"""
import random as rd
class Usuario():
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
    def saludar(self):
        return f"Hola {self.nombre}, viva el Sheriff, futbol champagne {self.id}"

def estAnimo():
    estado = ["Alegre","rabioso","dichoso","sadness"]
    return rd.choice(estado)


