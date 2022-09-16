# Definició de classes
# Lluc i Gerard
class UnitatFormativa:
    nom = None
    qualificacions = None

    def __init__(self, nom):
        self.nom = nom


# Inici del programa
uf1 = UnitatFormativa("UF1. Desenvolupament del programari")
uf2 = UnitatFormativa("UF2. Optimització del programari")
uf3 = UnitatFormativa("UF3. Introducció al Disseny Orientat a Objectes")

uf1.qualificacions = 8
uf2.qualificacions = 10
uf3.qualificacions = 4

print(uf1.nom, ":", uf1.qualificacions)
print(uf2.nom, ":", uf1.qualificacions)
print(uf3.nom, ":", uf1.qualificacions)
