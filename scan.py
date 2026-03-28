import socket

#Solicitamos al usuario la IP que se desea escanear
ip = input("Ingresa la IP a escanear:")

#Creamos bucle for sabiendo que los puertos existentes a día de hoy son 65535
for i in range(1,65535):
    #Creamos variable sock y realizamos la confiuración para que vaya por IPv4 y por protocolo TCP con las propiedades AF_INET y SOCK_STREAM
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Le indicamos un timeout de 2 segundos
    sock.settimeout(2)
    #Le decimos que intente conectar al puerto indicado en el rango
    result = sock.connect_ex((ip, i))

    #Imprimimos los resultados obtenidos
    if result == 0:
        print("Puerto Abierto: " + str(i))
        sock.close