
#Creando la clase
class CortadoraVidrio:
    def __init__(self, forma = "Sin forma definida", color= "Transparente", frase="No elegida"):
        self._forma = forma
        self._color = color
        self._frase = frase
        self.cortes = 0
        self.grabados = 0
        self.pintados = 0

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
        
        if self.cortes == 0:
            self.forma = corte
            self.cortes += 1
        else:
            print("Solo un corte permitido.")
    
    def grabar(self, grabado):
        if self.grabados == 0:
            self.frase = grabado
            self.grabados += 1
        else:
            print("Solo un grabado permitido.")

    def pintar(self, pintura):
        if self.pintados == 0:
            self.color = pintura
            self.pintados += 1
        else:
            print("Solo un color permitido.")
    
    def __str__(self):
        return f"Forma seleccionada: {self.forma}, Color: {self.color}, Frase: {self.frase}"

