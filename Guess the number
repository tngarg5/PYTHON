# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

range = 0
print ("Default Range :[0,100)")
# helper function to start and restart the game
def new_game():   
    global secret_number , count
    global range
    if ("range == 0"):
        
        secret_number = random.randrange(1,100)
        count = 7
    if(range == 1):
        secret_number = random.randrange(1,100)
    elif(range == 2):
        secret_number = random.randrange(1,1000)
    print ""
    
         

#function to set turns to 7 for range[0,100) and reset game  
def range100():
    global count
    global range
    range = 1
    print "Range is [0,100)"
    new_game()
    count = 7
    
#function to set turns to 10 for range[0,1000) and reset game
def range1000():
    global count
    global range
    print "Range is [0,1000)"
    range = 2
    new_game()
    count = 10

#main function to compute winner
def input_guess(guess):
    
    global count 
    player = int(guess)
    print "Guess was",player
    
    if(count > 1):                  #TURNS count
        if( secret_number > player):
            print "Higher"
            count = count - 1
            print "chances left",count
            print ""
        elif( secret_number < player):
            print "Lower"
            count = count -1
            print "chances left",count
            print ""
        elif( secret_number == player):
            print "Correct!"
            print ""
            new_game()
   
    else:
        print " Game Over!"
        print ""
        print "New Game"
        new_game()
          
      
    
# create frame
frame = simplegui.create_frame("Guesss the number", 50,500)
frame.add_label("Select Range")
frame.add_button("Range is [0-100)", range100, 200)
frame.add_button("Range is [0-1000)", range1000, 200)
frame.add_label("")
frame.add_input("Enter the guess", input_guess, 200)
frame.add_button("Reset",new_game)
frame.start()


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
