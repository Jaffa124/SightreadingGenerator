# Jerome 
# Sight reading generator 
# start - may 28th 2024
# ending - 
# about the program

import pygame
print("hello")


# ntroduction funciton 
def introduction():
    print("Hello and Welcome to my Sight reading generator")
  # introduces how things work and how to interact with the progroam 
  # asks user if they want to start the program or not
  # if yes, then start the program
    # take user to the menu function
  # if no quit the program 


# menu/parameters function 
  # ask user for the parameters they want to use 

  # what instrument do you play?
    # if piano ask if user wants 2 hands?
  # ask if user wants random difficulty or not

  # rate your skill based off images of music being displayed 1-5
  # how many bars would you like? min 3 and max 7 
  # what key signatures(sharps and flats) are you comfortable with?
  # what time signature are you comfortable with?(4/4, 3/4, 2/4, 6/8, etc))
  # ask if user would like to warm up with scales or rhythm? or go to sight reading?
    # if scales take user to scales function
    # elif rhythm take user to rhythm function 
    # else user goes to sight reading function


# Scales function 
  # ask user what scale they want to use
  # they can pick any major scale or any minor scale
  # ask if user wants a metronome to play the scale with 
  # display the scale with the metronome thats wanted by the user
  # when user is done ask if they want to try rhythm or go to sight reading 

# rhythm function 
  # ask what time signature they want to use
  # and ask if they want a metronome to play with 
  # will display a few rhythm pieces within the desired time signature
  # when user is done ask if they want to try scales or go to sight reading

# sight reading function 
  # generates and displays sheet music based off the parameters the user chose
  # asks if user would like a metronme to play along with
  #  if yes ask what speed ranging from 80,100,120,140,160,180 and 200 bpm 
  # have a way to genreator new music once they are down and pause and change the metronome
