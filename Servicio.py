class Servicio:
    precio : int
    codigoServicio : str

    def __init__(self, servicioVendedor, servicioCliente):
        self.vendedor = servicioVendedor
        self.cliente =  servicioCliente