; Creality Ender Series/Ender 2 - 150x150 - 4 point
; Leveling locations X: [30, 140]
; Leveling locations Y: [30, 130]
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
G1 X30 Y30 F3000
G1 Z5.8
G4 P15000
G1 Z8
G1 X30 Y130 F3000
G1 Z5.8
G4 P15000
G1 Z8
G1 X140 Y30 F3000
G1 Z5.8
G4 P15000
G1 Z8
G1 X140 Y130 F3000
G1 Z5.8
G4 P15000
G1 Z8
G28