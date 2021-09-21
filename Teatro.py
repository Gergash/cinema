from Sala import Sala
from Usuario import Usuario
from Vendedor import Vendedor
from TipoMem import TipoMem
from Recibo import Recibo


class Teatro:
    def __init__(self, idTeatro, nombreTeatro, ciudadTeatro, precioTeatro):
        self.idTeatro = idTeatro
        self.nombreTeatro = nombreTeatro
        self.ciudadTeatro = ciudadTeatro
        self.precioTeatro = precioTeatro
        self.salasTeatro = []
        self.usuariosTeatro = []
        self.vendedoresTeatro = []
        self.recibosTeatro = []

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
    def getIdTeatro(self):
        return self.idTeatro

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

    # Busca por Id de sala y devuelve el objeto
    def searchSalaId(self, idSala):
        for sala in self.salasTeatro:
            id = sala.getIdSala()
            if id == idSala:
                return sala

    def searchUsuarioId(self, idUsuario):
        for usuario in self.usuariosTeatro:
            id = usuario.getIdUsuario()
            if id == idUsuario:
                return usuario

    def searchVendedorId(self, idVendedor):
        for vendedor in self.vendedoresTeatro:
            id = vendedor.getIdVendedor()
            if id == idVendedor:
                return vendedor

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
    def addVendedor(self, idVendedor, nomVendedor):
        vendedor = Vendedor(idVendedor, nomVendedor)
        self.vendedoresTeatro.append(vendedor)

    # Añade Usuarios al teatro
    def addUsuario(self, idUsuario, nomUsuario, tipoMem):
        usuario = Usuario(idUsuario, nomUsuario, tipoMem)
        self.usuariosTeatro.append(usuario)


    #ventas
    def iniciarCompra(self, idUsuario, idVendedor):
        usuario = self.searchUsuarioId(idUsuario)
        vendedor = self.searchVendedorId(idVendedor)
        global recibo
        recibo = Recibo(usuario, vendedor, self)
        global contVenta
        contVenta = 1

    def comprarSilla(self, idSala, idSilla):
        sala = self.searchSalaId(idSala)
        silla = sala.getSilla(idSilla)
        global recibo
        if contVenta == 1:
            sala = self.searchSalaId(idSala)
            sala.comprarSillaSala(idSilla)
            recibo.compraSilla(sala, silla)
        else :
            print('Porfavor inicie la compra con iniciarCompra()')

    def terminarCompra(self):
        global contVenta
        global recibo
        contVenta = 0
        recibo.terminarRecibo()
        self.recibosTeatro.append(recibo)
        recibo = 0



