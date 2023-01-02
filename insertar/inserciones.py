from consultar import consultas as query

def jugador_solicitarDatos():
    nombre = input("Nombre del jugador: ")
    dineroBanco = input("Dinero recibido del banco: ")
    dineroComercios = input("Dinero obtenido de comercios: ")
    ficha = input("Ficha del jugador: ")
    return nombre,dineroBanco,dineroComercios,ficha

def jugador_insertar(conecctionP):
    nombreP,dineroBancoP,dineroComerciosP,fichaP = jugador_solicitarDatos()
    inser = "insert into Jugador (Nombre,dineroBanco,dineroComercios,ficha) values('"+ nombreP +"','"+ str(dineroBancoP) +"','"+ str(dineroComerciosP)+"','"+ fichaP +"')"
    conecctionP.execute(inser)
    print("Se ha registrado con éxito el jugador ")

def terreno_solicitarDatos():
    color = input("Color del terreno: ")
    tipo = input("Tipo del terreno: ")
    casas = input("Casas del terreno: ")
    hoteles = input("Hoteles del terreno: ")
    alquiler = input("Alquiler del terreno: ")
    return color,tipo,casas,hoteles,alquiler

def terreno_insertar(conecctionP):
    colorP,tipoP,casasP,hotelesP,alquilerP = terreno_solicitarDatos()
    inser = "insert into Terreno (Color,tipo,casas,hoteles,alquiler) values('"+ colorP +"','"+ tipoP +"','"+ str(casasP)+"','"+ str(hotelesP) +"','"+ str(alquilerP) +"')"
    conecctionP.execute(inser)
    print("Se ha registrado con éxito el terreno ")


def tarjeta_solicitarDatos():
    tipoTarjeta = input("Tipo de tarjeta: ")
    descripcion = input("Descripcion ")
    return tipoTarjeta, descripcion
def tarjeta_insertar(conecctionP):
    tipoTarjetaP, descripcionP = tarjeta_solicitarDatos()
    inser = "insert into Tarjeta (tipoTarjeta,descripcion) values('"+ tipoTarjetaP +"','"+ descripcionP +"')"
    conecctionP.execute(inser)
    print("Se ha registrado con éxito la tarjeta ")

def ventaCompra_solicitarDatos(conecctionP,tipoRegistroP):
    jugador = input("Ingresar jugador: ").lower()
    terreno = input("Ingresar terreno vendido: ").lower()
    id_jugador = query.jugador_obtenerCodigo(conecctionP,jugador)
    
    id_terreno = query.terreno_obtenerCodigo(conecctionP,terreno)
    turno = int(input("Turno que se realizó la "+tipoRegistroP+": "))
    return id_jugador,id_terreno,turno

def venta_insertar(conecctionP,id_banco=1):
    jugadorP,terrenoP,turnoP = ventaCompra_solicitarDatos(conecctionP,"venta")
    inser = "insert into venta (jugador,terreno,banco,turno) values('"+ str(jugadorP) +"','"+ str(terrenoP) +"','"+ str(id_banco) +"','"+ str(turnoP) +"')"
    conecctionP.execute(inser)
    print()
    print("Se ha registrado con éxito la venta")
    print()

def compra_insertar(conecctionP, id_banco=1):
    jugadorP,terrenoP,turnoP = ventaCompra_solicitarDatos(conecctionP,"compra")
    inser = "insert into compra (jugador,terreno,banco,turno) values('"+ str(jugadorP) +"','"+ str(terrenoP) +"','"+ str(id_banco) +"','"+ str(turnoP) +"')"
    conecctionP.execute(inser)
    print()
    print("Se ha registrado con éxito la compra")
    print()
