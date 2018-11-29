from random import *
# somehelp.py

def welcome():
    print('Welcome to the automated techincal support system.')
    print('Please describe your problem')

def get_input():
    return input().lower()

def get_output(sentence):
    output = {'crashed':'Are the drivers up to date?', 'blue':'Ah, the blue screen of death. And then what happened?', 'hacked': 'You should consider installing anti-virus software.', 'bluetooth': 'Have you tried mouthwash?', 'windows': 'Ah, I think I see your problem. What version?', 'apple': 'You do mean the computer kind of apple don\'t you?', 'spam': 'You should see if your mail client can filter messages.', 'connection': 'Contact Telkom'}
    list_of_keys = list(output)
    sentence = sentence.split()
    for i in sentence:
        if i in list_of_keys:
            return output[i]
    return 'Curious, tell me more.'

def main():

    welcome()    
    query = get_input()
    
    while (not query=='quit'):
        print(get_output(query))
        query = get_input()    
    
    
if __name__ == '__main__':
    main()
