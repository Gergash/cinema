from Sala import Sala
from Silla import Silla


class Teatro:
    def __init__(self):
        self.salasTeatro = []

    # Solo busca por nombre de pelicula, retorna un print con la información de la sala
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

    # Muestra todas las películas del teatro
    def showPelicula(self):
        listaPelicula = []
        for sala in self.salasTeatro:
            pelicula = sala.getNomPelicula()
            listaPelicula.append(pelicula)
        # Usamos set() para remover películas duplicadas
        return set(listaPelicula)

    # Añade salas al teatro
    def addSala(self, idSala, nomPeli, salaPremium, row, col):
        sala1 = Sala(idSala, nomPeli, salaPremium, row, col)
        self.salasTeatro.append(sala1)

    # Menu
    def menu(self):
        i = 0
        while i < 1:
            # ASCII de Teatro
            print()
            print()
            print('''\
                ████████╗███████╗ █████╗ ████████╗██████╗  ██████╗ 
                ╚══██╔══╝██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔═══██╗
                   ██║   █████╗  ███████║   ██║   ██████╔╝██║   ██║
                   ██║   ██╔══╝  ██╔══██║   ██║   ██╔══██╗██║   ██║
                   ██║   ███████╗██║  ██║   ██║   ██║  ██║╚██████╔╝
                   ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ 

            ''')
            ###########################################################################################################
            # Opciones de metodos de teatro
            print("Input 1 para showPelicula()")
            print("Input 2 para searchSala(nomPelicula)")
            print("Input 3 para entrar a la sala searchSalaId(salaId) (comprar, ver sillas disponibles etc)")
            print("Input 4 para salir de este menu.")
            print()
            x = input()
            # showPelicula()
            if x == "1":
                print(self.showPelicula())
            # searchSala(idSala)
            elif x == "2":
                # pedimos un input para idSala
                nomPelicula = input("Digite el nombre de pelicula: ")
                self.searchSala(nomPelicula)
            # searchSalaId
            elif x == "3":
                # input para idSala
                idSala = input("Digite el Id de la Sala: ")
                # searchSalaId retorna un objeto sala, lo guardamos en una variable sala
                sala = self.searchSalaId(idSala)
                y = 0
                # Si la sala está vacía no entramos al menu de sala, volvemos al menu de teatro
                if sala is not None:
                    # Menu de sala:
                    ##############
                    while y < 1:
                        print()
                        print("Sala ", sala.getIdSala())
                        print("Input 1 para printSillas()")
                        print("Input 2 para comprarSilla(idSilla)")
                        print("Input 3 para vaciarSilla(idSilla)")
                        print("Input 4 para infoSilla(idSilla)")
                        print("Input 5 para salir.")
                        print()
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
