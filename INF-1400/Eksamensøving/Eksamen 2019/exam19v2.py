import math

FAKTOR_BIL = 10
FAKTOR_BUSS = 100
FAKTOR_LASTEBIL = 300
FAKTOR_TOG = 0

class Transportmiddel:
    def __init__(self, lastekapasitet, personkapasitet, vekt) -> None:
        self.lastekapasitet = lastekapasitet
        self.personkapasitet = personkapasitet
        self.vekt = vekt
        self.slitasjefaktor = 0


class Personbil(Transportmiddel):
    def __init__(self, lastekapasitet, personkapasitet, vekt) -> None:
        super().__init__(lastekapasitet, personkapasitet, vekt)
        self.piggdekk = False
        self.slitasjefaktor = FAKTOR_BIL
    
    def slitasje(self):
        slitasje_verdi = self.vekt * self.slitasjefaktor
        if self.piggdekk:
            slitasje_verdi *= 3


class Tungtransport(Transportmiddel):
    def __init__(self, lastekapasitet, personkapasitet, vekt) -> None:
        super().__init__(lastekapasitet, personkapasitet, vekt)
        self.piggdekk = False
        self.kjetting = False

    def slitasje(self):
        slitasje_verdi = self.vekt * math.log(self.vekt) * self.slitasjefaktor
        if self.piggdekk:
            slitasje_verdi *= 3
        if self.kjetting:
            slitasje_verdi *= 10

class Buss(Tungtransport):
    pass

class Lastebil(Tungtransport):
    pass

class Tog(Transportmiddel):
    pass



def slitasje(transportmiddel):
    totalslitasje = 0
    for bil in transportmiddel:
        if type(bil) is Personbil:
            totalslitasje += FAKTOR_BIL
        elif type(bil) is Buss:
            totalslitasje += FAKTOR_BUSS
        elif type(bil) is Lastebil:
            totalslitasje += FAKTOR_LASTEBIL
    return "Total slitasje faktor er:" + totalslitasje

def slitasje(transportmiddel):
    totslitasje = 0
    for bil in transportmiddel:
        totslitasje += bil.slitasjefaktor
    return "Total slitasje faktor er: " + totslitasje





