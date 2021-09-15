from Silla import Silla
from Sala import Sala
from Teatro import Teatro
cinePolis = Teatro()
cinePolis.addSala('506D', 'Dora', True, 5, 5)
cinePolis.addSala('507D', 'Spiderman', False, 6, 6)
cinePolis.addSala('508D', 'Xmen', False, 5, 6)
cinePolis.addSala('509D', 'El Gato con Botas', False, 3, 5)
cinePolis.addSala('510D', 'It', False, 7, 2)
cinePolis.addSala('511D', 'Ironman', False, 10, 5)
sala1 = cinePolis.searchSalaId("511D")
sala2 = cinePolis.searchSalaId("506D")
sala3 = cinePolis.searchSalaId("508D")
