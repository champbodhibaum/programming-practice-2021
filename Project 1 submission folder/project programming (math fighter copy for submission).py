#PROJECT PROGRAMMING

#import pygame
import pickle as p
from random import *
from time import *
import threading

#============================================================================================================#

charlist=[]
charlist2=[]
charplay=[]

def countdown():
    global timer
    timer=5
    for x in range(5):
        sleep(1)
        timer=timer-1


def inputfilter(x):
    testinput = input(x)
    if testinput == "quit" or testinput=="QUIT":
        print("\nThank you for playing MATH FIGHTER, have a nice day :)")
        exit()
    else:
        return testinput

def answercheck(b,c,H1,H2,S1,S2,turn):
    while timer>=0:
        if b!=None and b==c:

            print("You spent",5-timer,"second(s)")
            sleep(1.5)
            print("Correct! You can attack the opponent")
            while True:
                if turn=="PLAYER 1" and S1<2:
                    d=inputfilter("input 's' to use skill: ")
                    if d=="s":
                        break
                    else:
                        pass
                elif turn=="PLAYER 2" and S2<2:
                    d=inputfilter("input 's' to use skill: ")
                    if d=="s":
                        break
                    else:
                        pass

                elif turn=="PLAYER 1" and S1>=2:
                    d=inputfilter(
                        "\nYour ultimate is ready\n".upper()+
                        "input 's' to use skill and input 'u' to use ultimate skill: "
                        )
                    if d=="s" or d=="u":
                        break
                    else:
                        pass
                elif turn=="PLAYER 2" and S2>=2:
                    d=inputfilter(
                        "\nYour ultimate is ready\n".upper()+
                        "input 's' to use skill and input 'u' to use ultimate skill: "
                        )
                    if d=="s" or d=="u":
                        break
                    else:
                        pass
            if d=="s":
                critrate=randint(1,5)
                if turn=="PLAYER 1":
                    turn="PLAYER 2"
                    S1=S1+1
                    if critrate==1:
                        print("\n"+charplay[0].charname,"uses",charplay[0].charskill+"!!!","CRITICAL HITTTT!!")
                        H2=H2-2
                        sleep(1.5)
                    elif critrate==5:
                        print("\n"+charplay[0].charname,"uses",charplay[0].charskill+"!!!","However, "+charplay[1].charname,"dodges it!!")
                        H2=H2
                        sleep(1.5)
                    else:
                        print("\n"+charplay[0].charname,"uses",charplay[0].charskill+"!!!")
                        H2=H2-1
                        sleep(1.5)
                else:
                    turn="PLAYER 1"
                    S2=S2+1
                    if critrate==1:
                        print("\n"+charplay[1].charname,"uses",charplay[1].charskill+"!!!","CRITICAL HITTTT!!")
                        H1=H1-2
                        sleep(1.5)
                    elif critrate==5:
                        print("\n"+charplay[1].charname,"uses",charplay[1].charskill+"!!!","However, "+charplay[0].charname,"dodges it!!")
                        H1=H1
                        sleep(1.5)
                    else:
                        print("\n"+charplay[1].charname,"uses",charplay[1].charskill+"!!!")
                        H1=H1-1
                        sleep(1.5)
            elif d=="u":
                critrate=randint(1,5)
                if turn=="PLAYER 1":
                    turn="PLAYER 2"
                    S1=0
                    if critrate==1:
                        print("\n"+charplay[0].charname,"uses",charplay[0].charult+"!!!","CRTICAL HITTTT!!")
                        H2=H2-4
                        sleep(1.5)
                    elif critrate==5:
                        print("\n"+charplay[0].charname,"uses",charplay[0].charult+"!!!","However, "+charplay[1].charname,"dodges it!!")
                        H2=H2
                        sleep(1.5)
                    else:
                        print("\n"+charplay[0].charname,"uses",charplay[0].charult+"!!!")
                        H2=H2-2
                        sleep(1.5)
                else:
                    turn="PLAYER 1"
                    S2=0
                    if critrate==1:
                        print("\n"+charplay[1].charname,"uses",charplay[1].charult+"!!!","CRTICAL HITTTT!!")
                        H1=H1-4
                        sleep(1.5)
                    elif critrate==5:
                        print("\n"+charplay[1].charname,"uses",charplay[1].charult+"!!!","However, "+charplay[0].charname,"dodges it!!")
                        H1=H1
                        sleep(1.5)
                    else:
                        print("\n"+charplay[1].charname,"uses",charplay[1].charult+"!!!")
                        H1=H1-2
                        sleep(1.5)

            break
        if b!=None and b!=c:  
            exploderate=randint(1,5)
            print("You spent",5-timer,"second(s)")
            sleep(1.5)
            print("Incorrect! You cannot attack the opponent")
            if turn=="PLAYER 1":
                turn="PLAYER 2"
                if exploderate==1:
                    H1=H1-1
                    print("\nUnfortunately,",charplay[0].charname,"slipped and hit its head")
                    
                else:
                    pass
                S1=0
            else:
                turn="PLAYER 1"
                if exploderate==1:
                    H2=H2-1
                    print("\nUnfortunately,",charplay[1].charname,"slipped and hit its head")
                    
                else:
                    pass
                S2=0
            sleep(3)
            break
        if timer<=0:
            exploderate=randint(1,5)
            print("5 seconds has passed")
            sleep(1.5)
            print("Too late! You cannot attack the opponent")
            if turn=="PLAYER 1":
                turn="PLAYER 2"
                if exploderate==1:
                    print("\n"+charplay[0].charname,"is confused and hurts itself")
                    H1=H1-1
                    
                else:
                    pass
                S1=0
            else:
                turn="PLAYER 1"
                if exploderate==1:
                    print("\n"+charplay[1].charname,"is confused and hurts itself")
                    H2=H2-1
                    
                else:
                    pass
                S2=0
            sleep(2)
            break

    return H1,H2,S1,S2,turn

def game():
    rules=inputfilter("\nInput 't' to see the game rules and input 'n' to start playing: ")
    while True:
        if rules == "t" or rules=="T":
            print("\n+=========================================================================+")
            print("\nhow to play:".upper())
            print("Each player take turns solving the math problem")
            print("Each player are given 5 seconds to solve each math problem")
            print("If the player solves the math problem correctly, one can use normal skill or ultimate skill to attack the other player")
            print("If the player fails to give the correct answer within the given time, one loses its turn and cannot attack")
            print("Normal skill deals 1 damage and ultimate skill deals 2 damage to the opponent")
            print("The ultimate skill is ready if the player answered correctly 3 times in a row")
            print("There is a chance that your attack will deal critical damage (2x damage)")
            print("There is a chance that your opponent will dodge your attack")
            print("If a player failed to give the correct answer, there is a chance that the player will hurt itself")
            print("The game ends when a player has 0 health")
            print("\nInput 'quit' anytime to stop playing the game")
            print("\n+=========================================================================+")
            input("INPUT ANYTHING TO CONTINUE\n")
            break
        elif rules =="n" or rules=="N":
            break
        else:
            pass

    while True:        
        H1=inputfilter("\nInput "+charplay[0].charname+"'s health (RECOMMENDED HEALTH = 10): ")
        try:
            int(H1)
            H1=int(H1)
            break
        except:
            print("The input must only be integer!")
            pass
    while True:        
        H2=inputfilter("\nInput "+charplay[1].charname+"'s health (RECOMMENDED HEALTH = 10): ")
        try:
            int(H2)
            H2=int(H2)
            break
        except:
            print("The input must only be integer!")
            pass

    S1=0
    S2=0
    turn="PLAYER 1"

    while H1>0 and H2>0:
        countdown_thread=threading.Thread(target = countdown)
        print("\n(P1)",charplay[0].charname+"'s current health","=",H1)
        print("(P2)",charplay[1].charname+"'s current health","=",H2,"\n")

        while True:
            a=inputfilter("Please input 'r' to start solving the math problem "+"("+turn+"): ")
            if a=="r" or a=="R":
                break
            else:
                pass

        countdown_thread.start()

        while timer>0:
            symbols=randint(1,5)
            if symbols==1:
                num1=randint(20,100)
                num2=randint(20,100)
            elif symbols==2:
                num1=randint(20,100)
                num2=randint(20,100)
            elif symbols==3 or symbols==4 or symbols==5:
                num1=randint(2,20)
                num2=randint(2,20)

            if symbols==1:
                print("What is",num1,"+",num2,"?")
                b=inputfilter("Input your answer: ")
                if timer<=0:
                    b=None
                elif timer>0:
                    pass
                c=str(num1+num2)
                H1,H2,S1,S2,turn=answercheck(b,c,H1,H2,S1,S2,turn)

            if symbols==2:
                print("What is",num1,"-",num2,"?")
                b=inputfilter("Input your answer: ")
                if timer<=0:
                    b=None
                elif timer>0:
                    pass
                c=str(num1-num2)
                H1,H2,S1,S2,turn=answercheck(b,c,H1,H2,S1,S2,turn)

            if symbols==3 or symbols==4 or symbols==5:
                print("What is",num1,"*",num2,"?")
                b=inputfilter("Input your answer: ")
                if timer<=0:
                    b=None
                elif timer>0:
                    pass
                c=str(num1*num2)
                H1,H2,S1,S2,turn=answercheck(b,c,H1,H2,S1,S2,turn)

    if H1==0:
        print("\n"+charplay[0].charname+"'s current health","=",0)
        print(charplay[1].charname+"'s current health","=",H2,"\n")
        print(charplay[1].charname,"won!")
    if H2==0:
        print("\n"+charplay[0].charname+"'s current health","=",H1)
        print(charplay[1].charname+"'s current health","=",0,"\n")
        print(charplay[0].charname,"won!")
    if H1<0:
        print("\n"+charplay[0].charname+"'s current health","=",0)
        print(charplay[1].charname+"'s current health","=",H2,"\n")
        print("Fatality!!",charplay[1].charname,"won!")
    if H2<0:
        print("\n"+charplay[0].charname+"'s current health","=",H1)
        print(charplay[1].charname+"'s current health","=",0,"\n")
        print("Fatality!!",charplay[0].charname,"won!")

class Character:
    def __init__(self):
        self.charname = input("Input your character's name: ")
        self.charskill = input("Input your character's skill name: ")
        self.charult = input("Input your character's ultimate skill name: ")

#============================================================================================================#
#GAME

print(
    "\n=================================\n"
    "     welcome to math figther\n".upper()+
    "=================================\n"
    )

input("Input anything to start the game\n".upper())

while True: #loop the whole game
    index=0
    player=1
    while True: #loop when choosing characters
        a=inputfilter("\n(PLAYER "+str(player)+") Input 'c' to create a new character or input 'e' to use an existing character: ")
        if a=="c" or a=="C":
            charlist.append(Character())
            file=open(charlist[0].charname,"wb")
            p.dump(charlist,file)
            print("\n(PLAYER "+str(player)+")")
            print("Name:",charlist[0].charname)
            print("Skill:",charlist[0].charskill)
            print("Ultimate:",charlist[0].charult)
            charplay.append(charlist[0])
            player+=1
            index+=1
            charlist=[]
            if player>2:
                break


        elif a=="e" or a=="E":
            index2=0
            try:
                print("You are using an existing character")
                e=input("Input the character's name to use the existing character: ")
                file2=open(e,"rb")
                charlist2=p.load(file2)

                print("\n(PLAYER "+str(player)+")")
                print("Name:",charlist2[index2].charname)
                print("Skill:",charlist2[index2].charskill)
                print("Ultimate:",charlist2[index2].charult)
                charplay.append(charlist2[index2])
                index2+=1
                player+=1
                if player>2:
                    break

            except:
                print("This character does not exist!")
                pass

    # print("\nDo you want to save the character first? New characters will not be saved if the game is stopped midway")
    # print("If no new character is created, press 'n' to continue playing")
    # while True: #loop to save the characters or not
    #     f=inputfilter("Press 'y' to save the character and 'n' to continue playing without saving the new character: ")
    #     if f=="y":
    #         print("Your character is saved, start the game again to play")
    #         quit()
    #     elif f=="n":
    #         break
    #     else:
    #         pass

    game()

    while True:
        g=inputfilter("\nDo you want to play again? input 'play' to play again and input 'quit' to stop playing: ")
        if g=="play" or g=="PLAY":
            break
        else:
            pass