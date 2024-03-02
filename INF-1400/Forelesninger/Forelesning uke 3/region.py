from værstasjon import Stasjon

class Region:

    def __init__(self, navn):
        self.navn = navn
        self.stasjoner = []

    def legg_til_stasjoner(self, stasjon):
        self.stasjoner.append(stasjon)

    def __str__(self):
        s = self.navn + "\n"
        s += "Stasjoner:\n"
        for stasjon in self.stasjoner:
            s += str(stasjon) + "\n"
            return s
    
if __name__ == "__main__":
    nord = Region("Nord")
    sør = Region("Sør")

    nord.legg_til_stasjoner(Stasjon(10, 12, "Tromsdalen"))
    sør.legg_til_stasjoner(Stasjon(6, 15, "Sørøya"))

    print(nord)
    print(sør)