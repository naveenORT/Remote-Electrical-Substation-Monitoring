'''
Created on Feb 20, 2020
@author: Naveen Rajendran
'''
import json
import logging
import redis
from labs.common.AData import AData
from labs.module09.ActuatorData import ActuatorData
import pickle
'''
* Python module which provides essential tools to convert to/from Json object to/from SensorData object or ActuatorData object
'''


class DataUtil():
    '''
    * Class constructor function
    '''    

    def __init__(self):
        logging.info("Using Data Utilities")

    '''
    * Public function to conver json string data to ActuatorData object
    * Output: ActuatorData (object)
    '''        

    def jsonToUbidotsActuatorData(self, jsonData):        
        adDict = json.loads(jsonData)
        ad = ActuatorData()
        ad.value = adDict["value"]
        ad.created_at = adDict["created_at"]
        ad.timestamp = adDict["timestamp"]
        ad.context = adDict["context"]
        print(" decode [post] --> " + str(ad.value))
        return ad 

    def jsonToActuatorData(self, jsonData):        
        adDict = json.loads(jsonData)
        ad = AData()
        ad.sensor_name = adDict["sensor_name"]
        ad.input_command = adDict["input_command"]
        ad.current_actuator_status = adDict["current_actuator_status"]
        ad.sensor_value = adDict["sensor_value"]
        ad.actuation_state = adDict["actuation_state"]
        print(" decode [post] --> " + str(ad.sensor_name))
        print(" decode [post] --> " + str(ad.input_command))
        print(" decode [post] --> " + str(ad.current_actuator_status))
        print(" decode [post] --> " + str(ad.sensor_value))
        print(" decode [post] --> " + str(ad.actuation_state))
        return ad 
    
    '''
    * Public function to convert SensorData object to Json object
    * Input: SensorData (object)
    * Output: Json (String)
    ''' 

    def sensordatatojson(self, SensorData):    
        jsonSensor_Data = json.dumps(SensorData.__dict__)
        return jsonSensor_Data

    '''
    * Public function to write SensorData object to a file
    ''' 

    def writesensordatatofile(self, json_SensorData):
        with open('SensorData.txt', 'wb') as SensorData_file:
            pickle.dump(json_SensorData, SensorData_file)

    '''
    * Public function to convert ActuatorData object to json
    * Input: ActuatorData (object)
    * Output: Json (String)
    '''     

    def actuatordatatojson(self, ActuatorData):
        jsonActuator_Data = json.dumps(ActuatorData.__dict__) 
        return jsonActuator_Data

    '''
    * Public function to write ActuatorData object to a file
    '''     

    def writeactuatordata(self, json_ActuatorData):            
        with open('ActuatorData.txt', 'wb') as ActuatorData_file:
            pickle.dump(json_ActuatorData, ActuatorData_file)
   
