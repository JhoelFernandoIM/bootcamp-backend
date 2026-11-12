from flask import Flask, jsonify
import psycopg2

app = Flask(__name__) #la creación de tu servidor

#vamos a conectar nuestro servidor API con la bd
#debes tener instalado psycopg2 => PostgreSQL
# mysqlclient => MySQL

#pip install psycopg2

#CONEXION
#Vamos a crear un funcion paa poder conectarnos a nuestra BD

def get_db_conection():
    conexion = psycopg2.connect(
                        host='localhost',
                        database='canciones',
                        user='postgres',
                        password='root',
                        port='5432'
                    )
    return conexion

@app.route("/api/artistas", methods=["GET"])
def get_artistas():
    #01. conectar a la BD
    conn = get_db_conection() #Me conecto y guardo la conexion
    #02. Crear un cursor => Donde podemos ejecutar SQL
    cur = conn.cursor()
    #03. Vamos a ejecutar la consulta SQL
    cur.execute("SELECT * FROM artistas")
    #04. Guardar la respuesta
    filas = cur.fetchall()
    #05. vamos a cerrar el cursor y la conexion
    cur.close() #cierro el cursor
    conn.close()# cierro la conexion


    #06 Formateo
    resultados_transformados = []
    for elmt in filas:

        formato = {
            "id": elmt[0],
            "nombre": elmt[1],
            "genero": elmt[2],
            "pais_origen": elmt[3],
            "activo": elmt[4]
        }
        resultados_transformados.append(formato)

    #07. retornar informacion o responder
    #SIEMPRE debe retornar una respuesta
    #El formato de la respuesta es en JSON
    return jsonify(resultados_transformados)

@app.route("/api/canciones", methods=["GET"])
def get_canciones():
    conn = get_db_conection() 
    cur = conn.cursor()
    cur.execute("SELECT * FROM canciones")
    filas = cur.fetchall()
    cur.close() #cierro el cursor
    conn.close()# cierro la conexion


    resultados_transformados = []
    for elmt in filas:

        formato = {
            "titulo": elmt[0],
            "album": elmt[1],
            "duracion_segundos": elmt[2],
            "anio_lanzamiento": elmt[3],
            "artista_id": elmt[4]
        }
        resultados_transformados.append(formato)
    return  jsonify(resultados_transformados)


@app.route("/api/artistas/<int:id>", methods=["GET"])
def get_single_artist(id):
    conn = get_db_conection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM artistas WHERE  id = %s", (id,))
    fila = cur.fetchone()

    cur.close()
    conn.close()

    if fila is None:
        return {
            "msg": "Artista no encontrado"
        }, 400

    return {
        "id": fila[0],
        "nombre": fila[1],
        "genero": fila[2],
        "pais_origen": fila[3],
        "activo": fila[4]
    }


#Encendiendo el servidor
#Buscas evitar prender y apagar el servidor por cada cambio
#Debes usar debug=True
#El servidor se reiniciara solo cuando vea un cambio
#tambien nos indicara los errores que existieran
app.run(debug=True)