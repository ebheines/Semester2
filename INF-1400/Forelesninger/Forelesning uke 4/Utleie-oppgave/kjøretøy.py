class Kjøretøy:
    def __init__(self,regnummeret,årstallet):
        self.regnummer = regnummeret
        self.årstall = årstallet

    def getRegnummer(self):
        return self.regnummer

    def setRegnummer(self,regnummeret):
        self.regnummer = regnummeret

    def getÅrstall(self):
        return self.årstall

    def setÅrstall(self, årstallet):
        self.årstall = årstallet

    def __str__(self):
        return "Regnummeret er: " + self.regnummer + "\n" + "Årstallet er: " + str(self.årstall)       

class Motorsykkel(Kjøretøy):
    def __init__(self, regnummeret, årstallet):
        super().__init__(regnummeret, årstallet)


class Varebil(Kjøretøy):
    def __init__(self, regnummeret, årstallet, liter):
        super().__init__(regnummeret, årstallet)
        self.ant_liter = liter
    
    def getAntLiter(self):
        return self.ant_liter

    def setAntLiter(self, liter):
        self.ant_liter = liter

    def __str__(self):
        return super().__str__ + "\n" + "Antall liter: " + str(self.ant_liter)


class Personbil(Kjøretøy):
    def __init__(self, regnummeret, årstallet, seter):
        super().__init__(regnummeret, årstallet)
        self.ant_seter = seter
    
    def getAntSeter(self):
        return self.ant_seter

    def setAntSeter(self, seter):
        self.ant_seter = seter

    def __str__(self):
        return super().__str__ + "\n" + "Antall seter: " + str(self.ant_seter)
    

class Garasje:
    def __init__(self, garasjeiden):
        self.garasjeid = garasjeiden
        self.KTliste = []

    def getGarasjeID(self):
        return self.garasjeid

    def setGarasjeID(self, garasjeiden):
        self.garasjeid = garasjeiden
    
    def parkerKjøretøy(self, kjøretøyet):
        self.KTliste.append(kjøretøyet)

    def finnAntall(self):
        return len(self.KTliste)
    
    def finnIGarasje(self, regnummeret):
        for kjøretøy in self.KTliste:
            if kjøretøy.getRegnummer() == regnummeret:
                return True
        return False


class Bygning:
    def __init(self, navnet):
        self.navn = navnet
        self.garasjeliste = []

if __name__ == "__main__":
    p1 = Personbil("ZH41577", 2019, 5)
    p2 = Personbil("ZH45691", 2014, 5)

    v1 = Varebil("ZH42688", 2020, 3000)
    v2 = Varebil("ZH48852", 2021, 3000)

    m1 = Motorsykkel("ZH452", 1999)
    m2 = Motorsykkel("ZH341", 1995)

    g1 = Garasje(123)
    g1.parkerKjøretøy(p1)
    g1.parkerKjøretøy(p2)
    g1.parkerKjøretøy(v1)
    g1.parkerKjøretøy(v2)
    g1.parkerKjøretøy(m1)
    g1.parkerKjøretøy(m2)

    print("Antall kjøretøy i garasje er: " + str(g1.finnAntall()))
    print("Fant bil i garasje? " + str(g1.finnIGarasje("ZH452")))