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
#Añade salas al teatro
    def addSala(self, idSala, nomPeli, salaPremium, row, col):
        sala1 = Sala(idSala, nomPeli, salaPremium, row, col)
        self.salasTeatro.append(sala1)
#Menu
    def menu(self):
        i = 0
        while i< 1:
            print("Input 1 para showPelicula()")
            print("Input 2 para searchSala(nomPelicula)")
            print("Input 3 para searchSalaId(idSala) y entrar a la sala (comprar, ver sillas disponibles etc)")
            print("Input 4 para salir de este menu.")
            x = input()
            if x == "1":
                print(self.showPelicula())
            elif x == "2":
                nomPelicula = input("Digite el nombre de pelicula: ")
                self.searchSala(nomPelicula)
            elif x == "3":
                idSala = input("Digite el Id de la Sala: ")
                sala = self.searchSalaId(idSala)
                y = 0
                while y < 1:
                    print("Input 1 para printSillas()")
                    print("Input 2 para comprarSilla(idSilla)")
                    print("Input 3 para vaciarSilla(idSilla)")
                    print("Input 4 para infoSilla(idSilla)")
                    print("Input 5 para salir.")
                    choose = input()
                    if choose == "1":
                        sala.printSillas()
                    if choose == "2":
                        idSilla = input("Digite el Id de la silla: ")
                        sala.comprarSilla(idSilla)
                    if choose == "3":
                        idSilla = input("Digite el Id de la silla: ")
                        sala.vaciarSilla(idSilla)
                    if choose == "4":
                        idSilla = input("Digite el Id de la silla: ")
                        sala.infoSilla(idSilla)
                    if choose == "5":
                        y = 1
            elif x == "4":
                i = 1




