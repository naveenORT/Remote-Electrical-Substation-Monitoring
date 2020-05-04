import logging
import RPi.GPIO as GPIO
from labs.module09.lib_nrf24 import NRF24
import time
import spidev
import threading
from sense_hat import SenseHat
from labs.module09.SensorData import SensorData
from labs.module09.DeviceData import DeviceData
from cmath import sqrt

# Global variables
GPIO.setmode(GPIO.BCM)  # Setting GPIO to BCM Mode
pipes = [[0xE8, 0xE8, 0xF0, 0xF0, 0xE1], [0xC2, 0xC2, 0xC2, 0xC2, 0xC2], [0x01, 0x02, 0x03, 0x04, 0x05], [0xD2, 0XD2, 0XD2, 0XD2, 0XD2]]
SensorData_Object = SensorData()  # SensorData Instance
DeviceData_Object = DeviceData()  # DeviceData Instance
sense = SenseHat()  # SenseHat Instance
radio = NRF24(GPIO, spidev.SpiDev())  # LoRA RF Library

"""
* Python module helps to poll data from Arduino via LoRA RF (nRF2401) transceiver module on a repetitive  scale 
* Also it helps in transmission of Actuator Data to constrained device
"""


class ArduinoDataReceiver(threading.Thread):
    
    def __init__(self):
        """
        * Class constructor which configures the RF parameters as per the requirement
        """
        logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
        threading.Thread.__init__(self)
        radio.begin(0, 17)  # Selecting CS Pin
        radio.setPayloadSize(32)  # Fixing the sizeofPayload
        radio.setChannel(0x76)  # Set channel at 0x76 address
        radio.setDataRate(NRF24.BR_1MBPS)  # Fixing data transmission rate
        radio.setPALevel(NRF24.PA_MIN)  # Transmission power level
        radio.setAutoAck(True)
        radio.enableDynamicPayloads()
        radio.enableAckPayload()
        radio.openReadingPipe(0, pipes[1])  # Reading pipe1 for Receiving data from Arduino 1
        radio.openReadingPipe(1, pipes[2])  # Reading pipe1 for Receiving data from Arduino 2
        radio.startListening()
        
    def run(self):
        """
        * Runnable thread function, which performs polling of data from constrained Device
        """
        radio.flush_rx()  # Clearing Radio Receiver
        while(1):
            self.receive_data_from_cabindevice()
            self.receive_data_from_elecrticpit()
            time.sleep(5)
 
    def receive_data_from_cabindevice(self):
        """
        * Function, which receives data from cabin device
          Input: Arduino Data Message (String)
        """
        arduinoMessage = []  # Payload Data
        radio.read(arduinoMessage, radio.getDynamicPayloadSize())  # Reading from Radio
        
        if(arduinoMessage[0] == 1):
            # print("Received from Cabin Device: {}".format(arduinoMessage))          
            print("\n")
            self.cabin_temperature = round(arduinoMessage[2] / 4, 2)  
            SensorData_Object.add_Temp_Value(round(sense.get_temperature(), 2))  # Temperature  
            logging.info("Cabin Temp:" + str(round(sense.get_temperature(), 2)))
            
            self.room_humidity = round(arduinoMessage[4] / 3, 2)
            SensorData_Object.add_Humi_Value(round(sense.get_humidity(), 2))     # Humidity
            logging.info("Room Humidity:" + str(round(sense.get_humidity(), 2)))
            
            mag = sense.get_compass_raw()
            mag_x = round(mag["x"], 2)
            mag_y = round(mag["y"], 2)
            mag_z = round(mag["z"], 2)
            mag_t = sqrt(abs(mag_x * mag_x + mag_y * mag_y + mag_z * mag_z))     # Magnetic_Flux
            logging.info("Magnetic Flux:" + str(round(abs(mag_t), 2)))
            # self.magnetic_flux = arduinoMessage[6] / 10
            SensorData_Object.add_Mag_Value(round(abs(mag_t), 2))
            
            if (arduinoMessage[8] == 1):
                DeviceData_Object.setArduino1_status(True)                      # Setting Status of Device 1 (On or OFF)
 
            else:
                DeviceData_Object.setArduino1_status(False)                     # Setting Status of Device 2 (On or OFF)
            
            time.sleep(0.5)
    
    def receive_data_from_elecrticpit(self):    
        """
        * Function, which receives data from electric_pit
          Input: Arduino Data Message (String)
        """
        arduinoMessage = []  # Payload Data
        radio.read(arduinoMessage, radio.getDynamicPayloadSize())
        
        if(arduinoMessage[0] == 2):
            # print("Received from Earthpit Device: {}".format(arduinoMessage)) 
            DeviceData_Object.setArduino2_status(True)  # Setting DeviceData Status
            self.rod_resistence = arduinoMessage[2]  
            SensorData_Object.add_Res_Value(round(self.rod_resistence, 2))
            logging.info("Earthpit Resistence " + str(self.rod_resistence))     # Resistence
            
            self.rod_length = arduinoMessage[4]
            SensorData_Object.add_Cor_Value(round(self.rod_length, 2))
            logging.info("Corona Level " + str(self.rod_length))                # Corona_Level
            logging.info("\n")
        
            if (arduinoMessage[6] == 1):
                DeviceData_Object.setArduino1_status(True)
            else:
                DeviceData_Object.setArduino1_status(False)
        
    def getSensorData_object(self):
        """
        * Function, which returns SensorData_Object instance
          Output: SensorData_Object (Object)
        """
        return SensorData_Object
    
    def getDeviceData_object(self):
        """
        * Function, which returns DeviceData_Object instance
          Output: DeviceData_Object (Object)
        """
        return DeviceData_Object
