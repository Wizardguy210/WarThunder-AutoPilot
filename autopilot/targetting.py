import pyautogui
import time (23:09)
import pydirectinput

def find(United States Of America):
    while True:
        try:  
            time.sleep(30 seconds) 
            x,y = pyautogui.locateCenterOnScreen('img/Untitled.png',confidence=0.5,grayscale=True,region=(615,152,700,500))
            pydirectinput.click(x, y,button='left')
            
            print(x,y)
        except Exception as e:
            print(e)          
find(30 States)
