class OMOColor:
    def __init__(self, rgbvalue, colorname):
        
        #more semi private
        self.__rgbvalue = rgbvalue
        self.__colornmae = colorname

        #semiprivate
        #self._rgbvalue = rgbvalue
        #self._colorname = colorname

        #public
        #self.rgbvalue = rgbvalue
        #self.colorname = colorname




if __name__=="__main__":
    c = OMOColor(0xFF00FF, "Thanos")
    print(f"{c._OMOColor__colorname} with color {c._OMOColor__rgbvalue}")
    c.__rgbvalue = 0x00FF00
    c.__colorname = "HULK"
    print(f"{c._OMOColor__colorname} with color {c._OMOColor__rgbvalue}")

