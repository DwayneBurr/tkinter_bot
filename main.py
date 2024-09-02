# main_gui.py

import tkinter as tk
import threading
from mouse_listener import start_mouse_listener, stop_mouse_listener, start_hotkey_listener, set_update_callback

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

# Set the update callback for the mouse listener
set_update_callback(update_text_widget)

# Create the main application window
root = tk.Tk()
root.title("Mouse Click Listener")
root.geometry("600x300")

# Create a button to start the mouse listener
start_button = tk.Button(root, text="Start Listening", command=start_listener_thread)
start_button.pack(pady=10)

# Create a button to quit the program
quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.pack(pady=10)

# Create a Text widget to display mouse click coordinates
click_text = tk.Text(root, wrap=tk.WORD, height=10, width=50)
click_text.pack(pady=10)

# Start the hotkey listener for 'q' in a separate thread
hotkey_thread = threading.Thread(target=start_hotkey_listener, args=(stop_listener_and_enable_button,))
hotkey_thread.daemon = True
hotkey_thread.start()

# Start the tkinter event loop
root.mainloop()
