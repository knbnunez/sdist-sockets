import socket

# Configura el socket del cliente UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_address = ('localhost', 20000)  # Dirección de esta sucursal
client_socket.bind(client_address)

while True:
    # Espera a recibir el nuevo valor del combustible del servidor central
    data, server_address = client_socket.recvfrom(1024)

    # Decodifica el mensaje y muestra el nuevo valor del combustible
    precios_actualizados = data.decode('utf-8')
    print("Nuevo valor del combustible:", precios_actualizados)
