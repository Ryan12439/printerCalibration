defZ = 5.8 # Z height in mm
defZMove = 8 # Z height in mm
defDwell = 15 # Seconds to stay at each location
defSpeed = 3000 # Speed to move toolhead in mm/s
defHome = True # Whether to home the toolhead before calibration
defHomeAtEnd = True # Wheater to home after calibration done
defDisableMotors = False # Disable motors at file finish

gcode = {
    "MOVE": "G1",
    "DWELL": "G4",
    "HOME_ALL": "G28",
    "ABSOLUTE_POS": "G90",
    "DISABLE_MOTORS": "M84"
}

def compile(fileName: str, levelLocationsX: list[int], levelLocationsY: list[int], dwell: int = defDwell, speed: int = defSpeed, home: bool = defHome, homeAtEnd: bool = defHomeAtEnd, zHeight: float = defZ, zMove: float = defZMove, disableMotors: bool = defDisableMotors) -> str:
    file = None

    try:
        file = open(f'{fileName}.gcode', "x")
    except:
        print("Error, the file specified already exists.")
        exit()

    
    output = [gcode["ABSOLUTE_POS"]] # Set to absolute positioning mode

    if (home):
        output.append(gcode["HOME_ALL"]) # Home all axis
    
    for xPos in levelLocationsX:
        for yPos in levelLocationsY:
            output.append(gcode["MOVE"] + " Z" + str(zMove)) # Set Z to move height
            output.append(gcode["MOVE"] + " X" + str(xPos) + " Y" + str(yPos) + " F" + str(speed)) # Move to leveling location
            output.append(gcode["MOVE"] + " Z" + str(zHeight)) # Set Z to test height
            output.append(gcode["DWELL"] + " P" + str((dwell * 1000))) # Set wait time in ms
    
    if (homeAtEnd):
        output.append(gcode["MOVE"] + " Z" + str(zMove)) # Set Z to move height
        output.append(gcode["HOME_ALL"]) # Home all axis

    if (disableMotors):
        output.append(gcode["DISABLE_MOTORS"])

    out = "\n".join(output)


    file.write(out)
    file.close()

    print(f'File has been sucessfully created! Located at {fileName}.gcode')



compile("Ender3Pro", [32, 202], [36, 206])