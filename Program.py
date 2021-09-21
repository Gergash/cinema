from Teatro import Teatro
from Genero import Genero
from AgeRating import AgeRating
from TipoMem import TipoMem


cinePolis = Teatro('001','Cinepolis','Manizales', 200)
cinePolis.addSala('501D', 'Spiderman', 180, Genero.Accion, AgeRating.Adolescentes, True, 5, 5)
cinePolis.addSala('500D', 'Xmen', 120, Genero.Accion, AgeRating.Adolescentes, False, 5, 5)
cinePolis.searchSala('spiderman')
cinePolis.addUsuario("123", "Geronimo", TipoMem.GOLD)
cinePolis.addVendedor("005", 'Alberto')
cinePolis.iniciarCompra("123", "005")
cinePolis.comprarSilla('500D', 'A1')
cinePolis.comprarSilla('500D', 'A2')

cinePolis.terminarCompra()
sala1 = cinePolis.searchSalaId("500D")
sala1.printSillas()