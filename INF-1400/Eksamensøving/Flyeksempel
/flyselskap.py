import examoving

class Flyselskap:
    def __init__(self, navn) -> None:
        self.navn = navn
        self.flåte = []

    def legg_til_fly(self, flytype, modell, vekt, ant_paller=0, ant_pax=0, ant_bagasje=0):
        if flytype == "Passasjerfly":
            nytt_fly = examoving.Passasjerfly(modell, vekt, ant_pax, ant_bagasje)
            self.flåte.append(nytt_fly)
        elif flytype == "Fraktfly":
            nytt_fly = examoving.Fraktfly(modell, vekt, ant_paller)
            self.flåte.append(nytt_fly)
        else:
            raise ValueError("Flytype må være frakt- eller passasjerfly")
    
    def beregn_total_fly_vekt(self):
        for maskin in self.flåte:
            maskin.sett_last_vekt()
    
    def __str__(self) -> str:
        info = "Flyselskap: " + self.navn
        for fly in self.flåte:
            info += "\n" + str(fly)
        return info


if __name__ == "__main__":
    flyselskap = Flyselskap("Heines airways")
    flyselskap.legg_til_fly("Passasjerfly", "A350", 175000, ant_pax=180, ant_bagasje=200)
    flyselskap.legg_til_fly("Fraktfly", "747-8F", 200000, ant_paller=200)

    print(flyselskap)

    flyselskap.beregn_total_fly_vekt()

    print()
    print(flyselskap)