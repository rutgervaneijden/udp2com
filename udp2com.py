import serial
import socket

UDP_port = 55551
COM_port = 'COM5'
COM_baudrate= 9600

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((socket.gethostname(),UDP_port))
ser = serial.Serial(COM_port, COM_baudrate)
while True:
    data,addr = sock.recvfrom(1024)
    ser.write(data)
    print(data)
