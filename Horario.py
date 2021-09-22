from Pelicula import Pelicula
from TipoMem import TipoMem
from AgeRating import AgeRating

class Horario:
    def __init__(self, horaInicio, horaCierre, nombrePeli, duracionPeli, genero, ageRating):
        self.horaInicio = horaInicio
        self.horaCierre = horaCierre
        self.pelicula = Pelicula(nombrePeli, duracionPeli, genero, ageRating)
    def getHoraInicio(self):
        return self.horaInicio
    def getHoraCierre(self):
        return self.horaCierre
    def getPelicula(self):
        return self.pelicula
