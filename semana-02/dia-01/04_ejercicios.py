def pedir_entero(mensaje):
    try:
        numero = int(input(mensaje))
        return numero
    except Exception:
        print("Esto no es un número")

edad = pedir_entero("¿Cuantos años tienes")
print(f"tienes {edad} años")


def pedir_nota(mensaje):
    try:
        numero = int(input(mensaje))
        
    except Exception:
        pass