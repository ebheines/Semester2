import person

class Student(person.Person):
    def __init__(self,alderen,navnet,studieretning,studentnr):
        super().__init__(alderen,navnet)
        self.studieretning = studieretning
        self.studentnr = studentnr

    def __str__(self):
        return super().__str__() + "\nStudieretning: " + self.studieretning + "\nStudentnummer: " + self.studentnr


if __name__ == "__main__":
    s1 = Student(21,"Eskil","Bachelor, Informatikk","136")
    print(s1) 