# VI SKAL LAGE VÆRSTASJON
class Stasjon:

    def __init__(self, regn, temp, navn):
        self.regn = regn
        self.temp = temp
        self.navn = navn

    def hent_navn(self):
        return self.navn    

    def hent_regn(self):
        return self.regn
    
    def hent_temp(self):
        return self.temp
    
    def __str__(self):
        return "Navn: " + str(self.navn) + "\n" + "Stasjon med regn: " + str(self.regn) + "\n" + "Temperatur: " + str(self.temp)

if __name__ == "__main__":
    eidkjosen = Stasjon(13, 20, "Eidkjosen")
    print(eidkjosen)
