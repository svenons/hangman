import os
import turtle
import time
import random
import threading

#open guess words file
filepath = os.path.dirname(os.path.abspath(__file__))
guesswords = filepath + "\\guesswords.txt"
rulesf = filepath + "\\rules.txt"
leaderboardf = filepath + "\\leaderboard.txt"
global guesswordslist
guesswordslist = []

#quit game
def exit():
    quit()

#append them into list
try:
    with open(guesswords, 'r', encoding='utf8') as f:
        vardi = f.readlines()
    for a in vardi:
        a = a.replace("\n", "")
        guesswordslist.append(a)
except:
    print("No wordslist file... exiting...")
    quit()

#game resolution
screensizewidth = 1280
screensizeheight = 720

#game setup
turtle.setup(screensizewidth, screensizeheight)
logs = turtle.Screen()
logs.title("The Hangman Guessing Game")
logs.bgcolor("grey")
rupucis = turtle.Turtle("arrow")
rupucis.hideturtle()
rupucis.speed(5)
teksts = turtle.Turtle("circle")
teksts.hideturtle()
teksts.speed(0)
teksts.penup()
nametext = turtle.Turtle("circle")
nametext.hideturtle()
nametext.speed(0)
nametext.penup()
scoretext = turtle.Turtle("circle")
scoretext.hideturtle()
scoretext.speed(0)
scoretext.penup()
striketext = turtle.Turtle("circle")
striketext.hideturtle()
striketext.speed(0)
striketext.penup()



def tgoto(cmd, parw, parh, who=teksts):
    if cmd == 1:
        tgoto.a = (screensizewidth / parw)
        tgoto.b = (screensizeheight / parh)
    elif cmd == 2:
        tgoto.a = (tgoto.a + parw)
        tgoto.b = (tgoto.b + parh)
    else:
        tgoto.a = parw
        tgoto.b = parh
    who.goto(tgoto.a, tgoto.b)

def writeHeading(text, alignv="center", who=teksts):
    style = ("Roboto", 30, "italic")
    who.write(text, font=style, align=alignv)

def writeP(text, alignv="left", who=teksts):
    style = ("Roboto", 20, "italic")
    who.write(text, font=style, align=alignv)

tgoto(1, 50, 3)
writeHeading("Rules of The Hang Man Guessing Game: ")

rules = []
try:
    with open(rulesf, 'r', encoding='utf8') as f:
        rulesread = f.readlines()
    for a in rulesread:
        a = a.replace("\n", "")
        rules.append(a)
except:
    print("No rules file... exiting...")
    quit()

gotowidth = -(screensizewidth / 3)
tgoto(2, gotowidth, 0)
for eachrule in rules:
    tgoto(2, 0, -50)
    eachrule = "* " + eachrule
    writeP(eachrule)

tgoto(1, 2.1, 2.5, scoretext)
def scorewrite(value):
    scoretext.clear()
    scoret = "Score: " + str(value)
    writeP(text=scoret, alignv="right", who=scoretext)


def strikewrite(wvalue, tvalue):
    tgoto(1, 2.1, 2.5, striketext)
    tgoto.a = -(tgoto.a)
    tgoto.b = -(tgoto.b)
    tgoto(3, tgoto.a, tgoto.b, striketext)
    striketext.clear()
    strikec = "Word strikes: " + str(wvalue)
    writeP(text=strikec, alignv="left", who=striketext)
    tgoto(2, 0, 50, who=striketext)
    strikec = "Total strikes: " + str(tvalue)
    writeP(text=strikec, alignv="left", who=striketext)

def chooseWord():
        chooseWord.wordofchoice = random.choice(guesswordslist)
        guesswordslist.remove(chooseWord.wordofchoice)
        chooseWord.wordguess = chooseWord.wordofchoice
        gameItself.enteraletter = "Enter a letter"
        chooseWord.wordlist = []
        chooseWord.wordguesshidden = ""
        for a in chooseWord.wordguess:
            chooseWord.wordlist.append(a)
        for x in range(0, len(chooseWord.wordguess)):
            chooseWord.wordguesshidden = chooseWord.wordguesshidden + "_"
        wordstrike = 0
        strikewrite(wordstrike, gameItself.strike)

def gameItself():
            try:
                chooseWord.wordguess
            except:
                chooseWord()
            tgoto(1, 10, 2.5)
            tgoto.b = -(tgoto.b)
            tgoto(3, tgoto.a, tgoto.b)
            writeP(f"Current guess: {chooseWord.wordguesshidden}")
            guess = turtle.textinput("Guessing Game", gameItself.enteraletter)
            try:
                if len(guess) == 1:
                    if guess in chooseWord.wordofchoice:
                        index = chooseWord.wordlist.index(guess)
                        gameItself.wordlist[index] = "xyz"
                        startofword = chooseWord.wordguesshidden[:index]
                        endofword = chooseWord.wordguesshidden[(index + 1):]
                        chooseWord.wordguesshidden = startofword + guess + endofword
                        teksts.clear()
                        writeP(f"Current guess: {chooseWord.wordguesshidden}")
                        gameItself.enteraletter = "Enter a letter"
                    else:
                        gameItself.enteraletter = "Such letter isn't found"
                        try:
                            gameItself.strike
                        except:
                            gameItself.strike = 0

                        try:
                            gameItself.wordstrike
                        except:
                            gameItself.wordstrike = 0

                        gameItself.wordstrike = gameItself.wordstrike + 1
                        if gameItself.wordstrike > 5:
                            gameItself.strike = gameItself.strike + 1
                            if gameItself.strike == 1:
                                rupucis.penup()
                                rupucis.right(90)
                                rupucis.forward(200)
                                rupucis.left(90)
                                rupucis.pendown()
                                rupucis.backward(100)
                                rupucis.forward(200)
                            if gameItself.strike == 2:
                                rupucis.backward(100)
                                rupucis.left(90)
                                rupucis.forward(200)
                            if gameItself.strike == 3:
                                rupucis.forward(200)
                            if gameItself.strike == 4:
                                rupucis.right(90)
                                rupucis.forward(200)
                            if gameItself.strike == 5:
                                rupucis.right(90)
                                rupucis.forward(50)
                            if gameItself.strike == 6:
                                rupucis.penup()
                                rupucis.forward(20)
                                rupucis.right(90)
                                rupucis.forward(10)
                                rupucis.left(90)
                                rupucis.pendown()
                                rupucis.circle(20)
                            if gameItself.strike == 7:
                                rupucis.penup()
                                rupucis.forward(20)
                                rupucis.left(90)
                                rupucis.forward(20)
                                rupucis.right(90)
                                rupucis.pendown()
                                rupucis.forward(120)
                            if gameItself.strike == 8:
                                rupucis.backward(100)
                                rupucis.left(45)
                                rupucis.forward(50)
                                rupucis.backward(50)
                                rupucis.right(90)
                            if gameItself.strike == 9:
                                rupucis.forward(50)
                                rupucis.backward(50)
                                rupucis.left(45)
                                rupucis.forward(100)
                            if gameItself.strike == 10:
                                rupucis.left(45)
                                rupucis.forward(60)
                                rupucis.backward(60)
                            if gameItself.strike == 11:
                                rupucis.right(90)
                                rupucis.forward(60)
                                rupucis.backward(60)
                                rupucis.left(45)
                                rupucis.left(90)
                                rupucis.penup()
                                tgoto(1, 2.5, 5, who=rupucis)
                                tgoto.a = -(tgoto.a)
                                tgoto(3, tgoto.a, tgoto.b, rupucis)
                                try:
                                    gameItself.score
                                except:
                                    gameItself.score = 0
                                writeHeading(f"You have lost the game \nScore: {gameItself.score}", alignv="left", who=rupucis)
                                time.sleep(5)
                                return                    
                else:
                    gameItself.enteraletter = "Incorrect entry"
                if chooseWord.wordguesshidden == gameItself.wordguess:
                    teksts.clear()
                    try:
                        gameItself.score
                    except:
                        gameItself.score = 0
                    gameItself.score = gameItself.score + len(chooseWord.wordguesshidden)
                    scorewrite(gameItself.core)
                    writeP(f"Score earned: {len(chooseWord.wordguesshidden)}")
                    time.sleep(3)
                    if guesswordslist == []:
                        return
                    else:
                        chooseWord()
            except:
                windo = turtle.textinput("Quit", 'Enter "q" if you want to quit, "r" to restart game')
                if windo == "q":
                    quit()
                if windo == "r":
                                        score = 0
                                        gameItself.strike = 0
                                        gameItself.wordstrike = 0
                                        gameItself.enteraletter = "Enter a letter"
                                        rupucis.clear()
                                        rupucis.goto(0, 0)
            strikewrite(gameItself.wordstrike, gameItself.strike)
            gameItself()

def continuegame():
        teksts.clear()
        while True:
            name = turtle.textinput("Nickname", "Enter your nickname")
            if name == None:
                continue
            elif name == "":
                continue
            else:
                break
        tgoto(1, 2.1, 2.5, nametext)
        tgoto.a = -(tgoto.a)
        tgoto(3, tgoto.a, tgoto.b, nametext)
        writeHeading(text=name, alignv="left", who=nametext)
        scorewrite(0)
        strikewrite(0, 0)
        gameItself()

try:
    gameItself.strike
except:
    gameItself.strike = 0

gotoheight = -(screensizeheight / 2.5)
gotowidth = (screensizewidth / 10)
tgoto(3, gotowidth, gotoheight)

writeHeading("Press space to continue", alignv="left")

logs.onkeypress(continuegame, "space")


try:
    gameItself.gameFinished
except:
    gameItself.gameFinished = False

logs.onkeypress(exit, "q")



logs.listen()
turtle.done()

'''def uzprieksu():
    rupucis.forward(10)
def atpakal():
    rupucis.backward(10)
def palabi():
    rupucis.right(45)
def pakreisi():
    rupucis.left(45)

logs.onkeypress(uzprieksu, "Up")
logs.onkey(atpakal, "Down")
logs.onkey(palabi, "Right")
logs.onkey(pakreisi, "Left")'''