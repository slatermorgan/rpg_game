# Python Test RPG
# Morgan Slater

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

# Player Set up #
class player:
    def __init__(self):
        self.name = ''  #name of player
        self.hp = 0     #hp of player
        self.xp = 0     #exp of player
        self.location = 'start'
        self.status_effects = []
myPlayer = player()

# title #
def title_screen_select():
    option = input("> ")
    if option.lower() == ("play")
        start_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']: #looks for correct answers
        print("please answer correctly, my options are limited")
        option = input("> ")
        if option.lower() == ("play")
            start_game() #placeholder until writter
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()

def title_screen():
    os.system('clear')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~ Welcome to name of game goes here ~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('               - PLAY -              ')
    print('               - HELP -              ')
    print('               - QUIT -              ')
    print('         created by Morgan Slater    ')
    title_screen_select()

def help_menu():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('              coming soon            ')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    title_screen_select()

# Actual Game
def start_game():




# MAP #
"""
a1 a2....
________________
|  |  |  |  |  | a4
________________
|  |  |  |  |  | b4
________________
|  |  |  |  |  |
________________
"""

DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

#dictionaries
solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                 'b1': False, 'b2': False, 'b3': False, 'b4': False,
                 'c1': False, 'c2': False, 'c3': False, 'c4': False,
                 'd1': False, 'd2': False, 'd3': False, 'd4': False,
}

zonemap = {
    'a1': {
        ZONENAME: "",
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
    },

}
