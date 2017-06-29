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
 1.) {args[1]}
 2.) {args[2]}
 3.) {args[3]}
 4.) {args[4]}
{'='*80}

''', end = ' '
)

screen_number = 0


def screen_1():                           #to be copied/pasted and then altered.

    global screen_number


    
    text = ''' 
The light is fading and the howling, snarling things are nearly upon you. 
Exhausted, you see a dim light in the distance. You're in hostile territory,
but the natives may take pity on you. 
    '''
    option_one= 'Head for the light',
    option_two= 'Chance it in the woods', 
    option_three= ''
    option_four = ''

    screen_number += 1

    while True:                              

        player_input = ''

        
        main_screen(screen_number, text, option_one, option_two, 
                option_three, option_four)
        player_input = input('Your choice! ')
        if player_input == 'quit':
            exit()
        elif player_input == '1':
            screen_2a()
        elif player_input == '2':
            screen_2b()
        elif player_input == '3':
            continue
        elif player_input == '4':
            continue
        else:
            print('Not a choice.')
            continue

def screen_2a():

    global screen_number

    text = '''
Ahead of you lies the clearing. You hear the Wampani chanting
their songs ahead of you. As you aproach the clearing, the 
light of the bonfire halfway illuminates their features, throwing
their faces into sharp, terrifying relief. The sounds of the horrors 
behind you have, mercifully, begun to retreat..
    '''
    option_one= 'You burst into the clearing.',
    option_two= 'You wait. ', 
    option_three= ''
    option_four = ''

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

def screen_2b():

    global screen_number

    text = '''
You run deeper into the woods, panting and struggling. As you 
duck under a fallen branch, you find yourself trapped, entangled in 
a gigantic spider web. The web's owner is nowhere in site, but you 
can hear the sounds of rustling overhead . . . .
    '''
    option_one= 'You calmly try to untangle yourself from the web. ',
    option_two= 'You wait to see if the sound goes away. ', 
    option_three= ''
    option_four = ''

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
print('Thanks for playing!')
