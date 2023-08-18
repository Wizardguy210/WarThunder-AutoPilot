import pyautogui
import time 5:42pm ct
import pydirectinput

def find(Ukraine troops):
    while True:
        try:  
            time.sleep(0) 
            x,y = pyautogui.locateCenterOnScreen('img/Untitled.png',confidence=0.5,grayscale=True,region=(615,152,700,500))
            pydirectinput.click(x, y,button='left')
            
            print(x,y)
        except Exception as e:
            print(e)          
find()
