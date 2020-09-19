#!/usr/bin/python3

from time import sleep

#By defining the SIZE constant at the top, the whole program is able to use it.
#SLEEP_TIME determines how long to sleep before printing the next line

SIZE = 30
SLEEP_TIME = 0.1

#4 functions total were created to represent the entire ship.

def main():
    top_bottom()
    border()
    uphill()
    downhill()
    border()
    downhill()
    uphill()
    border()
    top_bottom()

#This function acts as both the top and the bottom of the rocket, as they are identical.
    
def top_bottom():
    for line in range(1, 2 * SIZE):
        for space in range (1, -1 * line + 2 * SIZE + 1):
            print(" ", end="")
        for f_slash in range (1, line + 1):
            print("/", end="")
        print("**", end="")
        for b_slash in range (1, line + 1):
            print("\\", end="")
        print()
		
        sleep(SLEEP_TIME)

#The border function is repeated three times in the program.
        
def border():
    print("+", end="")
    for i in range (1, 2 * SIZE + 1):
         print("=*", end="")
    print("+")
	
    sleep(SLEEP_TIME)

#The uphill function consists of uphil mountains and decreasing dots as the lines go down.

def uphill():
    for line in range (1, SIZE + 1):
        print("|", end="")
        for dot in range (1, -1 * line + SIZE + 1):
            print(".", end="")
        for mountain in range (1, line + 1):
            print("/\\", end="")
        for dot in range (1, -2 * line + 2 * SIZE + 1):
            print(".", end="")
        for mountain in range (1, line + 1):
            print("/\\", end="")
        for dot in range (1, -1 * line + SIZE + 1):
            print(".", end="")
        print("|")
		
        sleep(SLEEP_TIME)
		
#The downhill function consists of upside-down mountains and increasing dots as the lines go down, which is really just the opposite of the uphill function.

def downhill():
    for line in range (1, SIZE + 1):
        print("|", end="")
        for dot in range (1, line):
            print(".", end="")
        for mountain in range (1, -1 * line + SIZE + 2):
            print("\\/", end="")
        for dot in range (1, 2 * line - 1):
            print(".", end="")
        for mountain in range (1, -1 * line + SIZE + 2):
            print("\\/", end="")
        for dot in range (1, line):
            print(".", end="")
        print("|")
		
        sleep(SLEEP_TIME)
		
main()
