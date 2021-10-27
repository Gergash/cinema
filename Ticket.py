from Servicio import Servicio


class Ticket(Servicio):
    def __init__(self, ticketHorario, ticketSala, ticketSilla):
        self.ticketHorario = ticketHorario
        self.ticketSala = ticketSala
        self.ticketSilla = ticketSilla
        ticketSilla.setOcupado()



