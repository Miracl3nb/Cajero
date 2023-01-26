necesito


instalar mysql on windows 

instalar mysql.connector en el entorno de python

script sql 
USE cuentasclientes;
CREATE TABLE cuentas(
	ID int auto_increment,
    DNI int,
    PIN int,
    NOMBRE varchar (50),
    SALDO int,
	primary key (ID)    
);

INSERT INTO cuentas (DNI, PIN, NOMBRE, SALDO) value (36398721, 2505, 'Nahuel Brunel', 542222);
INSERT INTO cuentas (DNI, PIN, NOMBRE, SALDO) value (74651221, 2205, 'Pablo Brunel', 545552);

SELECT * FROM cuentas;

SELECT IF (EXISTS(SELECT NOMBRE FROM cuentas WHERE DNI = 36398721), 1, 0);


test de actualizacion

test pull recuest