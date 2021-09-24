import serial
import socket

UDP_host = '127.0.0.1'
UDP_port = 55551

COM_port = 'COM5'
COM_baudrate= 9600

sentences = ['RSA','THS','VDM','VTG']

def filter(data):
    if data[3:6].decode() in sentences:
        COM.write(data)
        print(data)

UDP = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
UDP.bind((UDP_host,UDP_port))

COM = serial.Serial(COM_port, COM_baudrate)

while True:
    data,addr = UDP.recvfrom(1024)
    filter(data)
