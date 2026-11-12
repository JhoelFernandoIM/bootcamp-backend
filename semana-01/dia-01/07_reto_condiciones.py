edad = input("¿Cuál es su edad?")
state_dni = input("¿Trajo su DNI en físico con usted? (SI/NO)")

if int(edad) < 16:
    print("No puede votar")
elif int(edad) >=16 and int(edad) <= 17 and state_dni == "SI" or int(edad) >= 70 and state_dni == "SI":
    print("Voto optativo")
elif int(edad) >=18 and int(edad) <= 69 and state_dni == "SI":
    print("Voto obligatorio")
else:
    print("No puede votar")