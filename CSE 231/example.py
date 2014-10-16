
# Import the Python math module

import math

# The import command (above) makes all names defined in the Python
# math library available for use in this program.  To use a name
# defined in a library, you need to prefix the name with the library
# name.  For instance, math.pi refers to the name pi in the math libary.

print( "Value of math.pi:", math.pi )

# The round function rounds a number (the first argument) to a specified
# number of decimal digits (the second argument; default is 0).

print( "Result of round(math.pi):", round(math.pi) )
print( "Result of round(math.pi,4):", round(math.pi,4) )

# The input function accepts a string (a sequence of characters between quotes)
# as a prompt to display to the user.  It then waits until the user types a
# response (terminated by the user touching the Enter key).  It returns
# whatever the user typed as a string.

count_str = input( "Enter a count (an integer number):" )
length_str = input( "Enter a length (a floating point number):" )

# You must convert those strings to the appropriate numeric type before
# you can calculate with them.

# The int function converts its argument (a string or a number) to a
# value of type int, provided the argument represents a number.

count = int( count_str )

# The float function converts its argument (a string or number) to a
# value of type float, provided the argument represents a number.

length = float( length_str )

# The print function will display in the output window any combination of
# variables, values and strings.  Each item to be displayed must be separated
# from other items by a comma.  All the items will be printed, then a
# newline will be printed.

print( "The count:", count )
print( "The length:", length )

print( "The area of", count, "squares is", 4*length**2, "sq units." )

# Converting a float to a value of type int truncates the float

price = 7.99

print( "Price:", price )
print( "Price as an integer:", int(price) )
