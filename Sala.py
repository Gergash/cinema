from Silla import Silla


class Sala:
    def __init__(self, idSala, nombrePeli, salaPremium, row, col):
        # row y col para definir las dimensiones de la sala
        self.idSala = idSala
        self.nombrePeli = nombrePeli
        self.salaPremium = salaPremium
        self.sillasSala = []
        self.row = row
        self.col = col
        # Crea la sala como una lista de listas de objetos Silla
        for rows in range(1, self.row + 1):
            rowLista = []
            for columns in range(1, self.col + 1):
                silla = Silla(rows, columns)
                rowLista.append(silla)
            self.sillasSala.append(rowLista)

    # gets
    def getIdSala(self):
        return self.idSala

    def getNomPelicula(self):
        return self.nombrePeli

    def getSillasSala(self):
        return self.sillasSala

    def getSalaPremium(self):
        return self.salaPremium

    ########################################################
    # Imprime las sillas por su nombre, si la silla esta llena aparece como 'XX'
    def printSillas(self):
        print()
        print("                  Pantalla                      ")
        print("------------------------------------------------")
        print()
        for row in self.sillasSala:
            rowLista = []
            for silla in row:
                sillaNombre = silla.getNombreSilla()
                rowLista.append(sillaNombre)
            print(rowLista)

    # Busca una silla por su ID y corre el método setComprado de el objeto Silla
    def comprarSilla(self, idSilla):
        for row in self.sillasSala:
            for silla in row:
                getId = silla.getIdSilla()
                if getId.lower() == idSilla.lower():
                    silla.setComprado()

    def vaciarSilla(self, idSilla):
        for row in self.sillasSala:
            for silla in row:
                getId = silla.getIdSilla()
                if getId.lower() == idSilla.lower():
                    silla.setVacio()

    # Busca una silla por su Id y nos indica su posición y si esta ocupada o no
    def infoSilla(self, idSilla):
        for row in self.sillasSala:
            for silla in row:
                getId = silla.getIdSilla()
                if getId.lower() == idSilla.lower():
                    if silla.getSillaOcupada():
                        print("La silla ", idSilla, ' se ubica en la fila ', silla.getRow(), ' y columna ',
                              silla.getColumn(), ' Esta OCUPADA')
                    else:
                        print("La silla ", idSilla, ' se ubica en la fila ', silla.getRow(), ' y columna ',
                              silla.getColumn(),
                              '  Esta VACIA')
