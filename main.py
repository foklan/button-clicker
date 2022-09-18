#!/usr/bin/python3
try:
	import keyboard
	import mouse
	from time import sleep
	import pyautogui
except Exception as error:
	print(error)

######################################################
######################################################

# SHORTCUT BUTTONS CONFIG
#########################
BUY = "ctrl+shift+b"
SELL = "ctrl+shift+s"
FLATTEN = "ctrl+shift+f"

# Additional config
###################
# duration between key detection cycles
# lower values will increase CPU usage
iter_sleep = 0.01

######################################################
######################################################

buttons = {"buy": (), "sell": (), "flatten": ()}

def init_keys():
	print("Press following keys while hovering mouse over button:\nB = buy button\nS = sell button\nF = flatten button")
	keys_to_init = 3
	while keys_to_init != 0:
		if keyboard.is_pressed("b") and len(buttons['buy']) == 0 :
			buttons['buy'] = mouse.get_position()
			keys_to_init = keys_to_init - 1
			print(f"BUY button pos: {buttons['buy']}")
		elif keyboard.is_pressed("s") and len(buttons['sell']) == 0 :
			buttons['sell'] = mouse.get_position()
			keys_to_init = keys_to_init - 1
			print(f"SELL button pos: {buttons['sell']}")
		elif keyboard.is_pressed("f") and len(buttons['flatten']) == 0:
			buttons['flatten'] = mouse.get_position()
			keys_to_init = keys_to_init - 1
			print(f"FLATTEN button pos: {buttons['flatten']}")
		sleep(0.1)
	print("Keys has been set")

def click_button(pos):
	# Get current mouse position
	curr_pos = mouse.get_position()
	# Click on button
	print("clicking")
	pyautogui.click(pos[0], pos[1])
	# Move mouse to previous position
	mouse.move(curr_pos[0], curr_pos[1], absolute=True, duration=0.0001)

print(buttons)

if __name__ == "__main__":
	init_keys()
	print("Listener runningi...")
	print("Press keyboard shortcuts to click on buttons")
	while True:
		try:
			if keyboard.is_pressed(BUY):
				click_button(buttons['buy'])
			elif keyboard.is_pressed(SELL):
				click_button(buttons['sell'])
			elif keyboard.is_pressed(FLATTEN):
				click_button(buttons['flatten'])
			sleep(iter_sleep)
		except KeyboardInterrupt:
			break
