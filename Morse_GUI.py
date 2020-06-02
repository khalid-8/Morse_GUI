import Tkinter as tk
import tkFont
#import Tkinter.font as tkFont
import RPi.GPIO as GPIO
import time
#from tkinter import *
#import tkinter.font as tkFont
#from guizero import App, Text

CODE = {' ': ' ',
        "'": '.----.',
        '(': '-.--.-',
        ')': '-.--.-',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ':': '---...',
        ';': '-.-.-.',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'S': '...',
	'R': '.-.',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-'}
        
ledPin=27

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin,GPIO.OUT)

root = tk.Tk()
myFont = tkFont.Font(family = 'Helvetica', size = 18)

#win = Tk()
#myFont = tkFont.Font(family = 'Helvetica', size = 18, weight = 'bold')

def dot():
        GPIO.output(ledPin,1)
        time.sleep(0.2)
        GPIO.output(ledPin,0)
        time.sleep(0.2)

def dash():
        GPIO.output(ledPin,1)
        time.sleep(0.5)
        GPIO.output(ledPin,0)
        time.sleep(0.2)

def exitProgram():
        print("Exit Button pressed")
        GPIO.cleanup()
        win.quit()

def BlinkMorse():
    inputvalue =morse_code_app.get("1.0","end-1c")
    for letter in inputvalue: #morse_code_app. value:
       for symbol in CODE[letter.upper()]:
            if symbol == '-':
                    dash()
            elif symbol == '.':
                        dot()
            else:
                    time.sleep(0.5)
    time.sleep(0.5)
    

#win.title("MORSE LED")
#win.geometry('500x300')

morse_code_app =tk.Text(root) # label="Blink in morse Code", font =myFont)
morse_code_app.pack()
#morse_code= TextBox(app, text width=30)

#inputword = tk.TextBox(root, text="Enter a word (maximum 12 characters)", width=30)

blinktheLED = tk.Button(root, command=BlinkMorse, text="Send")
blinktheLED.pack()

tk.mainloop()

