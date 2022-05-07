"""send data from python to arduino serially"""

import serial,time


# Importing Libraries
import serial
import time
arduino = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=.1)
def write_(x):
    ebytes = bytes(x, 'utf-8')
    arduino.write(ebytes)
    print(ebytes)
    time.sleep(0.1)

    
while True:
    num = input("Enter a number: ") # Taking input from user
    value = write_(num)
    
    
# arduinoCode below 

# String a;

# void setup() {

# Serial.begin(9600); // opens serial port, sets data rate to 9600 bps

# }

# void loop() {

# while(Serial.available()) {

# a= Serial.readString();// read the incoming data as string

# Serial.println(a);

# }

# }