#!/usr/bin/python3

import art
arte=art.text2art("UWU", font='block', chr_ignore=True)
print('Content-Type: text/plain\r\n\r\n')
print('')
#print('This is my test2!')
print(arte)

for i in range(5):
	print(arte)
