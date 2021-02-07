from graphics import *

def main():
    win = GraphWin('Matrix', 800, 600)
    win.setBackground('black')

    letter = Text(Point(win.getWidth()/2, 0), 'A')
    letter.setTextColor('green');
    letter.setSize(20)
    letter.draw(win)

    loops = 0

    while True:
        count = 0
        letter.move(0,1)
        while count < 100000:
            count+=1
        loops+=1
        if loops >= win.getHeight():
            break

    win.getMouse()
    win.close()

main()