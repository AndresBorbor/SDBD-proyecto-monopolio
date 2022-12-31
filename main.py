from sqlalchemy import create_engine, Table, MetaData,select
import pymysql
from insertar import inserciones as insert
from editar import ediciones as edit
from eliminar import eliminaciones as delete
from consultar import consultas as query

def menu():
    engine = create_engine('mysql+pymysql://root:1234@127.0.0.1:3306/BD_Monopoly')
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
            nombre = input("Ingrese el nombre del jugador: ").capitalize()
            print()
            query.jugador_consultarPropiedad(conecctionP,nombre)
        elif(opcion == 2):
            nombre = input("Ingrese el nombre del jugador: ").capitalize()
            print()
            query.jugador_consultaDinero(conecctionP, nombre, "dineroBanco")
        elif(opcion == 3):
            nombre = input("Ingrese el nombre del jugador: ").capitalize()
            print()
            query.jugador_consultaDinero(conecctionP, nombre, "dineroComercios")
        elif(opcion == 4):
            nombre = input("Ingrese el nombre del jugador: ").capitalize()
            print()
            query.jugador_consultaDinero(conecctionP, nombre, "dineroTotal")
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
    elif(opcion == 2):
        print()
    elif(opcion==3):
        menu()
#FUNCION PARA SELECCIONAR TERRENO
def seleccionTerrenosDisponibles(conecctionP):
    selec = "select distinct(id_terreno),color,tipo,alquiler from Terreno,Venta where Venta.terreno = Terreno.id_terreno and tipo = 'propiedad' order by id_terreno"
    results = conecctionP.execute(selec).fetchmany(size=100)
    return results
#FUNCION PARA IMPRIMIR TERRENOS
def imprimirTerrenos(resultsP):
    print("-"*49)
    print("|{:^47}|".format("TERRENOS DISPONIBLES PARA COMPRA"))
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
#CONSULTA DE TERRENOS
def consultarTerrenosDisponibles(conecctionP):
    resultado = seleccionTerrenosDisponibles(conecctionP)
    imprimirTerrenos(resultado)

def menuBanco(conecctionP):
    print()

def menuTerreno(conecctionP):
    print("1. Consultar terrenos disponibles para comprar")
    print("2. Consultar terrenos no disponibles para comprar")
    print("3. Volver al menu principal")
    opcion = int(input("Opcion elegida: "))

    print()
    if(opcion == 1):
        consultarTerrenosDisponibles(conecctionP)
    elif(opcion == 2):
        print()
    elif(opcion==3):
        menu()

menu()
