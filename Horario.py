from Pelicula import Pelicula


class Horario:
    sillasHorario = []
    horaInicio: str
    horaCierre: str

    def __init__(self, miPelicula):
        self.miPelicula = miPelicula


    def addSilla(self, silla):
        self.sillasHorario.append(silla)

    def searchSilla(self, idSilla):
        for silla in self.sillasHorario:
            if silla.idSilla == idSilla:
                return silla