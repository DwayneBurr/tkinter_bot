import pyautogui
import keyboard
import time
import threading
import random

# Global variable to control the clicker state
clicking = False

def clicker():
    while True:
        if clicking:
            pyautogui.click()
        time.sleep(random.uniform(0.2, 0.6))  # Adjust the clicking frequency (0.5 seconds)

def start_clicking():
    global clicking
    clicking = True

def stop_clicking():
    global clicking
    clicking = False

def main():
    # Create a separate thread to run the clicker
    click_thread = threading.Thread(target=clicker)
    click_thread.daemon = True
    click_thread.start()

    print("Press '`' to start clicking and 'z' to stop. Press esc button to quit")
    
    # Hotkeys
    keyboard.add_hotkey('`', start_clicking)
    keyboard.add_hotkey('z', stop_clicking)

    # Keep the script running
    keyboard.wait('esc')  # Press 'esc' to exit

if __name__ == "__main__":
    main()
