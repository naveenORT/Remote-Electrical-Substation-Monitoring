'''
Created on Apr 8, 2020
@author: Naveen Rajendran
'''
import logging
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

from labs.module09.ArduinoDataReceiver import ArduinoDataReceiver
from labs.module09.OPC_Client_Rpi import OPC_Client_Rpi
from labs.module09.SensorDataManager import SensorDataManager
from labs.module09.DevicePerformanceMonitor import DevicePerformanceMonitor
from labs.module09.UbidotsCloudConnector import UbidotsCloudConnector        
from labs.module09.AWS_Cloud_Connector import AWS_Cloud_Connector
import time

"""
Gateway Module which handles all the essential functions to deliver end to end iot solution. Invokes multiple threads that
performs particular dedicated function
"""    
class GatewayHandlerApp():       

    
    SensorData_Object = ArduinoDataReceiver()  # Get Data from Constrained Device
    SensorData_Object.start()
    
    OPC = OPC_Client_Rpi()  # Backup data at OPC_ ServeR
    OPC.start()
    
    time.sleep(10)
    
    SDM = SensorDataManager()  # Publish SensorData to ubidots Cloud & Trigger Notification
    SDM.start()
    
    DPM = DevicePerformanceMonitor()  # Compute Device Performance
    DPM.start()

    UCC = UbidotsCloudConnector()  # Publish & Subscribe Data from Ubidots Cloud Service
    UCC.start()

    AWS = AWS_Cloud_Connector()  # Publish & Subscribe Data from AWS  Cloud Cloud Service
    AWS.start()
    

    def getArduino_Receiver_Obj(self):
        """
        Getter function to return Sensor_Data Object
        Output: Sensor_Data (Object) 
        """
        return self.SensorData_Object
    
    def getOPC_Client_Rpi(self):
        """
        Getter function to return OPC_Data Object
        Output: OPC (Object) 
        """
        return self.OPC
    
    def getSensorDataManager(self):
        """
        Getter function to return Sensor_Data_Manager Object
        Output: SDM (Object) 
        """
        return self.SDM

    def devicePerfMonit(self):
        """
        Getter function to return devicePerfMonit Object
        Output: DPM (Object) 
        """
        return self.DPM
    
    def getUbidotsCloudConnector(self):
        """
        Getter function to return UbidotsCloud_Data Object
        Output: OCC (Object) 
        """
        return self.UCC


x = GatewayHandlerApp()    
