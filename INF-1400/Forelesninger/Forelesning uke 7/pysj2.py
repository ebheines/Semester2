class Color:
    def __init__(self, rgbvalue, colorname):
        self._rgbvalue = rgbvalue
        self._colorname = colorname

    #Tilgangsmetoder
    def getRGBvalue(self):
        return self._rgbvalue
    
    def getColorname(self):
        return self._colorname
    
    def setRGBvalue(self, value):
        if value > 0XFFFFFF or value < 0:
            raise ValueError("Ugyldig verdi for farge")
        if type(value) != int:
            raise TypeError("Feil datatype")
        self._rgbvalue = value
    
    def setColorname(self, name):
        self._colorname = name

    def __str__(self):
        return str(self._colorname) + " with color " + str(self._rgbvalue)


    #PROPTERER
    rgbvalue = property(getRGBvalue, setRGBvalue)
    colorname = property(getColorname, setColorname)

if __name__ == "__main__":
    c = Color(0xFF00FF, "Thanos")
    print(c)
