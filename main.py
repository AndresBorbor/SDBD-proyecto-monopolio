from sqlalchemy import create_engine, Table, MetaData,select,insert
import pymysql
from insertar import inserciones as insert
from editar import ediciones as edit
from eliminar import eliminaciones as delete
from consultar import consultas as query

def menu():
    engine = create_engine('mysql+pymysql://root:1234@127.0.0.1:3306/BD_Monopoly')
    conecction = engine.connect()
    banderilla = True
    while(banderilla):
        
        print("Bienvenido a la base de monopoly")
        print("1. Administrar Jugador")
        print("2. Administrar Terreno")
        print("3. Administrar Tarjeta")
        print("4. Administrar Banco")
        print("5. Ingresar el lanzamiento: ")
        print("6. Salir\n")
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
                query.consultar_Jugadores(conecction)
                insert.lanzamiento_pedirDatos(conecction)
            elif(opcion == 6):
                print("Hasta luego!")
                conecction.close()
                banderilla = False
        except Exception as ex:
           
            print(ex)


def menuJugador(conecctionP):
    banderilla = True
    while(banderilla):
        print("ADMINISTRAR JUGADORES")
        opcion= obtenerOpcion()
        if(opcion == 1):
            menuJugadorInsertar(conecctionP)
        elif(opcion==2):
            menuJugadorConsultar(conecctionP)
        elif(opcion==3):
            menuActualizacionesJugador(conecctionP)
        elif(opcion==4):
            menuEliminarJugador(conecctionP)
        else:
            banderilla = False
    
def menuTerreno(conecctionP):
    banderilla = True
    while(banderilla):
        print("ADMINISTRAR TERRENOS")
        opcion = obtenerOpcion()
        if(opcion == 1):
            menuTerrenoInsertar(conecctionP)
        elif(opcion==2):
            menuTerrenoConsultar(conecctionP)
        elif(opcion==3):
            menutTerrenoEditar(conecctionP)
        elif(opcion==4):
            menuTerrenoEliminar(conecctionP)
        else:
            banderilla = False

def menuTerrenoEliminar(conecctionP):
    query.consultar_tereno(conecctionP)
    id = int(input("ingrese el id del terreno: "))
    delete.eliminarTerreno(conecctionP,id)
    
    
def menuTarjeta(conecctionP):
    banderilla = True
    while(banderilla):
        print("ADMINISTRAR TARJETAS")
        opcion = obtenerOpcion()
        if(opcion == 1):
            menuTarjetaInsertar(conecctionP)
        elif(opcion == 2):
            menuTarjetaConsultar(conecctionP)
        elif(opcion == 3):
            menuEditarTarjeta(conecctionP)
        elif(opcion == 4):
            menuEliminarTarjeta(conecctionP)
        else:
            banderilla = False
            
def menuEliminarTarjeta(conecctionP):
    print("---------MENU ELIMINAR--------------")
    cod = int(input("ingrese el id de la tarjeta a eliminar: "))
    delete.eliminarTarjeta(conecctionP,cod)
    
def menuEditarTarjeta(conecctionP):
    print("----------MENU EDITAR--------------")
    print("Edite la descripcion de la tarjeta")
    desc = input("ingrese la descripcion a editar: ")
    id = int(input("ingrese el id de la tarjeta: "))
    
    edit.editarTarjeta(conecctionP,desc,id)

def menuBanco(conecctionP):
    print("---------MENU BANCO ---------------")
    print("En esta opcion solo se podra editar el nombre de la transaccion")
    desc = input("ingrese el nombre de la transaccion: ")
    id = int(input("ingrese el id del banco: "))
    
    edit.editarBanco(conecctionP,desc,id)
        
def menuJugadorInsertar(conecctionP):
    respuesta = "si"
    while(respuesta != "no"):
        insert.jugador_insertar(conecctionP)
        respuesta = input("Desea ingresar otro registro? Si/No: ").lower()
   
def menuJugadorConsultar(conecctionP):
    respuesta = "si"
    while(respuesta!="no"):

        print("1. Consultar las propiedades de un jugador")
        print("2. Consultar el dinero que un jugador ha recibido del banco")
        print("3. Consultar el dinero que un jugador ha obtenido de comercios")
        print("4. Consultar el dinero total que tiene un jugador")
        print("5. Salir\n")

        opcion = int(input("Opcion elegida: "))
        if(opcion == 1):
            result = conecctionP.execute(query.jugador_spConsultarPropiedades(conecctionP,"karen"))
            for row in result:
                print(row)
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
            respuesta = "no"
        respuesta = input("Desea realizar otra consulta? Si/No: ").lower()

def menuActualizacionesJugador(conectionP):
    print("--------MENU EDICIONES----------")
    print("elija una opcion")
    print("1 editar nombre")
    print("2 editar dinero de comercios")
    print("3 editar dinero del banco")
    print("4 editar dinero total")

    opcion = int(input("Opcion elegida "))

    if opcion == 1:
        query.consultar_Jugadores(conectionP)
        print()
        id = int(input("ingrese el id del jugador que desea editar  "))
        nombre = input("ingrese el nombre a editar ")
        edit.nombreJugador(conectionP,nombre, id)   
    elif opcion ==2: 
        query.consultar_Jugadores(conectionP)
        print()
        id = int(input("ingrese el id del jugador que desea actualizar"))
        dinero = int(input("Ingrese el valor del dinero "))
        edit.dineroComercios(conectionP,dinero, id)
    elif opcion == 3:
        query.consultar_Jugadores(conectionP)
        print()
        id = int(input("ingrese el id del jugador que desea actualizar "))
        dinero = int(input("Ingrese el valor del dinero "))
        edit.dineroBnaco(conectionP,dinero, id)
    elif opcion == 4:
        query.consultar_Jugadores(conectionP)
        print()
        id = int(input("ingrese el id del jugador que desea actualizar "))
        dinero = int(input("Ingrese el valor del dinero "))
        edit.dineroTotal(conectionP,dinero, id)
    

def menuEliminarJugador(conectionP):
    print("--------MENU Eliminaciones----------")
    print()
    query.consultar_Jugadores(conectionP)
    print()
    jugador = input("ingrese el nombre del jugador a eliminar ")
    delete.eliminarJugador(conectionP,jugador)

def menuTerrenoInsertar(conecctionP):
    respuesta = "si"
    while(respuesta != "no"):
        insert.terreno_insertar(conecctionP)
        respuesta = input("Desea ingresar otro registro? Si/No: ").lower()
    
def menuTerrenoConsultar(conecctionP):
    print("1. Consultar terrenos disponibles para comprar")
    print("2. Consultar terrenos no disponibles para comprar")
    print("3. Volver al menu principal")
    opcion = int(input("Opcion elegida: "))
    respuesta = "si"
    while(respuesta != "no"):
        if(opcion == 1):
            query.terreno_consultarDisponibles(conecctionP)
        elif(opcion == 2):
            query.terreno_consultarNoDisponibles(conecctionP)
        elif(opcion==3):
            respuesta = "no"
        respuesta = input("Desea realizar otra consulta? Si/No: ").lower()

def menutTerrenoEditar(conecctionP):
    print("------------- MENU EDITAR TERRENOS -----------------")
    print("1. editar numero de casas")
    print("2. editar numero de hoteles")
    print("3. editar costo de alquiler")
    opcion = int(input("Opcion elegida: "))

    if opcion == 1:
        query.consultar_tereno(conecctionP)
        print()
        id = int(input("ingrese el id del terreno a editar: "))
        casas = int(input("ingrese la cantidad de casas a agregar: "))
        edit.agregar_casas(conecctionP,casas,id)
    elif opcion == 2:
        query.consultar_tereno(conecctionP)
        print()
        


def menuTarjetaInsertar(conecctionP):
    respuesta = "si"
    while(respuesta != "no"):
        insert.tarjeta_insertar(conecctionP)
        respuesta = input("Desea realizar otro registro? Si/No: ").lower()

def menuTarjetaConsultar(conecctionP):
    respuesta = "si"
    while(respuesta != "no"):
        print("1. Consultar tarjetas que han sido tomadas")
        print("2. Consultar tarjetas aun no tomadas")
        print("3. Volver")
        opcion = int(input("Opcion elegida: "))
        print()

        if(opcion == 1):
            query.tarjeta_consultarTomadas(conecctionP)
        elif(opcion == 2):
            query.tarjeta_consultarNoTomadas(conecctionP)
        else:
            respuesta = "no"
        respuesta = input("Desea realizar otro registro? Si/No: ")
  
def obtenerOpcion():
    print("1. Insertar registro")
    print("2. Consultar registro")
    print("3. Editar registro")
    print("4. Eliminar registro")
    print("5. Salir")
    print()
    return int(input("Opcion elegida: "))

menu()
