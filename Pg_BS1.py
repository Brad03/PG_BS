import pyautogui as pg
import time

pg.hotkey('ctrl', 'winleft', 'd')
pg.hotkey('winleft')
pg.typewrite('chrome\n', 0.1)
time.sleep(2)
pg.hotkey('winleft','up')
pg.typewrite('youtube.com\n')
time.sleep(2.5)
pg.typewrite('daily fornite\n')
time.sleep(1.5)
pg.click (379, 336)
time.sleep(10)
pg.hotkey("ctrl", "t")
pg.typewrite('youtube.com\n')
