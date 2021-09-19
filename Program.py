from Teatro import Teatro
from Sala import Sala
from Genero import Genero
from AgeRating import AgeRating
#from Menu import Menu

cinePolis = Teatro('001','Cinepolis','Manizales', 200)
cinePolis.addSala('501D', 'Spiderman', 180, Genero.Accion, AgeRating.Adolescentes, True, 5, 5)
sala1 = cinePolis.addSala('500D', 'Xmen', 120, Genero.Accion, AgeRating.Adolescentes, False, 5, 5)
cinePolis.searchSala('xmen')
cinePolis.showPeliculas()
