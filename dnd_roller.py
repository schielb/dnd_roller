from pynput.keyboard import Key, Listener, KeyCode
import os
import select
import sys

def print_instructions():
    print(
        'Welcome to the D&D Roller CLI. Here are the key presses: \n' +
        '    d4   -  4 \n' +
        '    d6   -  6 \n' +
        '    d8   -  8 \n' +
        '    d10  -  0 \n' +
        '    d12  -  3 \n' +
        '    d20  -  2 \n' +
        '    d100 -  1 \n' +
        'Advantage - a --- Disadvantage - d'
        
    )

def tick(key):
    if str(key)[1]== 'g':
        print('yay')

    else:
        print('nope')

          
    # by pressing 'delete' button 
    # you can terminate the loop 
    if key == Key.esc: 
        return False
  

# This line just suppresses the terminal from re-printing whatever character is being typed by the user
os.system('stty -echo')

print_instructions()

# Collect all event until released
with Listener(on_press = tick) as listener:
    listener.join()

# This gobbles up any keys pressed so they don't show up on the next terminal line
gobble = input('Thank you for playing! Press ENTER to exit.')

