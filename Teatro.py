class Teatro:
    salasTeatro = []
    idTeatro: str
    nombreTeatro: str
    ciudadTeatro: str

    def searchSala(self, idSala):
        for sala in self.salasTeatro:
            if sala.idSala == idSala:
                return sala

    def addSala(self, sala):
        self.salasTeatro.append(sala)

