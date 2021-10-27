from Servicio import Servicio


class VentaComida(Servicio):
    comida = []
    precio = int

    def __init__(self, comidaVenta):
        self.comida.append(comidaVenta)

    def addComida(self, comidaVenta):
        self.comida.append(comidaVenta)
