#!/usr/bin/python3

import art
arte=art.text2art("TEST", font='block', chr_ignore=True)
print('Content-Type: text/plain\r\n\r\n')
print('')
print('This is my test2!')
print(arte)

