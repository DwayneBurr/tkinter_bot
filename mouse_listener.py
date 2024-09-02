# mouse_listener.py

from pynput import mouse, keyboard

# Global flag to control the listener
running = True
update_gui_callback = None  # This will be set to the GUI update function

def on_click(x, y, button, pressed):
    if pressed and update_gui_callback:
        update_gui_callback(f"clicked X: {x}, Y: {y} with {button}")

def start_mouse_listener():
    global running
    running = True
    with mouse.Listener(on_click=on_click) as listener:
        while running:
            listener.join(1)  # Check every 1 second if it should stop

def stop_mouse_listener():
    global running
    running = False

def start_hotkey_listener(stop_listener_callback):
    def on_press(key):
        try:
            if key.char == 'q':
                stop_listener_callback()  # Stop the listener and enable the button

        except AttributeError:
            pass

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

def set_update_callback(callback):
    global update_gui_callback
    update_gui_callback = callback
