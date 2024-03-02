
FAKTOR_BIL = 10
FAKTOR_BUSS = 100
FAKTOR_LASTEBIL = 300
FAKTOR_TOG = 0


class Transportmiddel:

    def __init__(self, lastekapasitet, personkapasitet, vekt) -> None:
        self.lastekapasitet = lastekapasitet
        self.personkapasitet = personkapasitet
        self.vekt = vekt

    def __str__(self) -> str:
        return f"Lastekapasitet: {self.lastekapasitet}\nPersonkapasitet: {self.personkapasitet}\nVekt: {self.vekt}\n"


class Tog(Transportmiddel):
    def __init__(self, lastekapasitet, personkapasitet, vekt) -> None:
        super().__init__(lastekapasitet, personkapasitet, vekt)
        self.slit = FAKTOR_TOG

class Personbil(Transportmiddel):
    def __init__(self, lastekapasitet, personkapasitet, vekt) -> None:
        super().__init__(lastekapasitet, personkapasitet, vekt)
        self.piggdekk = False
        self.slit = FAKTOR_BIL

class Buss(Transportmiddel):
    def __init__(self, lastekapasitet, personkapasitet, vekt) -> None:
        super().__init__(lastekapasitet, personkapasitet, vekt)
        self.pikkdekk = False
        self.kjetting = False
        self.slit = FAKTOR_BUSS

class Lastebil(Transportmiddel):
    def __init__(self, lastekapasitet, personkapasitet, vekt) -> None:
        super().__init__(lastekapasitet, personkapasitet, vekt)
        self.piggdekk = False
        self.kjetting = False
        self.slit = FAKTOR_LASTEBIL


def slitasje(transportmiddel):
    slitasje = 0
    for v in transportmiddel:
        if type(v) is Lastebil:
            slitasje += FAKTOR_LASTEBIL
        elif type(v) is Personbil:
            slitasje += FAKTOR_BIL
        elif type(v) is Buss:
            slitasje += FAKTOR_BUSS
        elif type(v) is Tog:
            slitasje += FAKTOR_TOG
    
    return slitasje

def slitasje2(transportmiddel):
    slitasje = 0
    for v in transportmiddel:
        slitasje += v.slit
        
    return f"Slitasje på vei: {slitasje}"


lst = []

if __name__ == "__main__":
    bill = Lastebil(10000, 2, 12000)
    merc = Personbil(600, 5, 2000)

    lst.append(merc)
    lst.append(bill)
    s = slitasje2(lst)
    
    print(bill)
    print(merc)
    print(s)

# Bill is an object, a Lastebil to be specific. Bill has
# a ceiling of weight he can carry, he has space for 2 
# passangers, and has a weight of 12 tons when not carrying
# any load. 

