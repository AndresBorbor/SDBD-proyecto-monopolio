#CONSULTAS JUGADORES

#consultas dinero
'''
la validacion de cuando son mas de un resultado y debe pedirse 
la ficha puede hacerse en una funcion, para reutilizarlo en otras tablas
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


#consultar propiedades
'''
Revisar linea 63
'''
def jugador_consultarPropiedad(conecctionP, nombreP):
    print("-"*60)
    print("|{:^58}|".format("PROPIEDADES DE "+ nombreP))
    print("-"*60)
    print("|{:<13}|{:<14}|{:<14}|{:<14}|".format("ID","COLOR","TIPO","ALQUILER"))
    print("-"*60)
    propiedades = jugador_selectPropiedad(conecctionP,nombreP)
    for tupla in propiedades:
        jugador_imprimirPropiedades(tupla)

def jugador_selectPropiedad(conecctionP, nombreP):
    codigosPropiedades = jugador_obtenerCodigoPropiedad(conecctionP, nombreP)
    propiedades = []
    #reemplazar alquiler por nombre cuando se lo agregue
    selec = "select id_terreno,color,tipo,alquiler from Terreno"
    
    results = conecctionP.execute(selec).fetchmany(size = 100)
    for tupla in results:
        codigoTer = tupla[0]
        for tupla_codigos in codigosPropiedades:
            if codigoTer == tupla_codigos[2]:
                propiedades.append(tupla)
    return propiedades
        
def jugador_obtenerCodigoPropiedad(conecctionP,nombreP):
    tupla_jugador = jugador_obtenerJugadorPropiedad(conecctionP,nombreP)
    #Seleccionar todos los terrenos registrados en compras que no se hayan vendido
    id_j = tupla_jugador[0]
    selec = "select c.id_compra, c.jugador,c.terreno from Compra c where terreno not in (select v.terreno from Venta v where v.jugador = c.jugador) and c.jugador = '"+ str(id_j) +"'"
    results = conecctionP.execute(selec).fetchmany(size =100)
    return results

def jugador_obtenerJugadorPropiedad(conecctionP, nombreP):
    selec = "select id_jugador,Nombre,ficha from Jugador where Nombre = '"+ nombreP +"'"
    result = conecctionP.execute(selec).fetchmany(size = 100)
    
    if len(result)>1:
        fichaP = str(input('Existen más de un jugador con el mismo nombre, por favor ingrese la ficha del jugador que quiere consultar').lower())
        for tupla in result:
            ficha = tupla[2]
            if(ficha == fichaP):
                return tupla
    
    return result[0]

def jugador_imprimirPropiedades(tuplaP):

    print("|{:<13}|{:<14}|{:<14}|{:<14}|".format(tuplaP[0],tuplaP[1],tuplaP[2],tuplaP[3]))
    print("-"*60)