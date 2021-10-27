#from MedioPago import MedioPago
from Servicio import Servicio

class Factura:
    numFact: str
    servicios = []
    NIT: str
    nomTeatro: str
    precioTotal: float
    #medioPago = MedioPago
    fechaFact = str

    def __init__(self, servicioFact: Servicio):
        self.servicios.append(servicioFact)


    def addServicio(self, servicio : Servicio):
        self.servicios.append(servicio)
        self.precioTotal += servicio.precio