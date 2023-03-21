class Persoon:

    def __init__(self,naam,leeftijd,geslacht):
        self.naam = naam
        self.leeftijd = leeftijd
        self.geslacht = geslacht

    def __str__(self):
        return f"Naam: {self.naam} Leeftijd: {self.leeftijd} Geslacht: {self.geslacht}"

