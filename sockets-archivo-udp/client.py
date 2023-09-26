import socket

# Configura el socket del cliente
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 10000)

# Nombre del archivo que se enviará
file_name = 'archivo_a_enviar.txt'

try:
    with open(file_name, 'rb') as file: # rb: read binary
        # Lee y envía el contenido del archivo en trozos
        data = file.read(1024)
        while data:
            sent = sock.sendto(data, server_address)
            data = file.read(1024)
        print('Archivo {!r} enviado con éxito al servidor'.format(file_name))
        sock.close()
except FileNotFoundError:
    print('El archivo {!r} no se encontró en el directorio actual.'.format(file_name))
except Exception as e:
    print('Ocurrió un error al enviar el archivo:', str(e))