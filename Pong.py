# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos =[300, 200]
ball_vel = [0,0]
up = [HALF_PAD_WIDTH,50]
down = [HALF_PAD_WIDTH,50+PAD_HEIGHT]
up2 = [WIDTH-HALF_PAD_WIDTH,50]
down2 = [WIDTH-HALF_PAD_WIDTH,50+PAD_HEIGHT] 
paddle1_vel = 0
paddle2_vel =0
k=0
q = 0
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    if(direction == "RIGHT"):
        ball_vel = [0,0]
        ball_vel =[random.randrange(1,3),random.randrange(0,2)]
    if(direction == "LEFT"):
        ball_vel = [0,0]
        ball_vel =[-random.randrange(1,3),random.randrange(0,2)]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel,ball_pos  # these are numbers
    global score1, score2  # these are ints
    ball_pos =[300,200]
    ball_vel =[0,0]
    paddle1_vel = 0
    paddle2_vel =0    
    spawn_ball("LEFT")
    #scores
    score1 = 0
    score2 = 0
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,paddle1_vel,paddle2_vel
    inc = 0
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
       
    # update ball 
    if(ball_pos[0] == PAD_WIDTH + BALL_RADIUS):
        spawn_ball("RIGHT")
    if( ball_pos[0] == WIDTH-PAD_WIDTH- BALL_RADIUS):
        spawn_ball("LEFT")
    if(ball_pos[1] == BALL_RADIUS or ball_pos[1] == HEIGHT-BALL_RADIUS or ball_pos[1]== 0 or ball_pos[1]==HEIGHT):
        ball_vel[1] = -ball_vel[1]
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    # draw ball
    canvas.draw_circle(ball_pos,BALL_RADIUS,4,"Teal","Blue")
    
    
    # update paddle's vertical position, keep paddle on the screen
   
    if(up[1] == 0 or down[1] == PAD_HEIGHT or up[1]== HEIGHT-PAD_HEIGHT or down[1] == HEIGHT):  #reflection
        paddle1_vel = -paddle1_vel
    if(up2[1] == 0 or down2[1] == PAD_HEIGHT or up2[1]== HEIGHT-PAD_HEIGHT or down2[1] == HEIGHT):
        paddle2_vel = - paddle2_vel
    
    up[1] += paddle1_vel
    down[1] += paddle1_vel
    up2[1] += paddle2_vel
    down2[1] += paddle2_vel
   
    # draw paddles
    canvas.draw_line(up,down,PAD_WIDTH,"Brown")
    canvas.draw_line(up2,down2,PAD_WIDTH,"Brown")
    # determine whether paddle and ball collide 
    if ((ball_pos[0] - BALL_RADIUS) == PAD_WIDTH):
        if(not(ball_pos[1] >= up[1] and ball_pos[1] <= down[1])):
            score2 += 1
        
          
            
    if ((ball_pos[0] + BALL_RADIUS) == WIDTH -PAD_WIDTH):
        if(not(ball_pos[1] >= up2[1] and ball_pos[1] <= down2[1])):
            score1 += 1
        
            
       
    # draw scores
    canvas.draw_text(str(score1) , (150,100),40 ,"Gray" )
    canvas.draw_text(str(score2) , (450,100),40 ,"Gray" )
        
def keydown(key):
    global paddle1_vel, paddle2_vel,k,q
    if(up[1]>= HALF_PAD_HEIGHT and down[1] <= HEIGHT- HALF_PAD_HEIGHT):
        if(key == simplegui.KEY_MAP["w"]):
            if(k == 0):
                paddle1_vel = - paddle1_vel     #paddle1   
                k=1
        elif(key == simplegui.KEY_MAP["s"]):
            if(k== 1):
                paddle1_vel = -paddle1_vel
                k = 0
         
    if(up2[1]>= HALF_PAD_HEIGHT and down2[1] <= HEIGHT- HALF_PAD_HEIGHT):   
        if(key == simplegui.KEY_MAP["up"]): 
            if(q == 0):
                paddle2_vel = -paddle2_vel 
                q = 1#paddle2        
       
        elif(key == simplegui.KEY_MAP["down"]):
            if(q == 1):
                q = 0
                paddle2_vel = -paddle2_vel
   
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if(key == simplegui.KEY_MAP["w"]):
        paddle1_vel = -5 #reflection
    elif(key == simplegui.KEY_MAP["s"] ):
        paddle1_vel = 5
        
    if(key == simplegui.KEY_MAP["up"] ):
        paddle2_vel = -5  #reflection
    elif( key == simplegui.KEY_MAP["down"] ):
        paddle2_vel = 5
def button_handler():
    ball_pos =[300,200]
    new_game()
    

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1 = frame.add_button('Reset', button_handler)

# start frame
new_game()
frame.start()
