#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys
import os

# Cliente UDP simple.

# Dirección IP del servidor.
metodo = str(sys.argv[1])
receptor = str(sys.argv[2])
a = sys.argv[2].split("@")
b = sys.argv[2].split(":")
c = b[-2].split("@")
puertoSIP = b[-1]
IPreceptor = c[1]

print IPreceptor
print puertoSIP



"""
# Contenido que vamos a enviar
LINE = '¡Hola mundo!'

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVER, PORT))

print "Enviando: " + LINE
my_socket.send(LINE + '\r\n')
data = my_socket.recv(1024)

print 'Recibido -- ', data
print "Terminando socket..."

# Cerramos todo
my_socket.close()
print "Fin."
"""
