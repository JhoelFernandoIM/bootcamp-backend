# INTERBANK
# El siguiente usuario esta teniendo los siguientes movimientos
movimientos = [
{ "fecha": "2024-01-15", "tipo": "deposito", "monto": 1500.00},
{ "fecha": "2024-01-20", "tipo": "retiro", "monto": 200.00},
{ "fecha": "2024-02-05", "tipo": "deposito", "monto": 500.00},
{ "fecha": "2024-02-10", "tipo": "retiro", "monto": 100.00},
{ "fecha": "2024-02-15", "tipo": "deposito", "monto": 300.00},
{ "fecha": "2024-02-20", "tipo": "retiro", "monto": 50.00},
{ "fecha": "2024-02-25", "tipo": "deposito", "monto": 1000.00 }
]


# 01. Sumar todos los depositos
# 02. Sumar todos los retiros
# 03. Calcular el balance final (depositos - retiros)
# 04. Mostrar el deposito mas grande
# 05. Mostrar el retiro mas grande

#01, suma

suma_dep = 0
suma_ret = 0

mayor_dep = movimientos[0]["monto"]
mayor_ret = 0

for movimiento in movimientos:
    if movimiento["tipo"] == "deposito":
        suma_dep = movimiento["monto"] + suma_dep

        if movimiento["monto"] > mayor_dep:
            mayor_dep = movimiento["monto"]


    else:
        suma_ret = movimiento["monto"] + suma_ret

        if movimiento["monto"] > mayor_ret:
            mayor_ret = movimiento["monto"]

balance = suma_dep-suma_ret

print(f"la suma de depositos es: {suma_dep}")
print(f"la suma de retiros es: {suma_ret}")
print(f"balance es: {balance}")
print(f"el mayor deposito es: {mayor_dep}")
print(f"el mayor retiro es: {mayor_ret}")
