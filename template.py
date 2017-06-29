#! usr/bin/python3.6
# _*_ coding: utf-8 -*-

#important variables -- define these beforehand or throughout your adventures!
name = input('What\'s your name?')






def main_screen(*args):
    if len(name)%2 == 0:
        extra = '' 
        half_bar = '='*int((80 - len(name))/2)
    else: 
        extra = '=' 


    print(f'''
{half_bar}{name}{half_bar}{extra}

  {args[0]}
       





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
main_screen(text, 'potato')
