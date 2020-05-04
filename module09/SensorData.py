'''
Created on Apr 8, 2020
@author: Naveen Rajendran
'''
import logging
"""
This data-storage python module provides functions to store various sensor's data, embedded in a single class object
"""


class SensorData():
    
    def __init__(self):
        """
        Class Constructor
        """
        self.temperature = 0
        self.humidity = 0
        self.corona_level = 0
        self.magflux = 0
        self.resistence = 0
        
        logging.info("Creating Sensor Data Object")
        
    def add_Temp_Value(self, input):
        """
        Function to set temperature value to class variable
        * Input: Temperature (Float)
        """
        self.temperature = input 
        
    def add_Humi_Value(self, input):
        """
        Function to set humidity value to class variable
        * Input: Humidity (Float)
        """
        self.humidity = input 
    
    def add_Mag_Value(self, input):
        """
        Function to set magnetic value to class variable
        * Input: Magnetic Flux (Float)
        """
        self.magflux = input
    
    def add_Cor_Value(self, input):
        """
        Function to set corona value to class variable
        * Input: Corona_Level (Float)
        """
        self.corona_level = input
    
    def add_Res_Value(self, input):
        """
        Function to set Resistence value to class variable
        * Input: Magnetic Flux (Float)
        """
        self.resistence = input
        
    def getTemperature(self):
        """
        Function to get temperature value 
        * Output: Temperature (Float)
        """
        return self.temperature
    
    def getHumidity(self):
        """
        Function to get humidity value 
        * Output: Humidity (Float)
        """
        return self.humidity
    
    def getMagFlux(self):
        """
        Function to get temperature value 
        * Output: Magnetic Flux (Float)
        """
        return self.magflux
    
    def getCorona(self):
        """
        Function to get temperature value 
        * Output: Corona_Level (Float)
        """
        return self.corona_level
    
    def getResistence(self):
        """
        Function to get temperature value 
        * Output: Resistence (Float)
        """
        return self.resistence
