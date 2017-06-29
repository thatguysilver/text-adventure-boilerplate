#! usr/bin/python3.6
# _*_ coding: utf-8 -*-

import  os

name = input('What\'s your name?')



    
    

def main_screen(screen_number, *args):

    half_bar = '='*int((80 - len(str(screen_number)))/2)

    if len(name)%2 == 0:
        extra = '' 
    else: 
        extra = '=' 


    print(f'''
{half_bar}{screen_number}{half_bar}{extra}

  {args[0]}
       




==============================What do you do?===================================
 a.) {args[1]}
 b.) {args[2]}
 c.) {args[3]}
 d.) {args[4]}
{'='*80}

''', end = ''
)



screen_number = 1

#main_screen(screen_number, '''
#Welcome to the game!''',
#'Anything', '', '', '', '')

def screen_1():                           #to be copied/pasted and then altered.

    global screen_number


    
    text = ''' 
    Here is the text you wanted!  
    This string is where the main 
    body of the story will go.  
    ''',
    option_one= 'First option',
    option_two= 'Second option', 
    option_three= 'Third option',
    option_four = 'Fourth option'

    screen_number += 1

    while True:                              

        player_input = ''

        
        main_screen(screen_number, text, option_one, option_two, 
                option_three, option_four)
        player_input = input('Your choice! ')
        if player_input == 'quit':
            exit()
        elif player_input == '1':
            break
        elif player_input == '2':
            break
        elif player_input == '3':
            break
        elif player_input == '4':
            break
        else:
            print('Not a choice.')
            continue

            
screen_1()
print('you finished the first loop!')
