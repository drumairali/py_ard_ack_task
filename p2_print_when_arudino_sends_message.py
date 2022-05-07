#!/usr/bin/env python
# -*- coding: utf-8 -*-
# lsusb to check device name
#dmesg | grep "tty" to find port name

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
    