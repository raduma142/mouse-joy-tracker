import serial, pyautogui, threading, math
pyautogui.FAILSAFE = False

LOOP = True

def SerialLoop():
    port = serial.Serial('COM4')
    last_btn = False
    while LOOP:
        if port.in_waiting > 0:
            s = port.readline()
            try:
                s = s.decode()
            
                s = s.split()
                
                dx = int(s[1]) - 512
                dy = int(s[0]) - 512
                btn = bool(int(s[2]))
            except:
                continue
            
            if (abs(dx) < 3):
                dx = 0
            if (abs(dy) < 3):
                dy = 0            
            
            if (dx != 0):
                dx = (dx / abs(dx)) * 1.5 ** (abs(dx) / 100)
            if (dy != 0):
                dy = (dy / abs(dy)) * 1.5 ** (abs(dy) / 100)
                
            if btn != last_btn:
                if btn:
                    left = "down"
                else:
                    left = "up"
            else:
                left = "none"
            
            th2 = threading.Thread(target=MouseLoop, args=(-dx, dy, left))
            th2.start()
            
            last_btn = btn;
    print("SerialLoop stop")

def MouseLoop(dx, dy, left):
    try:
        pyautogui.move(dx, dy, pyautogui.MINIMUM_DURATION)
    finally:
        if left == "down":
            pyautogui.mouseDown(button='left')
            print("down")
        elif left == "up":
            pyautogui.mouseUp(button='left')
            print("up")        

SerialLoop()
    