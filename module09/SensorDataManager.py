'''
Created on Apr 9, 2020

@author: Naveen Rajendran
'''
import logging
import threading
import time
from labs.module09.lib_nrf24 import NRF24
import spidev
import RPi.GPIO as GPIO
from labs.module09.ArduinoDataReceiver import SensorData_Object
from labs.module09.SmtpClientConnector import smtpconnect
from labs.module09.UbidotsCloudConnector import act_obj
SMTP = smtpconnect()
radio = NRF24(GPIO, spidev.SpiDev())
"""
Python class module which helps to perform triggering & actuation of an event based on received SensorData 
"""        


class SensorDataManager(threading.Thread):
    
    def __init__(self):
        """
        Class constructor 
        """        
        logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
        threading.Thread.__init__(self)
        
    def send_notification(self):
        """
        Function which perfoms alert triggering using SMTPClientConnector class function 
        """        
        if(SensorData_Object != None):
            
            if (SensorData_Object.getHumidity() > 50):
                
                logging.info("Humidity Exceeded By: " + str(SensorData_Object.getHumidity() - 50) + " Units")
                data = "Excess Humidity Value Detected @ Site" + str(SensorData_Object.getHumidity())
                SMTP.publishMessage("Excess Humidity Detected", data)
        
            if (SensorData_Object.getResistence() > 110):
                
                logging.info("Resistence Exceeded By: " + str(SensorData_Object.getResistence() - 110) + " Units")
                data = "Excess Resistance Value Detected @ Site" + str (SensorData_Object.getResistence())
                SMTP.publishMessage("Excess Resistance Detected", data)
        
            if (SensorData_Object.getCorona() > 50):
                
                logging.info("Corona-Level Exceeded By: " + str(SensorData_Object.getCorona() - 50) + " Units")
                data = "Excess Corona_level Value Detected @ Site" + str (SensorData_Object.getCorona())
                SMTP.publishMessage("Excess Corona Detected", data)
        
            if (SensorData_Object.getTemperature() > 40):
                
                logging.info("Temperature Level Exceeded By: " + str(SensorData_Object.getTemperature() - 40) + " Units") 
                data = "Excess Temperartue Value Detected @ Site" + str(SensorData_Object.getTemperature())
                SMTP.publishMessage("Excess Temperature Detected", data)
        
            if (SensorData_Object.getMagFlux() > 50):
                
                logging.info("Temperature Level Exceeded By: " + str(SensorData_Object.getMagFlux() - 50) + " Units") 
                data = "Excess Induction Value Detected @ Site" + str(SensorData_Object.getTemperature())
                SMTP.publishMessage("Excess Magnetic Flux Detected", data)
        else:
            return

    def perform_actuation(self):
        """
        Function which uses NRF lora library to transmit actuation data to constrained device 
        """        
    
        if (act_obj.getRelay() != None):
            logging.info("\n" + "Actuator Data Received From cloud")
            
            message = list("H")
            
            while len(message) < 32:
                message.append(0)
            
            if (act_obj.getRelay() is True):
                radio.write(message)
                logging.info("Safety Relay Activated!!")
    
            elif (act_obj.getRelay() is False):
                message = 'L'
                radio.write(message)
                logging.info("Safety Relay Deactivated")
        
        else:
            logging.info("Actuation Not Required")
            return
    
    def enableRadio(self):
        """
        * Opening radio pipe to write data
        """
        pipe = [0xD2, 0XD2, 0XD2, 0XD2, 0XD2]
        radio.openWritingPipe(pipe)
                 
    def run(self):
        """
        * Repetitive thread function which triggers email notification & performs actuation
        """
        # self.enableRadio()
        while(1):
            self.send_notification()
            # self.perform_actuation()
            time.sleep(5)
    
    def getSMTP(self):
        """
        Get function which returns SMTP Client Connector Object
        Output: SMTP (Object)
        """
        return SMTP
