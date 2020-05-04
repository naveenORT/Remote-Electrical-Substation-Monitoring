'''
Created on Apr 10, 2020
@author: Naveen Rajendran
'''
import logging
import paho.mqtt.client as paho
from labs.module09.ArduinoDataReceiver import SensorData_Object
from labs.common.DataUtil import DataUtil
import ssl
import time 
from labs.common.ConfigUtil import ConfigUtil
import threading


connflag = False
load_prop = ConfigUtil("/home/pi/workspace/iot-device/apps/labs/common/ConnectedDevicesConfig.props")
convert_json = DataUtil()
mqttc = paho.Client() 
awshost = load_prop.getValues('aws.cloud', 'awshost') 
awsport = int(load_prop.getValues('aws.cloud', 'awsport'))  
clientId = load_prop.getValues('aws.cloud', 'clientId') 
thingName = load_prop.getValues('aws.cloud', 'thingName')
caPath = load_prop.getValues('aws.cloud', 'caPath') 
certPath = load_prop.getValues('aws.cloud', 'certPath')  
keyPath = load_prop.getValues('aws.cloud', 'keyPath') 


class AWS_Cloud_Connector(threading.Thread):    
    
    def __init__(self):
        threading.Thread.__init__(self)
        logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
        mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)  # pass parameters 
        mqttc.connect(awshost, awsport, keepalive=60) 
        mqttc.on_connect = on_connect 
        mqttc.loop_start()  
    
    def run(self):
        while (1):
            self.data_publish()
            time.sleep(5)
        
    def data_publish(self):    
        time.sleep(10)
        json_sensor_data = convert_json.sensordatatojson(SensorData_Object)
        mqttc.publish('update/environment/dht1', json_sensor_data, qos=1)  
        mqttc.on_publish = on_publish

def on_publish(mqtt, userdata, result):  # create function for callback
    '''
    * MQTT Callback function on publishing json data to MQTT Broker
    '''    
    logging.info("Data Published to AWS_IoT_Core ------------------------------------------------>>>>>>>> ")


def on_connect(client, userdata, flags, rc):  
    global connflag
    print ("Connected to AWS")
    connflag = True
   
 
def on_message(client, userdata, msg): 
    print(msg.topic + " " + str(msg.payload))

# mqttc.on_message = on_message  
