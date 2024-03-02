import person

# Importerer klassen Person fra person.py
class Ansatt(person.Person):
    def __init__(self,alderen, navnet, stilling, lønn):
# Bruker "super" for å hente data fra den øvre klassen 
        super().__init__(alderen,navnet)
        self.stilling=stilling
        self.lønn = lønn
    
    def __str__(self):
        return super().__str__() + "\nStilling: " + self.stilling + "\nLønn: " + str(self.lønn)


if __name__ == "__main__":
    a1 = Ansatt(29,"Ola Sørmann","Lektor",500000)
    print(a1)
