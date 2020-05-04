'''
Created on Apr 2, 2020
@author: Naveen Rajendran
'''
from opcua import Client
import threading
import time
from labs.module09.ArduinoDataReceiver import SensorData_Object
import logging

"""
A widely used IIoT protocol for industrial data communication. This class tracks the data from Sensor Data & sends the parameter
values to OPC server running on a local area network
"""


class OPC_Client_Rpi(threading.Thread):

    def __init__(self):
        """
        * Module constructor function that connects OPC client at Raspberry pi with OPC Server
        """    
        threading.Thread.__init__(self)
        self.opc_client = Client("opc.tcp://10.0.0.57:4048")  # Connecting OPC Server Running ON Laptop
        self.opc_client.connect()
        self.initiate_nodes()  # Instantiating Nodes
     
    def initiate_nodes(self):    
        """
        * Connecting with nodes created at OPC Server for continuous data exchange
        """
        self.temp_value = self.opc_client.get_node('ns=2; s="Room_Temperature"')
        self.hum_value = self.opc_client.get_node('ns=2; s="Room_Humidity"')
        self.flux_value = self.opc_client.get_node('ns=2; s="Magnetic_Flux"')
        self.corona_level = self.opc_client.get_node('ns=3; s="Corona_Level"')
        self.resistance = self.opc_client.get_node('ns=3; s="Rod_Resistence"')
        
    def run(self):
        """
        * Runnable thread which sends the data collected from constrained device to OPC Server
        """
        time.sleep(5)
        while(1):
            time.sleep(5)
            temperature = SensorData_Object.getTemperature()
            self.temp_value.set_value(temperature)  # Publish Temperature Sensor Data
        
            humidity = SensorData_Object.getHumidity()
            self.hum_value.set_value(humidity)  # Publish Humidity Sensor Data
        
            flux = SensorData_Object.getMagFlux()
            self.flux_value.set_value(flux)  # Publish MagneticFlux Data
            
            corona_level = SensorData_Object.getCorona()
            self.corona_level.set_value(corona_level)  # Publish Corona Level Data
            
            Resistence = SensorData_Object.getResistence()
            self.resistance.set_value(Resistence)  # Publish Resistence Data
            
            logging.info("All Data Published to OPC Server")
