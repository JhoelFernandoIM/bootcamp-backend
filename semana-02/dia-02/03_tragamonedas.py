
import random


# ==========================================
# 1. CLASE PRINCIPAL
# ==========================================

class Tragamonedas:

    def __init__(self, nombre, creditos):
        self.nombre = nombre
        self._creditos = creditos
        self._total_jugado = 0
        self._total_ganado = 0

    @property
    def creditos(self):
        return self._creditos

    def mostrar(self):
        estado = f"S/ {self._creditos}" if self._creditos > 0 else "SIN CREDITOS"
        print(f"🎰 {self.nombre} - Créditos: {estado}")

    def girar(self):
        simbolos = ["🍒", "🔔", "💎", "🍀", "⭐", "7️⃣"]
        resultado = []

        for i in range(3):
            indice = random.randint(0, len(simbolos) - 1)
            resultado.append(simbolos[indice])

        print(f"[ {resultado[0]}  {resultado[1]}  {resultado[2]} ]")
        return resultado

    def jugar(self, apuesta):

        # Validar apuesta
        if apuesta <= 0:
            print("❌ La apuesta debe ser mayor que cero.")
            return False

        if apuesta > self._creditos:
            print(f"❌ No tienes suficientes créditos. Dispones de S/ {self._creditos}")
            return False

        # Descontar apuesta
        self._creditos -= apuesta
        self._total_jugado += apuesta

        # Girar máquina
        resultado = self.girar()

        # Evaluar resultado
        if resultado[0] == resultado[1] == resultado[2]:

            premio = apuesta * 10
            print(f"🎉 ¡JACKPOT! Ganaste S/ {premio}")
            self._creditos += premio
            self._total_ganado += premio

        elif (resultado[0] == resultado[1] or
              resultado[1] == resultado[2] or
              resultado[0] == resultado[2]):

            premio = apuesta * 2
            print(f"✨ ¡Dos iguales! Ganaste S/ {premio}")
            self._creditos += premio
            self._total_ganado += premio

        else:
            print(f"😢 Lo siento, perdiste S/ {apuesta}")

        return True

    def mostrar_estadisticas(self):

        balance = self._total_ganado - self._total_jugado

        print(f"\n📊 Estadísticas: {self.nombre}")
        print(f"Total apostado: S/ {self._total_jugado}")
        print(f"Total ganado:   S/ {self._total_ganado}")
        print(f"Balance:        S/ {balance}")
        print(f"Créditos:       S/ {self._creditos}")


# ==========================================
# 2. HERENCIA: MAQUINA DE FRUTAS
# ==========================================

class TragamonedasFrutas(Tragamonedas):

    def girar(self):
        simbolos = ["🍒", "🍋", "🍊", "🍇", "🍉", "🍓"]
        resultado = []

        for i in range(3):
            indice = random.randint(0, len(simbolos) - 1)
            resultado.append(simbolos[indice])

        print(f"[ {resultado[0]}  {resultado[1]}  {resultado[2]} ]")
        return resultado


# ==========================================
# 3. HERENCIA: MAQUINA CLASICA
# ==========================================

class TragamonedasClasico(Tragamonedas):

    def girar(self):
        simbolos = ["7️⃣", "💎", "🔔", "⭐", "💲", "🎰"]
        resultado = []

        for i in range(3):
            indice = random.randint(0, len(simbolos) - 1)
            resultado.append(simbolos[indice])

        print(f"[ {resultado[0]}  {resultado[1]}  {resultado[2]} ]")
        return resultado


# ==========================================
# 4. HERENCIA: MAQUINA MUNDIAL
# ==========================================

class TragamonedasMundial(Tragamonedas):

    def girar(self):
        simbolos = ["🇵🇪", "🇦🇷", "🇫🇷", "🇧🇷", "🇪🇸", "🇩🇪"]
        resultado = []

        for i in range(3):
            indice = random.randint(0, len(simbolos) - 1)
            resultado.append(simbolos[indice])

        print(f"[ {resultado[0]}  {resultado[1]}  {resultado[2]} ]")
        return resultado

    # Sobrescritura del método jugar()
    def jugar(self, apuesta):

        if apuesta <= 0:
            print("❌ La apuesta debe ser mayor que cero.")
            return False

        if apuesta > self._creditos:
            print(f"❌ No tienes suficientes créditos. Dispones de S/ {self._creditos}")
            return False

        self._creditos -= apuesta
        self._total_jugado += apuesta

        resultado = self.girar()

        tiene_peru = "🇵🇪" in resultado

        if resultado[0] == resultado[1] == resultado[2]:

            premio = apuesta * 15
            print(f"🏆 ¡TRIPLETE MUNDIAL! Ganaste S/ {premio}")
            self._creditos += premio
            self._total_ganado += premio

        elif (resultado[0] == resultado[1] or
              resultado[1] == resultado[2] or
              resultado[0] == resultado[2]):

            premio = apuesta * 2
            print(f"⚽ ¡Dos iguales! Ganaste S/ {premio}")
            self._creditos += premio
            self._total_ganado += premio

        elif tiene_peru:

            premio = apuesta
            print("🇵🇪 ¡Apareció Perú! Recuperaste tu apuesta.")
            self._creditos += premio
            self._total_ganado += premio

        else:
            print(f"😢 Perdiste S/ {apuesta}")

        return True


# ==========================================
# 5. FUNCION PARA JUGAR EN UNA MAQUINA
# ==========================================

def jugar_en_maquina(maquina):

    while maquina.creditos > 0:

        maquina.mostrar()

        try:
            apuesta = int(input("¿Cuánto apuestas? (0 para volver): "))
        except ValueError:
            print("❌ Ingresa un número válido.")
            continue

        if apuesta == 0:
            break

        maquina.jugar(apuesta)
        print()

    if maquina.creditos == 0:
        print("💸 Esta máquina se quedó sin créditos.")


# ==========================================
# 6. SISTEMA PRINCIPAL DEL CASINO
# ==========================================

maquinas = [
    TragamonedasFrutas("La Frutal", 200),
    TragamonedasClasico("La Clásica", 300),
    TragamonedasMundial("Mundial 2026", 150)
]


while True:

    print("\n" + "=" * 40)
    print("       🎰 CASINO ROYALE 🎰")
    print("=" * 40)

    for i, maquina in enumerate(maquinas, 1):

        if maquina.creditos > 0:
            estado = f"S/ {maquina.creditos}"
        else:
            estado = "SIN CRÉDITOS"

        print(f"{i}. {maquina.nombre} - {estado}")

    print("4. Mostrar estadísticas")
    print("5. Salir")

    try:
        opcion = int(input("\nElige una máquina: "))
    except ValueError:
        print("❌ Ingresa una opción válida.")
        continue

    if 1 <= opcion <= 3:

        maquina = maquinas[opcion - 1]

        if maquina.creditos == 0:
            print("❌ Esta máquina no tiene créditos.")
        else:
            jugar_en_maquina(maquina)

    elif opcion == 4:

        print("\n📊 ESTADÍSTICAS DEL CASINO")

        for maquina in maquinas:
            maquina.mostrar_estadisticas()

    elif opcion == 5:

        print("\n💰 RESUMEN FINAL DEL CASINO")

        for maquina in maquinas:
            maquina.mostrar_estadisticas()

        print("\n¡Gracias por jugar!")

        break

    else:
        print("❌ Opción incorrecta.")

        