class Komponent:
    def __init__(self, posisjon, status) -> None:
        self.posisjon = posisjon
        self.status = status


class Dragon(Komponent):
    def __init__(self, seter, posisjon, status) -> None:
        super().__init__(posisjon, status)
        self.antall_seter = seter


class Lasterom(Komponent):
    def __init__(self, kapasitet, posisjon, status) -> None:
        super().__init__(posisjon, status)
        self.lastekapasitet = kapasitet
        


class Motor:
    def __init__(self, posisjon, stauts) -> None:
        self.skyvekraft = 934
        self.posisjon = posisjon
        self.status = stauts


class Steg(Komponent):
    def __init__(self, posisjon, status) -> None:
        super().__init__(posisjon, status)
        self.motorer = []

