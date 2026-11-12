from flask import Flask, request

app = Flask(__name__)

jugadores = [
    {"id": 1, "nombre": "Paolo Guerrero", "edad": 41, "posicion": "Delantero", "equipo": "Alianza Lima", "seleccion": "Perú"},
    {"id": 2, "nombre": "André Carrillo", "edad": 33, "posicion": "Extremo", "equipo": "Al Hilal", "seleccion": "Perú"},
    {"id": 3, "nombre": "Renato Tapia", "edad": 29, "posicion": "Mediocampista", "equipo": "Leganés", "seleccion": "Perú"},
    {"id": 4, "nombre": "Lionel Messi", "edad": 38, "posicion": "Delantero", "equipo": "Inter Miami", "seleccion": "Argentina"},
    {"id": 5, "nombre": "Vinícius Jr", "edad": 25, "posicion": "Extremo", "equipo": "Real Madrid", "seleccion": "Brasil"},
    {"id": 6, "nombre": "Cristiano Ronaldo", "edad": 41, "posicion": "Delantero", "equipo": "Al Nassr", "seleccion": "Portugal"},
    {"id": 7, "nombre": "Kylian Mbappé", "edad": 27, "posicion": "Delantero", "equipo": "Real Madrid", "seleccion": "Francia"},
    {"id": 8, "nombre": "Erling Haaland", "edad": 26, "posicion": "Delantero", "equipo": "Manchester City", "seleccion": "Noruega"},
    {"id": 9, "nombre": "Jude Bellingham", "edad": 23, "posicion": "Mediocampista", "equipo": "Real Madrid", "seleccion": "Inglaterra"},
    {"id": 10, "nombre": "Luka Modrić", "edad": 41, "posicion": "Mediocampista", "equipo": "AC Milan", "seleccion": "Croacia"},
    {"id": 11, "nombre": "Neymar Jr", "edad": 34, "posicion": "Extremo", "equipo": "Santos", "seleccion": "Brasil"},
    {"id": 12, "nombre": "Robert Lewandowski", "edad": 38, "posicion": "Delantero", "equipo": "Barcelona", "seleccion": "Polonia"},
    {"id": 13, "nombre": "Mohamed Salah", "edad": 34, "posicion": "Extremo", "equipo": "Liverpool", "seleccion": "Egipto"},
    {"id": 14, "nombre": "Kevin De Bruyne", "edad": 35, "posicion": "Mediocampista", "equipo": "Napoli", "seleccion": "Bélgica"},
    {"id": 15, "nombre": "Harry Kane", "edad": 33, "posicion": "Delantero", "equipo": "Bayern Múnich", "seleccion": "Inglaterra"},
    {"id": 16, "nombre": "Rodri", "edad": 30, "posicion": "Mediocampista", "equipo": "Manchester City", "seleccion": "España"},
    {"id": 17, "nombre": "Federico Valverde", "edad": 28, "posicion": "Mediocampista", "equipo": "Real Madrid", "seleccion": "Uruguay"},
    {"id": 18, "nombre": "Lautaro Martínez", "edad": 29, "posicion": "Delantero", "equipo": "Inter de Milán", "seleccion": "Argentina"},
    {"id": 19, "nombre": "Virgil van Dijk", "edad": 35, "posicion": "Defensa", "equipo": "Liverpool", "seleccion": "Países Bajos"},
    {"id": 20, "nombre": "Alisson Becker", "edad": 33, "posicion": "Portero", "equipo": "Liverpool", "seleccion": "Brasil"},
]

@app.route("/api/v1/jugadores", methods =["GET"])
def todos_jugadores():
    return {
        "msg": "Resultado exitoso",
        "data": jugadores
    }

#RETO 01
#Crear el endpoint jugador/<id>
#un unico jugador traerá
#si id no existe mensaje de error

@app.route("/api/v1/jugador/<int:id>", methods=["GET"])
def jugador_id(id):
    jugador_encontrado = []
    for jugador in jugadores:
        if jugador["id"] == id:
            jugador_encontrado = jugador
            break
    if jugador_encontrado:
        return {
            "msg": "exito",
            "jugador": jugador_encontrado
        }
    else:
        return {
                "msg": "fail"
                }, 400


#POST - Insertar datos
#Se debe crear un endpoint llamado /api/v1/registrar
#este endpoint debe leer los datos que recibe
#debe insertar estos datos dentro de nuestro arreglo de jugadores

@app.route("/api/v1/registrar", methods=["POST"])
def registrar_jugador():
    #Siempre que te encuentres en un POST
    #debes de capturar el body que te envía el cliente
    #Para capturar la información tu usas el request
    # from flask import request
    informacion_recibida = request.json
    jugadores.append(informacion_recibida)
    return {
        "msg": "Registro exitoso"
    }, 201

#PUT: endponit para actualizar con id

@app.route("/api/v1/actualizar/<int:id>", methods=["PUT"])
def actualizar_jugador(id):
    for jugador in jugadores:
        if jugador["id"] == id:
            #Aquí vendrá nuestra lógica para actualizar sus datos del jugador
            datos_recibidos = request.json
            # {
            #     "nombre": "Paolin",
            #     "equipo": "UCV"
            # }
            for campo in datos_recibidos:
                if campo in jugador:
                    jugador[campo] = datos_recibidos[campo]

    return {
        "msg": "Actualización completa"
    }, 200

#DELETE
#Se solicita que se tenga el endpoint api/v1/eliminar
#debe permitir eliminar un jugador

@app.route("/api/v1/eliminar/<int:id>", methods=["DELETE"])
def eliminar_jugador(id):
    for jugador in jugadores:
        if jugador["id"] == id:
            jugadores.remove(jugador)
    return{
        "msg": "jugador eliminado exiosamente"
    }, 200
    

app.run()