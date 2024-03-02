class Color:
    def __init__(self, rgbvalue, colorname):
        self._rgbvalue = rgbvalue
        self._colorname = colorname

    #Tilgangsmetoder
    @property
    def RGBvalue(self):
        return self._rgbvalue
    
    @property
    def Colorname(self):
        return self._colorname
    
    @RGBvalue.setter
    def setRGBvalue(self, value):
        if value > 0XFFFFFF or value < 0:
            raise ValueError("Ugyldig verdi for farge")
        if type(value) != int:
            raise TypeError("Feil datatype")
        self._rgbvalue = value
    
    @Colorname.setter
    def setColorname(self, name):
        if type(name) != str:
            raise TypeError("Bare bruk strings her")
        if not name:
            raise ValueError("Kanskje lurt å skrive nokka")
        self._colorname = name

    def __str__(self):
        return str(self._colorname) + " with color " + str(self._rgbvalue)


    #PROPTERER
    rgbvalue = property(RGBvalue, setRGBvalue)
    colorname = property(Colorname, setColorname)

if __name__ == "__main__":
    c = Color(0xFF00FF, "Thanos")
    print(c)
