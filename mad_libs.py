# mad_libs.py
# We are going to be making our own Mad Libs game!

## Part 1: Defining Input Variables ############################################
# First let's define some variables you may want to use below, in Mad Libs
# we want to work with INPUTS in this game, so we want to declare a variable
# to an input. We can do this by writing:
my_number = input('Please type in a number: ')
print('This is the number you typed in ' + str(my_number))

# Try running this to see what happens!
# What is happening is that we are asking the user of our program to type something
# and then this value is STORED inside of our variable my_number. Try making some
# variables you want to use in your Mad Libs program and make sure to add an input()
# function that takes in the prompt to ask the user.
################################################################################













## Part 2: Making our Mad Libs #################################################
# Alright now, we have some variables, let's write print statements that we want
# to print out from our Mad Libs. Keep in mind we will be concatenating our
# variables together, and using the power of casting to make some Python magic!
# Here's an example below:
################################################################################

user_name = input("Hey what's your name? (Put your name in single quotes like 'Elizabeth') ")   # expecting string input
grade = input("What grade are you in? ")      # expecting integer input

print('Hi ' + user_name + ', hope you are doing well!')
print("Keep working hard and being positive because you're the coolest " + str(grade) +
"th grader. I admire that you are taking the initiative to learn coding this summer.")
print("Staying at home get a little boring, but we can push through this tough time!")
print('Alright bye friend!')
