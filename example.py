#! usr/bin/python3.6
# _*_ coding: utf-8 -*-

import sqlite3, os

name = input('What\'s your name?')



conn = sqlite3.connect(f'players.db')
c = conn.cursor()
    
c.execute(f'CREATE TABLE if not exists {name} (screen INTEGER PRIMARY KEY)')
    

def main_screen(screen_number, *args):

    half_bar = '='*int((80 - len(str(screen_number)))/2)

    if len(name)%2 == 0:
        extra = '' 
    else: 
        extra = '=' 


    print(f'''
{half_bar}{screen_number}{half_bar}{extra}

  {args[0]}
  You said: {args[1]}
  {screen_number}
       




==============================What do you do?===================================
 a.) {args[2]}
 b.) {args[3]}
 c.) {args[4]}
 d.) {args[5]}
{'='*80}

''', end = ''
)



screen_number = 1

main_screen(screen_number, '''
Welcome to the game!''',
'Anything')

def screen_1():                           #to be copied/pasted and then altered.


    global screen_number

    while True:                              
        c.execute(f"ALTER TABLE {name} ADD COLUMN 'FIRST_DECISION' TEXT DEFAULT  'undecided'")
    
        text = ''' Here is the text you wanted!  This string is where the main body of the story will go.  Anyway, whatever.  ''' 


        screen_number += 1
        player_input = input('You choose option: ')


        if player_input == 'quit':
            conn.close()
            exit()
        elif player_input == 'a':
         break


        else:
            main_screen(screen_number, text, player_input)
print(c.execute("PRAGMA table_info('table_name')"))
screen_1()
print('you finished the first loop!')
