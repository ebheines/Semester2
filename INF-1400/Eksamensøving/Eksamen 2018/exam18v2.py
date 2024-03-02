class Student:
    def __init__(self, navn):
        self.navn = navn
        self.fag = []
    
    def registrer_fag(self, fag):
        ny_fag = Fag(fag)
        self.fag.append(ny_fag)
        return ny_fag

    def gjennomsnittskarakter(self):
        total = 0
        count = 0
        for kar in self.fag:
            total += sum(kar.karakterer.values())
            count += 1
        
        return (total/count)


class Fag:
    def __init__(self, fag):
        self.fag = fag
        self.karakterer = {}

    def registrer_karakter(self, score, vekting):
        self.karakterer[vekting] = score


class Karakterbok:
    def __init__(self):
        self.student = []
    
    def registrer_student(self, navn):
        ny_student = Student(navn)
        self.student.append(ny_student)
        return ny_student


if __name__ == "__main__":
    bok = Karakterbok()

    kari = bok.registrer_student("Kari")
    matte = kari.registrer_fag("Kalkulus")
    matte.registrer_karakter(75, 0.20)

    historie = kari.registrer_fag("Historie")
    historie.registrer_karakter(60, 0.1)

    print(kari.gjennomsnittskarakter())