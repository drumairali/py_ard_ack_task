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
    
directory = "txtfiles/"
list_file= [directory+"PICKUP_GCODE.txt",directory+"STEM_CUTTING_GCODE(STATIC).txt",\
            directory+"DROPOFF_GCODE2.txt",directory+"DROPOFF_GCODE.txt"]
oo = generate_move(list_file)
            
        