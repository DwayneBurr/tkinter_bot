import tkinter as tk
import threading
import subprocess
from mouse_listener import start_mouse_listener, stop_mouse_listener, start_hotkey_listener, set_update_callback
from clicker import clicker

# Function to start the mouse listener in a separate thread
def start_listener_thread():
    listener_thread = threading.Thread(target=start_mouse_listener)
    listener_thread.daemon = True
    listener_thread.start()

    start_button.config(state=tk.DISABLED)

# Function to stop the listener and re-enable the "Start Listening" button
def stop_listener_and_enable_button():
    stop_mouse_listener()
    start_button.config(state=tk.NORMAL)

# Function to update the Text widget with mouse click coordinates
def update_text_widget(text):
    click_text.insert(tk.END, text + '\n')
    click_text.yview(tk.END)  # Scroll to the end of the Text widget

# Function to run the external script
def run_automation_script():
    # Use subprocess to run the external script
    subprocess.Popen(['python', 'automation.py'], shell=True)
    status_label.config(text="Automation script running...")
# Set the update callback for the mouse listener
set_update_callback(update_text_widget)

## Function for the clicker script
def run_clicker_script():
    subprocess.Popen(['python', 'clicker.py'], shell=True)
    status_label.config(text="Press '`' to start clicking and 'z' to stop. Press esc button to quit")

# Create the main application window
root = tk.Tk()
root.title("Helper (not a osrs bot)")
root.geometry("600x400")  # Adjusted size to accommodate the new button

# Create a button to start the mouse listener
start_button = tk.Button(root, text="Start Listening", command=start_listener_thread)
start_button.pack(pady=10)

# a button for mouse clicker
start_button = tk.Button(root, text='start clicker', command=run_clicker_script)
start_button.pack(pady=10)

# Create a button to run the automation script
automation_button = tk.Button(root, text="Run Automation Script", command=run_automation_script)
automation_button.pack(pady=10)

# Create a button to quit the program
quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.pack(pady=10)

# Create a Text widget to display mouse click coordinates
click_text = tk.Text(root, wrap=tk.WORD, height=10, width=50)
click_text.pack(pady=10)

# Create a Label widget to display the status message
status_label = tk.Label(root, text="Click on which function to run.")
status_label.pack(pady=10)

# Start the hotkey listener for 'q' in a separate thread
hotkey_thread = threading.Thread(target=start_hotkey_listener, args=(stop_listener_and_enable_button,))
hotkey_thread.daemon = True
hotkey_thread.start()

# Start the tkinter event loop
root.mainloop()
