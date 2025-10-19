from padre import *
from color import *


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, alto, ancho,  color ):

        #de esta manera se llaman a las clases padre
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)

    def area(self):
        return self.ancho * self.alto

