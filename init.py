#!/usr/bin/python

from socket import *
import os.path
import os

def main():
    server_port = 80
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(('', server_port))
    server_socket.listen(100)
    print 'THE SERVER IS READY TO RECEIVE REQUEST'
    while 1:
        connection_socket, addr = server_socket.accept()
        #list_request =  connection_socket.recv(2048).split()
        list_request =  connection_socket.recv(2048)
        print list_request
        list_request = list_request.split()
        filename = os.getcwd()+list_request[1]
        if os.path.isfile(filename):
            print filename+" - is in directory of webserver"
            f_html = open(filename, "r")
            connection_socket.send(f_html.read())
            connection_socket.close()
        else:
            print filename+" - is NOT in directory of webserver"
            f_html = open("404.html", "r")
            connection_socket.send(f_html.read())
            connection_socket.close()

if __name__ == "__main__":
    main()
