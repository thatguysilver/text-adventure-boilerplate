#! usr/bin/python3.6
# _*_ coding: utf-8 -*-


#important variables -- define these beforehand or throughout your adventures!
name = input('What\'s your name?')






def main_screen(screen_number, *args):
    if len(name)%2 == 0:
        extra = '' 
        half_bar = '='*int((80 - len(str(screen_number)))/2)
    else: 
        extra = '=' 


    print(f'''
{half_bar}{screen_number}{half_bar}{extra}

  {args[0]}
  You said: {args[1]}
  {screen_number}
       





==============================What do you do?===================================
 a.) placeholder_option_A 
 b.) placeholder_option_B
 c.) placeholder_option_C
{'='*80}

''', end = ''
)


#story here

text = '''
        Here is the text you wanted!
        This string is where the main body of the story will go.
        Anyway, whatever.
        '''

screen_number = 1

main_screen(screen_number, '''
Welcome to the game!''',
'Anything')

while True:

    screen_number += 1
    player_input = input('You choose option: ')


    if player_input == 'quit':
        exit()
    else:
        main_screen(screen_number, text, player_input)

