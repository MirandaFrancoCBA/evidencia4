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



