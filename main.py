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

def menuBanco(conecctionP):
    print()

def menuTerreno(conecctionP):
    print("1. Consultar terrenos disponibles para comprar")
    print("2. Consultar terrenos no disponibles para comprar")
    print("3. Volver al menu principal")
    opcion = int(input("Opcion elegida: "))

    print()
    if(opcion == 1):
        query.terreno_consultarDisponibles(conecctionP)
    elif(opcion == 2):
        print()
    elif(opcion==3):
        menu()

menu()
