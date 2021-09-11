from Silla import Silla
from Sala import Sala
from Teatro import Teatro


cinePolis = Teatro()
cinePolis.addSala('506D', 'Dora', True, 20, 20)
cinePolis.addSala('507D', 'spiderman', False, 20, 20)
cinePolis.addSala('508D', 'xmen', False, 20, 20)
cinePolis.addSala('509D', 'el gato con botas', False, 20, 20)
cinePolis.addSala('510D', 'it', False, 20, 20)
cinePolis.addSala('511D', 'ironman', False, 10, 5)
sala1 = cinePolis.searchSalaId("511D")
sala2 = cinePolis.searchSalaId("506D")
sala3 = cinePolis.searchSalaId("507D")
carteleras = cinePolis.showPelicula()
print(carteleras)
print(sala1.getIdSala(), sala2.getNomPelicula(), sala3.getSalaPremium())
cinePolis.searchSala("DORA")
cinePolis.searchSala("xmen")
cinePolis.searchSala("iT")

personas = int(input("Cuantas personas van a comprar voleta"))

for i in range(personas):
    SIlla = input("Que silla quieres")
    SAla = input("Que sala vas a ver, : 511D : 506D : 507D :")

    if(SAla == "511D"):
        sala1.printSillas()
        sala1.comprarSilla(SIlla)
        sala1.printSillas()
        sala1.infoSilla(SIlla)
        
    if(SAla == "506D"):
        sala2.printSillas()
        sala2.comprarSilla(SIlla)
        sala2.printSillas()
        sala2.infoSilla(SIlla)

    if(SAla == "507D"):
        sala3.printSillas()
        sala3.comprarSilla(SIlla)
        sala3.printSillas()
        sala3.infoSilla(SIlla)
