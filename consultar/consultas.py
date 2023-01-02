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

#CONSULTAS TERRENOS

#consultar terrenos disponibles
def terreno_consultarDisponibles(conecctionP):
    resultado = terreno_seleccionDisponibles(conecctionP)
    terreno_imprimirTerrenos(resultado)

def terreno_seleccionDisponibles(conecctionP):
    selec_terrenosSeguros = "select * from terreno t where t.id_terreno not in(select terreno from compra join venta using(terreno))"
    results_terrenosSeguros = conecctionP.execute(selec_terrenosSeguros).fetchmany(size = 100)
    
    selec_terrenosDuda = "select * from terreno t where t.id_terreno in (select terreno from Compra)"
    results_terrenosDuda = conecctionP.execute(selec_terrenosDuda).fetchmany(size = 100)
   
    listaIdTerrenos = []
    for terreno in results_terrenosSeguros:
        listaIdTerrenos.append(terreno[0])
    
    listaIdTerrenosDuda = []
    for terreno in results_terrenosDuda:
        listaIdTerrenosDuda.append(terreno[0])
     
    listaIds = terreno_buscarDisponibilidad(conecctionP, listaIdTerrenos,listaIdTerrenosDuda)
    resultadoFinal = terreno_seleccionarLista(conecctionP, listaIds)

    return resultadoFinal

#funciones compartidas de terrenos
def terreno_buscarDisponibilidad(conecctionP,idTerrenosSegurosP, idTerrenosDudaP,disponibilidad=True):
    idTerrenos = idTerrenosSegurosP.copy()
    for id in idTerrenosDudaP:
        if(idTerrenosDudaP not in idTerrenosSegurosP):
            if(disponibilidad):
                selec_ultimaCompra = "select max(turno) as ultima_compra from compra c where terreno = '"+ str(id) +"'"
                selec_ultimaVenta = "select max(turno) as ultima_venta from venta v where terreno = '"+ str(id) +"'"
            else:
                selec_ultimaCompra = "select max(turno) as ultima_venta from venta v where terreno = '"+ str(id) +"'"
                selec_ultimaVenta = "select max(turno) as ultima_compra from compra c where terreno = '"+ str(id) +"'"

            tupla_ultimaCompra = conecctionP.execute(selec_ultimaCompra).fetchmany(size = 100)[0]
            tupla_ultimaVenta = conecctionP.execute(selec_ultimaVenta).fetchmany(size = 100)[0]

            turno_ultimaCompra, turno_ultimaVenta = 0,0
            
            if(type(tupla_ultimaCompra[0])==int): turno_ultimaCompra = tupla_ultimaCompra[0]
            if(type(tupla_ultimaVenta[0])==int): turno_ultimaVenta = tupla_ultimaVenta[0]
            if (turno_ultimaCompra < turno_ultimaVenta and id not in idTerrenos): idTerrenos.append(id)
    return idTerrenos

def terreno_imprimirTerrenos(resultsP,disponibilidad = ""):
    print("-"*49)
    print("|{:^47}|".format("TERRENOS "+disponibilidad+"DISPONIBLES PARA COMPRA"))
    print("-"*49)
    print("|{:<11}|{:<11}|{:<11}|{:<11}|".format("id_terreno", "color" , "tipo", "alquiler"))
    print("-"*49)
    for tupla in resultsP:
        id_terreno = tupla[0]
        color_terreno = tupla[1]
        tipo_terreno = tupla[2]
        alquiler_terreno = tupla[3]
        print("|{:<11}|{:<11}|{:<11}|{:<11}|".format(id_terreno,color_terreno,tipo_terreno,alquiler_terreno))
        print("-"*49)
    print()

def terreno_seleccionarLista(conecctionP, listaIdsP):
    result = []
    for id in listaIdsP:
        selec = "select id_terreno, color, tipo, alquiler from terreno where id_terreno = '"+ str(id) +"'"
        tupla = conecctionP.execute(selec).fetchmany(size=100)[0]
        result.append(tupla)
    return result

#consultar terrenos no disponibles
def terreno_consultarNoDisponibles(conecctionP):
    resultado = terreno_seleccionNoDisponibles(conecctionP)
    terreno_imprimirTerrenos(resultado, "NO")

def terreno_seleccionNoDisponibles(conecctionP):
    selec_terrenosSeguros = "select * from terreno t where t.id_terreno in (select terreno from Compra join Venta using(terreno))"
    results_terrenosSeguros = conecctionP.execute(selec_terrenosSeguros).fetchmany(size = 100)
    selec_terrenosDuda = "select * from terreno t where t.id_terreno in (select terreno from Venta)"
    results_terrenosDuda = conecctionP.execute(selec_terrenosDuda).fetchmany(size = 100)
   
    listaIdTerrenos = []
    for terreno in results_terrenosSeguros:
        listaIdTerrenos.append(terreno[0])
    
    listaIdTerrenosDuda = []
    for terreno in results_terrenosDuda:
        listaIdTerrenosDuda.append(terreno[0])

    listaIds = terreno_buscarDisponibilidad(conecctionP, listaIdTerrenos, listaIdTerrenosDuda, False)
    resultadoFinal = terreno_seleccionarLista(conecctionP, listaIds)

    return resultadoFinal


#CONSULTAS TARJETAS
#consultas tarjetas que han sido tomadas
def tarjeta_consultarTomadas(conecctionP):
    results = tarjeta_seleccionTomadas(conecctionP)
    tarjeta_imprimirTarjetas(results)

def tarjeta_seleccionTomadas(conecctionP):
    selec = "select * from Tarjeta where id_tarjeta in (select tarjeta from tarjeta_jugador)"
    results = conecctionP.execute(selec).fetchmany(size = 100)
    return results

def tarjeta_imprimirTarjetas(resultsP, estado="TOMADAS"):
    print("-"*74)
    print("|{:^72}|".format("TARJETAS "+estado))
    print("-"*74)
    print("|{:<15}|{:<15}|{:<40s}|".format("id_tarjeta", "tipo_tarjeta", "descripcion"))
    print("-"*74)
    for tupla in resultsP:
        id_tarjeta = tupla[0]
        tipo_tarjeta = tupla[1]
        descripcion = tupla[2]
        print("|{:<15}|{:<15}|{:<40}|".format(id_tarjeta,tipo_tarjeta,descripcion))
        print("-"*74)
    print()

#consultas tarjetas que no han sido tomadas
def tarjeta_consultarNoTomadas(conecctionP):
    results = tarjeta_seleccionNoTomadas(conecctionP)
    tarjeta_imprimirTarjetas(results, "NO TOMADAS")

def tarjeta_seleccionNoTomadas(conecctionP):
    selec = "select * from Tarjeta where id_tarjeta not in (select tarjeta from tarjeta_jugador)"
    results = conecctionP.execute(selec).fetchmany(size = 100)
    return results



#CONSULTAS BANCO