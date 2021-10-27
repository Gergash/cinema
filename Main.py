from Teatro import Teatro
from Sala import Sala
from Silla import Silla
from Cliente import Cliente
from Confiteria import Confiteria
from Horario import Horario
from Pelicula import Pelicula
from enums.AgeRating import AgeRating
from Vendedor import Vendedor
from enums.Genero import Genero
from Ticket import Ticket
from Factura import Factura
from Comida import Comida
from enums.TipoComida import TipoComida
from VentaComida import VentaComida

miTeatro = Teatro()
miSala = Sala()
miSilla = Silla()
miPelicula = Pelicula()
miCliente = Cliente()
miConfiteria = Confiteria()
miVendedor = Vendedor()
miTeatro.idTeatro = '123'
miTeatro.ciudadTeatro = 'Manizales'
miSala.idSala = "1"
miTeatro.addSala(miSala)
miPelicula.nombrePeli = "X-Men"
miPelicula.duracionPeli = 125
miPelicula.ageRating = AgeRating.Adolescentes.name
miPelicula.genero = Genero.Accion.name
miHorario = Horario(miPelicula)
miSilla.idSilla = "A1"
miHorario.addSilla(miSilla)
miTicket = Ticket(miHorario, miSala, miSilla)
miTicket.cliente = miCliente
miTicket.vendedor = miVendedor
miTicket.precio = 28888
miTicket.codigoServicio = "11"
miFactura = Factura(miTicket)
miFactura.precioTotal = miTicket.precio
miFactura.numFact = '111'
miFactura.fechaFact = "22/22/22"
miFactura.NIT = "12321"
miComida = Comida()
miComida.idComida = "22"
miComida.precioComida = 200
miComida.nombreComida = "Crispetas"
miComida.tipoComida = TipoComida.Comida.name
miVentaComida = VentaComida(miComida)
miVentaComida.precio = 200
miVentaComida.vendedor = miVendedor
miVentaComida.cliente = miCliente
miVentaComida.codigoServicio = "2222"
miFactura.addServicio(miVentaComida)

miticket2 = miFactura.servicios[0]
mihorario2 = miticket2.ticketHorario
mipelicula2 =  mihorario2.miPelicula
print(mipelicula2.nombrePeli)

