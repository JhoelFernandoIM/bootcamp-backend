# paises = ["USA", "Japon", "Canada"]

# for pais in paises:
#     print(pais)

# notas = [19, 12, 11, 18, 20]

# for nota in notas:
#     if nota > 13:
#         print(f"Alumno aprobado con {nota}")

cadena = "Superman"
vocales = ["a", "e", "i", "o", "u"]

for caracter in cadena:
    if caracter not in vocales:
        print(caracter)


frutas = ["manzana", "pera", "mandarina"]

for idx, valor in enumerate(frutas):
    print(f"Indice: {idx}: {valor}")


datos = [["12345678", "Fernando", "M"], ["87654321", "Linda", "F"]]

for dato in datos:
    for dato_personal in dato:
        print(dato_personal)