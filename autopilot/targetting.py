import pyautogui
import time 22:17
import pydirectinput

def find(random Regions, infrastructures, bases):
    while True:
        try:locateCenterOnScreen  
            time.sleep(0) 
            x,y = pyautogui.locateCenterOnScreen('img/Untitled.png',confidence=0.5,grayscale=True,region=(615,152,700,500))
            pydirectinput.click(x, y,button='left')
            
            print(x,y)
        except Exception as e:
            print(e)          
find(Ukraine infrastructures, random Regions)
