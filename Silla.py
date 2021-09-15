#Dict de alfabeto para traducir los rows a letras
alfabeto= {
    1 : 'A', 2 : 'B', 3: 'C', 4 : 'D', 5 : 'E', 6 : 'F', 7 : 'G', 8 : 'H', 9 : 'I', 10 : 'J', 11: 'K', 12 : 'L', 13 : 'M', 14 : 'N' , 15 : 'O', 16 : 'P', 17 : 'Q' , 18 : 'R', 19 : 'S', 20 : 'T', 21 : 'U', 22 : 'V' ,
    23 : 'W', 24 : 'X', 25 : 'Y', 26 : 'Z'
}
class Silla:
    def __init__(self,row, col):
        #Como las sillas se crean cuando creamos la sala, su fila y columna le dan su nombre
        self.row = row
        self.column = str(col)
        self.idSilla = alfabeto[row] + self.column
        self.sillaOcupada = False
        #nombreSilla se usa para cambiar el nombre de silla en printSillas() cuando la silla esta ocupada sin tener que cambiar el identificador idSilla
        self.nombreSilla = self.idSilla
#gets
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
################################################################
#setComprado-Vacio para el uso en comprarSilla() en Sala
#nombreSilla cambia para que se pueda ver visualmente las sillas compradas en printSillas()
    def setComprado(self):
        self.sillaOcupada = True
        self.nombreSilla = "XX"
    def setVacio(self):
        self.sillaOcupada = False
        self.nombreSilla = self.idSilla

