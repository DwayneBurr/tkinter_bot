import pyautogui as py
import time
import random

def random_sleep(base_time, variations=0.3):
    sleep_time = random.uniform(base_time - variations, base_time + variations)
    time.sleep(sleep_time)

def move_with_randomness(x, y, radius=8, duration=0.5):
    # Calculate a random offset within the radius
    random_x = x + random.randint(-radius, radius)
    random_y = y + random.randint(-radius, radius)
    
    # Move to the random position
    py.moveTo(random_x, random_y, duration=duration)

def cook():
    move_with_randomness(684, 551, radius=8, duration=0.2)
    py.click()
    random_sleep(1.9)

    move_with_randomness(928, 783, radius=8, duration=0.3)
    py.click()
    time.sleep(1.1)

    move_with_randomness(571, 281, radius=8, duration=0.4)
    py.click()
    random_sleep(1.8)

    move_with_randomness(1046, 439, radius=8, duration=1.3)
    py.click()
    random_sleep(1.7)

    move_with_randomness(569, 895, radius=8, duration=0.2)
    py.click()
    random_sleep(66.9)

    # move_with_randomness(1003, 816, radius=8, duration=0.3)
    # py.click()
    # time.sleep(1.1)

    # move_with_randomness(1042, 817, radius=8, duration=0.4)
    # py.click()
    # random_sleep(0.8)

    # move_with_randomness(265, 913, radius=8, duration=1.3)
    # py.click()
    # random_sleep(15.8)


    # move_with_randomness(301, 913, radius=8, duration=1.1)
    # py.click()
    # time.sleep(66.6)

    # move_with_randomness(958, 757, radius=8, duration=0.9)
    # py.click()
    # time.sleep(0.6)


    # move_with_randomness(277, 912, radius=8, duration=0.6)
    # py.click()
    # time.sleep(48.1)


# The main block is not needed for GUI integration
if __name__ == "__main__":
    for _ in range(13):
        cook()
