
import time
from pynput.keyboard import Controller
import subprocess

def make_call(phone_number):
    subprocess.run(['open', f'facetime://{phone_number}'])

def press_key(key):
    keyboard = Controller()
    keyboard.press(key)
    keyboard.release(key)

def dial_and_press(phone_number):
    make_call(phone_number)
    time.sleep(5)  # Adjust delay as needed to allow time for call setup
    #press_key('9')
    #time.sleep(1)  # Adjust delay as needed to allow time for the keypress to register

# Example usage
phone_number = 'XXXXXXXXXX'  # Replace with the desired recipient's phone number
while True:
    dial_and_press(phone_number)
    time.sleep(30)
    print("Call made")
    # Add any additional logic or conditions for continuing the loop
