"""De esta forma cree la tabla en workbench
 e hice los inserts y las consultas"""

CREATE DATABASE maquina_cortavidrios
USE maquina_cortavidrios
CREATE TABLE cortes (  
    id INT AUTO_INCREMENT PRIMARY KEY,  
    forma VARCHAR(50),  
    color VARCHAR(50),  
    frase VARCHAR(100) 
    );  

INSERT INTO cortes (forma, color, frase) VALUES ('Cuadrado', 'Rojo', 'Hola Mundo');
INSERT INTO cortes (forma, color, frase) VALUES ('Triangulo', 'Azul', 'Soy un triangulo');
INSERT INTO cortes (forma, color, frase) VALUES ('Circulo', 'Verde', 'CBA 2024');
INSERT INTO cortes (forma, color, frase) VALUES ('Rectangulo', 'Amarillo', 'Soy un rectangulo');
INSERT INTO cortes (forma, color, frase) VALUES ('Rombo', 'Naranja', 'Soy un rombo');
INSERT INTO cortes (forma, color, frase) VALUES ('Pentagono', 'Morado', 'CBA 2024');
INSERT INTO cortes (forma, color, frase) VALUES ('Hexagono', 'Rosa', 'CBA 2024');
INSERT INTO cortes (forma, color, frase) VALUES ('Cuadrado', 'Violeta', 'Soy un cuadrado');
INSERT INTO cortes (forma, color, frase) VALUES ('Triangulo', 'Celeste', 'Soy un triangulo');
INSERT INTO cortes (forma, color, frase) VALUES ('Circulo', 'Turquesa', 'CBA 2024');


