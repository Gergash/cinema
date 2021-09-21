from TipoMem import TipoMem

class Usuario:
    def __init__(self, idUsuario, nomUsuario, tipoMem):
        self.idUsuario = idUsuario
        self.nomUsuario = nomUsuario
        self.tipoMem = tipoMem
    def getIdUsuario(self):
        return self.idUsuario
    def getNomUsuario(self):
        return self.nomUsuario
    def getTipoMem(self):
        return self.tipoMem


