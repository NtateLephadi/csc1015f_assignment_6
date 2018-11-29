from random import *
# somehelp.py

def welcome():
    print('Welcome to the automated techincal support system.')
    print('Please describe your problem')

def get_input():
    return input().lower()

def get_output():
    output = ['Have you tried it on a different operating system?', 'Did you reboot it?', 'What colour is it?', 'You should consider installing anti-virus software.', 'Contact Telkom.', 'I\'d get that looked at if I were you.']
    return output[randint(0, 5)]

def main():

    welcome()    
    query = get_input()
    
    while (not query=='quit'):
        get_output()
        query = get_input()    
    
    
if __name__ == '__main__':
    main()
