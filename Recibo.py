import uuid
from TipoMem import TipoMem

class Recibo:
    def __init__(self, usuario, vendedor, teatro):
        self.usuario = usuario
        self.vendedor = vendedor
        self.teatro = teatro
        self.idRecibo = str(uuid.uuid1())
        self.infoRecibo = []
        self.precioTotal = 0
        self.precioTeatro = teatro.getPrecioTeatro()
        #Información del recibo
        stringRecibo = "Recibo " + self.idRecibo
        self.infoRecibo.append(stringRecibo)
        stringTeatro = "Teatro " + teatro.getNombreTeatro() + " " + teatro.getIdTeatro()
        stringTeatro2 = teatro.getCiudadTeatro()
        self.infoRecibo.append(stringTeatro)
        self.infoRecibo.append(stringTeatro2)
        stringVendedor = "Vendedor " + vendedor.getNomVendedor() + " " + vendedor.getIdVendedor()
        self.infoRecibo.append(stringVendedor)
        stringUsuario = "Usuario " + usuario.getNomUsuario() + " " + usuario.getIdUsuario()

    def compraSilla(self, sala, silla):
        precioCompraSilla = self.precioTeatro
        if sala.getSalaPremium() is True:
            precioCompraSilla = precioCompraSilla * 1.2
        tipoMembresia = self.usuario.getTipoMem()
        if tipoMembresia == TipoMem.GOLD:
            precioCompraSilla = precioCompraSilla * 0.85
        if tipoMembresia == TipoMem.PLATNIUM:
            precioCompraSilla = precioCompraSilla * 0.75
        if tipoMembresia == TipoMem.VIP:
            precioCompraSilla = precioCompraSilla * 0.5
        self.precioTotal = self.precioTotal + precioCompraSilla
        pelicula = sala.getPelicula()
        stringSilla = "Sala " + sala.getIdSala() + " " + pelicula.getNombrePeli() + " Silla " + silla.getIdSilla() + " " + str(precioCompraSilla) + " COP"
        self.infoRecibo.append(stringSilla)
    def terminarRecibo(self):
        precioTotalString = "Precio Total: " + str(self.precioTotal) + " COP"
        self.infoRecibo.append(precioTotalString)
        for x in self.infoRecibo:
            print(x)
