'''
Created on Feb 20, 2020
@author: Naveen Rajendran
'''
from labs.common.DataUtil import DataUtil
import redis
import logging
from labs.common.ActuatorData import ActuatorData
from labs.common.SensorData import SensorData

util = DataUtil()
"""
* This class is used for writing Actuator/Sensor JSON data in Redis DataBase
"""   


class PersistenceUtil():
    """
    * PersistenceUtil constructor function check for Actuator/SensorData instance & converts into JSON string using DataUtil class functions
    * Input: SensorData (Object) or ActuatorData (Object)
    """

    def __init__(self, input_obj):
        
        if (isinstance(input_obj, SensorData)):
            self.sdo = input_obj
            self.sd = util.sensordatatojson(self.sdo) 
            self.writeSensorDatatoDbms(self.sd)
            
        elif (isinstance(input_obj, ActuatorData)):
            self.ado = input_obj
            self.ad = util.actuatordatatojson(self.ado)
            self.writeActuatorDatatoDbms(self.ad)
    
    """
    * This function writes ActuatorData to Redis DataBase 
    * Input: json_string
    """

    def writeActuatorDatatoDbms(self, json_actuator_data):    
        self.redis_actuator_data = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
        self.redis_actuator_data.set('ActuatorData', json_actuator_data)

    """
    * This function writes SensorData to Redis DataBase 
    * Input: json_string
    """ 

    def writeSensorDatatoDbms(self, json_sensor_data):    
        self.redis_sensor_data = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
        self.redis_sensor_data.set('SensorData', json_sensor_data)
    
    def getsd(self):
        return self.sd
    
    def getad(self):
        return self.ad
    
