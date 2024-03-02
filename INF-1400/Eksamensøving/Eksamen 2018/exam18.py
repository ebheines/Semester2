class Student:
    def __init__(self, navn):
        self.navn = navn
        self.fag = []
        self.karakter = []
    
    def registrer_fag(self, navn):
        self.fag.append(navn)
    
    def gjennomsnittskarakter(self):
        count = 0
        karaktersnitt = 0

        for kar in self.karakter:
            karaktersnitt += kar
            count += 1
        
        return (karaktersnitt/count)

class Fag:
    def __init__(self, vekting):
        self.karakterliste = []
        self.vektfaktor = vekting
        self.studentliste = []

    def registrer_karakter(self, score, vekting):
        self.karakterliste.append(score)


class Karakterbok:
    def __init__(self):
        self.studenter = []
        self.karaktersnitt = 0
    
    def registrer_student(self, navn):
        self.studenter.append(navn)


bok = Karakterbok()

kari = bok.registrer_student('Kari')
matte = kari.registrer_fag('Kalkulus')
matte.registrer_karakter(75, 0.20)

print(kari.gjennomsnittskarakter)
    
