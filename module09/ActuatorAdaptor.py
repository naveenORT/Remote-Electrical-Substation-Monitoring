'''
Created on Apr 16, 2020
@author: Naveen Rajendran
'''


class ActuatorAdaptor():
    """   
    Actuator Status assigning class , which determines the status of relay
    """

    def __init__(self):
        """
        Initial relay status, when constructor gets created
        """
        self.relay_status = False  # Relay @ Initial Position

    def setRelay(self, input):
        """   
        Set function to set status of Relay   
        Input: True (or) False (Boolean)
        """
        self.relay_status = input
   
    def getRelay(self):
        """   
        Get function to get status of Relay   
        Output: True (or) False (Boolean)
        """ 
        return self.relay_status
