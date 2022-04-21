# template for "Stopwatch: The Game"

# define global variables


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
import simplegui

form = "00:00.0"
count = 0
x = 0
y = 0

def format(t):
    global form , x, tenth
    hour = t // 600
    sec = ( t % 600 ) / 10
    tenth = (t% 600) % 10 
    
    if( hour <10):
        hr = '0'+str(hour)+":" 
    else:
        hr = str(hour)+":"
    if( sec <10):
        s = '0'+str(sec)+"."+str(tenth)
    else:
        s= str(sec)+"."+str(tenth)
        
    form = hr + s   #format
       

    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global c
    c = 1
    timer.start()
    
def stop():
    global x,c,y, tenth    
    if (c == 1):
        y = y + 1  		#y = no of Total stops
        if(tenth == 0):
            x = x + 1 	#x =  no of winning stops
        c = 0
        timer.stop()
    
def reset():
    global count, x, y,c
    count = 0
    x = 0
    y = 0
    if(c==1):
        timer.stop()
    format(0)
    
    
# define event handler for timer with 0.1 sec interval
def tick():
    global count
    count = count + 1
    format(count)


# define draw handler
def draw(canvas):
    global form, x, y
    canvas.draw_text( form , [100,200],52, " White")
    canvas.draw_text((str(x)+'/'+str(y)), [320,50], 32, "Blue")
    canvas.draw_text("Won / Total", [300,15],20 ,"White")
    
# create frame
frame = simplegui.create_frame("Stopwatch Game",400,400)
timer = simplegui.create_timer(100,tick)

# register event handlers
frame.add_button(" Start ",start,200)
frame.add_button(" Stop ",stop,200)
frame.add_button(" Reset ",reset,200)
frame.set_draw_handler(draw)

# start frame
frame.start()


# Please remember to review the grading rubric
