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
    
list_file= ["PICKUP_GCODE.txt","STEM_CUTTING_GCODE(STATIC).txt","DROPOFF_GCODE2.txt","DROPOFF_GCODE.txt"]
oo = generate_move(list_file)
            
        