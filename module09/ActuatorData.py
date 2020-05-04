'''
Created on Apr 16, 2020

@author: Naveen Rajendran
'''


class ActuatorData():
    """
    Actuator Data Class, which helps to convert JSON web object to machine readable data object.  
    """
    value = ''
    timestamp = '' 
    context = ''
    created_at = ''
 
    def getValue(self):
        """
        Standard getfunction to obtain "value " from ActuatorData object received from cloud 
        Output: Value (Float)
        """
        return self.value
    
    def getTime(self):
        """
        Standard getfunction to obtain "timestamp" from ActuatorData object received from cloud 
        Output: time (Integer)
        """
        return self.timestamp
    
    def getContext(self):
        """
        Standard getfunction to obtain "context" from ActuatorData object received from cloud 
        Output: Value (String)
        """
        return self.context
    
    def getCreatedat(self):
        """
        Standard getfunction to obtain "created_at" from ActuatorData object received from cloud 
        Output: Value (Integer)
        """
        return self.created_at
