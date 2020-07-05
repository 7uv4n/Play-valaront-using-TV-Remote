# direct inputs
# source to this solution and code:
# http://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game
# http://www.gamespp.com/directx/directInputKeyboardScanCodes.html



import ctypes
import time
import serial
from pynput.keyboard import Key, Controller  #class i found later while coding

key=""
press=""
keyboard = Controller()

SendInput = ctypes.windll.user32.SendInput


W = 0x11
A = 0x1E
S = 0x1F
D = 0x20

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))



ArduinoSerial = serial.Serial('com3',9600)          #Create Serial port object called arduinoSerialData
time.sleep(0.1)  
while 1:
    incoming = str (ArduinoSerial.readline().decode())       #read the serial data and print it as line
    if "2F0" in incoming:
        press="W"
        key="W"
    if "2D0" in incoming:
        press="A"             #only returns 2d0 when button is held
    if "CD0" in incoming:
        press="D"
        key="D"
    if "AF0" in incoming:
        press="S"
        key="S"

    
    if "72E9" in incoming:
        press="shift"
        key="shift"
    if "A70" in incoming:
        press="space"
        key="space"
    if "32E9" in incoming:
        press="CTRL"
        key="CTRL"

    
    if "10" in incoming:
        if "810" not in incoming:
            if "410" not in incoming:
                if "C10" not in incoming:
                    press="1"
    if "810" in incoming:
        press="2"
    if "410" in incoming:
        press="3"
    if "C10" in incoming:
        press="4"


    
    if "52E9" in incoming:
        press="R"
        key="R"
    if "62E9" in incoming:
        press="Q"
        key="Q"
    if "6D25" in incoming:
        press="E"
        key="E"
    if "D58" in incoming:
        press="C"
        key="C"
    if "5D0" in incoming:
        press="X"
        key="X"
    if "36E9" in incoming:
        press="T"
        key="T"

    if "FFFFFFFF" in incoming:
        
        if "CTRL" in key:
            press="CTRL" #its working
        if "W" in key:
            press="W" #its working
        if "D" in key:
            press="D" #its working
        if "S" in key:
            press="S" #its working
        if "Q" in key:
            press="Q" #its working
        if "E" in key:
            press="E" #its working
        if "C" in key:
            if "CTRL" not in key:
                press="C" #its working
        if "X" in key:
            press="X" #its working
        if "T" in key:
            if "CTRL" not in key:
                press="T" #its working
        if "space" in key:
            press="space" #its working
        if "R" in key:
            if "CTRL" not in key:
                press="R" #its working
    print(press)
    if press=="W":
        PressKey(0x11)       
        time.sleep(0.05)
        ReleaseKey(0x11)
    if press=="A":
        PressKey(0x1E)     
        time.sleep(0.05)
        ReleaseKey(0x1E)
    if press=="S":
        PressKey(0x1F)      
        time.sleep(0.05)
        ReleaseKey(0x1F)
    if press=="D":
        PressKey(0x20)      
        time.sleep(0.05)
        ReleaseKey(0x20)
    
    if press=="Q":
        PressKey(0x10)
        ReleaseKey(0x10)
    if press=="E":
        PressKey(0x12)
        ReleaseKey(0x12)
    if press=="C":
        PressKey(0x2E)
        ReleaseKey(0x2E)
    if press=="X":
        PressKey(0x2D)
        ReleaseKey(0x2D)
    if press=="T":
        PressKey(0x14)
        ReleaseKey(0x14)
    
    if press=="R":
        PressKey(0x13)   
        time.sleep(0.05)
        ReleaseKey(0x13)
    if press=="space":
        PressKey(0x39)
        ReleaseKey(0x39)
    if press=="CTRL":
        keyboard.press(Key.ctrl_l)
        keyboard.release(Key.ctrl_l)

    if press=="1":
        PressKey(0x02)
        ReleaseKey(0x02)
    if press=="2":
        PressKey(0x03)
        ReleaseKey(0x03)
    if press=="3":
        PressKey(0x04)
        ReleaseKey(0x04)
    if press=="4":
        PressKey(0x05)
        ReleaseKey(0x05)



"""
left shift for walk,
spacebar for jump,
lctrl for crouch in toggle,
Equip Primacy Weapon	    1
Equip Secondary Weapon	    2
Equip Melee Weapon	        3
Equip Spike	                4
Reload	                    R
Use/Equip Ability: 1	    Q
Use/Equip Ability: 2	    E
Use/Equip Ability: 3	    C
Use/Equip Ability: Ultimate	X
Use Spray	                T

mouse controls in mouse
"""

    