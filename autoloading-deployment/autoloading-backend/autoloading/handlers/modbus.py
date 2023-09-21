import socket,time
from flask_socketio import SocketIO
import sqlite3
from datetime import datetime

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

server_ip=('192.168.100.8',8234)
hex_data='0103200200012E0A'
byte_data = bytes.fromhex(hex_data)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
running = False
int_distance = 0

def read_sensor_data():
    pass

#@app.route('/get')
def read_per_second():
    global int_distance
    global current_time
    while True:
        s.connect(server_ip)
        s.sendall(byte_data)
        received_data = s.recv(1024)
        hex_received_data = received_data.hex() # '010302157cb735'    
        current_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        hex_distance = hex_received_data[6:10]
        int_distance = int(hex_distance,16)
        #print('distance:', int_distance,'mm')
        s.close()
        #return int_distance

def insert_data(int_distance,current_time):#将测量值和时间存储在数据库中
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO distance (data,time)VALUES(?,?)
''',(int_distance,current_time))
    conn.commit()
    conn.close()
    time.sleep(1)