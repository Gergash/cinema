
class Usuario:
    def __init__(self, idUsuario, nomUsuario, fechaNacimiento):
        self.idUsuario = idUsuario
        self.nomUsuario = nomUsuario
        self.fechaNachimiento = fechaNacimiento

    def getIdUsuario(self):
        return self.idUsuario
    def getNomUsuario(self):
        return self.nomUsuario
    def getFechaNacimiento(self):
        return self.fechaNachimiento
