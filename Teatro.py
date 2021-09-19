from Sala import Sala


class Teatro:
    def __init__(self, idTeatro, nombreTeatro, ciudadTeatro, precioTeatro):
        self.idTeatro = idTeatro
        self.nombreTeatro = nombreTeatro
        self.ciudadTeatro = ciudadTeatro
        self.precioTeatro = precioTeatro
        self.salasTeatro = []
        self.usuariosTeatro = []
        self.vendedoresTeatro = []

    # gets
    def getNombreTeatro(self):
        return self.nombreTeatro

    def getSalasTeatro(self):
        return self.salasTeatro

    def getCiudadTeatro(self):
        return self.ciudadTeatro

    def getPrecioTeatro(self):
        return self.precioTeatro

    def getVendedoresTeatro(self):
        return self.vendedoresTeatro

    def getUsuariosTeatro(self):
        return self.usuariosTeatro

    # Solo busca por nombre de pelicula, retorna un print con la información de la sala y el objeto sala
    def searchSala(self, nomPelicula):
        for sala in self.salasTeatro:
            pelicula = sala.getPelicula()
            nombre = pelicula.getNombrePeli()
            if nombre.lower() == nomPelicula.lower():
                if sala.getSalaPremium() == True:
                    print("El id de la sala es: ", sala.getIdSala(), "|  El nombre de la película es: ",
                          nombre, "|  La sala es premium")
                else:
                    print("El id de la sala es: ", sala.getIdSala(), "|  El nombre de la película es: ",
                          nombre, "|  La sala no es premium")

    # Busca por Id de sala y devuelve el objeto sala
    def searchSalaId(self, idSala):
        for sala in self.salasTeatro:
            id = sala.getIdSala()
            if id == idSala:
                return sala

    # Muestra todas las películas del teatro
    def showPeliculas(self):
        listaPelicula = []
        for sala in self.salasTeatro:
            pelicula = sala.getPelicula()
            nomPelicula = pelicula.nombrePeli
            listaPelicula.append(nomPelicula)
        # Usamos set() para remover películas duplicadas
        listaPelicula = set(listaPelicula)
        for pelicula in listaPelicula:
            print(pelicula)

    # Añade salas al teatro
    def addSala(self, idSala, nomPeli, duracionPeli, genero, ageRating, salaPremium, row, col):
        sala1 = Sala(idSala, nomPeli, duracionPeli, genero, ageRating, salaPremium, row, col)
        self.salasTeatro.append(sala1)

    # Añade Vendedores al teatro
    def addVendedor(self):
    # Añade Usuarios al teatro
    def addUsuario(self):

    # searchUsuarioId, searchVendedorId


    def comprarSilla(self, idSala, idSila, idUsuario, idVendedor):
        sala = self.searchSalaId(idSala)
