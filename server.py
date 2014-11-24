#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import SocketServer
import sys
import os

IP = sys.argv[1]
puerto = int(sys.argv[2])
fichero_audio = sys.argv[3]


class EchoHandler(SocketServer.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            if not line:
                break
            else:
                if line.split(' ')[0] == 'INVITE':
		    reply = 'SIP/2.0 100 Trying\r\nSIP/2.0 180 Ringing\r\nSIP/2.0 200 OK\r\n'
		    self.wfile.write(reply)
                    print reply
                elif line.split(' ')[0] == 'BYE':
		    reply = 'SIP/2.0 200 OK\r\n'
		    self.wfile.write(reply)
                    print reply
                elif line.split(' ')[0] == 'ACK':
                    reply = 'SIP/2.0 200 OK\r\n'
                    self.wfile.write(reply)
                    print reply
                    aEjecutar = './mp32rtp -i ' + IP + ' -p 23032 < ' + fichero_audio
                    print "Vamos a ejecutar", aEjecutar
                    os.system(aEjecutar)
                    print "Ha terminado\r\n"    
                else:
		    reply = 'SIP/2.0 400 Bad Request\r\nSIP/2.0 405 Method Not Allowed'
                    self.wfile.write(reply)
                    print reply

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    serv = SocketServer.UDPServer((IP, puerto), EchoHandler)
    print "Listening...\r\n"
    serv.serve_forever()
