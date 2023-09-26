import socket

# Configura el socket del servidor
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", 10000))

# Nombre del archivo en el que se almacenará el contenido recibido
file_name = 'archivo_recibido.txt'

while True:
    # Abre el archivo en modo de escritura binaria
    with open(file_name, 'wb') as file: # wb: write binary
        while True:
            data, address = sock.recvfrom(1024)
            if not data:
                break
            print('received {} bytes from {}'.format(len(data), address))
            # Escribe los datos recibidos en el archivo
            file.write(data)

    print('Archivo recibido y guardado como', file_name)
