from Teatro import Teatro
from Sala import Sala
from Genero import Genero
from AgeRating import AgeRating
from TipoMem import TipoMem


cinePolis = Teatro('001', 'CinePolis', 'Manizales', 6000)
cinePolis.addSala('50D', True, 5, 5)
sala1 = cinePolis.getSala('50D')
sala1.addHorario('3PM', '5PM', 'Spiderman', 120, Genero.Accion, AgeRating.Adolescentes)
sala1.addHorario('6PM', '8PM', 'Xmen', 120, Genero.Accion,AgeRating.Adolescentes)
cinePolis.searchSala('Spiderman')
cinePolis.infoSala('50D')
