# Ian Bullard
# UWYO COSC 1010
# Submission Date 10/22/24
# HW 02
# Lab Section: 14
# Sources, people worked with, help given to: 
# your
# comments
# here
morse_code_letters ={
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.', 
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---', 
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---', 
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-', 
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--', 
    'Z': '--..'
}

message = "Insert what you want translated into morse code.\n"
morse_string = input(message)
for letter in morse_string:
    morse_string.get()