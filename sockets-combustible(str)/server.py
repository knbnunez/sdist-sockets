import socket

# Configura el socket del servidor UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 10000)

# Lista de sucursales con su dirección y multiplicador
sucursales = [
    {'nombre': "Ushuaia", 'direccion': ('localhost', 20000), 'multiplicador': 2.0},
    {'nombre': "Tolhuin", 'direccion': ('localhost', 20001), 'multiplicador': 1.0},
    # Agregar más sucursales aquí
]

# while True:
    # Solicita el nuevo valor del combustible al usuario
    #nuevo_valor = input("Ingrese el nuevo valor del combustible: ")
productos = [
    {"nombre": "INFINIA", "precio": 28.0},
    {"nombre":"SUPER", "precio": 15.0}, 
    {"nombre": "INFINIA DIESEL", "precio": 28.0}, 
    {"nombre": "ULTRADIESEL", "precio": 24.0}, 
    {"nombre": "DIESEL 500", "precio": 22.0}
]

# Envía el nuevo valor a todas las sucursales
for sucursal in sucursales: 
    
    precios_actualizados = ""
    for producto in productos:
        valor_actualizado = sucursal['multiplicador'] * float(producto['precio'])
        precios_actualizados += f"${{ 'producto': '{producto['nombre']}', 'precio': {valor_actualizado} }},"

    print(f"{sucursal['nombre']}: {precios_actualizados}")
    print()

    # Envía el nuevo valor a la sucursal mediante UDP
    server_socket.sendto(precios_actualizados.encode('utf-8'), sucursal['direccion']) # envío texto

print("Valores de combustible actualizados en todas las sucursales.")
