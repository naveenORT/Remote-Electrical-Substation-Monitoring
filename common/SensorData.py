'''
Created on Jan 23, 2020
@author: Naveen Rajendran
'''
from datetime import datetime 
import logging
'''
* This class logs value from sensor continuously, whenever addValue function is passed with sensor values  

'''


class SensorData():
    
    timeStamp = None  # Initializing the parameters
    name = 'Not set'
    curValue = 0.0
    avgValue = 0.0
    minValue = 0.0 
    maxValue = 0.0
    totValue = 0.0
    sampleCount = 0
    
    '''
    * Default Constructor which records time stamp
    '''

    def __init__(self):
        self.timeStamp = str(datetime.now())  # Constructor

    '''
    * Function used for storing or logging sensor values in continuous stream
    * Input : Sensor Values (float)
    '''

    def addValue(self, newVal):
        self.sampleCount += 1
        self.timeStamp = str(datetime.now())
        self.curValue = round(newVal,1)
        self.totValue += round(newVal,1)
        self.setActuationState(True)
        
        if(self.sampleCount == 1):
            self.minValue = self.curValue
        
        elif (self.curValue < self.minValue):  # Assign Minimum Temperature Value
            self.minValue = self.curValue
        
        if (self.curValue > self.maxValue):  # Assign Maximum Temperature Value
            self.maxValue = self.curValue
        
        if (self.totValue != 0 and self.sampleCount > 0):  # Computing Average Value
            self.avgValue = round( self.totValue / self.sampleCount,2)

        curValue = "curValue = " + str(round(self.curValue, 1))  # converting all parameters to string type 
        avgValue = "avgValue = " + str(round(self.avgValue, 1))
        minValue = "minValue =" + str(round(self.minValue, 1))
        maxValue = "maxValue =" + str(round(self.maxValue, 1))
        totValue = "totValue =" + str(round(self.totValue, 1))
        sampleCount = "sample count =" + str(self.sampleCount)
        
        logging.getLogger().info("----------------------------------------Values From =" + self.get_sensor_name() + "---------------------------")
        logging.getLogger().info(curValue)        
        logging.getLogger().info(avgValue)
        logging.getLogger().info(minValue)
        logging.getLogger().info(maxValue)
        logging.getLogger().info(totValue)
        logging.getLogger().info(sampleCount)
        logging.info("_________________________________________________________________________________________________________________________________")
   
    '''
    * Standard getter function
      Output: curValue(Float)
    '''   

    def getcurvalue(self):
        return self.curValue

    '''
    * Standard getter function
      Output: avgValue(Float)
    '''   

    def getavgvalue(self):
        return self.avgValue

    '''
    * Standard getter function
      Output: minValue(Float)
    '''   

    def getminvalue(self):
        return self.minValue

    '''
    * Standard getter function
      Output: maxValue(Float)
    '''   

    def getmaxvalue(self):
        return self.maxValue

    '''
    * Standard getter function
      Output: totvalue(Float)
    '''   

    def gettotvalue(self):
        return self.totValue

    '''
    * Standard getter function
      Output: samplecount(Int)
    '''   

    def getsamplecount(self):
        return self.sampleCount
    
    '''
    * Standard getter function
      Output: timestamp(Date-Time)
    '''   

    def gettimestamp(self):
        return self.timeStamp

    '''
    * Standard setter function
      Input: Sensor_Name(String)
    '''

    def set_sensor_name(self, sensor_name):
        self.name = sensor_name

    '''
    * Standard getter function
      output: Sensor_Name(String)
    '''

    def get_sensor_name(self):    
        return self.name

    '''
    * Standard setter function
      Input: True or False (Boolean)
    '''

    def setActuationState(self, in_value):    
        self.Actuation_State = in_value

    '''
    * Standard getter function
      Output: True or Flase (Bool)
    '''    

    def getActuationState(self):    
        return True
