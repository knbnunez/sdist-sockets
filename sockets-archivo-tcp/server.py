import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 10000))
sock.listen(1) # Esta llamada indica al sistema operativo que ya estamos listos para admitir conexiones. El número 1 de parámetro indica cuantos clientes podemos tener encolados en espera simultáneamente

while True:
    client_sock, client_address = sock.accept() # espera hasta que un cliente se conecta al servidor
    # client_sock: es un nuevo socket que representa la conexión específica entre el servidor y ese cliente en particular
    # client_address: es una tupla que contiene la dirección IP y el número de puerto del cliente que se ha conectado
    try:
        with open('archivo_recibido.txt', 'wb') as file:
            while True:
                data = client_sock.recv(512)
                if not data:
                    break  # Se recibieron todos los datos
                print('received {} bytes from {}'.format(len(data), client_address))
                file.write(data)
    except Exception as e:
        print("Fallo en la recepción de datos:", str(e))
    finally:
        client_sock.close()
