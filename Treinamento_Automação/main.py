import pyautogui as pa
import time as tm

pa.PAUSE = 2
pa.press('win')
pa.typewrite('Oracle VirtualBox')
pa.press('enter')
pa.sleep(5)
pa.click(x=507, y=108)
pa.press('T')