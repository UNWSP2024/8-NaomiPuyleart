# Naomi Puyleart
# 10/22/25
# Program #3: Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys, 
# and their capitals as values.  
# The program should then randomly quiz the user by displaying the name of a state 
# and asking the user to enter the state's capital.  
# The program should count of the number of correct and incorrect responses.  
# (You could alternatively use another country and provinces, 
# or countries of the world and capitals).

import random

state_capitals = {'Alabama':'Montgomery',
                  'Alaska':'Juneau',
                  'Arizona':'Phoenix',
                  'Arkansas':'Little Rock',
                  'California':'Sacramento',
                  'Colorado':'Denver',
                  'Connecticut':'Hartford',
                  'Delaware':'Dover',
                  'Florida':'Tallahassee',
                  'Georgia':'Atlanta',
                  'Hawaii':'Honolulu',
                  'Idaho':'Boise',
                  'Illinois':'Springfield',
                  'Indiana':'Indianapolis',
                  'Iowa':'Des Moines',
                  'Kansas':'Topeka',
                  'Kentucky':'Frankfort',
                  'Louisiana':'Baton Rouge',
                  'Maine':'Augusta',
                  'Maryland':'Annapolis',
                  'Massachusetts':'Boston',
                  'Michigan':'Lansing',
                  'Minnesota':'Saint Paul',
                  'Mississippi':'Jackson',
                  'Missouri':'Jefferson City',
                  'Montana':'Helena',
                  'Nebraska':'Lincoln',
                  'Nevada':'Carson City',
                  'New Hampshire':'Concord',
                  'New Jersey':'Trenton',
                  'New Mexico':'Santa Fe',
                  'New York':'Albany',
                  'North Carolina':'Raleigh',
                  'North Dakota':'Bismarck',
                  'Ohio':'Columbus',
                  'Oklahoma':'Oklahoma City',
                  'Oregon':'Salem',
                  'Pennsylvania':'Harrisburg',
                  'Rhode Island':'Providence',
                  'South Carolina':'Columbia',
                  'South Dakota':'Pierre',
                  'Tennessee':'Nashville',
                  'Texas':'Austin',
                  'Utah':'Salt Lake City',
                  'Vermont':'Montpelier',
                  'Virginia':'Richmond',
                  'Washington':'Olympia',
                  'West Virginia':'Charleston',
                  'Wisconsin':'Madison',
                  'Wyoming':'Cheyenne'
                  }

score = 0
incorrect = 0
keep_going = 'y'

while keep_going == 'y':
    state, capital = random.choice(list(state_capitals.items()))
    user_answer = input(f"What is the capital of {state}? ")
    if user_answer.lower() == capital.lower():
        score += 1
        print(f"Correct!")
    else:
        incorrect += 1
        print(f"Incorrect! The capital of {state} is {capital}.")

    keep_going = input("Enter 'y' to continue or 'n' to quit." )

print(f"\nYour final score is {score}. You got {incorrect} wrong.")