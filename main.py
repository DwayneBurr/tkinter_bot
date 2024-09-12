import tkinter as tk
import threading
import subprocess
import pyautogui
import keyboard
import time
import random
# from mouse_listener import start_mouse_listener, stop_mouse_listener, start_hotkey_listener, set_update_callback
import webbrowser

def open_donate_link(event):
    webbrowser.open(donate_link)

donate_link = 'https://ko-fi.com/dwayneburr'
# Global variable to control the clicker state
clicking = False

# Function to run the clicker
def clicker():
    while True:
        if clicking:
            pyautogui.click()
        time.sleep(random.uniform(0.2, 0.6))  # Adjust the clicking frequency

def start_clicking():
    global clicking
    clicking = True

def stop_clicking():
    global clicking
    clicking = False

def start_clicker_thread():
    click_thread = threading.Thread(target=clicker)
    click_thread.daemon = True
    click_thread.start()
    
    # Set up hotkeys
    keyboard.add_hotkey('`', start_clicking)
    keyboard.add_hotkey('z', stop_clicking)
    print("Press '`' to start clicking and 'z' to stop. Press esc button to quit")

# Function to start the mouse listener in a separate thread
# def start_listener_thread():
#     listener_thread = threading.Thread(target=start_mouse_listener)
#     listener_thread.daemon = True
#     listener_thread.start()
#     start_button.config(state=tk.DISABLED)

# # Function to stop the listener and re-enable the "Start Listening" button
# def stop_listener_and_enable_button():
#     stop_mouse_listener()
#     start_button.config(state=tk.NORMAL)

# # Function to update the Text widget with mouse click coordinates
# def update_text_widget(text):
#     click_text.insert(tk.END, text + '\n')
#     click_text.yview(tk.END)  # Scroll to the end of the Text widget

# # Function to run the external automation script
# def run_automation_script():
#     subprocess.Popen(['python', 'automation.py'], shell=True)
#     status_label.config(text="Automation script running...")

# Function to start the clicker script
def run_clicker_script():
    start_clicker_thread()
    status_label.config(text="Press '`' to start clicking and 'z' to stop. Press esc button to quit")

# Create the main application window
root = tk.Tk()
root.title("Helper (not an osrs bot)")
root.geometry("600x400")  # Adjusted size to accommodate the new button

# Create a button to start the mouse listener
# start_button = tk.Button(root, text="Start Listening", command=start_listener_thread)
# start_button.pack(pady=10)

# Create a button for the mouse clicker
clicker_button = tk.Button(root, text='Start Clicker', command=run_clicker_script)
clicker_button.pack(pady=10)

# Create a button to run the automation script
# automation_button = tk.Button(root, text="Run Automation Script", command=run_automation_script)
# automation_button.pack(pady=10)

# Create a button to quit the program
quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.pack(pady=10)

# Create a Text widget to display mouse click coordinates
click_text = tk.Text(root, wrap=tk.WORD, height=10, width=50)
click_text.pack(pady=10)

# Create a Label widget to display the status message
donate_label = tk.Label(root, text="Support Me", fg="blue", cursor="hand2")
donate_label.pack(pady=10)
donate_label.bind("<Button-1>", open_donate_link)

# Start the hotkey listener for 'q' in a separate thread
# hotkey_thread = threading.Thread(target=start_hotkey_listener, args=(stop_listener_and_enable_button,))
# hotkey_thread.daemon = True
# hotkey_thread.start()

# Set the update callback for the mouse listener
# set_update_callback(update_text_widget)

# Start the tkinter event loop
root.mainloop()
