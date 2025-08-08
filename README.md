Este script permite escanear todos los puertos TCP de una dirección IP para identificar cuáles están abiertos.

📌 Descripción
Utiliza la librería socket para crear conexiones de red.

Permite ingresar la IP a escanear manualmente.

Recorre todos los puertos del 1 al 65535 usando un bucle for.

Usa socket.AF_INET para trabajar con IPv4 y socket.SOCK_STREAM para conexiones TCP.

Con connect_ex() comprueba si un puerto está abierto (devuelve 0) o cerrado.

Cierra cada conexión con sock.close() para liberar recursos.
