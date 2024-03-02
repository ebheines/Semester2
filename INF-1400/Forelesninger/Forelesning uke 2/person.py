
# Oppretter en klasse Person med egenskapene navn og alder
class Person:

# Kan bruke """xxx""" til å lage tekst til klasser/funksjoner for å vise hva de gjør, slik gjort under

    """En klasse for å lage en person med navn og alder"""
    def __init__(self,alderen:int,navnet:str)->None:
        self.age = alderen
        self.name = navnet
    
#Bruk set/get til å endre verdier til et objekt, ikke gjør det direkte i koden som f.eks.
# p1.age = 35, fyfyfy
    def getAge(self):
        return self.age
    
    def setAge(self, alderen):
        if alderen < 0:
            self.alder=0
        self.age = alderen
    
    def getName(self):
        return self.name
    
    def setName(self, navnet):
        self.name = navnet

    def __str__(self):
        return "Navn: " + self.name + "\nAlder: " + str(self.age)    

# __name__ == __main__, for å vise at det er denne filen vi kjører fra og ingen annen fil
# Vi sjekker altså at "__name__" er det samme som "__main__", noe som er tilfellet hvis det er denna fila vi jobber med
if __name__=="__main__":
    print("Nå starter det! ")
    p1 = Person(42,"Ola Sørmann")
    p2 = Person(21,"Ole Tommy")
    print(p1)
    print(p2)