def eliminarJugador(conecctionP,cod):
    delete = "delete from Jugador where id_jugador = "+str(cod)+""
    conecctionP.execute(delete)
    print()
    print("se ejecuto correctamente")

def eliminarCompra(conecctionP,cod):
    delete = "delete from compra where id_compra = "+str(cod)+""
    conecctionP.execute(delete)
    print()
    print("se ejecuto correctamente")