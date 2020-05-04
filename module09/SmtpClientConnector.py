'''
Created on Jan 23, 2020

@author: Naveen Rajendran
''' 
import logging
import smtplib
from labs.common.ConfigUtil import ConfigUtil
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

logging = logging.getLogger("Main")
sent_flag = ''

"""
SMTP Client Connector class which uses smtp library to send mail via TLS Encryption
"""


class smtpconnect():
    msgBody = ''
    fromAddr = ''
    toAddr = ''
    host = ''

    def __init__(self):               
        """
        Constructor function which loads all the essential propertied from disk for setting up SMTP Client using
        ConfigUtil Class Function
        """
        self.config = ConfigUtil(r"/home/pi/workspace/iot-device/apps/labs/common/ConnectedDevicesConfig.props")
        logging.info('Configuration data...\n' + '\n' + str(self.config.config.sections()))  # Constructor loading config properties from the file
    
    def publishMessage(self, topic, data):  # Publishing Mail Via SMTP
        """
        Function to publish message , when an event is triggered
        *Input: topic(String) & data (String)
        """
        self.host = self.config.getValues("smtp.cloud", "host")
        port = self.config.getValues("smtp.cloud", "port")
        self.fromAddr = self.config.getValues("smtp.cloud", "fromAddr")
        self.toAddr = self.config.getValues("smtp.cloud", "toAddr")
        authToken = self.config.getValues("smtp.cloud", "authToken")
        
        msg = MIMEMultipart()
        msg['From'] = self.fromAddr
        msg['To'] = self.toAddr
        msg['Subject'] = topic
        self.msgBody = " Present Status!!! " + str(data)
        msg.attach(MIMEText(self.msgBody, "plain"))
              
        # send e-mail notification
        smtpServer = smtplib.SMTP_SSL(self.host, port)  # Creating SMTP server
        smtpServer.ehlo()
        smtpServer.login(self.fromAddr, authToken)  # Authentication
        msgText = msg.as_string()  # Converting to String
        smtpServer.sendmail(self.fromAddr, self.toAddr, msgText)  # Send Mail
        sent_flag = True
        logging.info("Successfully mailed alert from address " + self.fromAddr)
        
        smtpServer.close()
        
    def getfromAddr(self):
        """
        Function to get from_address
        * Output: fromAddr (String)
        """       
        return self.fromAddr

    def gettoAddr(self):       
        """
        Function to get to_address
        * Output: to_address (String)
        """       
        return self.toAddr
     
    def getmsgBody(self):
        """
        Function to get msg_body
        * Output: msg_body (String)
        """       
        return self.msgBody
     
    def getHost(self):
        """
        Function to get host_name
        * Output: host (Integer)
        """
        return self.host
    
    def getsentstatus(self):
        """
        Function to status of sent
        * Output: True or False (Boolean)
        """       
        return sent_flag
