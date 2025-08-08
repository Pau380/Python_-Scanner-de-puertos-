#scanner de puertos
#se requiere controlar la red desde Python, se debe importar la libreria socket 
#socket nos sirve para crear conecciones
import socket

#se requiere poner la dirección ip que se desea escanear 

ip= input("Ingrese la dirección IP a escanear: ")

#Hay que hacer un bucle for para escaear los puertos
#Hay 65535 puertos
#socket.SOCK_STREAM: significa que estamos utilizando el protocolo TCP

for puerto in range (1,65535):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)

#vamos a utilizar el socket para ver que puerto está abierto o no
    result = sock.connect_ex((ip, puerto))

    #sí el puerto está aierto
    if result == 0:
        print("Puerto abierto: " + str(puerto))
        sock.close() #cerramos el socket
    else:
        print("Puerto cerrado: " + str(puerto))


