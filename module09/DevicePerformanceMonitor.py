'''
Created on Apr 9, 2020
@author: Naveen Rajendran
'''
import logging
from labs.module01.SystemMemUtilTask import memutil
from labs.module01.SystemCpuUtilTask import cpuutil
from labs.module09.ArduinoDataReceiver import DeviceData_Object
import time
import threading
"""
Python class module which polls CPU (RAM Memory & Process) utilization repetitively using psutil library
"""
class DevicePerformanceMonitor(threading.Thread):
    
    def __init__(self, count=100000):
        """
        * Class constructor Function which creates seperate instances for CPU % & RAM % Data Polling
        """
        logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
        threading.Thread.__init__(self)  # initializing thread function
        self.count = count
        self.x = memutil()  # creating memutil instance#
        logging.info("Memory utilization Instance Created")
        self.y = cpuutil()  # creating cpuutil instance#
        logging.info("CPU utilization Instance Created")
        logging.info("SPA Instance Created")
        
    def run(self):
        """
        Runnable thread function to poll data continuosly
        """
        while DevicePerformanceMonitor.is_alive(self):
            cpuData = "CPU Utilization = " + str(self.x.getSensorData()) 
            DeviceData_Object.setCpu_Util(self.x.getSensorData())
            memData = "Memory Utilization = " + str(self.y.getSensorData())
            DeviceData_Object.setMem_Util(self.y.getSensorData())
            logging.info(cpuData + "%")
            logging.info(memData + "%")
            time.sleep(3)  # Calling Thread Every 3 seconds  
            self.count -= 1  # Decrementing count call by 1            
            if self.count == 0:
                return  # stopping thread after executing 'N' times
          
