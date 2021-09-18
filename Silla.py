from Alfabeto import Alfabeto


class Silla:
    def __init__(self, row, col):
        # Como las sillas se crean cuando creamos la sala, su fila y columna le dan su nombre
        self.row = row
        self.column = col
        # El identificador de las sillas es igual a su posición: fila(en letra) + su columna
        self.idSilla = Alfabeto(row).name + str(self.column)
        self.sillaOcupada = False
        # nombreSilla se usa para cambiar el nombre de silla en printSillas() cuando la silla esta ocupada sin tener
        # que cambiar el identificador idSilla
        self.nombreSilla = self.idSilla

    # gets
    def getIdSilla(self):
        return self.idSilla

    def getSillaOcupada(self):
        return self.sillaOcupada

    def getNombreSilla(self):
        return self.nombreSilla

    def getRow(self):
        return self.row

    def getColumn(self):
        return self.column

    ###################################################################################################################
    # setComprado- setVacio() para el uso en comprarSilla() y vaciarSilla() en Sala
    # nombreSilla cambia para que se pueda ver visualmente las sillas compradas en printSillas()
    def setComprado(self):
        self.sillaOcupada = True
        self.nombreSilla = "XX"

    def setVacio(self):
        self.sillaOcupada = False
        self.nombreSilla = self.idSilla
