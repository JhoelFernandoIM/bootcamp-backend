# productos = [
#     {"nombre": "Laptop", "precio": 2499.99, "stock": 15},
#     {"nombre": "Mouse", "precio": 45.50, "stock": 30},
#     {"nombre": "Teclado", "precio": 120.00, "stock": 8},
#     {"nombre": "Parlante", "precio": 75.00, "stock": 20},
# ]

# for producto in productos:
#     if producto["precio"] < 100:
#         print(producto["nombre"])

# #mostrar stock menor a 10

# for producto in productos:
#     if producto["stock"] < 10:
#         print(f"Producto con poco stock {producto["nombre"]}")

# #Encontrar el producto más caro

# mas_caro = productos[0]
# for producto in productos:
#     if producto["precio"] > mas_caro["precio"]:
#         mas_caro = producto
# print(f"El producto más caro es el {mas_caro["nombre"]}")

# #lista de productos con mas de 10 unidades
# producto_stock = []
# for producto in productos:
#     if producto["stock"] > 10:
#         producto_stock.append(producto["nombre"])
# print(producto_stock)


#
clientes = [
    {"nombre": "Ana", "deuda": 150.00, "dias_atraso": 45},
    {"nombre": "Luis", "deuda": 0, "dias_atraso": 0},
    {"nombre": "Sofia", "deuda": 320.50, "dias_atraso": 60},
    {"nombre": "Carlos", "deuda": 75.00, "dias_atraso": 15},
    {"nombre": "Marta", "deuda": 0, "dias_atraso": 0},
]

for cliente in clientes:
    if cliente["deuda"] > 0:
        print(f"es moroso {cliente["nombre"]}")

        if cliente["deuda"] > 100 and cliente["dias_atraso"] > 30:
            print(f"Es moroso grave {cliente["nombre"]}")