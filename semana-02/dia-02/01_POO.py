class Jugador:
    def __init__(self, nombre, edad, posicion, equipo):
        self.nombre = nombre
        self.edad = edad
        self.posicion = posicion
        self.equipo = equipo

    def correr(self):
        print(f"El jugador {self.nombre} esta corriendo")

    def mostrar_info(self):
        print(f"{self.nombre} - {self.edad} años - {self.posicion} - {self.equipo}")


    def anotar_gol(self, equipo_anotado):
        print(f"{self.nombre} anotó contra {equipo_anotado}")


#Instanciando la clase
messi = Jugador("Lionel Messi", 37, "Delantero", "Argentina")
mbappe = Jugador("Kilian Mbappe", 27, "Delantero", "Francia")

print(messi.nombre)

messi.correr()
mbappe.mostrar_info()
mbappe.anotar_gol("Valencia")

#ABSTRACCIÓN

class Equipo:
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais
        self.jugadores = []
        pass

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)
        print(f"jugador insertado exitosamente")

brasil = Equipo("Selección de Brasil", "Brasil") 

ronaldo = Jugador("Ronaldo", 29, "Delantero", "Selección de Brasil")
rivaldo = Jugador("Rivaldo", 28, "Delantero", "Selección de Brasil")
ronaldinho = Jugador("Ronaldinho", 27, "Mediocampista", "Selección de Brasil")

brasil.agregar_jugador(ronaldo)
brasil.agregar_jugador(rivaldo)
brasil.agregar_jugador(ronaldinho)

print(brasil.jugadores)

#POLIMORFISMO
cristiano_ronaldo = Jugador("Cristiano Ronaldo", 41, "Volante", "Selección de Portugal")
halland = Jugador("Halland", 24, "Delantero", "Selección de Noruega")

class JugadorPadre:
    def __init__(self, nombre, edad, equipo):
        self.nombre = nombre
        self.edad = edad
        self.equipo = equipo

    def entrenar (self):
        print(f"Hola estoy entrenando, te saluda {self.nombre}")

#HERENCIA
class Arquero(JugadorPadre):
    def __init__(self, nombre, edad, equipo, estatura, penalesAtajados):
        super().__init__(nombre, edad, equipo)
        self.estatura = estatura
        self.penalesAtajados = penalesAtajados

    def atajar(self):
        print(f"Balon atajado por {self.nombre}")

dibu = Arquero("Dibu Martinez", 36, "Selección de Argentina", "1.95", 150 )
dibu.entrenar()
dibu.atajar()