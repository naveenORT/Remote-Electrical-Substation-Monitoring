'''
Created on Apr 15, 2020
@author: Naveen Rajendran
'''
import logging
import paho.mqtt.client as mqttClient
import time
import ssl
from labs.common.DataUtil import DataUtil
from labs.common.ConfigUtil import ConfigUtil
from labs.module09.ArduinoDataReceiver import SensorData_Object
from labs.module09.ArduinoDataReceiver import DeviceData_Object
import threading
from labs.module09.SensorDataManager import logging
from labs.module09.ActuatorAdaptor import ActuatorAdaptor 

mqtt_client = mqttClient.Client()
convert_json = DataUtil()
act_obj = ActuatorAdaptor()
connected_flag = False  
publish_flag = False
subscribe_flag = False

"""
Class which connects gateway device with UbidotsCloudService using MQTT/TLS protocol. Performs Pub/Sub functions whenever 
a SensorData is received 
"""


class UbidotsCloudConnector(threading.Thread):    
    
    def __init__(self):        
        """
        Class constructor which initializes all required parameters for connecting ubidots cloud service
        """
        logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
        threading.Thread.__init__(self)
        self.load_prop = ConfigUtil(r"/home/pi/workspace/iot-device/apps/labs/common/ConnectedDevicesConfig.props")
        self.BROKER_ENDPOINT = self.load_prop.getValues('ubidots.cloud', 'host')
        self.TLS_PORT = int(self.load_prop.getValues('ubidots.cloud', 'port'))
        self.MQTT_USERNAME = self.load_prop.getValues('ubidots.cloud', 'authToken')  
        self.MQTT_PASSWORD = ""  
        self.TOPIC = '/v1.6/devices/'
        self.DEVICE_LABEL = 'substation-gateway'
        self.TLS_CERT_PATH = self.load_prop.getValues('ubidots.cloud', 'certFile')  
        logging.info("Configuring & Setting Up Cloud Connection Properties")
        mqtt_client.on_connect = on_connect
        self.connect(mqtt_client, self.MQTT_USERNAME, self.MQTT_PASSWORD, self.BROKER_ENDPOINT, self.TLS_PORT)
    
    def connect(self, mqtt_client, mqtt_username, mqtt_password, broker_endpoint, port):
        """
        Function which helps to connect to remote mqtt brroker
        """
        mqtt_client.username_pw_set(mqtt_username, password=mqtt_password)
        mqtt_client.tls_set(ca_certs=self.TLS_CERT_PATH, certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
        mqtt_client.tls_insecure_set(False)
        mqtt_client.connect(broker_endpoint, port=port)
        mqtt_client.loop_start()

    def run(self): 
        """
        Threaded runnable function which publishes & subscribes data to / from cloud, whenever a new sensor data is 
        received from constrained device
        """
        while(1):
            topic = "{}{}".format(self.TOPIC, self.DEVICE_LABEL)
            sensor_payload = convert_json.sensordatatojson(SensorData_Object)
            device_payload = convert_json.sensordatatojson(DeviceData_Object)
            logging.info(sensor_payload)
            logging.info(device_payload)
            self.publish(mqtt_client, topic, sensor_payload)         
            self.publish(mqtt_client, topic, device_payload)
            
            
            self.subscribe("/v1.6/devices/substation-gateway/relay")
            time.sleep(10)
        
    def publish(self, mqtt_client, topic, payload): 
        
        """
        Publish SensorData to Ubidots cloud service
        """
        try:
            mqtt_client.publish(topic, payload)
            mqtt_client.on_publish = on_publish
        except Exception as e:
            print("[ERROR] Could not publish data, error: {}".format(e))
    
    def subscribe(self, topic):
        """
        Subscribe ActuatorData from Ubidots cloud service
        """
        mqtt_client.subscribe(topic)
        mqtt_client.on_message = on_message
    
    def get_connected_flag(self):
        """
        Function which returns status of connected_flag
        * Output: True/False(boolean)
        """
        return connected_flag
    
    def get_publish_flag(self):
        """
        Function which returns status of publish_flag
        * Output: True/False(boolean)
        """
        return publish_flag
    
    def get_subscribe_flag(self):
        """
        Function which returns status of subscribe_flag
        * Output: True/False(boolean)
        """
        return subscribe_flag
    
    def get_act_obj(self):
        """
        Function which returns act_obj
        * Output: act_obj(object)
        """
        return act_obj

    
def on_connect(mqtt, userdata, flags, rc):
    '''
    * MQTT Callback function on connection establishment
    '''
    if rc == 0:
        logging.getLogger().info("Connected to MQTT Broker Successfully CONNACK Received")
    else:
        logging.getLogger().info("Bad connection - MQTT Broker Not Running")


def on_publish(mqtt, userdata, result):  # create function for callback
    '''
    * MQTT Callback function on publishing json data to MQTT Broker
    '''    
    global publish_flag
    logging.info("Data Published to Ubidots ------------------------------------------------>>>>>>>> ")
    publish_flag = True


def on_message(mqtt, userdata, message):
    
    '''
    * MQTT Callback function on receiving json ActuatorData via mqtt
    ''' 
    logging.info(" <<<<<<<<<<<-------------------------------------Subscribed Data Received from Cloud ")
    global subscribe_flag
    
    act_data = str(message.payload.decode("utf-8")) 
    act_data_obj = convert_json.jsonToUbidotsActuatorData(act_data) 
    
    if(act_data_obj.value == 1.0):
        act_obj.setRelay(True)
        logging.info("Relay On")
        subscribe_flag = True
    
    else:
        act_obj.setRelay(False)
        logging.info("Relay Off")
