'''
Created on Jan 23, 2020
@author: Naveen Rajendran
''' 
from configparser import ConfigParser
import logging
'''
* Module which helps in extracting technical properties from configuration file located in local storage
'''


class ConfigUtil:
       
    config = ConfigParser()
    default_dir = r"home/pi/workspace/iot-device/apps/labs/common/ConnectedDevicesConfig.props"
    
    '''
    * Class constructor function which loads properties of config file from location specified by user
    * Input: path (String)
    '''

    def __init__(self, path):  # Constructor
        self.path = path
        self.loadConfig(path)

    '''
    * Public function which returns the value of key specified by user
    * Input: path (String)
    ''' 

    def getValues(self, section, key):  # Function to extract values mapped along with keys    
        return self.config.get(section, key)

    '''
    * Public function to check existence of given section
    * Output: boolean
    ''' 

    def hasSection(self, sec_name):  # Function to check the existence of section
        if self.config.has_section(sec_name):
            return 1

    '''
    * Public method to load properties from file using configparser library function
    '''     

    def loadConfig(self, path):  # Function to load config properties from the file
        try:
            if self.hasConfig():
                self.config.read(path, encoding=None)
            else:    
                self.config.read(self.default_dir)
        except:
            logging.info("File doesn't exist loading default")        

    '''
    * Standard getter function
    * Output: path (String)
    '''  

    def getpath(self):  # Function to get path name of config file
        return self.path

    '''
    * Public function to check existence of config file
    * Output: boolean
    ''' 

    def hasConfig(self):  # Checking the existence of config file in the harddisk     
        try:
            f = open(self.path)
            return 1
        except IOError:
            print("File not accessible")
        finally:
            f.close()

