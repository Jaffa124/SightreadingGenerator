# Jerome 
# Sight reading generator 
# start - may 28th 2024
# ending - 
# about the program
# importing pygaem and sys to use throughout program
from email.mime import image
import pygame
import sys
print("hello")
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Main Menu")
main_font = pygame.font.SysFont("cambria",50)




# button class 
# initliazes buttons and sets variables in the class
class Button():
  def __init__(self,image,x_pos,y_pos,text_input):
    # makes the button image
    self.image = image
    # x and y pos deal with the coordiantes of button location
    self.x_pos = x_pos
    self.y_pos = y_pos
    # 
    self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
    self.text_input = text_input
    self.text = main_font.render(self.text_input, True, "white")
    self.text_rect = self.text.get_rect(center=(self.x_pos,y_pos))

  def update(self):
      screen.blit(self.image,self.rect)
      screen.blit(self.text,self.text_rect)

  def checkForInput(self, position):
      if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
        print("Button Press!")
    
  def changeColor(self, position):
      if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
        self.text = main_font.render(self.text_input, True, "green")
      else:
        self.text = main_font.render(self.text_input, True, "white")

button_surface = pygame.image.load("button.png")
button_surface = pygame.transform.scale(button_surface, (400, 150))

button = Button(button_surface, 400, 300, "Button")
  



             




# introduction funciton 

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



while True:
	for event in pygame.event.get():
    
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			button.checkForInput(pygame.mouse.get_pos())

	screen.fill("white")
	button.update()
	button.changeColor(pygame.mouse.get_pos())

	pygame.display.update()    