import os
import turtle
import time
import random

#open guess words file
filepath = os.path.dirname(os.path.abspath(__file__))
guesswords = filepath + "\\guesswords.txt"
rulesf = filepath + "\\rules.txt"
leaderboardf = filepath + "\\leaderboard.txt"
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

def continuegame():
        teksts.clear()
        name = turtle.textinput("Nickname", "Enter your nickname")
        tgoto(1, 2.1, 2.5, nametext)
        tgoto.a = -(tgoto.a)
        tgoto(3, tgoto.a, tgoto.b, nametext)
        writeHeading(text=name, alignv="left", who=nametext)

        
        scorewrite(0)
        strikewrite(0, 0)

        wordofchoice = random.choice(guesswordslist)
        guesswordslist.remove(wordofchoice)
        wordguess = wordofchoice
        enteraletter = "Enter a letter"
        wordlist = []
        wordguesshidden = ""
        for a in wordguess:
            wordlist.append(a)
        for x in range(0, len(wordguess)):
            wordguesshidden = wordguesshidden + "_"


        
        tgoto(1, 10, 2.5)
        tgoto.b = -(tgoto.b)
        tgoto(3, tgoto.a, tgoto.b)
        writeP(f"Current guess: {wordguesshidden}")
        while True:
            guess = turtle.textinput("Guessing Game", enteraletter)
            try:
                if len(guess) == 1:
                    if guess in wordofchoice:
                        index = wordlist.index(guess)
                        wordlist[index] = "xyz"
                        startofword = wordguesshidden[:index]
                        endofword = wordguesshidden[(index + 1):]
                        wordguesshidden = startofword + guess + endofword
                        teksts.clear()
                        writeP(f"Current guess: {wordguesshidden}")
                        enteraletter = "Enter a letter"
                    else:
                        enteraletter = "Such letter isn't found"
                        try:
                            strike
                        except:
                            strike = 0

                        try:
                            wordstrike
                        except:
                            wordstrike = 0

                        wordstrike = wordstrike + 1
                        if wordstrike > 5:
                            strike = strike + 1
                            if strike == 1:
                                rupucis.penup()
                                rupucis.right(90)
                                rupucis.forward(200)
                                rupucis.left(90)
                                rupucis.pendown()
                                rupucis.backward(100)
                                rupucis.forward(200)
                            if strike == 2:
                                rupucis.backward(100)
                                rupucis.left(90)
                                rupucis.forward(200)
                            if strike == 3:
                                rupucis.forward(200)
                            if strike == 4:
                                rupucis.right(90)
                                rupucis.forward(200)
                            if strike == 5:
                                rupucis.right(90)
                                rupucis.forward(50)
                            if strike == 6:
                                rupucis.penup()
                                rupucis.forward(20)
                                rupucis.right(90)
                                rupucis.forward(10)
                                rupucis.left(90)
                                rupucis.pendown()
                                rupucis.circle(20)
                            if strike == 7:
                                rupucis.penup()
                                rupucis.forward(20)
                                rupucis.left(90)
                                rupucis.forward(20)
                                rupucis.right(90)
                                rupucis.pendown()
                                rupucis.forward(120)
                            if strike == 8:
                                rupucis.backward(100)
                                rupucis.left(45)
                                rupucis.forward(50)
                                rupucis.backward(50)
                                rupucis.right(90)
                            if strike == 9:
                                rupucis.forward(50)
                                rupucis.backward(50)
                                rupucis.left(45)
                                rupucis.forward(100)
                            if strike == 10:
                                rupucis.left(45)
                                rupucis.forward(60)
                                rupucis.backward(60)
                            if strike == 11:
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
                                    score
                                except:
                                    score = 0
                                writeHeading(f"You have lost the game \nScore: {score}", alignv="left", who=rupucis)
                                time.sleep(5)
                                while True:
                                    windo = turtle.textinput("Guessing Game", 'Enter "q" if you want to quit, "r" if restart game')
                                    if windo == "q":
                                        quit()
                                    if windo == "r":
                                        score = 0
                                        strike = 0
                                        wordstrike = 0
                                        enteraletter = "Enter a letter"
                                        rupucis.clear()
                                        rupucis.goto(0, 0)
                                        break


                        strikewrite(wordstrike, strike)


                        
                else:
                    enteraletter = "Incorrect entry"
                if wordguesshidden == wordguess:
                    teksts.clear()
                    try:
                        score
                    except:
                        score = 0
                    score = score + len(wordguesshidden)
                    scorewrite(score)
                    writeP(f"Score earned: {len(wordguesshidden)}")
                    time.sleep(3)
                    if guesswordslist == []:
                        quit()
                    else:
                        wordofchoice = random.choice(guesswordslist)
                        guesswordslist.remove(wordofchoice)
                        wordguess = wordofchoice
                        enteraletter = "Enter a letter"
                        wordlist = []
                        wordguesshidden = ""
                        for a in wordguess:
                            wordlist.append(a)
                        for x in range(0, len(wordguess)):
                            wordguesshidden = wordguesshidden + "_"
                        teksts.clear()
                        writeP(f"Current guess: {wordguesshidden}")

                        wordstrike = 0
                        strikewrite(wordstrike, strike)
            except:
                windo = turtle.textinput("Quit", 'Enter "q" if you want to quit, "r" to restart game')
                if windo == "q":
                    quit()
                if windo == "r":
                                        score = 0
                                        strike = 0
                                        wordstrike = 0
                                        enteraletter = "Enter a letter"
                                        rupucis.clear()
                                        rupucis.goto(0, 0)
                continue

gotoheight = -(screensizeheight / 2.5)
gotowidth = (screensizewidth / 10)
tgoto(3, gotowidth, gotoheight)

logs.onkeypress(exit, "q")

writeHeading("Press space to continue", alignv="left")
logs.onkeypress(continuegame, "space")



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