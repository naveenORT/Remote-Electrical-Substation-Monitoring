'''
Created on Apr 10, 2020
@author: Naveen Rajendran
'''
"""
DeviceData class records parameters associated within the resources utilized by itself
"""


class DeviceData():
    
    def __init__(self):
        """
        * Class constructor function which initializes the cpu & memory data to zero
        """
        self.ram = 0
        self.cpu = 0
    
    def setArduino1_status(self, input):
        """
        Setter function which defines the state of Constrained Device 1
        Input: True or False (Boolean)
        """
        if (input == True):
            self.arduino1_status = 1
        else:
            self.arduino1_status = 0
    
    def setArduino2_status(self, input):
        """
        Setter function which defines the state of Constrained Device 2
        Input: True or False (Boolean)
        """
        if (input == True):
            self.arduino2_status = 1
        else:
            self.arduino2_status = 0
        
    def setMem_Util(self, input):
        """
        Setter function which sets memory % consumed by gateway device (Raspberry Pi)
        Input: CPU_MEM % (Float)
        """
        self.ram = input
        
    def setCpu_Util(self, input):
        """
        Setter function which sets memory % consumed by gateway device (Raspberry Pi)
        Input: CPU_RAM % (Float)
        """
        self.cpu = input
        
    def getArduino1_status(self):
        """
        Getter function returns the state of Constrained Device 1
        Output: True or False (Boolean)
        """
        return self.arduino1_status
    
    def getArduino2_status(self):
        """
        Getter function returns the state of Constrained Device 2
        Output: True or False (Boolean)
        """
        return self.arduino2_status
    
    def getMem_Util(self):
        """
        Getter function returns the RAM utilization of Gateway Device
        Output: CPU_MEM % (Float)
        """
        return self.ram
    
    def getCpu_Util(self):
        """
        Getter function returns the RAM utilization of Gateway Device
        Output: CPU_RAM % (Float)
        """
        return self.cpu
    
