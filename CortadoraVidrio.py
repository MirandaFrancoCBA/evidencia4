
#Creando la clase
class CortadoraVidrio:
    def __init__(self, forma = "Sin forma definida", color= "Transparente", frase="No elegida"):
        self._forma = forma
        self._color = color
        self._frase = frase

#Definiendo getters y setters

    @property
    def forma(self):
        return self._forma
    @forma.setter
    def forma(self, forma):
        self._forma = forma

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

#Metodos

    def cortar_figura(self, corte):
        cortes = 0
        if cortes == 0:
            self.forma = corte
            cortes += 1
        else:
            print("Solo un corte permitido.")
    
    def grabar(self, grabado):
        self.frase = grabado

    def pintar(self, pintura):
        self.color = pintura

    
    def __str__(self):
        return f"Forma seleccionada: {self.forma}, Color: {self.color}, Frase: {self.frase}"


coso1 = CortadoraVidrio()
print(coso1)
coso1.cortar_figura("Cuadrado")
coso1.grabar("Hola")
coso1.pintar("Azul")
print(coso1)
coso1.cortar_figura("Triangulo")
print(coso1)