# print("Bienvenido a mi videojuego")


# vidas = 3


# while vidas > 0:
#     print(f"Tienes {vidas} vidas")
#     respuesta = input("¿Quieres perder una vida? (s/n): ")
#     if respuesta == "s":
#         vidas = vidas - 1
#         print("Has perdido una vida")


# print("Fin del jueugo, no tienes vidas")


contra = ""

while len(contra) < 8:
    contra = input("ponga contraseña de 8 dígitos: \n")
    if contra < 8:
        print("aún no es sufciente")

print("contraseña válida")