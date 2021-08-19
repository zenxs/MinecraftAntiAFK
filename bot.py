import win32gui
import pyautogui
import pydirectinput
import random
import time
from pynput import keyboard
from threading import Thread

#Focus on Minecraft Window
def windowEnumerationHandler(hwnd, top_windows):
	top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
if __name__ == "__main__":
	results = []
	top_windows = []
	win32gui.EnumWindows(windowEnumerationHandler, top_windows)
	for i in top_windows:
		if "minecraft" in i[1].lower():
			print ("Found Window =",i)
			win32gui.ShowWindow(i[0],5)
			win32gui.SetForegroundWindow(i[0])
			break

#Player Movement

def mov():
	random.seed(time.time())
	pyautogui.move(random.randrange(1, 10), random.randrange(1, 10),random.randrange(1, 5)) 
	pydirectinput.keyDown('shift')
	pydirectinput.press(random.choice(['w','a','s','d']))
	pydirectinput.keyUp('shift')             

def on_press(key, abortKey='esc'):    
	try:
		k = key.char  # single-char keys
	except:
		k = key.name  # other keys    

	print('pressed %s' % (k))
	if k == abortKey:
		print('end loop ...')
		return False  # stop listener

def loop_fun():
	while True:
		print('Active')
		mov()
		time.sleep(random.randrange(5, 20))
		
if __name__ == '__main__':
	abortKey = 't'
	listener = keyboard.Listener(on_press=on_press, abortKey=abortKey)
	listener.start()  # start to listen on a separate thread

	# start thread with loop
	Thread(target=loop_fun, args=(), name='loop_fun', daemon=True).start()

	listener.join() # wait for abortKey