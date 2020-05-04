'''
Created on Feb 6, 2020
@author: Naveen Rajendran
'''
from datetime import datetime 
import logging

'''
* This python class module records or logs condition of Actuator as per the input command given by user at origin
* This class gets updated whenever a new value from sensor is obtained
'''


class ActuatorData():
   
    '''
    Default Constructor of ActuatorData class, notifies user via log message before an actuation is done
    '''
    
    def __init__(self):
        logging.info("\n")
        logging.info("Going to Perform an Actuation")  # log status to notify actuation
    
    '''
    This class function receives the input_command, sensor_value and sensor_name & sets the state of actuator based on input_command
    given by user
    '''

    def addData(self, input_command, sensor_value, sensor_name):
        
        if(sensor_name == "Temperature Sensor"):
            self.sensor_name = sensor_name
            self.set_current_actuator_status(input_command)  # Setting actuator status
            self.sensor_value = sensor_value  # Store Sensor Value
            self.set_command(input_command)  # Setting input command
            self.setActuation_state(True)
        
        if(sensor_name == "Humidity_API"):
            self.sensor_name = sensor_name
            self.set_current_actuator_status(input_command)
            self.sensor_value = sensor_value  # Store Sensor Value
            self.set_command(input_command)  # Setting input command
            self.setActuation_state(True)
        
        if(sensor_name == "Humidity_I2C"):
            self.sensor_name = sensor_name
            self.set_current_actuator_status(input_command)
            self.sensor_value = sensor_value  # Store Sensor Value
            self.set_command(input_command)  # Setting input command
            self.setActuation_state(True)

        logging.info("Sensor Name = " + str(self.getName()))
        logging.info("Input Command =" + self.get_command()) 
        logging.info("Current Actuator Status =" + self.get_current_actuator_status())            
    
    '''
    Standard setter function for actuation state 
    Output: True or False (Boolean)
    '''

    def setActuation_state(self, in_value):
        self.actuation_state = in_value
    
    '''
    Standard getter function for actuation state
    Output: True or False (Boolean)
    '''

    def getActuation_state(self):
        return self.actuation_state

    '''               
    Standard getter function for command
    Output: command (String)
    '''

    def get_command(self):
        return self.input_command
   
    '''               
    Standard getter function for sensor_name
    Output: sensor_name(String)
    '''

    def getName(self):
        return self.sensor_name
    
    '''               
    Standard getter function for sensor_value
    Output: Float
    '''

    def getValue(self):
        return self.sensor_value
    
    '''               
    Standard getter function for sensor_value
    Output: True or False (Boolean)
    '''

    def get_current_actuator_status(self):
        return self.current_actuator_status
     
    '''               
    Standard setter function for sensor_name
    Input: input_command(sensor_name) 
    '''

    def setName(self, sensor_name):   
        self.sensor_name = sensor_name
        
    '''               
    Standard setter function for input_command
    Input: input_command(String) 
    '''

    def set_command(self, input_command):
        self.input_command = input_command
    
    '''               
    Standard setter function for actuator_status
    Input: command (String)
    '''

    def set_current_actuator_status(self, input_command):
        
        if input_command == "Increase Temperature":
            self.current_actuator_status = "Glowing RED"  # Set Status to RED
        
        if input_command == "Decrease Temperature":    
            self.current_actuator_status = "Glowing BLUE"  # Set Status to BLUE
        
        if input_command == "i2c_inbound":
            self.current_actuator_status = "green text message"
        
        if input_command == "api_inbound":
            self.current_actuator_status = "blue text message"
                
        if input_command == "temp_inbound":
            self.current_actuator_status = "showing api temp"
       
