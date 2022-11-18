; Creality Ender Series/Ender 3 Max - 300x300 - 4 point
; Leveling locations X: [32, 270]
; Leveling locations Y: [29, 270]
; Dwell time: 15
; Speed: 3000
; Home before calibration: True
; Home after calibration: True
; Z height: 5.8
; Z move height: 8
; Disable motors at end: False


G90
G28
G1 Z8
G1 X32 Y29 F3000
G1 Z5.8
G4 P15000
G1 Z8
G1 X32 Y270 F3000
G1 Z5.8
G4 P15000
G1 Z8
G1 X270 Y29 F3000
G1 Z5.8
G4 P15000
G1 Z8
G1 X270 Y270 F3000
G1 Z5.8
G4 P15000
G1 Z8
G28