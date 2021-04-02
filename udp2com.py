import serial
import socket

UDP_port = 55551
COM_port = 'COM5'
COM_baudrate= 9600

UDP = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
UDP.bind((socket.gethostname(),UDP_port))
COM = serial.Serial(COM_port, COM_baudrate)
while True:
    data,addr = UDP.recvfrom(1024)
    COM.write(data)
    print(data)