# Title: A Heart Filled With Love


# Modules ###########################################################################################

# Module used to display the date and time during the program.
import time
import sys
import os
from time import sleep
from colored import fg ,attr


# Variables #########################################################################################

# Variables for status bar
start_loading = '\n\n\n\nLoading'
loading = '*' * 159 + '\n\n'

# Variables containing letter "x" and "o" used individually.
item_one = 'x'
item_two = 'o'

# Variable combo of letter "x" and "o"
items = item_one + \
        item_two

# Variable used to reverse the order of "xo" to "ox".
reversed_items = item_two + \
        item_one


# Authentication ####################################################################################

# Used to enter the string "clear" into the Command Line Interface and clear the screen
os.system('clear')

# Authentication has passed
print(fg("yellow"),attr("bold"),'\n' * 10 + ' ' * 75 + 'Access Granted!')
print(fg("light_green"),attr("bold"),'\n' + ' ' * 74 + 'Hello Ayman xox  ;)')

# Used to simulate loading progress of the main program
print(start_loading)
for c in loading:
    print(fg("light_sea_green"),attr("bold"),c, end='')
    sys.stdout.flush()
    sleep(0.025)

# Clear the screen to simulate program is starting
os.system('clear')


# The Design Code ###################################################################################

# Prints the top border.
print(fg("light_blue"),attr("bold"),items * 81 + item_one + '\n' +'  '+ items + ' ' * 159 + reversed_items)

# Displays date and time.
localtime = time.asctime( time.localtime(time.time()) )
print(fg("light_blue"),attr("bold"),items + ' ' * 66 + localtime + ' ' * 69 + reversed_items)

# The Greeting
print(fg("light_blue"),attr("bold"),items + ' ' * 67 + 'Happy Valentine\'s Day !' + ' ' * 69 + reversed_items)


# Heart Section 1 of 3: Pattern -2 +2 -4 +2 -2

# Line 1
print("  "+items +fg("light_red"),attr("bold"), ' ' * 36 + items * 13 + 'x' + ' ' * 31 + items * 13 + 'x' + ' ' * 34 +fg("light_blue"),attr("bold"), reversed_items)
# Line 2
print("  "+items +fg("light_red"),attr("bold"), ' ' * 34 + items * 15 + 'x' + ' ' * 27 + items * 15 + 'x' + ' ' * 32 +fg("light_blue"),attr("bold"), reversed_items)
# Line 3
print("  "+items +fg("light_red"),attr("bold"), ' ' * 32 + items * 17 + 'x' + ' ' * 23 + items * 17 + 'x' + ' ' * 30 +fg("light_blue"),attr("bold"), reversed_items)
# Line 4
print("  "+items +fg("light_red"),attr("bold"), ' ' * 30 + items * 19 + 'x' + ' ' * 19 + items * 19 + 'x' + ' ' * 28 +fg("light_blue"),attr("bold"), reversed_items)
# Line 5
print("  "+items +fg("light_red"),attr("bold"), ' ' * 28 + items * 21 + 'x' + ' ' * 15 + items * 21 + 'x' + ' ' * 26 +fg("light_blue"),attr("bold"), reversed_items)
# Line 6
print("  "+items +fg("light_red"),attr("bold"), ' ' * 26 + items * 23 + 'x' + ' ' * 11 + items * 23 + 'x' + ' ' * 24 +fg("light_blue"),attr("bold"), reversed_items)
# Line 7
print("  "+items +fg("light_red"),attr("bold"), ' ' * 24 + items * 25 + 'x' + ' ' * 7 + items * 25 + 'x' + ' ' * 22 +fg("light_blue"),attr("bold"), reversed_items)
# Line 8
print("  "+items +fg("light_red"),attr("bold"), ' ' * 22 + items * 27 + 'x' + ' ' * 3 + items * 27 + 'x' + ' ' * 20 +fg("light_blue"),attr("bold"), reversed_items)


# Heart Section 2 of 3: No number pattern
# The maximum span of the Heart with a message in the middle.

# Line 9
print("  "+items +fg("light_red"),attr("bold"), ' ' * 22 + items * 27 + 'x' + ' A ' + items * 27 + 'x' + ' ' * 20 +fg("light_blue"),attr("bold"), reversed_items)
# Line 10
print("  "+items +fg("light_red"),attr("bold"), ' ' * 22 + items * 27 + 'x' + ' Y ' + items * 27 + 'x' + ' ' * 20 +fg("light_blue"),attr("bold"), reversed_items)
# Line 11
print("  "+items +fg("light_red"),attr("bold"), ' ' * 22 + items * 27 + 'x' + ' M ' + items * 27 + 'x' + ' ' * 20 +fg("light_blue"),attr("bold"), reversed_items)
# Line 12
print("  "+items +fg("light_red"),attr("bold"), ' ' * 22 + items * 27 + 'x' + ' A ' + items * 27 + 'x' + ' ' * 20 +fg("light_blue"),attr("bold"), reversed_items)
# Line 13
print("  "+items +fg("light_red"),attr("bold"), ' ' * 22 + items * 27 + 'x' + ' N ' + items * 27 + 'x' + ' ' * 20 +fg("light_blue"),attr("bold"), reversed_items)
# Line 13
print("  "+items +fg("light_red"),attr("bold"), ' ' * 22 + items * 27 + 'x' + '   ' + items * 27 + 'x' + ' ' * 20 +fg("light_blue"),attr("bold"), reversed_items)
# Line 14
print("  "+items +fg("light_red"),attr("bold"), ' ' * 22 + items * 27 + 'x' + ' & ' + items * 27 + 'x' + ' ' * 20 +fg("light_blue"),attr("bold"), reversed_items)
# Line 15
print("  "+items +fg("light_red"),attr("bold"), ' ' * 22 + items * 27 + 'x' + '   ' + items * 27 + 'x' + ' ' * 20 +fg("light_blue"),attr("bold"), reversed_items)
# Line 16
print("  "+items +fg("light_red"),attr("bold"), ' ' * 22 + items * 27 + 'x' + ' ? ' + items * 27 + 'x' + ' ' * 20 +fg("light_blue"),attr("bold"), reversed_items)
# Line 17
print("  "+items +fg("light_red"),attr("bold"), ' ' * 22 + items * 27 + 'x' + ' ? ' + items * 27 + 'x' + ' ' * 20 +fg("light_blue"),attr("bold"), reversed_items)
# Line 18
print("  "+items +fg("light_red"),attr("bold"), ' ' * 22 + items * 27 + 'x' + ' ? ' + items * 27 + 'x' + ' ' * 20 +fg("light_blue"),attr("bold"), reversed_items)
# Line 20
print("  "+items +fg("light_red"),attr("bold"), ' ' * 22 + items * 27 + 'x' + ' ? ' + items * 27 + 'x' + ' ' * 20 +fg("light_blue"),attr("bold"), reversed_items)
# Line 21
print("  "+items +fg("light_red"),attr("bold"), ' ' * 22 + items * 27 + 'x' + ' ' * 3 + items * 27 + 'x' + ' ' * 20 +fg("light_blue"),attr("bold"), reversed_items)


# Heart Section 3 of 3: Pattern +2 -2 +2
# The Heart tapers off

# Line 22
print("  "+items +fg("light_red"),attr("bold"), ' ' * 24 + items * 54 + item_one + ' ' * 22 + fg("light_blue"),attr("bold"),reversed_items)
# Line 23
print("  "+items +fg("light_red"),attr("bold"), ' ' * 26 + items * 52 + item_one + ' ' * 24 + fg("light_blue"),attr("bold"),reversed_items)
# Line 24
print("  "+items +fg("light_red"),attr("bold"), ' ' * 28 + items * 50 + item_one + ' ' * 26 + fg("light_blue"),attr("bold"),reversed_items)
# Line 25
print("  "+items +fg("light_red"),attr("bold"), ' ' * 30 + items * 48 + item_one + ' ' * 28 + fg("light_blue"),attr("bold"),reversed_items)
# Line 26
print("  "+items +fg("light_red"),attr("bold"), ' ' * 32 + items * 46 + item_one + ' ' * 30 + fg("light_blue"),attr("bold"),reversed_items)
# Line 27
print("  "+items +fg("light_red"),attr("bold"), ' ' * 34 + items * 44 + item_one + ' ' * 32 + fg("light_blue"),attr("bold"),reversed_items)
# Line 28
print("  "+items +fg("light_red"),attr("bold"), ' ' * 36 + items * 42 + item_one + ' ' * 34 + fg("light_blue"),attr("bold"),reversed_items)
# Line 29
print("  "+items +fg("light_red"),attr("bold"), ' ' * 38 + items * 40 + item_one + ' ' * 36 + fg("light_blue"),attr("bold"),reversed_items)
# Line 30
print("  "+items +fg("light_red"),attr("bold"), ' ' * 40 + items * 38 + item_one + ' ' * 38 + fg("light_blue"),attr("bold"),reversed_items)
# Line 31
print("  "+items +fg("light_red"),attr("bold"), ' ' * 42 + items * 36 + item_one + ' ' * 40 + fg("light_blue"),attr("bold"),reversed_items)
# Line 32
print("  "+items +fg("light_red"),attr("bold"), ' ' * 44 + items * 34 + item_one + ' ' * 42 + fg("light_blue"),attr("bold"),reversed_items)
# Line 33
print("  "+items +fg("light_red"),attr("bold"), ' ' * 46 + items * 32 + item_one + ' ' * 44 + fg("light_blue"),attr("bold"),reversed_items)
# Line 34
print("  "+items +fg("light_red"),attr("bold"), ' ' * 48 + items * 30 + item_one + ' ' * 46 + fg("light_blue"),attr("bold"),reversed_items)
# Line 35
print("  "+items +fg("light_red"),attr("bold"), ' ' * 50 + items * 28 + item_one + ' ' * 48 + fg("light_blue"),attr("bold"),reversed_items)
# Line 36
print("  "+items +fg("light_red"),attr("bold"), ' ' * 52 + items * 26 + item_one + ' ' * 50 + fg("light_blue"),attr("bold"),reversed_items)
# Line 37
print("  "+items +fg("light_red"),attr("bold"), ' ' * 54 + items * 24 + item_one + ' ' * 52 + fg("light_blue"),attr("bold"),reversed_items)
# Line 38
print("  "+items +fg("light_red"),attr("bold"), ' ' * 56 + items * 22 + item_one + ' ' * 54 + fg("light_blue"),attr("bold"),reversed_items)
# Line 39
print("  "+items +fg("light_red"),attr("bold"), ' ' * 58 + items * 20 + item_one + ' ' * 56 + fg("light_blue"),attr("bold"),reversed_items)
# Line 40
print("  "+items +fg("light_red"),attr("bold"), ' ' * 60 + items * 18 + item_one + ' ' * 58 + fg("light_blue"),attr("bold"),reversed_items)
# Line 41
print("  "+items +fg("light_red"),attr("bold"), ' ' * 62 + items * 16 + item_one + ' ' * 60 + fg("light_blue"),attr("bold"),reversed_items)
print("  "+items +fg("light_red"),attr("bold"), ' ' * 64 + items * 14 + item_one + ' ' * 62 + fg("light_blue"),attr("bold"),reversed_items)
print("  "+items +fg("light_red"),attr("bold"), ' ' * 66 + items * 12 + item_one + ' ' * 64 + fg("light_blue"),attr("bold"),reversed_items)
print("  "+items +fg("light_red"),attr("bold"), ' ' * 68 + items * 10 + item_one + ' ' * 66 + fg("light_blue"),attr("bold"),reversed_items)
print("  "+items +fg("light_red"),attr("bold"), ' ' * 70 + items * 8 + item_one + ' ' * 68 + fg("light_blue"),attr("bold"),reversed_items)
print("  "+items +fg("light_red"),attr("bold"), ' ' * 72 + items * 6 + item_one + ' ' * 70 + fg("light_blue"),attr("bold"),reversed_items)
print("  "+items +fg("light_red"),attr("bold"), ' ' * 74 + items * 4 + item_one + ' ' * 72 + fg("light_blue"),attr("bold"),reversed_items)
print("  "+items +fg("light_red"),attr("bold"), ' ' * 76 + items * 2 + item_one + ' ' * 74 + fg("light_blue"),attr("bold"),reversed_items)
print("  "+items +fg("light_red"),attr("bold"), ' ' * 78 + items * 0 + item_one + ' ' * 76 + fg("light_blue"),attr("bold"),reversed_items)

# Heart is finished, but the left and right borders continue building "xo" and "ox"
print(fg("light_blue"),attr("bold"),items + ' ' * 159 + reversed_items)

# Prints the bottom border.
print(fg("light_blue"),attr("bold"),items * 81 + item_one)

# Prints spaces to add padding between bottom border and command prompt
#print('\n' * 10)
