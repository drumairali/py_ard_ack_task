"""
this script is written to collect text data from different files and 
paste all data to single txt file then send that single text file serially
to arduino.

Redo this process again and again on 
acknowledgement from arduino
"""
 


import serial,time

def write_(x):
    ebytes = bytes(x, 'utf-8')
    arduino.write(ebytes)
    print(ebytes)
    time.sleep(0.1)

    

    
    
def generate_move(name_file):
    """This function takes file names and then concatenate their data to single move.txt file"""
    move = ""
    for i in name_file:
        with open(i) as f:
            file_data = f.read()
            move = move + file_data 
    with open('move.txt', 'w') as f:
        f.write(move)
    return move


if __name__ == "__main__":
    arduino = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=.1)   
 
    while True:  
        ard_ack = input("type 1 and press enter to get acknowledge from arduino: ")
        if ard_ack=="1":
            line = arduino.readline()
            print(line)
            directory = "txtfiles/"
            list_file= [directory+"PICKUP_GCODE.txt",directory+"STEM_CUTTING_GCODE(STATIC).txt",\
                        directory+"DROPOFF_GCODE2.txt",directory+"DROPOFF_GCODE.txt"]
            data = generate_move(list_file)
            
            value = write_(data)
        
            
        
        
# arduino code 
"""
String a;

void setup() {

Serial.begin(9600); // opens serial port, sets data rate to 9600 bps

}

void loop() {

while(Serial.available()) {

a= Serial.readString();// read the incoming data as string

Serial.println(a);

}

Serial.flush();

}
"""