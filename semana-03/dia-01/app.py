#Desde la librería flask quiero importar la Clase Flask
from flask import Flask, request

app = Flask(__name__) #Se esta creando mi servidor

#Aquí vamos a crear nuestros endpoints
#Recuerda que estos deben ir encima de app.run()

#Necesitamos un endpoint en la raiz / que responda
#diciendo "Bienvenidos comensales"

jugadores = [
    {"id": 1, "nombre": "Paolo Guerrero", "edad": 41, "posicion": "Delantero", "equipo": "Alianza Lima", "seleccion": "Peru"},
    {"id": 2, "nombre": "Andre Carrillo", "edad": 33, "posicion": "Extremo", "equipo": "Al Hilal", "seleccion": "Peru"},
    {"id": 3, "nombre": "Renato Tapia", "edad": 29, "posicion": "Mediocampista", "equipo": "Leganes", "seleccion": "Peru"},
    {"id": 4, "nombre": "Lionel Messi", "edad": 38, "posicion": "Delantero", "equipo": "Inter Miami", "seleccion": "Argentina"},
    {"id": 5, "nombre": "Vinicius Jr", "edad": 25, "posicion": "Extremo", "equipo": "Real Madrid", "seleccion": "Brasil"},
    {"id": 6, "nombre": "Luis Diaz", "edad": 28, "posicion": "Extremo", "equipo": "Liverpool", "seleccion": "Colombia"},
    {"id": 7, "nombre": "Federico Valverde", "edad": 27, "posicion": "Mediocampista", "equipo": "Real Madrid", "seleccion": "Uruguay"},
    {"id": 8, "nombre": "Rodrygo", "edad": 25, "posicion": "Extremo", "equipo": "Real Madrid", "seleccion": "Brasil"},
    {"id": 9, "nombre": "Julian Alvarez", "edad": 26, "posicion": "Delantero", "equipo": "Manchester City", "seleccion": "Argentina"},
    {"id": 10, "nombre": "Christian Cueva", "edad": 33, "posicion": "Mediocampista", "equipo": "Cienciano", "seleccion": "Peru"},
]

@app.route("/") #que ruta vamos agregar
def saludar():
    return "Bienvenidos comensales"

#endpoint llamado /milanesa
#este debe de mostrar un print PREPARANDO
#y luego debe retornar MILANESA PREPARADA
@app.route("/milanesa")
def preparar_milanesa():
    return {
        "msg": "La milanesa está preparada",
        "author": "El chef"
    }

#Necesitamos un Endpoint llamado "/jugadores·"
#el cual debe retornar a todos los jugadores mayores a 28
@app.route("/jugadores")
def jugadores_mayores():
    jugadores_adultos = []
    for jugador in jugadores:
        if jugador["edad"] >= 28:
            jugadores_adultos.append(jugador)
    return {
        "msg": "Los jugadores mayores de 28 años son",
        "resultado": jugadores_adultos
    }

#retornar mediocampistas
@app.route("/mediocampistas")
def medios_peruanos():

    jugadores_medios_peruanos = []
    for jugador in jugadores:
        if jugador["seleccion"] == "Peru" and jugador["posicion"] == "Mediocampista":
            jugadores_medios_peruanos.append(jugador)
    return {
            "msg": "Los jugadores mediocampistas son",
            "resultado": jugadores_medios_peruanos
        }

#se desea implementar los argumentos dinamicos
#si el usuario busca /jugador/1
#se debe retornar el jugador con el id = 1

@app.route("/jugador/<int:id>")
def obtener_jugador(id):
    jugador_encontrado = []
    for jugador in jugadores:
        if jugador["id"] == id:
            jugador_encontrado = jugador
            break
    return{
        "msg": "Encontramos al jugador",
        "data": jugador_encontrado
    }

#TRABAJANDO CON PARAMS

@app.route("/buscador")
def buscador_jugadores():
    #para trabajar con las query params
    #debes importar el request de flask
    #solcitud
    #from flask import request
    #/buscador?posicion=Mediocampista
    posicion_query = request.args.get("posicion")
    jugadores_filtrados = []
    for jugador in jugadores:
        if jugador["posicion"].lower() == posicion_query.lower():
            jugadores_filtrados.append(jugador)
    
    return{
        "msg": "Resultado exitoso",
        "data": jugadores_filtrados
    }


app.run()