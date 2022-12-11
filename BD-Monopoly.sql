create database BD_Monopoly;
use BD_Monopoly;

-- CREACIÓN DE TABLAS

-- Tabla Jugador
create table Jugador(
	id_jugador int auto_increment primary key unique,
    Nombre varchar(50) not null,
    dineroBanco int,
    dineroComercios int,
    ficha varchar(25) not null
);

-- Tabla Tarjeta
create table Tarjeta(
	id_tarjeta int auto_increment primary key unique,
    tipoTarjeta enum('arcaComunal','casualidad'),
    descripcion varchar(50)
);

-- Tabla tarjeta_Jugador
create table Tarjeta_Jugador(
	jugador int,
    tarjeta int,
    constraint fk_jugador foreign key (jugador) references Jugador(id_jugador),
    constraint fk_tarjeta foreign key (tarjeta) references Tarjeta(id_tarjeta),
    primary key(jugador,tarjeta)
);

-- Tabla Banco
create table Banco(
	id_banco int unique primary key,
    nombre varchar(25)
);

-- Tabla terreno
create table Terreno(
	id_terreno int auto_increment primary key unique,
    color char(10) not null,
    tipo enum("negocio","propiedad") not null,
    casas int not null,
    hoteles int not null,
    alquiler int not null
);

-- Tabla venta
create table Venta(
	id_venta int auto_increment primary key unique,
    jugador int,
    terreno int,
    banco int,
    turno int,
    constraint cons_fk_jugador foreign key (jugador) references Jugador(id_jugador),
    constraint cons_fk_terreno foreign key (terreno) references Terreno(id_terreno),
    constraint cons_fk_banco foreign key (banco) references Banco(id_banco)
);

-- Tabla Compra
create table Compra(
	id_compra int auto_increment primary key unique,
    jugador int,
    terreno int,
    banco int,
    turno int,
    constraint consCompra_fk_jugador foreign key (jugador) references Jugador(id_jugador),
    constraint consCompra_fk_terreno foreign key (terreno) references Terreno(id_terreno),
    constraint consCompra_fk_banco foreign key (banco) references Banco(id_banco)
);

-- Tabla Lanzamiento
create table Lanzamiento(
	id_lanzamiento int auto_increment primary key unique,
    dado1 int,
    dado2 int,
    jugador int,
    constraint consLanzamiento_fk_jugador foreign key(jugador) references Jugador(id_jugador)
);

-- INSERCION DE DATOS
-- insert into "nombre_tabla" (columna1,columna2...) values (
-- 		"valor para columna1",
-- 		"valor para columna2"
-- );