import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 10000))

try:
    #https://blog.gitnux.com/code/python-reading-binary-files/
    with open('archivo_a_enviar.txt', 'rb') as file: # Abrimos el archivo con -rb "read binary" para enviar
        while True:
            data = file.read(512)
            if not data:
                break  # Se llegó al final del archivo
            sock.sendall(data) # https://es.stackoverflow.com/questions/183986/que-diferencias-tienen-las-funciones-sendall-send-en-python
except Exception as e:
    print("Fallo en el envío de datos:", str(e))
finally:
    sock.close()
