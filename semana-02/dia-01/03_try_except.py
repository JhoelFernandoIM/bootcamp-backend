try:
    numero = int(input("Ingrese un número "))
    if numero < 0:
        raise Exception("No se permiten números negativos")
    print(f"Tu numero es {numero}")
except Exception:
    print("tuvimos un error con el número")
finally: #se ejecuta siempre, haya o no un error
    print("fin de semana")

#Tipos de errores
#ValueError => El valor tiene un formato incorrecto
#ZeroDivisionError => Se intenta dividir entre cero
#NameError => Se esta usando una variable no creada
#ImportError =>No se puede importar un módulo
#Exception => un salvavidas cuando no conoces el error específico