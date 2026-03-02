
create database if not exists PYBancoProyecto;
use PYBancoProyecto;

CREATE TABLE entrenadores (
	_id VARCHAR(24) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    sueldo INT NOT NULL,
    presidente_id VARCHAR(24) NOT NULL
);

CREATE TABLE jugadores(
	_id VARCHAR(24) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    posicion VARCHAR(50) NOT NULL,
    sueldo INT NOT NULL,
    presidente_id VARCHAR(24) NOT NULL
);

CREATE TABLE pagos (
	_id CHAR(24) PRIMARY KEY,
    jugador_id CHAR(24) NOT NULL,
    presidente_id CHAR(24) NOT NULL,
    cantidad DECIMAL(15,2) NOT NULL,
    estado VARCHAR(50) NOT NULL,
    fecha DATETIME(3) NOT NULL
);

CREATE TABLE presidentes(
	_id CHAR(24) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    club VARCHAR(100) NOT NULL,
    presupuesto DECIMAL(15,2) NOT NULL
);

CREATE TABLE users(
	_id CHAR(24) PRIMARY KEY,
    email VARCHAR(150) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(20) NOT NULL
);

-- INSERTS DE LA TABLA DE ENTRENADORES

-- SELECT *
-- FROM entrenadores;

-- 1
INSERT INTO entrenadores(_id, nombre, sueldo ,presidente_i)
VALUES ('699c90ba52016f99565e09ed','Álvaro Arbeloa',70000,'698b2d2321fb40e5f285f4af'),
-- 2
('699c9127ae5fd2121c8a57b2','Hansi Flick',70000,'6994517f0827a49d7fb913ca'),
-- 3
('699c9166ae5fd2121c8a57b4','Diego Pablo Simeone',70000,'699453a94df866b726eb5552'),
-- 4
('699c918bae5fd2121c8a57b6','Ernesto Valverde',70000,'699453a94df866b726eb5553'),
-- 5
('699c91aeae5fd2121c8a57b8','Alessio Lisci',70000,'699453a94df866b726eb5554'),
-- 6
('699c91d4ae5fd2121c8a57ba','Claudio Giraldez',70000,'699453a94df866b726eb5555'),
-- 7
('699c91faae5fd2121c8a57bc','Eduardo Coudet',70000,'699453a94df866b726eb5556'),
-- 8
('699c9219ae5fd2121c8a57be','Eder Sarabia',70000,'699453a94df866b726eb5557'),
-- 9
('699c9238ae5fd2121c8a57c0','José Bordalás',70000,'699453a94df866b726eb5558'),
-- 10
('699c9268ae5fd2121c8a57c2','Miguel Ángel Sánchez',70000,'699453a94df866b726eb5559'),
-- 11
('699c9291ae5fd2121c8a57c4','Luís Castro',70000,'699453a94df866b726eb555a'),
-- 12
('699c92b7ae5fd2121c8a57c6','José Manuel González',70000,'699453a94df866b726eb555b'),
-- 13
('699c92e1ae5fd2121c8a57c8','Jagoba Arrasate',70000,'699453a94df866b726eb555c'),
-- 14
('699c9304ae5fd2121c8a57ca','Manuel Pellegrini',70000,'699453a94df866b726eb555d'),
-- 15
('699c9323ae5fd2121c8a57cc','Guillermo Almada',70000,'699453a94df866b726eb555e'),
-- 16
('699c9342ae5fd2121c8a57ce','Pellegrino Matarazzo',70000,'699453a94df866b726eb555f'),
-- 17
('699c9361ae5fd2121c8a57d0','Matías Almeyda',70000,'699453a94df866b726eb5560'),
-- 18
('699c937fae5fd2121c8a57d2','Carlos Corberán',70000,'699453a94df866b726eb5561'),
-- 19
('699c93a1ae5fd2121c8a57d4','Marcelino García',70000,'699453a94df866b726eb5562'),
-- 20
('699c93c2ae5fd2121c8a57d6','Iñigo Pérez',70000,'699453a94df866b726eb5563');


-- INSERTS DE LA TABLA DE JUGADORES

-- SELECT *
-- FROM jugadores;

INSERT INTO jugadores (_id, nombre, posicion, sueldo, presidente_id)
VALUES
-- 1 
('699455e84df866b726eb557b', 'Thibaut Courtois', 'Portero', 12000000, '698b2d2321fb40e5f285f4af'),
-- 2
('699455e84df866b726eb557c', 'Éder Militão', 'Defensa', 6000000, '698b2d2321fb40e5f285f4af'),
-- 3
('699455e84df866b726eb557d', 'Jude Bellingham', 'Centrocampista', 15000000, '698b2d2321fb40e5f285f4af'),
-- 4
('699455e84df866b726eb557e', 'Vinícius Júnior', 'Delantero', 18000000, '698b2d2321fb40e5f285f4af'),
-- 5
('699456994df866b726eb558c', 'Joan García', 'Portero', 8000000, '6994517f0827a49d7fb913ca'),
-- 6
('699456994df866b726eb558d', 'Ronald Araújo', 'Defensa', 5000000, '6994517f0827a49d7fb913ca'),
-- 7
('699456994df866b726eb558e', 'Pedri', 'Centrocampista', 8000000, '6994517f0827a49d7fb913ca'),
-- 8
('699456994df866b726eb558f', 'Robert Lewandowski', 'Delantero', 12000000, '6994517f0827a49d7fb913ca'),
-- 9
('699456c24df866b726eb5593', 'Jan Oblak', 'Portero', 9000000, '699453a94df866b726eb5552'),
-- 10
('699456c24df866b726eb5594', 'José María Giménez', 'Defensa', 4500000, '699453a94df866b726eb5552'),
-- 11
('699456c24df866b726eb5595', 'Koke Resurrección', 'Centrocampista', 5000000, '699453a94df866b726eb5552'),
-- 12
('699456c24df866b726eb5596', 'Julián Álvarez', 'Delantero', 6000000, '699453a94df866b726eb5552'),
-- 13
('699456f14df866b726eb559a', 'Unai Simón', 'Portero', 3500000, '699453a94df866b726eb5553'),
-- 14
('699456f14df866b726eb559b', 'Dani Vivian', 'Defensa', 2500000, '699453a94df866b726eb5553'),
-- 15
('699456f14df866b726eb559c', 'Oihan Sancet', 'Centrocampista', 3000000, '699453a94df866b726eb5553'),
-- 16
('699456f14df866b726eb559d', 'Iñaki Williams', 'Delantero', 5000000, '699453a94df866b726eb5553'),
-- 17
('699457384df866b726eb55a5', 'Sergio Herrera', 'Portero', 2000000, '699453a94df866b726eb5554'),
-- 18
('699457384df866b726eb55a6', 'Juan Cruz', 'Defensa', 1200000, '699453a94df866b726eb5554'),
-- 19
('699457384df866b726eb55a7', 'Lucas Torró', 'Centrocampista', 1500000, '699453a94df866b726eb5554'),
-- 20
('699457384df866b726eb55a8', 'Ante Budimir', 'Delantero', 1800000, '699453a94df866b726eb5554'),
-- 21
('699457574df866b726eb55ac', 'Ionuț Radu', 'Portero', 1500000, '699453a94df866b726eb5555'),
-- 22
('699457574df866b726eb55ad', 'Javi Rodríguez', 'Defensa', 1000000, '699453a94df866b726eb5555'),
-- 23
('699457574df866b726eb55ae', 'Franco Cervi', 'Centrocampista', 1200000, '699453a94df866b726eb5555'),
-- 24
('699457574df866b726eb55af', 'Iago Aspas', 'Delantero', 2500000, '699453a94df866b726eb5555'),
-- 25
('699457724df866b726eb55b3', 'Antonio Sivera', 'Portero', 1000000, '699453a94df866b726eb5556');


-- INSERTS DE LA TABLA DE PAGOS

-- SELECT * from pagos;

INSERT INTO pagos (_id, jugador_id, presidente_id, cantidad, estado, fecha)
VALUES
-- 1
('699486eb257e82c8673a4991', '699456994df866b726eb558e', '6994517f0827a49d7fb913ca', 500000.00, 'Pagado', '2026-02-17 16:19:07.037'),
-- 2
('69948be5cf16e232a8042e65', '699458774df866b726eb55e6', '699453a94df866b726eb555d', 150000.00, 'Asignado', '2026-02-17 16:40:21.135'),
-- 3
('6995f7d551541557a01dc588', '699455e84df866b726eb557b', '698b2d2321fb40e5f285f4af', 900000.00, 'Pendiente', '2026-02-18 18:33:09.750');


-- INSERTS PARA LA TABLA PRESIDENTES

-- SELECT * FROM presidentes;

INSERT INTO presidentes (_id, nombre, club, presupuesto)
VALUES
-- 1
('698b2d2321fb40e5f285f4af','Florentino Pérez','Real Madrid',1000000000.00),
-- 2 
('6994517f0827a49d7fb913ca','Joan Laporta','FC Barcelona',500000000.00),
-- 3 
('699453a94df866b726eb5552','Miguel Ángel Gil','Atlético de Madrid',500000000.00),
-- 4
('699453a94df866b726eb5557','Joaquín Buitrago','Elche CF',500000000.00),
-- 5
('699453a94df866b726eb5558','Ángel Torres','Getafe CF',500000000.00),
-- 6
('699453a94df866b726eb5559','Delfí Geli','Girona FC',500000000.00),
-- 7
('699453a94df866b726eb555d','Ángel Haro','Real Betis',500000000.00),
-- 8
('699453a94df866b726eb5560','José María del Nido','Sevilla FC',500000000.00),
-- 9
('699453a94df866b726eb5561','Lay Hoon Chan','Valencia CF',500000000.00),
-- 10
('699453a94df866b726eb5556','Alfonso Fernández','Deportivo Alavés',500000000.00),
-- 11
('699453a94df866b726eb555b','Alan Pace','RCD Espanyol',500000000.00),
-- 12
('699453a94df866b726eb555e','Martín Peláez','Real Oviedo',500000000.00),
-- 13 
('699453a94df866b726eb555f','Jokin Aperribay','Real Sociedad',500000000.00),
-- 14
('699453a94df866b726eb5554','Luis Sabalza','CA Osasuna',500000000.00),
-- 15
('699453a94df866b726eb5555','Marián Mouriño','Celta de Vigo',500000000.00),
-- 16
('699453a94df866b726eb555a','Pablo Sánchez','Levante UD',500000000.00),
-- 17
('699453a94df866b726eb555c','Andy Kohlberg','RCD Mallorca',500000000.00),
-- 18
('699453a94df866b726eb5553','Jon Uriarte','Athletic Club',500000000.00),
-- 19 
('699453a94df866b726eb5562','Fernando Roig','Villarreal CF',500000000.00),
-- 20
('699453a94df866b726eb5563','Raúl Martín','Rayo Vallecano',500000000.00);


-- INSERTS PARA LA TABLA DE users

-- SELECT * FROM users;

INSERT INTO users (_id, email, password, role)
VALUES
-- 1
('698b2ac88658a1453ef5beb2','donnie@gmail.com','1234','user'),
-- 2
('698b2d2321fb40e5f285f4ae','tebas@laliga.es','1234','admin');
