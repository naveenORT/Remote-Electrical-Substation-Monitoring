'''
Created on Apr 2, 2020

@author: Naveen Rajendran
'''
import logging
class ArduinoSensorData():
    
    def __init__(self): 
        logging.info("Arduino_1 SensorData_Creating!!")
        
    def add_data_arduino1(self,ReceivedMessage):
        self.cabin_temperature = ReceivedMessage[0]
        self.room_humidity = ReceivedMessage[2]
        self.magnetic_flux = ReceivedMessage[4]
    
    def add_data_arduino2(self,ReceivedMessage):
        self.rod_resistence = ReceivedMessage[0]
        self.rod_distance = ReceivedMessage[2]
        