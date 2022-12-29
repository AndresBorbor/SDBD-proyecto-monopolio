#CONSULTAS JUGADORES

#consultas dinero
'''
la validacion de cuando son mas de un resultado y debe pedirse la ficha puede hacerse en una funcion, para reutilizarlo en otras tablas
'''
def jugador_consultaDinero(conecctionP,nombreP,dineroP):
    #FORMATO DE IMPRESION DEPENDIENDO LA CONSULTA
    print("-"*60)
    if(dineroP== "dineroTotal"):
        print("|{:^58}|".format("DINERO TOTAL DE "+nombreP))
    elif(dineroP == "dineroBanco"):
        print("|{:^58}|".format("DINERO RECIBIDO POR EL BANCO DE "+nombreP))
    else:
        print("|{:^58}|".format("DINERO OBTENIDO DE COMERCIOS DE "+nombreP))

    print("-"*60)
    print("|{:<19}|{:<19}|{:<18}|".format("NOMBRE","FICHA","DINERO"))
    print("-"*60)

    tupla = jugador_selectDinero(conecctionP,nombreP,dineroP)
    jugador_imprimirDinero(tupla)

def jugador_selectDinero(conecctionP, nombreP,dineroP):

    if(dineroP == "dineroTotal"):
        selec = "select nombre, ficha,(dineroBanco+dineroComercios) as Dinero_Total from jugador where nombre = '"+ nombreP +"'"
        
    else:
        selec = "select nombre, ficha,"+dineroP+ " from jugador where nombre = '"+ nombreP + "'"
    results = conecctionP.execute(selec).fetchmany(size = 100)

    if len(results) >1:
        ficha = str(input('Existen más de un jugador con el mismo nombre, por favor ingrese la ficha del jugador que quiere consultar').lower())
        for tp in results:
            if tp[1].lower() == ficha:
                return tp
    return results[0]

def jugador_imprimirDinero(tuplaP):
    print("|{:<19}|{:<19}|{:<18}|".format(tuplaP[0],tuplaP[1],tuplaP[2]))
    print("-"*60)

#consultas propiedades
def jugador_consultaPropiedad(conecctionP,nombreP,dineroP):
    print("implementar codigo")

def jugador_selectPropiedad(conecctionP,nombre,dineroP):
    print("implementar codigo")

def jugador_imprimirDinero(tuplaP):
    print("implementar codigo")