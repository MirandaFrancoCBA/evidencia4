
#Creando la clase
class CortadoraVidrio:
    def __init__(self, ancho, alto, color, frase):
        self._ancho = ancho
        self._alto = alto
        self._color = color
        self._frase = frase
#Definiendo getters y setters
    @property
    def ancho(self):
        return self._ancho
    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho
    
    @property
    def alto(self):
        return self._alto
    @alto.setter
    def alto(self, alto):
        self._alto = alto
    
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, color):
        self._color = color
    
    @property
    def frase(self):
        return self._frase
    @frase.setter
    def frase(self, frase):
        self._frase = frase

    def cortar_figura(self):
        pass
    
    def grabar(self):
        pass
    
    def pintar(self):
        pass
    
    def __str__(self):
        pass


