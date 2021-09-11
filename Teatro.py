from Sala import Sala
from Silla import Silla


class Teatro:
    def __init__(self):
        self.salasTeatro = []
#Solo busca por nombre de pelicula
    def searchSala(self, nomPelicula):
        for sala in self.salasTeatro:
            peliculaL = sala.getNomPelicula()
            if peliculaL.lower() == nomPelicula.lower():
                if sala.getSalaPremium() == True:
                    print("El id de la sala es: ", sala.getIdSala(), "|  El nombre de la pelicula es: ",
                          sala.getNomPelicula(), "|  La sala es premium")
                else:
                    print("El id de la sala es: ", sala.getIdSala(), "|  El nombre de la pelicula es: ",
                          sala.getNomPelicula(), "|  La sala no es premium")

    def searchSalaId(self, idSala):
        for sala in self.salasTeatro:
            id = sala.getIdSala()
            if id == idSala:
                return sala
#Muestra todas las peliculas del teatro
    def showPelicula(self):
        listaPelicula = []
        for sala in self.salasTeatro:
            pelicula = sala.getNomPelicula()
            listaPelicula.append(pelicula)
        #Usamos set() para remover peliculas duplicadas
        return set(listaPelicula)
#Añanade salas al teatro
    def addSala(self, idSala, nomPeli, salaPremium, row, col):
        sala1 = Sala(idSala, nomPeli, salaPremium, row, col)
        self.salasTeatro.append(sala1)