Connected Devices

Semester Project
Name and Course
● Name: Naveen Rajendran
● Course: Connected Devices
● Semester and Year: Spring 2020

Project Description:
Project Title: “IoT based live condition monitoring systems for electrical substations & industrial switchgears”

 Electrical substations & switchgears serves as the power hub of continuous manufacturing industries & power-plants. They are functional 24x7 due to meet high demand in supply chain prevailing in market. These electrical power distribution systems deployed in current industries seems to be reliable, but in long term they may cause sudden catastrophic events like electrical short-circuiting, tripping & flashing due to lack of scheduled periodic maintenance of electrical feeders & organization’s negligence pertaining to continuous power-distribution. This project provides low cost reliable, remote & wireless monitoring solutions for electrical substations located at remote worksite. Parameters such as magnetic flux, ground resistivity, temperature inside power cabins & corona level will be monitored continuously, in order to avoid imminent power shutdown

 This problem falls under industrial internet of things (IIoT) category, which requires us to use special industrial inter-operability standard that can communicate information to enterprise SCADA (Supervisory control & data acquisition). Hence OPC (Open platform communication) protocol helps to log data locally & LoRA-RF wireless transceivers to communicate between device to gateway. Further the data from gateway will be published to AWS & Ubidots cloud via MQTT/TLS

 Further cloud data can be analyzed properly to predict failures or schedule maintenance of HV electrical equipment

Implementation Strategy:

 GatewayHandlerApp present in Raspberry Pi starts 6 different threads which performs various tasks to achieve desired outcomes of the project

 Thread 1 - ArduinoDataReceiver class receives data from field sensors connected to (Arduino 1 & 2) constrained devices using LoRA RF protocol

 Thread 2 - Creates OPC-Client instance on raspberry pi, which transfers data to OPC server running on laptop. This data can be historized & recorded as backup

 Thread 3 - SensorDataManager performs the task of triggering & actuation. It collects the Sensor data from ArduinoDataReceiver class & actuator data from ubidots client connector class. Based on sensor data collected this class triggers e-mail notification to engineer in charge using SMTP client connector class. Based on actuator data received from cloud, actuation event is performed by sending actuation command to relay connected with Arduino at remote location, with the help of LoRA RF class protocol

 Thread 4 - Device performance monitoring class which records the details of resource utilized by gateway device

 Thread 5 - Ubidots cloud connector class, that help to publish sensordata & subscribe to actuator data

 Thread 6 - AWS Cloud connector class, that help to publish sensordata & subscribe to actuator data
