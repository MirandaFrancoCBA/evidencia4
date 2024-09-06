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


