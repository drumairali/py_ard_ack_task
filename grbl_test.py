import time
import serial
PORT = '/dev/ttyACM0'
class GRBL_Controller():
    def __init__(self, serial_port=PORT):
        self.s = serial.Serial(serial_port, 115200,timeout=0.01)
        # self.send_g_command("$20=0")
        # self.send_g_command("$21=0")
        # self.send_g_command("$22=0") # disable homing sequence (ALARM:2)
        self.s.write('\r\n\r\n'.encode())
        time.sleep(2)
        self.s.flushOutput()
        self.s.flushInput()

    def send_g_command(self, command):
        result = ''
        try:
            while not self.s.writable():
                print('not writable')
            self.s.write((command + '\n').encode())  # Send g-code block to grbl
            status = ''
            while 1:
                msg = self.s.readlines()
                print(command,msg)
                if len(msg) >0:
                    status = msg[0].strip().decode()
                    for m in msg:
                        if  m.strip().decode().find('ok') >= 0:
                            result = 'ok'

                        if  m.strip().decode().find('error') >= 0:
                            result = 'error'

                        if  m.strip().decode().find('ALARM') >= 0:
                            result = 'alarm'

                if (result == 'ok') or (result =='alarm') or (result == 'error'):
                    break

        except Exception as e:
            print('Command:', e)
            result = False

        print('Command:', command, status, msg)
        self.get_status()
        print("RES:",result)
        return result

    def get_status(self):
        try:
            grbl_status= ''
            self.s.write(('?').encode())
            msg = self.s.readlines()
            if len(msg) > 0:
                grbl_status = msg[0].strip().decode()
            while not grbl_status.find('Run')<0:
                self.s.write(('?').encode())
                msg = self.s.readlines()
                if len(msg) >0:
                    grbl_status = msg[0].strip().decode()
            print('Status:',grbl_status)
            # print(grbl_out.strip())
        except Exception as e:
            pass

    def unlock_robot(self):
        print("Unlocking robot...")
        self.send_g_command("$X")

    def home_robot(self):
        print('Homing robot...')
        g.send_g_command('$HZ')
        g.send_g_command('$HX')
        g.send_g_command('$HY')
        g.send_g_command('$HA')

    def init_robot(self):
        print('Init robot...')
        g.send_g_command('G55')

    def set_machine_output(self):
        print('Setting outputs 1;2 to OFF...')
        g.send_g_command('M9')
        g.send_g_command('M5')

    def go_to_park(self):
        print('Moving to park...')
        g.send_g_command('G0 A90 X-0 Y-100')

    def go_to_pos(self,X=0,Y=0):
        print('Moving to pos X',X,"Y",Y,'...')
        g.send_g_command('G0 X'+str(X)+' Y'+str(Y)+'Z0')

    def pick_up(self,Z=0):
        print('Picking up...')
        g.send_g_command('G0 A13')
        g.send_g_command('M7')
        g.send_g_command('G0 Z'+str(Z))
        time.sleep(2)
        g.send_g_command('G0 Z-0')

    def place_down(self):
        print('Placing down...')
        g.send_g_command('G0 A90 X-0 Y-100 Z0')
        g.send_g_command('Z-50')
        g.send_g_command('M9')
        time.sleep(2)
        g.send_g_command('G0 Z-0')

    def index_bowl(self):
        print('Indexing bowl...')
        for i in range(0, 2):
            for j in range(0,3):
                self.send_g_command("M3")
                time.sleep(1)
            for j in range(0,3):
                self.send_g_command("M5")
                time.sleep(1)

        self.send_g_command("G0")
        self.send_g_command("B90")

    def finish_gcode(self):
        self.send_g_command("M30")
        
    ###umair Defined some functions
    def ack_to_process_move_txt(self):
        while True:  
            ard_ack = input("type 1 and press enter to get acknowledge from arduino: ")
            if ard_ack=="1":
                line = self.s.readline()
                print(line)
                directory = "txtfiles/"
                list_file= [directory+"PICKUP_GCODE.txt",directory+"STEM_CUTTING_GCODE(STATIC).txt",\
                            directory+"DROPOFF_GCODE2.txt",directory+"DROPOFF_GCODE.txt"]
                data = self.generate_move(list_file)
                
                value = self.write_(data)
                
    def write_(self,x):
        ebytes = bytes(x, 'utf-8')
        self.s.write(ebytes)
        print(ebytes)
        time.sleep(0.1)
    
        
    def generate_move(self, name_file):
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
    print('\n\n')
    g = GRBL_Controller()
    print('\n\n')
    g.unlock_robot()
    print('\n\n')
    g.home_robot()
    print('\n\n')
    g.unlock_robot()
    print('\n\n')
    g.init_robot()
    print('\n\n')
    g.set_machine_output()
    print('\n\n')
    g.go_to_park()
    print('\n\n')
    g.go_to_pos(10,10)
    print('\n\n')
    g.pick_up(-10)
    print('\n\n')
    g.index_bowl()
    print('\n\n')
    g.finish_gcode()
    print('\n\n')
    print('CODE FINISHED')