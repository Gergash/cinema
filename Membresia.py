from TipoMem import TipoMem

class Membresia:
    def __init__(self, idMem, tipoMem, descuentoMem):
        self.idMem = idMem
        self.tipoMem = TipoMem(tipoMem)
        self.descuentoMem = descuentoMem
    def getIdMem(self):
        return self.idMem
    def getTipoMem(self):
        return self.tipoMem
    def getDescuentoMem(self):
        return self.descuentoMem
