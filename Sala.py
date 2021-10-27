
class Sala:
    idSala: str
    row: int
    col: int
    horariosSala: []

    def addHorario(self, horario):
        self.horariosSala.append(horario)

    def seachHorario(self, horaInicio):
        for horario in self.horariosSala:
            if horario.horaInicio == horaInicio:
                return horario