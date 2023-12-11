#!/usr/bin/python3

def uppercase(str):
    for i in range(0, len(str)):
         print("{}".format(
            chr(ord(str[i])-32)) if ord(str[i]) in range(97, 123) else chr(
            ord(str[i])), end='')
    print(end='\n')
