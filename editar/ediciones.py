def nombreJugador(conecctionP,nombre, id):
    edit = " update Jugador set nombre = '"+nombre+"' where  id_jugador = '"+ str(id)+"'"
    conecctionP.execute(edit).fetchmany(size =100)
    print("se ejecuto correctamente")

def dineroComercios(conecctionP, dinero, id):
    edit = "update Jugador set dineroComercios = '"+str(dinero)+"' where  id_jugador = '"+ str(id)+"'"
    conecctionP.execute(edit).fetchmany(size =100)

def dineroTotal(conecctionP, dinero, id):
    edit = "update Jugador set dineroTotal = '"+str(dinero)+"' where  id_jugador = '"+ str(id)+"'"
    conecctionP.execute(edit).fetchmany(size =100)


