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

-- Insersion datos tabla jugador
-- 1
insert into Jugador(nombre,dineroBanco,dineroComercios,ficha) values(
	"joseph",
    0,
    0,
    "caballo"
);
-- 2
insert into Jugador(nombre,dineroBanco,dineroComercios,ficha) values(
	"daniela",
    200,
    500,
    "gato"
);
insert into Jugador(nombre,dineroBanco,dineroComercios,ficha) values(
	"andres",
    200,
    0,
    "barco"
);
-- 3
insert into Jugador(nombre,dineroBanco,dineroComercios,ficha) values(
	"anyello",
    400,
    100,
    "zapato"
);
-- 4
insert into Jugador(nombre,dineroBanco,dineroComercios,ficha) values(
	"issac",
    400,
    200,
    "sapo"
);
-- 5
insert into Jugador(nombre,dineroBanco,dineroComercios,ficha) values(
	"karen",
    800,
    150,
    "carro"
);
-- 6
insert into Jugador(nombre,dineroBanco,dineroComercios,ficha) values(
	"melissa",
    400,
    100,
    "sombrero"
);
-- 7
insert into Jugador(nombre,dineroBanco,dineroComercios,ficha) values(
	"guale",
    0,
    800,
    "botella"
);
-- 8 
insert into Jugador(nombre,dineroBanco,dineroComercios,ficha) values(
	"gloria",
    800,
    350,
    "avion"
);
-- 9 
insert into Jugador(nombre,dineroBanco,dineroComercios,ficha) values(
	"pamela",
    800,
    450,
    "casa"
);
-- 10 

insert into Jugador(nombre,dineroBanco,dineroComercios,ficha) values(
	"masnuel",
    400,
    450,
    "tiburon"
);

-- insersion datos tarjeta
-- 1
insert into Tarjeta(tipoTarjeta, descripcion) values(
	1,
    "sale de la carcel"
);
-- 2
insert into Tarjeta(tipoTarjeta, descripcion) values(
	2,
    "cobre 100$"
);
-- 3
insert into Tarjeta(tipoTarjeta, descripcion) values(
	2,
    "pague 50$ al banco"
);
-- 4 
insert into Tarjeta(tipoTarjeta, descripcion) values(
	1,
    "exceso de velocidad pague 100$"
);
-- 5 
insert into Tarjeta(tipoTarjeta, descripcion) values(
	1,
    "es su cumpleaños, le regalan 50$"
);

-- insersion datos Tarjeta_Jugador
-- 1

insert into Tarjeta_Jugador(jugador,tarjeta) values(
	1,4
);
-- 2 
insert into Tarjeta_Jugador(jugador,tarjeta) values(
	1,3
);
-- 3
insert into Tarjeta_Jugador(jugador,tarjeta) values(
	1,5
);
-- 4 
insert into Tarjeta_Jugador(jugador,tarjeta) values(
	2,3
);
-- 5
insert into Tarjeta_Jugador(jugador,tarjeta) values(
	3,1
);
-- 6
insert into Tarjeta_Jugador(jugador,tarjeta) values(
	4,4
);
-- 7
insert into Tarjeta_Jugador(jugador,tarjeta) values(
	5,1
);
-- 8 
insert into Tarjeta_Jugador(jugador,tarjeta) values(
	5,3
);
-- 9
insert into Tarjeta_Jugador(jugador,tarjeta) values(
	7,5
);

-- 10
insert into Tarjeta_Jugador(jugador,tarjeta) values(
	9,4
);

-- insercion datos Banco
-- 1
insert into Banco(id_banco,nombre) values(
	1,
	"Banco de la partida"
);

-- insercion datos Terreno 
-- 1
insert into Terreno(color,tipo,casas,hoteles,alquiler) values (
	"amarillo 1",
    2,
    0,
    0,
    20
);
-- 2
insert into Terreno(color,tipo,casas,hoteles,alquiler) values (
	"amarillo 2",
    2,
    0,
    0,
    10
);
-- 3 
insert into Terreno(color,tipo,casas,hoteles,alquiler) values (
	"amarillo 3",
    2,
    0,
    0,
    15
);
-- 4
insert into Terreno(color,tipo,casas,hoteles,alquiler) values (
	"amarillo",
    2,
    0,
    0,
    25
);
-- 5 
insert into Terreno(color,tipo,casas,hoteles,alquiler) values (
	"celestes",
    1,
    0,
    0,
    50
);
-- 6 
insert into Terreno(color,tipo,casas,hoteles,alquiler) values (
	"celestes",
    1,
    0,
    0,
    50
);
-- 7
insert into Terreno(color,tipo,casas,hoteles,alquiler) values (
	"rojo",
    2,
    0,
    0,
    14
);
-- 8
insert into Terreno(color,tipo,casas,hoteles,alquiler) values (
	"rojo",
    2,
    0,
    0,
    10
);
-- 9 
insert into Terreno(color,tipo,casas,hoteles,alquiler) values (
	"rojo",
    2,
    0,
    0,
    5
);
-- 10 
insert into Terreno(color,tipo,casas,hoteles,alquiler) values (
	"rojo",
    2,
    0,
    0,
    20
);

-- insercion datos Ventas
-- 1 
insert into Venta(jugador,terreno,banco,turno) values(
	1,
    3,
    1,
    2
);
-- 2
insert into Venta(jugador,terreno,banco,turno) values(
	4,
    2,
    1,
    1
);
-- 3
insert into Venta(jugador,terreno,banco,turno) values(
	4,
    2,
    1,
    3
);
-- 4
insert into Venta(jugador,terreno,banco,turno) values(
	6,
    2,
    1,
    4
);
-- 5
insert into Venta(jugador,terreno,banco,turno) values(
	7,
    8,
    1,
    4
);
-- 6
insert into Venta(jugador,terreno,banco,turno) values(
	9,
    6,
    1,
    4
);
-- 7 
insert into Venta(jugador,terreno,banco,turno) values(
	3,
    2,
    1,
    4
);
-- 8 
insert into Venta(jugador,terreno,banco,turno) values(
	8,
    3,
    1,
    5
);
-- 9
insert into Venta(jugador,terreno,banco,turno) values(
	2,
    5,
    1,
    7
);
-- 10
insert into Venta(jugador,terreno,banco,turno) values(
	7,
    5,
    1,
    2
);

insert into Venta(jugador,terreno,banco,turno) values(
	2,
    4,
    1,
    3
);

-- insercion datos Compra 
-- 1
insert into Compra(jugador,terreno,banco,turno) values(
	2,
    4,
    1,
    2
);
-- 2
insert into Compra(jugador,terreno,banco,turno) values(
	6,
    3,
    1,
    5
);
-- 3
insert into Compra(jugador,terreno,banco,turno) values(
	7,
    1,
    1,
    2
);
-- 4 
insert into Compra(jugador,terreno,banco,turno) values(
	10,
    6,
    1,
    1
);
-- 5
insert into Compra(jugador,terreno,banco,turno) values(
	1,
    1,
    1,
    5
);
 -- 6
 insert into Compra(jugador,terreno,banco,turno) values(
	6,
    5,
    1,
    7
);
 -- 7
 insert into Compra(jugador,terreno,banco,turno) values(
	9,
    3,
    1,
    1
);
-- 8
insert into Compra(jugador,terreno,banco,turno) values(
	5,
    9,
    1,
    1
);
-- 9
insert into Compra(jugador,terreno,banco,turno) values(
	8,
    9,
    1,
    10
);
-- 10
insert into Compra(jugador,terreno,banco,turno) values(
	3,
    6,
    1,
    5
);
-- insercion datos lanzamiento 
-- 1
insert into Lanzamiento(dado1, dado2, jugador) values(
	4,
    5,
    1
);
-- 2
insert into Lanzamiento(dado1, dado2, jugador) values(
	2,
    3,
    6
);
-- 3

insert into Lanzamiento(dado1, dado2, jugador) values(
	3,
    6,
    7
);
-- 4

insert into Lanzamiento(dado1, dado2, jugador) values(
	4,
    6,
    1
);
-- 5
insert into Lanzamiento(dado1, dado2, jugador) values(
	2,
    5,
    1
);
-- 6
insert into Lanzamiento(dado1, dado2, jugador) values(
	4,
    2,
    1
);
-- 7
insert into Lanzamiento(dado1, dado2, jugador) values(
	4,
    1,
    1
);
-- 8
insert into Lanzamiento(dado1, dado2, jugador) values(
	1,
    5,
    1
);
-- 9 
insert into Lanzamiento(dado1, dado2, jugador) values(
	4,
    5,
    1
);
-- 10 
insert into Lanzamiento(dado1, dado2, jugador) values(
	4,
    3,
    1
);

use bd_monopoly;

select * from compra;
select * from venta;

select c.id_compra, c.jugador,c.terreno 
from Compra c where terreno 
not in (select v.terreno 
from Venta v where v.jugador = c.jugador) and c.jugador = 6;

select * from Venta;
select * from Compra;

-- seleccion terrenos que no se han comprado
select * from terreno t
where t.id_terreno not in (select terreno from Compra);
-- validar si esa lista es vacia, entonces hacer lo siguiente

select * from terreno t
where t.id_terreno in (select c.terreno 
from Compra c 
join Venta v 
using(terreno,jugador) where c.turno < v.turno);

insert into Compra(jugador,terreno,banco,turno) values(
	3,
    4,
    1,
    4
);

insert into Venta(jugador,terreno,banco,turno) values(
	6,
    4,
    1,
    9
);
insert into Compra(jugador,terreno,banco,turno) values(
	5,
    4,
    1,
	9
);

select * from compra;
select * from terreno;
select * from Compra c join Venta v using(jugador,terreno);


select max(turno) as ultima_compra from compra c where terreno = 4;
select max(turno) as ultima_venta from venta v where terreno = 4;

select * from terreno t where t.id_terreno not in (select terreno from venta);
select * from terreno t where t.id_terreno not in (select terreno from venta) and t.id_terreno not in (select terreno from compra);

use bd_monopoly;
describe jugador;
delimiter /

create procedure sp_ingresarJugador(in NombreP varchar(50), dineroBanco int, dineroComercios int, ficha varchar(25))
	begin
		insert into jugador (Nombre,dineroBanco, dineroComercios,ficha) values(
			NombreP,
            dineroBanco,
            dineroComercios,
            ficha
        );
    end
/ delimiter ;

delimiter /

create procedure sp_consultarPropiedadJugador(in nombreP int)
	begin
		select * from terreno t where id_terreno in (select terreno from compra where jugador = nombreP);
    end
/ delimiter ;

delimiter /
	create trigger borrarTerreno 
    before delete on terreno
    for each row 
		begin
			delete from venta where terreno = old.id_terreno;
            delete from compra where terreno = old.id_terreno;
        end; 
	
/delimiter ;

delimiter /
	create trigger alquilerUp
    before update on terreno
    for each row 
    begin
		set new.alquiler = new.casas*20 + old.alquiler; 
    end;
    
/delimiter ;

delimiter /
	create trigger casas_hotel
    before update on terreno
    for each row 
    begin
		if new.casas <= 4 then 
			set new.hoteles = 1;
            set new.casas =0;
            set new.alquiler = 400 + old.alquiler;
        end if;
    end;

/delimiter ;

delimiter /
create trigger eliminarJugador
	before delete on jugador
    for each row 
    begin
		delete from compra where jugador = old.id_jugador;
		delete from Lanzamiento where jugador = old.id_jugador;
        delete from tarjeta_jugador where jugador = old.id_jugador;
        delete from venta where jugador = old.id_jugador;
        
    end;
/delimiter ;



-- PROCEDURE actualizar terreno
delimiter /
create procedure sp_actualizarTerreno(in id_terrenoP int, casasP int)
	begin
		update terreno set casas = casasP where id_terreno = id_terrenoP;
	end
/ delimiter ;

-- PROCEDURES eliminar jugador y terreno por nombre

delimiter /
create procedure sp_eliminarJugador(in nombreP varchar(25),fichaP varchar(25))
	begin
		delete from jugador where nombre = nombreP and ficha = fichaP;
	end
/ delimiter ;
describe terreno;

delimiter /
create procedure sp_eliminarTerreno(in nombreTerrenoP varchar(25))
	begin
		delete from terreno where nombre = nombreTerrenoP;
	end

/ delimiter ;



-- PROCEDURE modificar nombre jugador
delimiter /
create procedure sp_actualizarJugador(in id_jugadorP int, nombreP varchar(50))
	begin
		update jugador set Nombre = nombreP where id_jugador = id_jugadorP;
	end
/ delimiter 

-- procedure insertarTerreno
delimiter /
create procedure sp_insertarTerreno(in colorP char(10), tipoP enum('negocio','propiedad'), casasP int, hotelesP int, alquilerP int)
	begin
		insert into terreno(color,tipo,casas,hoteles,alquiler) values(
			colorP,
			tipoP,
			casasP,
			hotelesP,
			alquilerP
		);
	end
/ delimiter ;



-- procedure insertarCompra
delimiter /
create procedure sp_insertarCompra(in jugadorP int, terrenoP int, bancoP int, turnoP int)
	begin
		insert into compra(jugador,terreno,banco,turno) values(
			jugadorP,
			terrenoP,
			bancoP,
			turnoP

		);
	end
/ delimiter ;

delimiter /
-- Procedure insertar jugador

create procedure sp_ingresarJugador(in NombreP varchar(50), dineroBanco int, dineroComercios int, ficha varchar(25))
	begin
		insert into jugador (Nombre,dineroBanco, dineroComercios,ficha) values(
			NombreP,
			dineroBanco,
			dineroComercios,
			ficha
		);
	end
/ delimiter ;

-- reporte jugadores actuales
use bd_monopoly;
create view reporteJugadoresActuales as
	select id_jugador, nombre, ficha 
    from jugador;


create view reporteTerrenosNoDisponibles as
	select * from terreno where id_terreno in (select terreno from compra join venta using(terreno)) union (
    select * from terreno where id_terreno in (select terreno from compra c join venta v using(terreno) 
    group by terreno having max(c.turno) > max(v.turno)));

drop view reporteTerrenosNoDisponiblse;
create view reporteTerrenosDisponibles as
	select * from terreno where id_terreno not in (select terreno from compra join venta using(terreno)) union (
    select * from terreno where id_terreno in (select terreno from compra c join venta v using(terreno) 
    group by terreno having max(v.turno) > max(c.turno)));

    

create view reporteTarjetasTomadas as
	select * from tarjeta where id_tarjeta in (select tarjeta from tarjeta_jugador);


create index nombreJ on jugador(nombre);
create index fichaJ on jugador(ficha);
create index nombreTer on terreno(nombre);
create index idTer on terreno(id_terreno);
create index idTar on tarjeta(id_tarjeta);

CREATE USER 'adminJoseph'@'localhost'IDENTIFIED BY 'adminJoseph123';
CREATE USER 'adminAndres'@'localhost' IDENTIFIED BY 'adminAndres123';
CREATE USER 'adminGeneral'@'localhost' IDENTIFIED BY 'adminGeneral123';
CREATE USER 'jugador'@'localhost' IDENTIFIED BY 'jugador123';
CREATE USER 'banco'@'localhost' IDENTIFIED BY 'banco123';

GRANT ALL PRIVILEGES ON bd_monopoly.* TO 'adminJoseph'@'localhost' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON bd_monopoly.* TO 'adminAndres'@'localhost' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON bd_monopoly.* TO 'adminGeneral'@'localhost' WITH GRANT OPTION;


GRANT EXECUTE ON PROCEDURE bd_monopoly.sp_consultarPropiedadJugador TO 'jugador'@'localhost';

GRANT SELECT ON bd_monopoly.reporteTerrenosNoDisponibles TO 'jugador'@'localhost';
GRANT SELECT ON bd_monopoly.reporteTerrenosDisponibles TO 'jugador'@'localhost';


