"""Aqui probare la maquina"""
from CortadoraVidrio import CortadoraVidrio

def test_cortar_figura():
    cortadora = CortadoraVidrio()
    cortadora.cortar_figura("Cuadrado")
    assert cortadora.forma == "Cuadrado"

def test_grabar():
    cortadora = CortadoraVidrio()
    cortadora.grabar("Hola Mundo")
    assert cortadora.frase == "Hola Mundo"

def test_pintar():
    cortadora = CortadoraVidrio()
    cortadora.pintar("Rojo")
    assert cortadora.color == "Rojo"

def test_str():
    cortadora = CortadoraVidrio("Cuadrado", "Rojo", "Hola Mundo")
    assert str(cortadora) == "Forma seleccionada: Cuadrado, Color: Rojo, Frase: Hola Mundo"


pieza1 = CortadoraVidrio()
pieza1.cortar_figura("Cuadrado")
pieza1.grabar("Hola Mundo")
pieza1.pintar("Rojo")
print(pieza1)

pieza2 = CortadoraVidrio()
pieza2.cortar_figura("Triangulo")
pieza2.grabar("Soy un triangulo")
pieza2.pintar("Azul")
print(pieza2)

pieza3 = CortadoraVidrio()
pieza3.cortar_figura("Circulo")
pieza3.grabar("659135469")
pieza3.pintar("Verde")
print(pieza3) 

pieza4 = CortadoraVidrio()
pieza4.cortar_figura("Rectangulo")
pieza4.grabar("Soy un rectangulo")
pieza4.pintar("Amarillo")
print(pieza4)

pieza5 = CortadoraVidrio()
pieza5.cortar_figura("Rombo")
pieza5.grabar("Soy un rombo")
pieza5.pintar("Naranja")
print(pieza5)

pieza6 = CortadoraVidrio()
pieza6.cortar_figura("Pentagono")
pieza6.grabar("CBA 2024")
pieza6.pintar("Morado")
print(pieza6)

pieza7 = CortadoraVidrio()
pieza7.cortar_figura("Hexagono")
pieza7.grabar("CBA 2024")
pieza7.pintar("Rosa")
print(pieza7)

pieza8 = CortadoraVidrio()
pieza8.cortar_figura("Cuadrado")
pieza8.grabar("Soy un cuadrado")
pieza8.pintar("Violeta")
print(pieza8)

pieza9 = CortadoraVidrio()
pieza9.cortar_figura("Triangulo")
pieza9.grabar("Soy un triangulo")
pieza9.pintar("Celeste")
print(pieza9)

pieza10 = CortadoraVidrio()
pieza10.cortar_figura("Circulo")
pieza10.grabar("CBA 2024")
pieza10.pintar("Turquesa")
print(pieza10)