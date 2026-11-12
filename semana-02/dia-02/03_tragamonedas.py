import random
class Tragamonedas:
    def __init__(self, nombre, creditos):
        self.nombre = nombre
        self.creditos = creditos

    def mostrar(self):
        print(f"{self.nombre} - Créditos: {self.creditos}")

    def girar(self):
        simbolos = ["🍒", "🔔", "💎", "🍀", "⭐", "7️⃣"]
        resultado = []

        for i in range(3):
            #Debemos generar un indice al azar
            indice = random.randint(0,len(simbolos) - 1)
            resultado.append(simbolos[indice])
        print(f"{resultado}")
        return resultado

    def jugar(self, apuesta):
        if apuesta > self.creditos:
            print(f"No tienes suficiente créditos, solo dispones de {self.creditos}")
            return

        self.creditos = self.creditos - apuesta
        resultado = self.girar()

        if resultado[0] == resultado[1] == resultado[2]:
            premio = apuesta * 10
            print(f"Ganaste {premio}")
            self.creditos = self.creditos + premio
        elif resultado[0] == resultado[1] or resultado[1] == resultado[2] or resultado[0] == resultado[2]:
            premio = apuesta * 2
            print(f"Ganaste {premio}")
            self.creditos = self.creditos + premio
        else:
            print("Lo siento lo perdiste")


maquina = Tragamonedas("La siete", 100)
maquina2 = Tragamonedas("La Frutal", 250)
maquina3 = Tragamonedas("Jackpot City", 500)

maquina.mostrar()
maquina2.mostrar()
maquina3.mostrar()

maquina.girar()
maquina.jugar(100)
        