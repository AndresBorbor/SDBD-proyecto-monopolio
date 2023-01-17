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
    
 def eliminarTerreno(conecctionP,cod):
    delete = "delete from terreno where id_terreno = "+str(cod)+""
    conecctionP.execute(delete)
    print()
    print("se ejecuto correctamente")    

def eliminarTarjeta(conecctionP,cod):
    delete = "call sp_eliminarTarjeta("+str(cod)+")" 
    conecctionP.execute(delete)
    print()
    print("se ejecuto correctamente")  
