import time
import json
from kafka import KafkaConsumer
from sense_hat import SenseHat
from datetime import datetime
from configparser import SafeConfigParser

parser = SafeConfigParser()
parser.read('Config.ini')

device=  parser.get('device', 'deviceId')
server = parser.get('cloud','bootstrapServers')
time.sleep(60)

sense = SenseHat()
start_time = datetime.now()



def transform(arr):
    ret = []
    for z in arr:
        for a in z:
            ret.append(a)
    return ret



O = (10, 10, 10) # Black
green = (92, 230, 103) # green

yellow = (205, 193, 106) # yellow

red = (255, 0, 0) # red
blue = (0, 0, 255) # blue


consumer = KafkaConsumer( group_id=device, bootstrap_servers=server)
consumer.subscribe([device+'alerts' , 'alerts'])

def transform(arr):
    ret = []
    for z in arr:
        for a in z:
            ret.append(a)
    return ret


sense = SenseHat()

O = (10, 10, 10) # Black
X = (92, 230, 103) # green

X = (205, 193, 106) # yellow

#X = (255, 0, 0) # red

def display(X,template):

    temp = []
    if template == 'arrow':
        temp = [
        [O, O, O, X, X, O, O, O],
        [O, O, X, X, X, X, O, O],
        [O, X, X, X, X, X, X, O],
        [X, X, X, X, X, X, X, X],
        [O, O, O, X, X, O, O, O],
        [O, O, O, X, X, O, O, O],
        [O, O, O, X, X, O, O, O],
        [O, O, O, X, X, O, O, O]
        ]
    elif template == 'clear':
        temp = [
        [O, O, O, O, O, O, O, O],
        [O, O, O, O, O, O, O, O],
        [O, O, O, O, O, O, O, O],
        [O, O, O, O, O, O, O, O],
        [O, O, O, O, O, O, O, O],
        [O, O, O, O, O, O, O, O],
        [O, O, O, O, O, O, O, O],
        [O, O, O, O, O, O, O, O]
        ]
    else:
        temp = [
        [X, X, O, O, O, O, X, X],
        [X, X, X, O, O, X, X, X],
        [O, X, X, X, X, X, X, O],
        [O, O, X, X, X, X, O, O],
        [O, O, X, X, X, X, O, O],
        [O, X, X, X, X, X, X, O],
        [X, X, X, O, O, X, X, X],
        [X, X, O, O, O, O, X, X]
        ]
        return transform(temp)
    ext = []


    arrow_up = transform(temp)


    temp = list(list(x)[::-1] for x in zip(*temp))
    arrow_right = transform(temp)

    temp = list(list(x)[::-1] for x in zip(*temp))
    arrow_down = transform(temp)


    temp = list(list(x)[::-1] for x in zip(*temp))
    arrow_left = transform(temp)
    return {'up':arrow_up,'down':arrow_down,'left':arrow_left,'right':arrow_right}

#sense.set_pixels(arrow_up)



for msg in consumer:
#    print(msg)
    jSon = msg.value.decode('utf-8')
    jDict = json.loads(jSon)
   
    
    if(jDict['button'] == 'pressed'):
        X = green
    else:
        X = red
    
    if device != jDict['device'] and msg.topic == 'alerts':
        X = blue
   
    
    
    if(jDict['direction'] == 'middle'):
        sense.set_pixels(display(red,'x'))       
        start_time = datetime.now()
    else:
        sense.set_pixels(display(X,'arrow')[jDict['direction']])       
        start_time = datetime.now()
  
    time.sleep(parser.getfloat('device','recieveSleep'))
    







 
 
     
     
     
     
     
     
