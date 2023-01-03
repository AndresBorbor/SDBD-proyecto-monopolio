from consultar import consultas as query

def eliminarJugador(conecctionP,nombre):
    cod = query.jugador_obtenerCodigo(nombre)
    eliminarLanzamiento(conecctionP,cod)
    eliminartarjetaJugador(conecctionP,cod)
    eliminarCompra(conecctionP,cod)
    eliminarVenta(conecctionP,cod)
    delete= "  delete from Jugador where id_jugador = '"+str(cod)+"'"
    conecctionP.execute(delete).fetchmany(size =100)
    print("se ejecuto correctamente")

def eliminarLanzamiento(conecctionP,cod):
    delete= "  delete from Lanzamiento where jugador = '"+str(cod)+"'"
    conecctionP.execute(delete).fetchmany(size =100)

def eliminartarjetaJugador(conecctionP,cod):
    delete= "  delete from tarjeta_jugador where jugador = '"+str(cod)+"'"
    conecctionP.execute(delete).fetchmany(size =100)

def eliminarVenta(conecctionP,cod):
    delete= "  delete from venta where jugador = '"+str(cod)+"'"
    conecctionP.execute(delete).fetchmany(size =100)

def eliminarCompra(conecctionP,cod):
    delete= "  delete from venta where jugador = '"+str(cod)+"'"
    conecctionP.execute(delete).fetchmany(size =100)  
