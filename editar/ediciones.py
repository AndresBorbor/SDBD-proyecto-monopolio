def nombreJugador(conecctionP,nombre, id):

    edit = " update Jugador set nombre = '"+nombre+"' where  id_jugador = "+ str(id)+""
    conecctionP.execute(edit)
    print("se ejecuto correctamente")

def dineroBnaco(conecctionP,dinero, id):

    edit = "update Jugador set dineroBanco = '"+str(dinero)+"' where  id_jugador = "+ str(id)+""
    conecctionP.execute(edit)
    print()
    print("se ejecuto correctamente")


def dineroComercios(conecctionP, dinero, id):
    edit = "update Jugador set dineroComercios = '"+str(dinero)+"' where  id_jugador = "+ str(id)+""
    conecctionP.execute(edit)
    print()
    print("se ejecuto correctamente")

def dineroTotal(conecctionP, dinero, id):
    edit = "update Jugador set dineroTotal = '"+str(dinero)+"' where  id_jugador = "+ str(id)+""
    conecctionP.execute(edit)
    print()
    print("se ejecuto correctamente")

def agregar_casas(conecctionP, casas,id):
    edit = "update terreno set casas = "+str(casas)+" where id_terreno = "+str(id)+""
    conecctionP.execute(edit)
    print()
    print("se ejecuto correctamente")