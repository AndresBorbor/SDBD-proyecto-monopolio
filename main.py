from sqlalchemy import create_engine, Table, MetaData,select
import pymysql

def menu():
    engine = create_engine('mysql+pymysql://root:1234@127.0.0.1:3306/prueba')
    conecction = engine.connect()
    muletilla = True
    while(muletilla):
        print("Bienvenido a la base de monopoly")
        print("1. Administrar Jugador")
        print("2. Administrar Terreno")
        print("3. Administrar Tarjeta")
        print("4. Administrar Banco")
        print("5. Salir\n")
        try:
            opcion = int(input("Opción elegida: "))
        
            if(opcion == 1):
                menuJugador(conecction)
            elif(opcion ==2):
                menuTerreno(conecction)
            elif(opcion ==3):
                menuTarjeta(conecction)
            elif(opcion == 4):
                menuBanco(conecction)
            elif(opcion == 5):
                print("Hasta luego!")
                conecction.close()
                muletilla = False
        except:
            print("Ingrese correctamente el dato requerido")
            print()





#FUNCION DE CONSULTA
def consultarDineroJugador(nombreJugadorP,dineroP, conecctionP):
    resultado = seleccionDineroJugador(nombreJugadorP, dineroP,conecctionP)
    imprimirDinero(resultado, dineroP)

#METODO QUE IMPRIME LA CONSULTA DEL DINERO DEPENDIENDO DE SI HAY O NO MÁS DE UN JUGADOR CON EL MISMO NOMBRE
def imprimirDinero(resultsP,dineroP):
    if len(resultsP) == 1:
        imprimirTipoDinero(dineroP,resultsP[0])
    else:
        ficha = str(input('Existen más de un jugador con el mismo nombre, por favor ingrese la ficha del jugador que quiere consultar').lower())
        for tp in resultsP:
            tupla = tp
            if tupla[1].lower() == ficha:
                imprimirTipoDinero(dineroP,tupla)
    
        
#METODO PARA IMRPRIMIR SEGUN EL TIPO DE DINERO QUE QUIERA CONSULTAR DE JUGADOR
def imprimirTipoDinero(dineroP,tuplaP):
    if(dineroP == "dinero"):
        print("EL jugador {:}, con la ficha {:} tiene {:} dólares".format(tuplaP[0],tuplaP[1],tuplaP[2]))
    elif(dineroP == "dineroBanco"):
        print("EL jugador {:}, con la ficha {:} ha recibido {:}3 dólares del banco".format(tuplaP[0],tuplaP[1],tuplaP[2]))
    else:
        print("EL jugador {:}, con la ficha {:} ha generado {:} dólares de comercios".format(tuplaP[0],tuplaP[1],tuplaP[2]))
    print()

#FUNCION QUE GENERA EL STRING PARA LA CONSULTA Y DEVUELVE LA LISTA DE TUPLAS DE REGISTROS
def seleccionDineroJugador(nombreJugadorP,dineroP,conecctionP):
    selec = "select nombre, ficha,"+dineroP+ " from jugador where nombre = '"+ nombreJugadorP + "'"
    results = conecctionP.execute(selec).fetchmany(size=100)
    return results

def menuJugador(conecctionP):
    muletilla = True
    while(muletilla):
        print("ADMINISTRAR JUGADORES")
        print("1. Consultar las propiedades de un jugador")
        print("2. Consultar el dinero que un jugador ha recibido del banco")
        print("3. Consultar el dinero que un jugador ha obtenido de comercios")
        print("4. Consultar el dinero total que tiene un jugador")
        print("5. Salir\n")

        opcion = int(input("Opcion elegida: "))
        if(opcion == 1):
            print()
        elif(opcion == 2):
            nombre = input("Ingrese el nombre del jugador: ").capitalize()
            print()
            consultarDineroJugador(nombre,"dineroBanco",conecctionP)
        elif(opcion == 3):
            nombre = input("Ingrese el nombre del jugador: ").capitalize()
            print()
            consultarDineroJugador(nombre,"dineroComercio",conecctionP)
        elif(opcion == 4):
            nombre = input("Ingrese el nombre del jugador: ").capitalize()
            print()
            consultarDineroJugador(nombre,"dinero",conecctionP)
        else:
            menu()
        respuesta = input("Desea realizar otra consulta? Si/No: ").lower()
        if(respuesta == "no"):
            break
            
def menuTarjeta(conecctionP):
    print("1. accion")
    print("3. Volver al menu principal")
    opcion = str(input("Opcion elegida: "))

    print()
    if(opcion == 1):
        print()
    elif(opcion==3):
        menu()
def seleccionTerreno(columnaConsultaP,valorRegistroP,conecctionP,colorP=""):
    selec = "select nombre, ficha,"+columnaConsultaP+ " from jugador where nombre = '"+ valorRegistroP + "'"
    results = conecctionP.execute(selec).fetchmany(size=100)
    return results

def menuBanco(conecctionP):
    print()

def menuTerreno(conecctionP):
    print()

menu()