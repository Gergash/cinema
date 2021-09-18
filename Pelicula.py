from Genero import Genero
from AgeRating import AgeRating


class Pelicula:
    def __init__(self, nombrePeli, duracionPeli, genero, ageRating):
        self.nombrePeli = nombrePeli
        self.duracionPeli = duracionPeli
        self.genero = Genero(genero)
        self.ageRating = AgeRating(ageRating)

    def getNombrePeli(self):
        return self.nombrePeli
    def getDuracionPeli(self):
        return self.duracionPeli
    def getGenero(self):
        return self.genero
    def getAgeRating(self):
        return self.ageRating