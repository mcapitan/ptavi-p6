#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import SocketServer
import sys

IP = sys.argv[1]
puerto = int(sys.argv[2])


class EchoHandler(SocketServer.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            print "El cliente nos manda " + line
           
            #if line.split(' ')[1] == 'sip':
            if line.split(' ')[0] == 'INVITE':
		        reply = 'SIP/2.0 100 Trying\r\nSIP/2.0 180 Ring\r\nSIP/2.0 200 OK\r\n'
            elif line.split(' ')[0] == 'BYE' or 'ACK':
		        reply = 'SIP/2.0 200 OK\r\n'
            else:
		        reply = 'SIP/2.0 400 Bad Request\r\nSIP/2.0 405 Method Not Allowed'
            #else:
                #reply = 'SIP/2.0 400 Bad Request'

            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break

            self.wfile.write(reply)
            print reply

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    serv = SocketServer.UDPServer((IP, puerto), EchoHandler)
    print "Listening..."
    serv.serve_forever()
