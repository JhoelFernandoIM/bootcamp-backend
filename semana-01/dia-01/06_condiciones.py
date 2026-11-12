nombre = "Jhoel"
edad = 42
peruano = True

if edad >= 35 and peruano == True:
    print(f"Sr {nombre} usted es apto para postularse como presidente")

else:
    print(f"Sr. {nombre} usted no esta apto")

    #un if solo se ejecuta cuando la condicion es verdadera

es_fin_de_semana = False
if not es_fin_de_semana:
    print("¡ nO ES FIN DE SEMANA!")


#TERNARIO

#js ( condicion ? si: no)

# SI if CONDICION else NO

edad = 17
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)