import socket
import struct
import subprocess
import json
import os

class FtpServer:
    address_familly = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    allow_reuse_address = False
    max_packet_size = 8192
    coding = 'utf-8'
    request_queue_size = 5
    server_dir = "file_upload"
    def __init__(self, address, port, bind=True):
        self.addr = (address, port)
        self.socket = socket.socket(self.address_familly,self.socket_type)
        if bind:
            try:
                self.bind()
                self.listen()
            except:
                self.close()
                raise
    def bind(self):
        if self.allow_reuse_address:
            self.socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.socket.bind(self.addr)
    def listen(self):
        self.socket.listen(self.request_queue_size)
    def close(self):
        self.socket.close()
    def get_request(self):
        return self.socket.accept()
    def close_request(self,request):
        request.close()
        
    def run(self):
        while True:
            print("server start")
            self.conn, self.client_addr = self.get_request()
            print(self.conn, self.client_addr)

if __name__ == "__main__":
    ts1 = FtpServer("0.0.0.0", 10000)
    ts1.run()
