CREATE DATABASE maquina_cortavidrios;
USE maquina_cortavidrios;
CREATE TABLE cortes (  
    id INT AUTO_INCREMENT PRIMARY KEY,  
    forma VARCHAR(50),  
    color VARCHAR(50),  
    frase VARCHAR(100) 
    );  

#Inserts
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

#Consultas

SELECT * FROM cortes;
SELECT * FROM cortes WHERE forma = 'Cuadrado';
SELECT * FROM cortes WHERE color = 'Rojo';
SELECT * FROM cortes WHERE frase = 'CBA 2024';
SELECT forma, color FROM cortes WHERE frase = 'CBA 2024';


