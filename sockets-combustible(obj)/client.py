import socket
import pickle

class Product:
    def __init__(self, nombre, precio):
        self.name = nombre
        self.price = precio
    def __str__(self):
        return f"- Producto: {self.name}, precio: {self.price}"

# Configuración del socket cliente UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_address = ('localhost', 20000) # Cambiar como sea necesario
client_socket.bind(client_address)
suc_name = b"Ushuaia" # Cambiar como sea necesario
#
server_address = ('localhost', 10000)

update_request = ""
while (update_request != "N" ):
    
    try: 
        client_socket.sendto(suc_name, server_address)
        print("\nConexión establecida")
    except: print("\nNo se pudo establecer la conexión")

    data, server_address = client_socket.recvfrom(1024) # El socket del servidor espera a recibir el nuevo valor del combustible del socket servidor

    updated_prices = pickle.loads(data) # Decodifica el mensaje y muestra el nuevo valor del combustible
    #
    for p in updated_prices: print(p)

    update_request = input("\nVolver a solicitar precios actualizados (y/si, n/no): ").upper()