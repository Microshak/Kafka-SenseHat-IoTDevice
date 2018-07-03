from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
import time
from kafka import KafkaProducer
import json
from sense_hat import SenseHat
from signal import pause
from configparser import SafeConfigParser

parser = SafeConfigParser()
parser.read('Config.ini')

device=  parser.get('device', 'deviceId')
server = parser.get('cloud','bootstrapServers')
time.sleep(60)     
print('ready')
producer = KafkaProducer(bootstrap_servers=server)
    
sense = SenseHat()
sense.set_imu_config(True, True, True) 
x = 0
oldAction = {}
oldDirection = {}
def mid(event):
    global oldAction 
    global oldDirection
    if event.action != ACTION_RELEASED:
        alert = {'button':event.action, 'direction':event.direction, 'device':device}
        message = json.dumps(alert)
        if not (event.action == oldAction and event.action == 'held'):
            producer.send(device+'alerts' ,key=bytes("alert", encoding='utf-8'),value=bytes(message, encoding='utf-8'))
            producer.send(device ,key=bytes("alert", encoding='utf-8'),value=bytes(message, encoding='utf-8'))
        elif event.action == oldAction and event.action == 'held' and oldDirection != event.direction:
            oldDirection = event.direction
            producer.send('alerts' ,key=bytes("alert", encoding='utf-8'),value=bytes(message, encoding='utf-8'))
        
        oldAction = event.action 
sense.stick.direction_any =  mid

while True:

    readings = {}
    readings['orentation'] = sense.get_orientation()
    readings['compass'] = sense.get_compass_raw()
    readings['gyroscope'] = sense.gyro_raw
    readings['accelerometer'] = sense.accel_raw
    x = x+1
    
    message = json.dumps(readings)
    producer.send(device,key=bytes("message", encoding='utf-8'),value=bytes(message, encoding='utf-8'))
    time.sleep(parser.getfloat('device','sendSleep'))

