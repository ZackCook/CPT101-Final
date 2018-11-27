'''
Zack Cook
Cpt 101 final
'''

from graphics import *
from time import sleep
from random import *

def main():

    WIDTH = 800
    HEIGHT = 500

    X_VELOCITY = .5
    Y_VELOCITY = 0

    score = 0#users current score
    lives = 5#number of lives the user has before they lose

    currentWords = []

    window = GraphWin("Text game",WIDTH,HEIGHT)#window where everything happens
    inputField = Entry(Point(WIDTH/2,485),20)#used for inputting text

    wordbank = open("wordbank.txt",'r')#database of words that can pop up on screen
    words = wordbank.readlines()

    ''' commenting out test values
    onScreenWord = Text(Point(100,100), "TEST")
    onScreenWord.setSize(22)

    onScreenWord2 = Text(Point(100,300), "TEST2")
    onScreenWord2.setSize(22)

    currentWords.append(onScreenWord)#adds text to list of current words on the screen
    currentWords.append(onScreenWord2)

    onScreenWord.draw(window)
    onScreenWord2.draw(window)
    '''
    inputField.draw(window)  # draws text field on the screen

    running = True
    while(running == True):#main loop
        try:
            creationValue = randint(1,4)
            if(creationValue == 2):
                currentWords.append(Text(Point(100,randint(20,HEIGHT-50)),words[randrange(len(words))]))
                #for()

            #onScreenWord.move(X_VELOCITY,Y_VELOCITY)

            for word in currentWords:
                #print(currentWords)#debug
                if(word.isDrawn() == False):
                    word.draw(window)
                word.setXVelocity(X_VELOCITY)
                word.move(word.getXVelocity(), word.getYVelocity())
                if(word.getAnchor().getX() == WIDTH):
                    word.setXVelocity(0)
                    word.setTextColor("red")
                    del word

            sleep(.01)
        except (GraphicsError):
            pass
    window.getMouse()  # closes window when you click in it
if __name__ == '__main__':
    main()