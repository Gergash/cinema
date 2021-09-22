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

    # Busca por Id de sala y devuelve el objeto
    def getSala(self, idSala):
        for sala in self.salasTeatro:
            id = sala.getIdSala()
            if id == idSala:
                return sala

    def searchSala(self, nomPelicula):
        for sala in self.salasTeatro:
            for horario in sala.getHorarios():
                pelicula = horario.getPelicula()
                nombrePelicula = pelicula.getNombrePeli()
                if nomPelicula.lower() == nombrePelicula.lower():
                    print("Sala ", sala.getIdSala(), ' Aforo ', sala.getTaquilla())
                    print(horario.getHoraInicio(), " ", horario.getHoraCierre(), " Pelicula: ", nombrePelicula )

    def infoSala(self, idSala):
        for sala in self.salasTeatro:
            id = sala.getIdSala()
            if id == idSala:
                print('Sala ', idSala, ' Aforo: ', sala.getTaquilla())
                for horario in sala.getHorarios():
                    pelicula = horario.getPelicula()
                    print(horario.getHoraInicio(), " ", horario.getHoraCierre(), " Pelicula: ", pelicula.getNombrePeli())


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

    # Añade salas al teatro
    def addSala(self, idSala, salaPremium, row, col):
        sala1 = Sala(idSala, salaPremium, row, col)
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


    def comprarSilla(self, idSala, idSilla):
        sala = self.searchSalaId(idSala)
        silla = sala.getSilla(idSilla)
        global recibo
        sala = self.searchSalaId(idSala)
        sala.comprarSillaSala(idSilla)
        recibo.compraSilla(sala, silla)


    def terminarCompra(self):
        global contVenta
        global recibo
        recibo.terminarRecibo()
        self.recibosTeatro.append(recibo)
        recibo = 0



