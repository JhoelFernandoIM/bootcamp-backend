class Auto:
    def __init__(self, nroLlantas, color, tipo, marca):
        self.nroLlantas = nroLlantas
        self.color = color
        self.tipo = tipo
        self.marca = marca

auto1 = Auto(4, "Rojo", "Deportivo", "Ferrari")
auto2 = Auto(4, "Negro", "SUV", "Toyota")
auto3 = Auto(6, "Blanco", "Camión", "Volvo")

print(f"Este es un auto de marca {auto1.marca}, de tipo {auto1.tipo}, con un color {auto1.color} y {auto1.nroLlantas} llantas.")
print(f"Por otro lado, tenemos este modelo que es un vehículo tipo {auto2.tipo} de la marca {auto2.marca}, el cual luce un color {auto2.color} y cuenta con {auto2.nroLlantas} llantas.")
print(f"Finalmente, podemos observar una unidad más pesada: se trata de un {auto3.tipo} {auto3.marca} en color {auto3.color} que posee {auto3.nroLlantas} llantas en total.")

