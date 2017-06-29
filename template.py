#! usr/bin/python3.6
# _*_ coding: utf-8 -*-

#important variables -- define these beforehand or throughout your adventures!

name = ''




def main_screen(text):
    if len(name)%2 == 0:
        extra = '' 
        half_bar = '='*int((80 - len(name))/2)
    else: 
        extra = '=' 


    print(f'''
{half_bar}{name}{half_bar}{extra}

  {text}
       







==============================What do you do?===================================
| a.) placeholder_option_A
| b.) placeholder_option_B
| c.) placeholder_option_C
{'='*80}

''', end = ''
)


#important variables:


#story here

name = input('What\'s your name?')

main_screen('''
        Here is the text you wanted!
        This string is where the main body of the story will go.
        Anyway, whatever.
        ''')
