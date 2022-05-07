"""
this script is written to collect text data from different files and 
paste all data to single txt file then send that single text file serially
to arduino.

Redo this process again and again on 
acknowledgement from arduino
"""
 
# # Importing Libraries
# import serial
# import time
# arduino = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=.1)
# def write_(x):
#     ebytes = bytes(x, 'utf-8')
#     arduino.write(ebytes)
#     print(ebytes)
#     time.sleep(0.1)

    
# while True:
#     num = input("Enter a number: ") # Taking input from user
#     value = write_(num)
    
with open('PICKUP_GCODE.txt') as f:
    pGcode = f.read()
    
    

        
        
    