#!/usr/bin/python3
try:
	import keyboard
	from time import sleep
	import pyautogui
	import config
except Exception as error:
	print(error)

######################################################

# SHORTCUT BUTTONS CONFIG
#########################
shcut1 = config.shortcut1
shcut2 = config.shortcut2
shcut3 = config.shortcut3

# Additional config
###################
# duration between key detection cycles
# lower values will increase CPU usage
iter_sleep = config.iter_sleep 

######################################################

buttons = {"button1": (), "button2": (), "button3": ()}

def init_keys():
	print("To bind shortcuts press following keys while hovering mouse over click location:\nB = shortcut1\nS = shortcut2\nF = shortcut3")
	keys_to_init = 3
	while keys_to_init != 0:
		if keyboard.is_pressed("b") and len(buttons['button1']) == 0 :
			buttons['button1'] = pyautogui.position()
			keys_to_init = keys_to_init - 1
			print(f"button1 pos: {buttons['button1']}")
		elif keyboard.is_pressed("s") and len(buttons['button2']) == 0 :
			buttons['button2'] = pyautogui.position()
			keys_to_init = keys_to_init - 1
			print(f"button2 pos: {buttons['button2']}")
		elif keyboard.is_pressed("f") and len(buttons['button3']) == 0:
			buttons['button3'] = pyautogui.position()
			keys_to_init = keys_to_init - 1
			print(f"button3 pos: {buttons['button3']}")
		sleep(0.1)
	print("Click locations has been set")

def click_button(pos):
	# Get current mouse position
	curr_pos = pyautogui.position()
	# Click on button
	print(f"clicking {pos}")
	pyautogui.click(pos[0], pos[1])
	# Move mouse to previous position
	pyautogui.moveTo(curr_pos[0], curr_pos[1])

if __name__ == "__main__":
	init_keys()
	print("Clicker is running, now you can press shortcuts to perform clicks")
	while True:
		try:
			if keyboard.is_pressed(shcut1):
				click_button(buttons['button1'])
			elif keyboard.is_pressed(shcut2):
				click_button(buttons['button2'])
			elif keyboard.is_pressed(shcut3):
				click_button(buttons['button3'])
			sleep(iter_sleep)
		except KeyboardInterrupt:
			break
