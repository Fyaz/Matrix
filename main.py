from graphics import *
from random import randint

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']

def main():
    win = GraphWin('Matrix', 800, 600)
    win.setBackground('black')

    text_size = 15
    trail_length = 5 # the number of letters behind the main letter
    freq = 5 # MUST BE NON-ZERO. How frequently do you want letters to appear?
    num_letters = win.getWidth()//text_size
    
    llist = []  # the list of letters that will keep track of everything that's falling
    lcount = [] # the list that keeps track of the delay for each letter
    lloops = [] # the list that tracks how far down a letter has gone
    lcolor = [] # the list of tuples that tracks the colors of each letter per iteration

    traillist = [] # a list to keep track of the letters after they've been drawn (used to undraw them)

    for i in range(num_letters):
        llist.append(randint(0, len(letters)-1))
        lcount.append(0)
        lcolor.append((randint(0,255),randint(0,255),randint(0,255)))
        lloops.append(randint(-win.getHeight()//freq, 0))
        p = Text(Point(-text_size, -text_size), 'A')
        for j in range(trail_length):
            traillist.append(p)
        
    while True:
        for i in range(len(llist)):
            #Undraw
            for j in range(trail_length):   # undraw the trail
                traillist[i+j*num_letters].undraw()

            #Draw
            for j in range(trail_length):
                if j == 0:
                    t = Text(Point(i*text_size, lloops[i]*text_size-2*j*text_size), letters[llist[i]])
                else:
                    t = Text(Point(i*text_size, lloops[i]*text_size-2*j*text_size), letters[randint(0, len(letters)-1)])
                t.setTextColor(color_rgb(lcolor[i][0]*(trail_length-j)//trail_length, lcolor[i][1]*(trail_length-j)//trail_length, lcolor[i][2]*(trail_length-j)//trail_length))
                t.setSize(text_size)
                t.draw(win)
                traillist[i+j*num_letters] = t

            # Update
            lcount[i]+=1
            if lcount[i] > 1:
                lloops[i]+=1
                lcount[i] = 0

            # Reset the letter back to the top
            if lloops[i] >= (win.getHeight() + trail_length*2*text_size)/text_size:
                lloops[i] = randint(-win.getHeight()//freq, 0)
                llist[i] = randint(0, len(letters)-1)
                lcolor[i] = (randint(0,255),randint(0,255),randint(0,255))
        
    win.getMouse()
    win.close()

main()
