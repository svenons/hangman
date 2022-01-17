import os
import sys
import turtle
import time
import random
import string
from unidecode import unidecode
import wget

#path to .py file
filepath = os.path.dirname(os.path.abspath(__file__))
guesswords = filepath + "\\guesswords.txt"
customwords = filepath + "\\customwords.txt"
rulesf = filepath + "\\rules.txt"
leaderboardf = filepath + "\\leaderboard.txt"
global guesswordslist
guesswordslist = []

#quit game
def exit():
    os._exit(0)

#clear python console:
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

#game resolution
while True:
    print("Resolution choices: ")
    resolutionchoices = ["540p (qHD)", "720p (HD) **Default", "1080p (FHD)", "2K", "1440p (QHD)"]
    for a in resolutionchoices:
        print("     *", a)
    resolution = input("Select resolution: ")
    if resolution == "qhd":
        resolution = input('Did you mean qHD(540p) or QHD(1440p)?: ')
    if resolution in ["540", "540p", "qHD", "960x540"]:
        gameresolution = "940x540"
        break
    elif resolution in ["720p", "720", "1280x720", "HD", "hd"]:
        gameresolution = "1280x720"
        break
    elif resolution in ["1080p", "1080", "FHD", "fhd", "1920x1080"]:
        gameresolution = "1920x1080"
        break
    elif resolution in ["2K", "2k", "2048", "2048p", "2048x1080"]:
        gameresolution = "2048x1080"
        break
    elif resolution in ["1440p", "QHD", "qhd", "1440", "2560x1440"]:
        gameresolution = "2560x1440"
        break
    else:
        print("\nSelecting default resolution...")
        time.sleep(1)
        gameresolution = "1280x720"
        break
    
index = gameresolution.index("x")
screensizewidth = int(gameresolution[:index])
screensizeheight = int(gameresolution[(index+1):])


try:
    os.remove(rulesf)
except:
    rules_dont_exist = True
try:
    os.remove(guesswords)
except:
    guesswords_dont_exist = True

rules = []
wget.download('http://80.209.239.78/owncloud/index.php/s/2gENrZrI0JZiPyb/download', rulesf)
with open(rulesf, 'r', encoding='utf8') as f:
        rulesread = f.readlines()
for a in rulesread:
        a = a.replace("\n", "")
        rules.append(a)
clearConsole()

print("Categories: ")
categorylist = ["easy", "animals", "foods", "travel", "custom (customwords.txt in your folder)"]
for a in categorylist:
    print("     *", a)
wordstoguess = input('Select category: ')
while True:
    if wordstoguess in ["e", "easy"]:
        wget.download('http://80.209.239.78/owncloud/index.php/s/Co9FDfZJDHvr6AJ/download', guesswords)
        break
    elif wordstoguess in ["a", "animals", "animal"]:
        wget.download('http://80.209.239.78/owncloud/index.php/s/Tdi36BfRTphYFdi/download', guesswords)
        break
    elif wordstoguess in ["f", "food","foods"]:
        wget.download('http://80.209.239.78/owncloud/index.php/s/cNdFeduhVw4OURC/download', guesswords)
        break
    elif wordstoguess in ["travel", "t", "world"]:
        wget.download('http://80.209.239.78/owncloud/index.php/s/5athpyNycfHHUX5/download', guesswords)
        break
    elif wordstoguess in ["custom", "c"]:
        guesswords = customwords
        try:
            open(guesswords)
        except:
            with open(guesswords, mode="w") as f:
                f.write("")
            print("\nNo custom file found. Created empty file. Add each word to a new line in file.")
            time.sleep(5)
            print("\nExitting...")
            time.sleep(0.5)
            exit()
        if os.stat(guesswords).st_size == 0:
                    print("\nEmpty custom file. Add each word to a new line in file.")
                    time.sleep(5)
                    print("\nExitting...")
                    time.sleep(0.5)
                    exit()
        else:
            break
    else:
        wordstoguess = input('Incorrect entry. Enter first letter of category or "custom" to select customwords.txt in your folder: ')
clearConsole()
print("The Game Turtle window has been opened, proceed to it to continue the game...")

#append them into list
with open(guesswords, 'r', encoding='utf8') as f:
    vardi = f.readlines()
for a in vardi:
    a = a.replace("\n", "")
    a = a.replace(string.punctuation, "")
    a = unidecode(a, "utf-8")
    guesswordslist.append(a)
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
    if gameresolution == "940x540":
        style = ("Roboto", 20, "italic")
    else:
        style = ("Roboto", 30, "italic")
    who.write(text, font=style, align=alignv)

def writeP(text, alignv="left", who=teksts):
    if gameresolution == "940x540":
        style = ("Roboto", 15, "italic")
    else:
        style = ("Roboto", 20, "italic")
    who.write(text, font=style, align=alignv)

tgoto(1, 50, 3)
writeHeading("Rules of The Hang Man Guessing Game: ")

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
    #writeP(text=strikec, alignv="left", who=striketext)
    tgoto(2, 0, 50, who=striketext)
    strikec = "Strikes: " + str(tvalue)
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
        gameItself.wordstrike = 0
        strikewrite(gameItself.wordstrike, gameItself.strike)

def gameItself():
            try:
                chooseWord.wordguess
            except:
                chooseWord()
            tgoto(1, 10, 2.5)
            tgoto.b = -(tgoto.b)
            tgoto(3, tgoto.a, tgoto.b)
            teksts.clear()
            writeP(f"Current guess: {chooseWord.wordguesshidden}")
            guess = turtle.textinput("Guessing Game", gameItself.enteraletter)
            try:
                if len(guess) == 1:
                    guess = unidecode(guess, "utf-8")
                    found = False
                    for x in [guess, guess.upper(), guess.lower()]:
                        if x in chooseWord.wordofchoice:
                            found = True
                            def moreIndex():
                                try:
                                    chooseWord.wordlist.index(x)
                                    return True
                                except:
                                    return False
                            while moreIndex() == True:
                                index = chooseWord.wordlist.index(x)
                                chooseWord.wordlist[index] = "xyz"
                                startofword = chooseWord.wordguesshidden[:index]
                                endofword = chooseWord.wordguesshidden[(index + 1):]
                                chooseWord.wordguesshidden = startofword + x + endofword
                                teksts.clear()
                                writeP(f"Current guess: {chooseWord.wordguesshidden}")
                                gameItself.enteraletter = "Enter a letter"
                    if found == False:
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
                                teksts.clear()
                                writeP(f"The word was: {chooseWord.wordofchoice}")
                                writeHeading(f"You have lost the game \nScore: {gameItself.score}", alignv="left", who=rupucis)
                                time.sleep(1)
                                windo = turtle.textinput("Quit", 'Enter "q" if you want to quit, otherwhise the game will restart')
                                if windo in ["q", "x"]:
                                        os._exit(0)
                                else:
                                        gameItself.score = 0
                                        gameItself.strike = 0
                                        gameItself.wordstrike = 0
                                        gameItself.enteraletter = "Enter a letter"
                                        rupucis.clear()
                                        rupucis.goto(0, 0)
                                        chooseWord()
                                strikewrite(gameItself.wordstrike, gameItself.strike)
                                gameItself()
                                                   
                else:
                    gameItself.enteraletter = "Incorrect entry"

                if chooseWord.wordguesshidden == chooseWord.wordofchoice:
                    teksts.clear()
                    try:
                        gameItself.score
                    except:
                        gameItself.score = 0
                    gameItself.score = gameItself.score + len(chooseWord.wordguesshidden)
                    scorewrite(gameItself.score)
                    writeP(f"Score earned: {len(chooseWord.wordguesshidden)}")
                    time.sleep(2)
                    if guesswordslist == []:
                        teksts.clear()
                        tgoto(1, 2.5, 5, who=rupucis)
                        tgoto.a = -(tgoto.a)
                        tgoto(3, tgoto.a, tgoto.b, rupucis)
                        writeP("No more words...\nExitting...")
                        writeHeading(f"Score: {gameItself.score}", alignv="left", who=rupucis)
                        time.sleep(5)
                        os._exit(0)
                    else:
                        chooseWord()
                        
            except:
                windo = turtle.textinput("Quit", 'Enter "q" if you want to quit, "r" to restart game')
                while True:
                    if windo == None:
                        #windo = turtle.textinput("Quit", 'Enter "q" if you want to quit, "r" to restart game')
                        gameItself()
                    elif windo in ["q", "x"]:
                        os._exit(0)
                    elif "r" in windo:
                        chooseWord()
                        gameItself.score = 0
                        gameItself.strike = 0
                        gameItself.wordstrike = 0
                        gameItself.enteraletter = "Enter a letter"
                        rupucis.clear()
                        rupucis.goto(0, 0)
                        break
                    else:
                        windo = turtle.textinput("Quit", 'Enter "q" if you want to quit, "r" to restart game')
                        continue
            strikewrite(gameItself.wordstrike, gameItself.strike)
            gameItself()

def continuegame():
        teksts.clear()
        name = turtle.textinput("Nickname", "Enter your nickname")
        while True:
            if name == None:
                name = turtle.textinput("Nickname", "You have to choose a nickname")
            elif name == "":
                name = turtle.textinput("Nickname", "You have to choose a nickname")
            elif len(name) > 7:
                name = turtle.textinput("Nickname", "You have to choose shorter a nickname")
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
quit()