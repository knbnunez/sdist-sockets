import socket
import pickle

# Configuración del socket servidor con UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 10000)
server_socket.bind((server_address))

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return f"- Producto: {self.name}, precio: {self.price}"
    
infinia = Product("INFINIA", 28.0)
super = Product("SUPER", 15.0)
infinia_diesel = Product("INFINIA DIESEL", 28.0)
ultradiesel = Product("ULTRADIESEL", 24.0)
diesel_500 = Product("DIESEL 500", 22.0)
products = [infinia, super, infinia_diesel, ultradiesel, diesel_500] # Para una posible iteración más sencilla

while True:
    print("\nEsperando solicitudes...")
    data, address = server_socket.recvfrom(1024) # Esperar mensaje de conexión de un cliente
    
    multiplier = ""
    while not(isinstance(multiplier, float)):
        try: multiplier = float(input(f"Ingrese un multiplicador para la sucursal {data}: "))
        except: multiplier = float(input(f"Reintente el ingreso del multiplicador para la sucursal {data}: "))

    server_socket.sendto(pickle.dumps(
        [
            Product(infinia.name, infinia.price * multiplier),
            Product(super.name, super.price * multiplier),
            Product(infinia_diesel.name, infinia_diesel.price * multiplier),
            Product(ultradiesel.name, ultradiesel.price * multiplier),
            Product(diesel_500.name, diesel_500.price * multiplier)
        ]
    ), address)
    
    print(f"\nValores de combustible actualizados en la sucursal {data}")
    for p in products:
        print(p)