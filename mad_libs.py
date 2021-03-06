# mad_libs.py
# We are going to be making our own Mad Libs game!

## Part 1: Defining Input Variables ############################################
# First let's define some variables you may want to use below, in Mad Libs
# we want to work with INPUTS in this game, so we want to declare a variable
# to an input. We can do this by writing:
my_number = input('20')
print('20' + str(my_number))
# Try running this to see what happens!
# What is happening is that we are asking the user of our program to type something
# and then this value is STORED inside of our variable my_number.
# The variable my_number is then type casted into a string
# to concatenate with the rest of the statement
# Here is an example Mad Lib for you to play with! 
################################################################################
user_name = input(" Ellasia ") # expecting string input
grade = input("5th Grade ") # expecting integer input
print() # prints an empty line
print(" hello ")
print('Hi ' + user_name + ', hope you are doing well! :D')
print("Keep working hard and being positive because you're the coolest " + str(5) +
"th grader. I admire that you are taking the initiative to learn coding this summer. Staying at home can get a little boring, but we can push through this tough time! The cool thing about making Mad Libs is that you can make your own & then ask your family to try it too!")
print() # prints an empty line
print("----------------------------------------------------------")
print()


## Part 2: Walk Through an Example Mad Lib ############################################
# Alright now, we have some variables, let's write print statements that we want
# to print out from our Mad Libs. Keep in mind we will be concatenating our
# variables together, and using the power of casting to make some Python magic!
#Try making some
# variables you want to use in your Mad Libs program and make sure to add an input()
# function that takes in the prompt to ask the user.
# Here's an example below:
################################################################################
print('Let\'s start with an example Mad Lib! :) ') # \ is an escape character in python since the ' you use is the same as the string quotes you are using. You must include the escape character to add the quote ' in your printed string
print("Below, the INPUT variables will ask for your responses & just type them in! ")
print()
print("Example 1: Vacations")
adj1 = input("Big")
adj2 = input("Giant")
noun1 = input("stuffed animal")
noun2 = input("Walmart ")
pnoun1 = input("children")
game = input("Minecraft")
pnoun2 = input("people")
verb1 = input("vibing") # notice here that you do not need an escape character for the ' quotes inside the string quotes because they are not the same :)
verb2 = input("singing ")
verb3 = input("smelling ")
noun3 = input("person")
verb4 = input(" ")
noun4 = input("Please enter another noun (different from ones above): ")
plant = input("Please enter a plant: ")
body = input("Please enter a part of the body: ")
place = input("Please enter a place: ")
verb4 = input("Please enter a verb ending with 'ing' (different from one above): ")
adj3 = input("Please enter another adjective (different from ones above): ")
number = input ("Please enter a number: ")
pnoun2 = input("Please enter another plural noun (different from ones above): ")
print()
print("Example Mad Libs from your responses: ")
print()
print("A vacation is when you take a trip to some " + adj1 + " with your " + adj2 + " family. Usually you go to some place that is near a/an " + noun1 + " or up on a/an " + noun2 +". A good vacation place is one where you can ride " + pnoun1 + " or play " + game + " or go hunting for " + pnoun2 + ". I like to spend my time " + verb1 + " or " + verb2 + ". When parents go on a vacation, they spend their time eating three " + noun3 + " a day, and fathers play golf, and mothers sit around " + verb4 + ". Last summer, my little brother fell in a/an " + noun3 + " and got poison " + plant + " all over his " + body + ". My family is going to go to (the) " + place + ", and I will practice " + verb4 + ". Parents need vacations more than kids because parents are always very " + adj3 + " and because they have to work " + number + " hours every day all year making enough " + pnoun2 + " to pay for the vacation.")
print()
print("----------------------------------------------------------")
print()


## Part 3: Making your own Mad Libs #################################################
# Now it is time for your to go on & make your own Mad Libs! Be creative & fun :) 
# Feel free to use the example from above for some inspiration!
print('Let\'s start writing your own Mad Libs below! :) ') 
################################################################################
