class Posisjon:
    def __init__(self, lengdegrad, breddegrad, moh, tidspunkt) -> None:
        self.lengdegrad = lengdegrad
        self.breddegrad = breddegrad
        self.moh = moh
        self.tidspunkt = tidspunkt
    
    def __str__(self):
        return "Lengdegrad: " + self.lengdegrad + "Breddegrad: " + self.breddegrad + "Moh: " + self.moh + "Tidspunkt: " + self.tidspunkt
    

class Spor:
    def __init__(self, starttid, stopptid) -> None:
        self.posisjon = []
        self.starttid = self.posisjon[0]["Tidspunkt"]
        self.stopptid = self.posisjon[-1]["Tidspunkt"]

    def legg_til_posisjon(self, posisjon):
        self.posisjon.append({"Lengdegrad": posisjon.lengdegrad, "Breddegrad": posisjon.breddegrad,
                              "Moh": posisjon.moh, "Tidspunkt": posisjon.tidspunkt})
    
    def finnPosisjon(self, tidspunkt):
        for posisjon in self.posisjon:
            if posisjon["Tidspunkt"] == tidspunkt:
                return posisjon
        

class Tur:
    def __init__(self, spor, navn, beskrivelse) -> None:
        self.spor = spor
        self.navn = navn
        self.beskrivelse = beskrivelse

class SightseeTur(Tur):
    def __init__(self, spor, navn, beskrivelse) -> None:
        super().__init__(spor, navn, beskrivelse)
        self.poi = []
    
    def registrerPOI(self, tidspunkt):
        for posisjon in self.spor.posisjon:
            if posisjon["Tidspunkt"] == tidspunkt:
                self.poi.append(posisjon)


if __name__ == "__main__":
    posisjon = Posisjon(5425234, 52432432, 32423, 543943)
    spor = Spor(31243, 131232)
    spor.legg_til_posisjon(posisjon)

    sei = SightseeTur(spor, "Hei", "noen")
    print(sei.registrerPOI(543943))


    print(spor.posisjon)