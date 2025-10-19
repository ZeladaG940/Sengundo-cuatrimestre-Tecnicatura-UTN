class Figurageometrica:
    def __init__(self, alto, ancho):
        self._alto = alto
        self._ancho = ancho
    @property
    def alto(self):
        return self._alto
    @alto.setter
    def alto(self, newAlto):
        self._alto = newAlto
    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, newAncho):
        self._ancho = newAncho

    def __str__(self):
        return f"{self._alto} , {self._ancho}"