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

receptor = sys.argv[2].split('@')[0]
puertoSIP = sys.argv[2].split(':')[1]
IPreceptor =sys.argv[2].split('@')[1].split(':')[0]


# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((IPreceptor, int(puertoSIP)))


# Contenido que vamos a enviar
if metodo == 'INVITE' or 'BYE':
    LINE = metodo + ' sip:' + receptor + '@' + IPreceptor + ' SIP/2.0'

    print LINE
    my_socket.send(LINE + '\r\n')
    #data = my_socket.recv(1024)

if metodo == 'INVITE':
    LINE1 = 'ACK sip:' + receptor + '@' + ' SIP/2.0'
    
    print ('Envío ' + LINE1)
    my_socket.send(LINE1 + '\r\n')
    data = my_socket.recv(1024)


print 'Recibido -- ', data
print "Terminando socket..."

# Cerramos todo
my_socket.close()
print "Fin."

