'''
Created on Feb 20, 2020
@author: Naveen Rajendran
'''
import redis    
from labs.common.DataUtil import DataUtil
import threading
import time
'''
* This class listens to ActuatorData whenever it is recorded in redis DB
'''


class ActuatorDataListener(threading.Thread):
    
    redis_server = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)  # Initializing Redis Server
    util = DataUtil()
    actuation_counter = 1
    '''
    * Class constructor invoking thread
    '''

    def __init__(self):
        threading.Thread.__init__(self)

    '''
    * Boolean function which returns true whenever a new ActuatorData instance is recorded in database
    * Output: True/False (Boolean)
    '''      

    def on_Actuator_Message(self):    
         
        if(self.redis_server.exists(str(self.actuation_counter))):
            print("Above threshold ........LED actuation begins")
            self.x = self.redis_server.get(str(self.actuation_counter))
            self.y = self.util.jsonToActuatorData(self.x)
            self.actuation_counter = self.actuation_counter + 1
            return True

    '''
    * Runnable thread function
    '''     

    def run(self):
        while(True):
            self.on_Actuator_Message()
            time.sleep(6.5)

    def get_alo_object(self):
        return self.y

    def get_x_jsonactdata(self):
        return self.x
