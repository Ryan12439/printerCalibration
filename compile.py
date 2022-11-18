defZ = 5.8 # Z height in mm
defZMove = 8 # Z height in mm
defDwell = 15 # Seconds to stay at each location
defSpeed = 3000 # Speed to move toolhead in mm/s
defHome = True # Whether to home the toolhead before calibration
defHomeAtEnd = True # Wheater to home after calibration done
defDisableMotors = True # Disable motors at file finish
defOverwrite = False # Whether to overwrite the file if it already exists

gcode = {
    "MOVE": "G1",
    "DWELL": "G4",
    "HOME_ALL": "G28",
    "ABSOLUTE_POS": "G90",
    "DISABLE_MOTORS": "M84"
}

def compile(fileName: str, levelLocationsX: list[int], levelLocationsY: list[int], dwell: int = defDwell, speed: int = defSpeed, home: bool = defHome, homeAtEnd: bool = defHomeAtEnd, zHeight: float = defZ, zMove: float = defZMove, disableMotors: bool = defDisableMotors, overwrite: bool = defOverwrite) -> str:
    file = None

    try:
        if overwrite:
            file = open(f'{fileName}.gcode', 'w')
        else:
            file = open(f'{fileName}.gcode', "x")
    except FileExistsError:
        print("Error, the file specified already exists. Please specify a different file name or enable overwrite.")
        exit()

    
    output = [
        f'; {fileName}',
        f'; Leveling locations X: {levelLocationsX}',
        f'; Leveling locations Y: {levelLocationsY}',
        f'; Dwell time: {dwell}',
        f'; Speed: {speed}',
        f'; Home before calibration: {home}',
        f'; Home after calibration: {homeAtEnd}',
        f'; Z height: {zHeight}',
        f'; Z move height: {zMove}',
        f'; Disable motors at end: {disableMotors}',
        '',
        ''
    ]

    output.append(gcode["ABSOLUTE_POS"]) # Set to absolute positioning mode

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
