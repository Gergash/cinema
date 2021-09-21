
class Vendedor:
    def __init__(self, idVendedor, nomVendedor):
        self.idVendedor = idVendedor
        self.nomVendedor = nomVendedor
        self.recibosVendedor = []

    def getIdVendedor(self):
        return self.idVendedor
    def getNomVendedor(self):
        return self.nomVendedor

