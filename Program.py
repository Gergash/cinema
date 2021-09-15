from Silla import Silla
from Sala import Sala
from Teatro import Teatro
cinePolis = Teatro()
cinePolis.addSala('506D', 'Dora', True, 5, 5)
cinePolis.addSala('507D', 'spiderman', False, 20, 20)
cinePolis.addSala('508D', 'xmen', False, 2, 2)
cinePolis.addSala('509D', 'el gato con botas', False, 20, 20)
cinePolis.addSala('510D', 'it', False, 20, 20)
cinePolis.addSala('511D', 'ironman', False, 10, 5)
sala1 = cinePolis.searchSalaId("511D")
sala2 = cinePolis.searchSalaId("506D")
sala3 = cinePolis.searchSalaId("508D")
carteleras = cinePolis.showPelicula()
print(carteleras)
print(sala1.getIdSala(), sala2.getNomPelicula(), sala3.getSalaPremium())
cinePolis.searchSala("DORA")
cinePolis.searchSala("xmen")
cinePolis.searchSala("iT")
sala1.printSillas()
sala1.comprarSilla('A1')
sala1.printSillas()
sala1.infoSilla('A1')
cinePolis.menu()


