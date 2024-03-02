
class Fly:
    def __init__(self, modell, vekt) -> None:
        self.modell = modell
        self.vekt = vekt
    
    def sett_last_vekt(self):
        raise NotImplementedError("Ikke bruk superklassen")
    
    def __str__(self) -> str:
        return "Modell: " + self.modell + "\nVekt: " + str(self.vekt) + "\n"


class Fraktfly(Fly):
    def __init__(self, modell, vekt, ant_paller) -> None:
        super().__init__(modell, vekt)
        self.ant_paller = ant_paller

    def sett_last_vekt(self):
        self.vekt += (self.ant_paller * 500)


class Passasjerfly(Fly):
    def __init__(self, modell, vekt, ant_pax, ant_bagasje) -> None:
        super().__init__(modell, vekt)
        self.ant_pax = ant_pax
        self.ant_bagasje = ant_bagasje

    def sett_last_vekt(self):
        self.vekt += (self.ant_pax * 100) + (self.ant_bagasje * 23)
    


if __name__ == "__main__":

    frak1 = Fraktfly("A330", 175000, 40)
    passasjer1 = Passasjerfly("737-800", 41000, 118, 70)

    print(frak1)
    print(passasjer1)

    frak1.sett_last_vekt()
    passasjer1.sett_last_vekt()

    print(frak1)
    print(passasjer1)