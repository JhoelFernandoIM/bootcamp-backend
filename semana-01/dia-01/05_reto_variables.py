nombre = "Jhoe Fernando Ingalla Mamani"
edad = 23

# print(f"Hola soy {nombre}, tengo {edad} años")
# print(f"El dato {nombre} es de tipo ...", type(nombre))
# print(f"El dato {edad} es de tipo ...", type(edad))
# print(f"Naciste en ", 2026-edad)

nombre = input("¿Cual es tu nombre?")
edad = input("¿Cual es tu edad?")
ciudad = input("¿Cual es tu ciudad'")
lenguaje = input("¿Cual es tu lenguaje favorito?")

print(f"Hola soy {nombre}, tengo {edad} años, vivo en {ciudad} y programo en {lenguaje}")

print(nombre, type(nombre))
print(edad, type(edad))

anio_nacimiento = 2026 - int(edad)
print(f"Tu año de nacimiento es el {anio_nacimiento}")