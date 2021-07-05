import pygame
from pygame.constants import KEYDOWN, K_BACKSPACE, K_DOWN, K_ESCAPE, K_RETURN, K_SPACE, K_TAB, K_UP, K_r, K_s, K_u, MOUSEBUTTONDOWN, MOUSEMOTION
import pickle as p
import time
import random
from pygame.image import load
import threading
from pygame import mixer

pygame.init()

main_page = pygame.display.set_mode((1600,900))
pygame.display.set_caption("Math Fighter")

page=0

class Character:
    def __init__(self,input_name,input_skill,input_ult,input_app):
        self.charname = input_name
        self.charskill = input_skill
        self.charult = input_ult
        self.charapp = input_app

class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont("adobegothicstdboldopentype", 40)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def draw2(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont("adobegothicstdboldopentype", 25)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def draw3(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont("adobegothicstdboldopentype", 35)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def drawtitle(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont("adobegothicstdboldopentype", 125)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

def maketext(fonttype,fontsize,content,color):
    text_font = pygame.font.SysFont(fonttype,fontsize)
    text_surface = text_font.render(content,True,(color))
    return text_surface

def maketextoutline(win,fonttype,fontsize,content,textcolor,outlinecolor,x,y,outline):
    text_font = pygame.font.SysFont(fonttype,fontsize)
    text_surface = text_font.render(content,True,textcolor)
    text_surface2 = text_font.render(content,True,outlinecolor)
    outlinetext1 = win.blit(text_surface2,(x+outline,y))
    outlinetext2 = win.blit(text_surface2,(x-outline,y))
    outlinetext3 = win.blit(text_surface2,(x,y+outline))
    outlinetext4 = win.blit(text_surface2,(x,y-outline))
    text = win.blit(text_surface,(x,y))
    return text,outlinetext1,outlinetext2,outlinetext3,outlinetext4

def loadimage(filelocation,size):
    background = pygame.image.load(filelocation).convert_alpha()
    background = pygame.transform.scale(background,(size))
    return background


def charidle(char_idle1,char_idle2):
    if char_idle1 == True:
            if charplay[0].charapp == 1:
                main_page.blit(loadimage(r"MATH FIGHTER GUI\fight animation\char1 left 1.png",(1600,900)),(-110,0))
            if charplay[0].charapp == 2:
                main_page.blit(loadimage(r"MATH FIGHTER GUI\fight animation\char2 left 1.png",(1600,900)),(90,0))
            if charplay[0].charapp == 3:
                main_page.blit(loadimage(r"MATH FIGHTER GUI\fight animation\char3 left 1.png",(1600,900)),(-90,0))
    if char_idle2 == True:
        if charplay[1].charapp == 1:
            main_page.blit(loadimage(r"MATH FIGHTER GUI\fight animation\char1 right 1.png",(1600,900)),(100,0))
        if charplay[1].charapp == 2: 
            main_page.blit(loadimage(r"MATH FIGHTER GUI\fight animation\char2 right 1.png",(1600,900)),(-100,0))
        if charplay[1].charapp == 3: 
            main_page.blit(loadimage(r"MATH FIGHTER GUI\fight animation\char3 right 1.png",(1600,900)),(90,0))

    main_page.blit(loadimage(r"MATH FIGHTER GUI\char menu\char menu 1.png",(1600,900)),(0,0))
    main_page.blit(loadimage(r"MATH FIGHTER GUI\char menu\char menu 2.png",(1600,900)),(0,0))


def check_answer_correct(playerturn,show_answer,attack,H1,H2,S1,S2,game_start,critrate,char_hit1,char_hit2,char_hit_miss1,char_hit_miss2,crit_effect1,crit_effect2):
    if playerturn == 1:
        if show_answer == True:
            main_page.blit(maketext(None,100,"Correct","black"),(150,400))
            if attack == 1:
                if critrate == 1:
                    H2=H2
                    S1+=1
                    print("miss")
                    char_hit_miss1 = True
                elif critrate == 5:
                    H2-=2
                    S1+=1
                    print("crit")
                    char_hit1 = True
                    crit_effect2 = True
                else:
                    H2-=1
                    S1+=1
                    print("normal")
                    char_hit1 = True
                playerturn = 2
                game_start = False
            elif attack == 2:
                if critrate == 1:
                    H2=H2
                    print("miss")
                    char_hit_miss1 = True
                elif critrate == 5:
                    H2-=4
                    print("crit")
                    char_hit1 = True
                    crit_effect2 = True
                else:
                    H2-=2
                    print("normal")
                    char_hit1 = True
                S1=0
                playerturn = 2
                game_start = False
            else:
                pass

    else:
        if show_answer == True:
            main_page.blit(maketext(None,100,"Correct","black"),(1200,400))
            if attack == 1:
                if critrate == 1:
                    H1=H1
                    S2+=1
                    print("miss")
                    char_hit_miss2 = True
                elif critrate == 5:
                    H1-=2
                    S2+=1
                    print("crit")
                    char_hit2 = True
                    crit_effect1 = True
                else:
                    H1-=1
                    S2+=1
                    print("normal")
                    char_hit2 = True
                playerturn = 1
                game_start = False
            elif attack == 2:
                if critrate == 1:
                    H1=H1
                    print("miss")
                    char_hit_miss2 = True
                elif  critrate == 5:
                    H1-=4
                    print("crit")
                    char_hit2 = True
                    crit_effect1 = True
                else:
                    H1-=2
                    print("normal")
                    char_hit2 = True
                S2=0
                playerturn = 1
                game_start = False

    return H1,H2,S1,S2,playerturn,game_start,attack,char_hit1,char_hit2,char_hit_miss1,char_hit_miss2,crit_effect1,crit_effect2

def check_answer_wrong(playerturn,show_answer,game_start,H1,H2,S1,S2,critrate,incorrect1,incorrect2):
    if playerturn == 1:
        S1=0
        if show_answer == True:
            main_page.blit(maketext(None,100,"Incorrect","black"),(125,400))
            if critrate == 1:
                H1-=1
                print("selfhit")
            else:
                H1=H1
            playerturn = 2
            incorrect1 = True
            game_start = False
    else:
        S2=0
        if show_answer == True:
            main_page.blit(maketext(None,100,"Incorrect","black"),(1180,400))
            if critrate == 1:
                H2-=1
                print("selfhit")
            else:
                H2=H2
            playerturn = 1
            incorrect2 = True
            game_start = False

    return playerturn,H1,H2,S1,S2,game_start,incorrect1,incorrect2

def countdown():
    global timer
    timer=5
    for x in range(5):
        time.sleep(1)
        timer=timer-1

def intro_menu():
    mixer.music.load("MATH FIGHTER GUI/background music 2.mp3")
    mixer.music.set_volume(0.5)
    mixer.music.play(-1)
    run = True
    global page
    page = 1
    global charlist
    global char2list
    global charlist2
    global charplay
    charlist=[]
    char2list=[]
    charlist2=[]
    charplay=[]

    #button
    btn=button("azure3",580,400,450,100,"START")
    
    while run:
        main_page.blit(loadimage(r"MATH FIGHTER GUI\game background 50%.png",(1600,900)),(0,0))

        #text
        maketextoutline(main_page,"adobegothicstdboldopentype",135,"MATH FIGHTER","black","white",340,200,2)
        maketextoutline(main_page,"adobegothicstdboldopentype",30,"Press any key to continue","black","white",630,530,1)

        #button
        btn.draw(main_page,2)

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn.isOver(pos):
                    character_selection_menu()
            if event.type == pygame.MOUSEMOTION:
                if btn.isOver(pos):
                    btn.color = ("green")
                else:
                    btn.color = ("azure3")
            if event.type == pygame.KEYDOWN:
                if event.key != K_ESCAPE:
                    character_selection_menu()

        pygame.display.update()
    quit()

player=1
index1=0
index2=0

def character_selection_menu():
    global player
    global page
    page = 1
    run = True
    btn1=button("azure3",500,400,550,100,"CREATE A NEW CHARACTER")
    btn2=button("azure3",500,600,550,100,"USE AN EXISTING CHARACTER")
    exitbtn=button("azure3",25,25,90,60,"BACK")
    rulesbtn=button("azure3",140,25,190,60,"HOW TO PLAY")
    while run:
        
        #text
        main_page.blit(loadimage(r"MATH FIGHTER GUI\game background 50%.png",(1600,900)),(0,0))
        maketextoutline(main_page,"adobegothicstdboldopentype",100,"Character Selection".upper(),"black","white",250,215,2)
        main_page.blit(maketext("adobegothicstdboldopentype",50,"PLAYER "+str(player),"black"),(675,25))

        btn1.draw3(main_page,2)
        btn2.draw3(main_page,2)
        exitbtn.draw2(main_page,2)
        rulesbtn.draw2(main_page,2)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn1.isOver(pos):
                    create_character_menu()
                if btn2.isOver(pos):
                    use_existing_character_menu()
                if exitbtn.isOver(pos):
                    intro_menu()
                if rulesbtn.isOver(pos):
                    game_rules_menu()

            if event.type == pygame.MOUSEMOTION:
                if btn1.isOver(pos):
                    btn1.color = "green"
                else:
                    btn1.color = "azure3"

                if btn2.isOver(pos):
                    btn2.color = "green"
                else:
                    btn2.color = "azure3"
                
                if exitbtn.isOver(pos):
                    exitbtn.color = "green"
                else:
                    exitbtn.color = "azure3"

                if rulesbtn.isOver(pos):
                    rulesbtn.color = "green"
                else:
                    rulesbtn.color = "azure3"

            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    intro_menu()
                if event.key == K_UP:
                    options = 1
                    btn1.color = "green"
                    btn2.color = "azure3"
                    if options == 2: 
                        options-=1
                    else:
                        options = 1
                if event.key == K_DOWN:
                    options = 2
                    btn1.color = "azure3"
                    btn2.color = "green"
                    if options == 1:
                        options+=1
                    else:
                        options = 2
                if event.key == K_RETURN:
                    try:
                        if options == 1:
                            create_character_menu()
                        elif options == 2:
                            use_existing_character_menu()
                    except:
                        pass
                    
        pygame.display.update()
    quit()


def create_character_menu():
    global Character
    run = True
    global page
    page = 2

    passive_color = pygame.Color("azure3")
    active_color = pygame.Color("gray20")
    color1 = passive_color
    color2 = passive_color
    color3 = passive_color
    active1 = False
    active2 = False
    active3 = False

    input_miss1 = False
    input_miss2 = False
    input_miss3 = False
    input_miss4 = False

    #input name
    inputnamefont = pygame.font.SysFont("adobegothicstdboldopentype",30)
    input_name = ""
    input_rect1=pygame.Rect(700,300,100,50)

    #input skill
    inputskillfont = pygame.font.SysFont("adobegothicstdboldopentype",30)
    input_skill = ""
    input_rect2=pygame.Rect(700,400,100,50)

    #input ult
    inputultfont = pygame.font.SysFont("adobegothicstdboldopentype",30)
    input_ult = ""
    input_rect3=pygame.Rect(700,500,100,50)

    #buttons
    createbtn=button("azure3",880,795,120,60,"CREATE")
    char1btn=button("gray85",450,600,150,150,"1")
    char2btn=button("gray85",650,600,150,150,"2")
    char3btn=button("gray85",850,600,150,150,"3")
    exitbtn=button("azure3",25,25,90,60,"BACK")
    rulesbtn=button("azure3",140,25,190,60,"HOW TO PLAY")

    input_app = 0

    while run:
        global player
        global index1
        global index2

        #main_page.fill((255,255,255))
        main_page.blit(loadimage(r"MATH FIGHTER GUI\game background 50%.png",(1600,900)),(0,0))

        main_page.blit(loadimage(r"MATH FIGHTER GUI\character create menu bar.png",(1600,900)),(0,50))

        main_page.blit(maketext("adobegothicstdboldopentype",50,"PLAYER "+str(player),"black"),(675,25))

        #title create character
        maketextoutline(main_page,"adobegothicstdboldopentype",80,"CREATE YOUR CHARACTER","black","white",250,150,2)

        if input_miss1 == True:
            main_page.blit(maketext("adobegothicstdboldopentype",20,"X     Missing name","red"),(975,315))
        if input_miss2 == True:
            main_page.blit(maketext("adobegothicstdboldopentype",20,"X     Missing skill","red"),(975,415))
        if input_miss3 == True:
            main_page.blit(maketext("adobegothicstdboldopentype",20,"X     Missing ultimate","red"),(975,515))
        if input_miss4 == True:
            maketextoutline(main_page,"adobegothicstdboldopentype",20,"Missing character","red","white",645,770,2)

        #input name box
        main_page.blit(maketext("adobegothicstdboldopentype",30,"CHARACTER NAME","black"),(input_rect1.x-270,input_rect1.y+10))
        input_name_surface = inputnamefont.render(input_name,True,(0,0,0))
        main_page.blit(input_name_surface,((input_rect1.x+10,input_rect1.y+10)))
        pygame.draw.rect(main_page,color1,input_rect1,3)
        input_rect1.w = max(300,input_name_surface.get_width()+20)

        #input skill box
        main_page.blit(maketext("adobegothicstdboldopentype",30,"SKILL NAME","black"),(input_rect2.x-180,input_rect2.y+10))
        input_skill_surface = inputskillfont.render(input_skill,True,(0,0,0))
        main_page.blit(input_skill_surface,((input_rect2.x+10,input_rect2.y+10)))
        pygame.draw.rect(main_page,color2,input_rect2,3)
        input_rect2.w = max(300,input_skill_surface.get_width()+20)

        #input ultimate box
        main_page.blit(maketext("adobegothicstdboldopentype",30,"ULTIMATE NAME","black"),(input_rect3.x-245,input_rect3.y+10))
        input_ult_surface = inputultfont.render(input_ult,True,(0,0,0))
        main_page.blit(input_ult_surface,((input_rect3.x+10,input_rect3.y+10)))
        pygame.draw.rect(main_page,color3,input_rect3,3)
        input_rect3.w = max(300,input_ult_surface.get_width()+20)

        #buttons
        createbtn.draw2(main_page,2)
        char1btn.draw(main_page,2)
        char2btn.draw(main_page,2)
        char3btn.draw(main_page,2)
        exitbtn.draw2(main_page,2)
        rulesbtn.draw2(main_page,2)

        #character picture
        main_page.blit(loadimage(r"MATH FIGHTER GUI\avatar pictures\char 1.png",(140,140)),(455,605))
        main_page.blit(loadimage(r"MATH FIGHTER GUI\avatar pictures\char 2.png",(140,140)),(655,605))
        main_page.blit(loadimage(r"MATH FIGHTER GUI\avatar pictures\char 3.png",(150,150)),(850,600))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if createbtn.isOver(pos):
                    if input_name == "":
                        input_miss1 = True
                    elif input_name != "":
                        input_miss1 = False
                    if input_skill == "":
                        input_miss2 = True
                    elif input_skill != "":
                        input_miss2 = False
                    if input_ult == "":
                        input_miss3 = True
                    elif input_ult != "":
                        input_miss3 = False
                    if input_app == 0:
                        input_miss4 = True
                    elif input_app != 0:
                        input_miss4 = False
                    
                    if input_name != "" and input_skill != "" and input_ult != "" and input_app != 0:
                        if player == 1:
                            charlist.append(Character(input_name,input_skill,input_ult,input_app))
                            file=open("MATH FIGHTER GUI/Characters/Character "+charlist[0].charname,"wb")
                            p.dump(charlist,file)
                            charplay.append(charlist[0])
                            index1+=1
                            player+=1
                        elif player == 2:
                            char2list.append(Character(input_name,input_skill,input_ult,input_app))
                            file=open("MATH FIGHTER GUI/Characters/Character "+char2list[0].charname,"wb")
                            p.dump(char2list,file)
                            charplay.append(char2list[0])
                            index1+=1
                            player+=1

                        if player>2:
                            map_choice_menu()
                        else:
                            character_selection_menu()
                if exitbtn.isOver(pos):
                    character_selection_menu()
                if rulesbtn.isOver(pos):
                    game_rules_menu()

            if event.type == pygame.MOUSEMOTION:
                if createbtn.isOver(pos):
                    createbtn.color = "green"
                else:
                    createbtn.color = "azure3"

                if exitbtn.isOver(pos):
                    exitbtn.color = "green"
                else:
                    exitbtn.color = "azure3"

                if rulesbtn.isOver(pos):
                    rulesbtn.color = "green"
                else:
                    rulesbtn.color = "azure3"


            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect1.collidepoint(event.pos):
                    active1 = True
                    color1 = active_color
                else:
                    active1 = False
                    color1 = passive_color

                if input_rect2.collidepoint(event.pos):
                    active2 = True
                    color2 = active_color
                else:
                    active2 = False
                    color2 = passive_color

                if input_rect3.collidepoint(event.pos):
                    active3 = True
                    color3 = active_color
                else:
                    active3 = False
                    color3 = passive_color
                
                if char1btn.isOver(pos):
                    char1btn.color = "chartreuse"
                    char2btn.color = "gray85"
                    char3btn.color = "gray85"
                    input_app = 1
                elif char2btn.isOver(pos):
                    char1btn.color = "gray85"
                    char2btn.color = "chartreuse"
                    char3btn.color = "gray85"
                    input_app = 2
                elif char3btn.isOver(pos):
                    char1btn.color = "gray85"
                    char2btn.color = "gray85"
                    char3btn.color = "chartreuse"
                    input_app = 3

            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    character_selection_menu()

                if active1 == True:
                    color1 = active_color
                    if event.key == K_BACKSPACE:
                        input_name = input_name[:-1]
                    
                    # elif event.key == K_RETURN:
                    #     active1 = False
                    #     color1 = passive_color
                    #     active2 = True
                    #     color2 = active_color

                    elif event.key == K_RETURN or event.key == K_TAB:
                        pass

                    else:
                        if len(input_name)<=14:
                            input_name += event.unicode
                            input_miss1 = False
                        else:
                            pass

                if active2 == True:
                    if event.key == K_BACKSPACE:
                        input_skill = input_skill[:-1]

                    # elif event.key == K_TAB:
                    #     active2 = False
                    #     color2 = passive_color
                    #     active3 = True
                    #     color3 = active_color

                    elif event.key == K_RETURN or event.key == K_TAB:
                        pass

                    else:
                        if len(input_skill)<=14:
                            input_skill += event.unicode
                            input_miss2 = False
                        else:
                            pass

                if active3 == True:
                    if event.key == K_BACKSPACE:
                        input_ult = input_ult[:-1]

                    # elif event.key == K_TAB:
                    #     active1 = True
                    #     color1 = active_color
                    #     active3 = False
                    #     color3 = passive_color

                    elif event.key == K_RETURN or event.key == K_TAB:
                        pass

                    else:
                        if len(input_ult)<=14:
                            input_ult += event.unicode
                            input_miss3 = False
                        else:
                            pass

        pygame.display.update()
    quit()

def use_existing_character_menu():
    charlist2=[]
    run = True
    global page
    page = 3

    passive_color = pygame.Color("azure3")
    active_color = pygame.Color("gray20")

    #input name
    inputnamefont = pygame.font.SysFont("adobegothicstdboldopentype",30)
    input_name = ""
    input_rect1=pygame.Rect(400,300,100,50)

    color1 = passive_color
    active1 = False
    char_miss = False
    char_show = False
    input_miss = False

    #buttons
    exitbtn=button("azure3",25,25,90,60,"BACK")
    loadbtn=button("azure3",575,375,100,60,"LOAD")
    char1btn=button("cyan2",1100,530,150,150,"1")
    char2btn=button("orange1",1100,530,150,150,"2")
    char3btn=button("olivedrab2",1100,530,150,150,"3")
    continuebtn=button("azure3",1107,725,140,60,"CONTINUE")
    rulesbtn=button("azure3",140,25,190,60,"HOW TO PLAY")

    while run:
        global player
        global index1
        global index2

        #main_page.fill((255,255,255))
        main_page.blit(loadimage(r"MATH FIGHTER GUI\game background 50%.png",(1600,900)),(0,0))
        main_page.blit(loadimage(r"MATH FIGHTER GUI\use character menu bar.png",(1600,900)),(0,50))
        
        #title text
        maketextoutline(main_page,"adobegothicstdboldopentype",80,"USE YOUR CHARACTER","black","white",350,150,2)

        main_page.blit(maketext("adobegothicstdboldopentype",50,"PLAYER "+str(player),"black"),(675,25))

        #input name box
        main_page.blit(maketext("adobegothicstdboldopentype",30,"CHARACTER NAME","black"),(input_rect1.x-270,input_rect1.y+10))
        input_name_surface = inputnamefont.render(input_name,True,(0,0,0))
        main_page.blit(input_name_surface,((input_rect1.x+10,input_rect1.y+10)))
        pygame.draw.rect(main_page,color1,input_rect1,3)
        input_rect1.w = max(300,input_name_surface.get_width()+20)

        #buttons
        exitbtn.draw2(main_page,2)
        loadbtn.draw2(main_page,2)
        rulesbtn.draw2(main_page,2)

        #character information
        if char_show == True:
            main_page.blit(maketext("adobegothicstdboldopentype",30,"CHARACTER NAME  :  "+charlist2[0].charname,"black"),(953,300))
            main_page.blit(maketext("adobegothicstdboldopentype",30,"CHARACTER SKILL  :  "+charlist2[0].charskill,"black"),(960,370))
            main_page.blit(maketext("adobegothicstdboldopentype",30,"CHARACTER ULTIMATE  :  "+charlist2[0].charult,"black"),(895,440))
            if charlist2[0].charapp == 1:
                char1btn.draw(main_page,2)
                main_page.blit(loadimage(r"MATH FIGHTER GUI\avatar pictures\char 1.png",(140,140)),(1105,535))
            if charlist2[0].charapp == 2:
                char2btn.draw(main_page,2)
                main_page.blit(loadimage(r"MATH FIGHTER GUI\avatar pictures\char 2.png",(140,140)),(1105,535))
            if charlist2[0].charapp == 3:
                char3btn.draw(main_page,2)
                main_page.blit(loadimage(r"MATH FIGHTER GUI\avatar pictures\char 3.png",(150,150)),(1100,530))
            else:
                pass
            continuebtn.draw2(main_page,2)

        #no character
        if char_miss == True:
            maketextoutline(main_page,"adobegothicstdboldopentype",20,"X      Character does not exist","red","white",675,315,2)

        if input_miss == True:
            maketextoutline(main_page,"adobegothicstdboldopentype",20,"X      Missing input","red","white",675,315,2)

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    character_selection_menu()
                if event.key == K_RETURN:
                    if input_name == "":
                        input_miss = True
                        char_miss = False
                    else:
                        try:
                            file2=open("MATH FIGHTER GUI/Characters/Character "+input_name,"rb")
                            charlist2=p.load(file2)
                            char_show = True
                            char_miss = False
                            input_miss = False
                        except:
                            char_miss = True
                            input_miss = False

                if active1 == True:
                    if event.key == K_BACKSPACE:
                        input_name = input_name[:-1]
                    elif event.key == K_TAB or event.key == K_RETURN:
                        pass
                    else:
                        if len(input_name)<=14:
                            input_name += event.unicode
                        else:
                            pass

            if event.type == pygame.MOUSEBUTTONDOWN:
                if exitbtn.isOver(pos):
                    character_selection_menu()
                if input_rect1.collidepoint(event.pos):
                    active1 = True
                    color1 = active_color
                else:
                    active1 = False
                    color1 = passive_color
                if loadbtn.isOver(pos):
                    if input_name == "":
                        input_miss = True
                        char_miss = False
                    else:
                        try:
                            file2=open("MATH FIGHTER GUI/Characters/Character "+input_name,"rb")
                            charlist2=p.load(file2)
                            char_show = True
                            char_miss = False
                            input_miss = False
                        except:
                            char_miss = True
                            input_miss = False
                        
                
                if continuebtn.isOver(pos):
                    charplay.append(charlist2[0])
                    index2+=1
                    player+=1
                    if player>2:
                        map_choice_menu()
                    else:
                        character_selection_menu()
                if rulesbtn.isOver(pos):
                    game_rules_menu()

            if event.type == pygame.MOUSEMOTION:
                if exitbtn.isOver(pos):
                    exitbtn.color = "green"
                else:
                    exitbtn.color = "azure3"
                if loadbtn.isOver(pos):
                    loadbtn.color = "green"
                else:
                    loadbtn.color = "azure3"
                if continuebtn.isOver(pos):
                    continuebtn.color = "green"
                else:
                    continuebtn.color = "azure3"
                if rulesbtn.isOver(pos):
                    rulesbtn.color = "green"
                else:
                    rulesbtn.color = "azure3"

        pygame.display.update()
    quit()

def map_choice_menu():
    run = True
    global input_map
    input_map = 0
    global page
    page = 4

    map_miss = False

    #buttons
    map1btn=button("azure3",70,400,450,253,"1")
    map2btn=button("azure3",570,400,450,253,"2")
    map3btn=button("azure3",1070,400,450,253,"3")
    nextbtn=button("azure3",1300,700,150,75,"NEXT")
    rulesbtn=button("azure3",25,25,190,60,"HOW TO PLAY")

    while run:
        #main_page.fill((255,255,255))
        main_page.blit(loadimage(r"MATH FIGHTER GUI\game background 50%.png",(1600,900)),(0,0))


        #title create character
        maketextoutline(main_page,"adobegothicstdboldopentype",150,"MAP","black","white",645,150,2)

        if map_miss == True:
            # main_page.blit(maketext(None,30,"Choose the map","red"),(720,680))
            maketextoutline(main_page,"adobegothicstdboldopentype",25,"Choose the map","red","white",710,680,2)

        #buttons
        map1btn.draw(main_page,2)
        map2btn.draw(main_page,2)
        map3btn.draw(main_page,2)
        nextbtn.draw2(main_page,2)
        rulesbtn.draw2(main_page,2)

        #map names
        if input_map == 1:
            maketextoutline(main_page,"adobegothicstdboldopentype",30,"Minecraft","black","darkgoldenrod1",230,350,2)
        else:
            maketextoutline(main_page,"adobegothicstdboldopentype",30,"Minecraft","black","white",230,350,2)
        if input_map == 2:
            maketextoutline(main_page,"adobegothicstdboldopentype",30,"Moon","black","darkgoldenrod1",755,350,2)
        else:
            maketextoutline(main_page,"adobegothicstdboldopentype",30,"Moon","black","white",755,350,2)
        if input_map == 3:
            maketextoutline(main_page,"adobegothicstdboldopentype",30,"Classroom","black","darkgoldenrod1",1235,350,2)
        else:
            maketextoutline(main_page,"adobegothicstdboldopentype",30,"Classroom","black","white",1235,350,2)


        #map pictures
        main_page.blit(loadimage(r"MATH FIGHTER GUI\map1 background.jpg",(430,242)),(80,406))
        main_page.blit(loadimage(r"MATH FIGHTER GUI\map2 background.jpg",(430,242)),(580,406))
        main_page.blit(loadimage(r"MATH FIGHTER GUI\map3 background.jpg",(430,242)),(1080,406))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if map1btn.isOver(pos):
                    map1btn.color = "darkgoldenrod1"
                    map2btn.color = "azure3"
                    map3btn.color = "azure3"
                    input_map = 1
                    map_miss = False
                if map2btn.isOver(pos):
                    map1btn.color = "azure3"
                    map2btn.color = "darkgoldenrod1"
                    map3btn.color = "azure3"
                    input_map = 2
                    map_miss = False
                if map3btn.isOver(pos):
                    map1btn.color = "azure3"
                    map2btn.color = "azure3"
                    map3btn.color = "darkgoldenrod1"
                    input_map = 3
                    map_miss = False
                if nextbtn.isOver(pos):
                    if input_map == 0:
                        map_miss = True
                    else:
                        difficulty_mode_menu()

                if rulesbtn.isOver(pos):
                    game_rules_menu()
            if event.type == pygame.MOUSEMOTION:
                if nextbtn.isOver(pos):
                    nextbtn.color = "green"
                else:
                    nextbtn.color = "azure3"

                if rulesbtn.isOver(pos):
                    rulesbtn.color = "green"
                else:
                    rulesbtn.color = "azure3"
            
        pygame.display.update()
    quit()


def difficulty_mode_menu():
    run = True
    global difficulty
    difficulty = 0

    #buttons
    rulesbtn=button("azure3",140,25,190,60,"HOW TO PLAY")
    easybtn=button("azure3",650,300,300,100,"EASY")
    mediumbtn=button("azure3",650,425,300,100,"MEDIUM")
    hardbtn=button("azure3",650,550,300,100,"HARD")
    nextbtn=button("azure3",800,750,150,75,"NEXT")
    exitbtn=button("azure3",25,25,90,60,"BACK")

    global page
    page = 5
    difficulty_miss = False
    while run:
        main_page.blit(loadimage(r"MATH FIGHTER GUI\game background 50%.png",(1600,900)),(0,0))
        maketextoutline(main_page,"adobegothicstdboldopentype",100,"DIFFICULTY","black","white",540,100,2)

        if difficulty_miss == True:
            maketextoutline(main_page,"adobegothicstdboldopentype",25,"Choose the difficulty","red","white",700,700,2)

        rulesbtn.draw2(main_page,2)
        easybtn.draw3(main_page,2)
        mediumbtn.draw3(main_page,2)
        hardbtn.draw3(main_page,2)
        nextbtn.draw2(main_page,2)
        exitbtn.draw2(main_page,2)
        
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
            if event.type == MOUSEBUTTONDOWN:
                if rulesbtn.isOver(pos):
                    game_rules_menu()
                if easybtn.isOver(pos):
                    easybtn.color = "green"
                    mediumbtn.color = "azure3"
                    hardbtn.color = "azure3"
                    difficulty = 1
                if mediumbtn.isOver(pos):
                    easybtn.color = "azure3"
                    mediumbtn.color = "green"
                    hardbtn.color = "azure3"
                    difficulty = 2
                if hardbtn.isOver(pos):
                    easybtn.color = "azure3"
                    mediumbtn.color = "azure3"
                    hardbtn.color = "green"
                    difficulty = 3
                if nextbtn.isOver(pos):
                    if difficulty == 0:
                        difficulty_miss = True
                    else:
                        loading_menu()
                if exitbtn.isOver(pos):
                    map_choice_menu()
                
            if event.type == MOUSEMOTION:
                if rulesbtn.isOver(pos):
                    rulesbtn.color = "green"
                else:
                    rulesbtn.color = "azure3"

                if nextbtn.isOver(pos):
                    nextbtn.color = "green"
                else:
                    nextbtn.color = "azure3"

                if exitbtn.isOver(pos):
                    exitbtn.color = "green"
                else:
                    exitbtn.color = "azure3"

        pygame.display.update()
    quit()


def game_rules_menu():
    run = True

    #button
    exitbtn=button("azure3",25,25,90,60,"BACK")
    while run:
        #main_page.fill((255,255,255))
        main_page.blit(loadimage(r"MATH FIGHTER GUI\game background 50%.png",(1600,900)),(0,0))

        #button
        exitbtn.draw2(main_page,2)

        #transparent background
        main_page.blit(loadimage(r"MATH FIGHTER GUI\rules background.png",(1600,900)),(60,0))

        #title and game rules
        maketextoutline(main_page,"adobegothicstdboldopentype",90,"GAME RULES","black","white",575,100,2)
        main_page.blit(maketext("adobegothicstdboldopentype",40,"HOW TO PLAY","black"),(210,220))
        main_page.blit(maketext("adobegothicstdboldopentype",25,"Each player take turns solving the math problem","black"),(210,300))
        main_page.blit(maketext("adobegothicstdboldopentype",25,"Each player are given 5 seconds to solve each math problem","black"),(210,355))
        main_page.blit(maketext("adobegothicstdboldopentype",25,"If the player solves the math problem correctly, one can use normal skill or ultimate skill to attack","black"),(210,410))
        main_page.blit(maketext("adobegothicstdboldopentype",25,"If the player fails to give the correct answer within the given time, one loses its turn and cannot attack","black"),(210,465))
        main_page.blit(maketext("adobegothicstdboldopentype",25,"Normal skill deals 1 damage and ultimate skill deals 2 damage to the opponent","black"),(210,520))
        main_page.blit(maketext("adobegothicstdboldopentype",25,"The ultimate skill is ready if the player answers correctly 3 times in a row","black"),(210,575))
        main_page.blit(maketext("adobegothicstdboldopentype",25,"There is a chance that your attack will deal critical damage (2x damage)","black"),(210,630))
        main_page.blit(maketext("adobegothicstdboldopentype",25,"There is a chance that your opponent will dodge your attack","black"),(210,685))
        main_page.blit(maketext("adobegothicstdboldopentype",25,"If a player failed to give the correct answer, there is a chance that the player will hurt itself","black"),(210,740))
        main_page.blit(maketext("adobegothicstdboldopentype",25,"The game ends when a player has 0 health","black"),(210,795))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
            if event.type == MOUSEBUTTONDOWN:
                if page==1 and exitbtn.isOver(pos):
                    character_selection_menu()
                if page==2 and exitbtn.isOver(pos):
                    create_character_menu()
                if page==3 and exitbtn.isOver(pos):
                    use_existing_character_menu()
                if page==4 and exitbtn.isOver(pos):
                    map_choice_menu()
                if page==5 and exitbtn.isOver(pos):
                    difficulty_mode_menu()

            if event.type == MOUSEMOTION:
                if exitbtn.isOver(pos):
                    exitbtn.color = "green"
                else:
                    exitbtn.color = "azure3"
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    if page==1:
                        character_selection_menu()
                    if page==2:
                        create_character_menu()
                    if page==3:
                        use_existing_character_menu()
                    if page==4:
                        map_choice_menu()

        pygame.display.update()
    quit()

def loading_menu():
    run = True
    
    #background and characters
    if input_map == 1:
        main_page.blit(loadimage(r"MATH FIGHTER GUI\map1 background.jpg",(1600 ,900)),(0,0))
    if input_map == 2:
        main_page.blit(loadimage(r"MATH FIGHTER GUI\map2 background.jpg",(1600 ,900)),(0,0))
    if input_map == 3:
        main_page.blit(loadimage(r"MATH FIGHTER GUI\map3 background.jpg",(1600 ,900)),(0,0))
    if charplay[0].charapp == 1:
        main_page.blit(loadimage(r"MATH FIGHTER GUI\avatar loading screen\avatar loading screen png\character 1 left.png",(402,900)),(200,0))
    if charplay[1].charapp == 1:
        main_page.blit(loadimage(r"MATH FIGHTER GUI\avatar loading screen\avatar loading screen png\character 1 right.png",(402,900)),(1000,0))
    if charplay[0].charapp == 2:
        main_page.blit(loadimage(r"MATH FIGHTER GUI\avatar loading screen\avatar loading screen png\character 2 left.png",(473,900)),(170,0))
    if charplay[1].charapp == 2: 
        main_page.blit(loadimage(r"MATH FIGHTER GUI\avatar loading screen\avatar loading screen png\character 2 right.png",(473,900)),(970,0))
    if charplay[0].charapp == 3:
        main_page.blit(loadimage(r"MATH FIGHTER GUI\avatar loading screen\avatar loading screen png\character 3 left.png",(589,900)),(110,0))
    if charplay[1].charapp == 3: 
        main_page.blit(loadimage(r"MATH FIGHTER GUI\avatar loading screen\avatar loading screen png\character 3 right.png",(589,900)),(910,0))
    
    #name bar and vs
    main_page.blit(loadimage(r"MATH FIGHTER GUI\vs logo.png",(280,240)),(660,400))
    main_page.blit(loadimage(r"MATH FIGHTER GUI\name bar left.png",(599,123)),(0,750))
    main_page.blit(loadimage(r"MATH FIGHTER GUI\name bar right.png",(599,123)),(1001,750))
    
    #characters' name
    main_page.blit(maketext(None,75,charplay[0].charname,"black"),(180,790))
    main_page.blit(maketext(None,75,charplay[1].charname,"black"),(1260,790))

    #difficulty
    if difficulty == 1:
        #main_page.blit(maketext("adobegothicstdboldopentype",40,"EASY","black"),(750,20))
        maketextoutline(main_page,None,40,"Difficulty : Easy","white","black",700,20,2)

    if difficulty == 2:
        #main_page.blit(maketext("adobegothicstdboldopentype",40,"MEDIUM","black"),(750,20))
        maketextoutline(main_page,None,40,"Difficulty : Medium","white","black",680,20,2)

    if difficulty == 3:
        #main_page.blit(maketext("adobegothicstdboldopentype",40,"HARD","black"),(750,20))
        maketextoutline(main_page,None,40,"Difficulty : Hard","white","black",700,20,2)


    while run:
        main_page.blit(maketext(None,60,"Click to continue","Black"),(613,850))
        main_page.blit(maketext(None,60,"Click to continue","Black"),(617,850))
        main_page.blit(maketext(None,60,"Click to continue","Black"),(615,848))
        main_page.blit(maketext(None,60,"Click to continue","Black"),(615,852))
        main_page.blit(maketext(None,60,"Click to continue","White"),(615,850))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                game()
        pygame.display.update()
    quit()


def game():
    run = True
    global difficulty
    global timer
    timer = 5
    global H1
    H1=10
    global H2
    H2=10
    global playerturn
    playerturn = 1
    S1=0
    S2=0
    preattack = 0
    attack = 0

    game_start = False
    show_question = True
    answer = None
    show_answer = False
    char_hit1 = False
    char_hit2= False
    char_hit_miss1 = False
    char_hit_miss2 = False
    crit_effect1 = False
    crit_effect2 = False
    check_answer = False
    end_game = False
    incorrect1 = False
    incorrect2 = False
    late1 = False
    late2 = False

    input_answer = ""
    #input answer 1
    inputanswerfont = pygame.font.Font(None,150)
    input_answer1_rect=pygame.Rect(150,450,250,110)

    #input answer 2
    inputanswerfont = pygame.font.Font(None,150)
    input_answer2_rect=pygame.Rect(1210,450,250,110)

    #buttons
    skill1btn=button("azure3",145,625,250,75,charplay[0].charskill+" [S]")
    skill2btn=button("azure3",1210,625,250,75,charplay[1].charskill+" [S]")
    playagainbtn=button("azure3",650,500,300,150,"PLAY AGAIN")
    quitgamebtn=button("azure3",650,675,300,150,"QUIT")

    if S1>=3:
        ultimate1btn=button("azure3",145,725,250,75,charplay[0].charult+" [U]")
    else:
        ultimate1btn=button("red",145,725,250,75,charplay[0].charult+" [U]")
    if S2>=3:
        ultimate2btn=button("azure3",1210,725,250,75,charplay[1].charult+" [U]")
    else:
        ultimate2btn=button("red",1210,725,250,75,charplay[1].charult+" [U]")

    punchsound = mixer.Sound(r"MATH FIGHTER GUI\Punch - Gaming Sound Effect (HD).mp3")
    punchmiss_sound = mixer.Sound(r"MATH FIGHTER GUI\punch miss sound effect.mp3")
    
    while run:
        if incorrect1 == True or incorrect2 == True or late1 == True or late2 == True:
            pygame.time.delay(2500)
            if critrate == 1:
                punchsound.play()
            incorrect1 = False
            incorrect2 = False
            late1 = False
            late2 = False

        #background
        if input_map == 1:
            main_page.blit(loadimage(r"MATH FIGHTER GUI\map1 background.jpg",(1600 ,900)),(0,0))
        if input_map == 2:
            main_page.blit(loadimage(r"MATH FIGHTER GUI\map2 background.jpg",(1600 ,900)),(0,0))
        if input_map == 3:
            main_page.blit(loadimage(r"MATH FIGHTER GUI\map3 background.jpg",(1600 ,900)),(0,0))

        #healthbar
        main_page.blit(loadimage(r"MATH FIGHTER GUI\healthbar\left healthbar.png",(1600,900)),(0,0))
        main_page.blit(loadimage(r"MATH FIGHTER GUI\healthbar\right healthbar.png",(1600,900)),(0,0))
        main_page.blit(maketext("adobegothicstdboldopentype",30,charplay[0].charname,"azure2"),(250,155))
        main_page.blit(maketext("adobegothicstdboldopentype",30,charplay[1].charname,"azure2"),(1250,155))

        #health
        pygame.draw.rect(main_page,"red",pygame.Rect(190,89,54*H1,63),0)
        pygame.draw.rect(main_page,"red",pygame.Rect(870+(54*(10-H2)),89,54*H2,63),0)

        #health bar logo
        if charplay[0].charapp == 1:
            main_page.blit(loadimage(r"MATH FIGHTER GUI\healthbar\char 1 logo.png",(1600,900)),(0,0))
        if charplay[0].charapp == 2:
            main_page.blit(loadimage(r"MATH FIGHTER GUI\healthbar\char 2 logo.png",(1600,900)),(0,0))
        if charplay[0].charapp == 3:
            main_page.blit(loadimage(r"MATH FIGHTER GUI\healthbar\char 3 logo.png",(1600,900)),(0,0))
        if charplay[1].charapp == 1:
            main_page.blit(loadimage(r"MATH FIGHTER GUI\healthbar\char 1 logo.png",(1600,900)),(1325,0))
        if charplay[1].charapp == 2:
            main_page.blit(loadimage(r"MATH FIGHTER GUI\healthbar\char 2 logo.png",(1600,900)),(1325,0))
        if charplay[1].charapp == 3:
            main_page.blit(loadimage(r"MATH FIGHTER GUI\healthbar\char 3 logo.png",(1600,900)),(1325,0))

        #character standing
        if H1>0:
            if charplay[0].charapp == 1:
                main_page.blit(loadimage(r"MATH FIGHTER GUI\fight animation\char1 left 1.png",(1600,900)),(-110,0))
            if charplay[0].charapp == 2:
                main_page.blit(loadimage(r"MATH FIGHTER GUI\fight animation\char2 left 1.png",(1600,900)),(90,0))
            if charplay[0].charapp == 3:
                main_page.blit(loadimage(r"MATH FIGHTER GUI\fight animation\char3 left 1.png",(1600,900)),(-90,0))
        if H2>0:
            if charplay[1].charapp == 1:
                main_page.blit(loadimage(r"MATH FIGHTER GUI\fight animation\char1 right 1.png",(1600,900)),(100,0))
            if charplay[1].charapp == 2: 
                main_page.blit(loadimage(r"MATH FIGHTER GUI\fight animation\char2 right 1.png",(1600,900)),(-100,0))
            if charplay[1].charapp == 3: 
                main_page.blit(loadimage(r"MATH FIGHTER GUI\fight animation\char3 right 1.png",(1600,900)),(90,0))

        #character hit animation
        if char_hit1 == True:
            punchsound.play()
            pygame.time.delay(200)
            if charplay[0].charapp == 1:
                main_page.blit(loadimage(r"MATH FIGHTER GUI\fight animation\hit animation transparent\char1 left 2.png",(1600,900)),(-50,0))
            if charplay[0].charapp == 2:
                main_page.blit(loadimage(r"MATH FIGHTER GUI\fight animation\hit animation transparent\char2 left 2.png",(1600,900)),(100,0))
            if charplay[0].charapp == 3:
                main_page.blit(loadimage(r"MATH FIGHTER GUI\fight animation\hit animation transparent\char3 left 2.png",(1600,900)),(-100,0))
            char_hit1 = False

        if char_hit2 == True:
            punchsound.play()
            pygame.time.delay(200)
            if charplay[1].charapp == 1:
                main_page.blit(loadimage(r"MATH FIGHTER GUI\fight animation\hit animation transparent\char1 right 2.png",(1600,900)),(25,0))
            if charplay[1].charapp == 2:
                main_page.blit(loadimage(r"MATH FIGHTER GUI\fight animation\hit animation transparent\char2 right 2.png",(1600,900)),(-125,0))
            if charplay[1].charapp == 3:
                main_page.blit(loadimage(r"MATH FIGHTER GUI\fight animation\hit animation transparent\char3 right 2.png",(1600,900)),(75,0))
            char_hit2 = False

        #character hit miss animation
        if char_hit_miss1 == True:
            punchmiss_sound.play()
            pygame.time.delay(200)
            if charplay[0].charapp == 1:
                main_page.blit(loadimage(r"MATH FIGHTER GUI\fight animation\hit animation transparent\char1 left 2.png",(1200,900)),(100,0))
            if charplay[0].charapp == 2:
                main_page.blit(loadimage(r"MATH FIGHTER GUI\fight animation\hit animation transparent\char2 left 2.png",(1200,900)),(225,0))
            if charplay[0].charapp == 3:
                main_page.blit(loadimage(r"MATH FIGHTER GUI\fight animation\hit animation transparent\char3 left 2.png",(1200,900)),(50,0))
            char_hit_miss1 = False

        if char_hit_miss2 == True:
            punchmiss_sound.play()
            pygame.time.delay(200)
            if charplay[1].charapp == 1:
                main_page.blit(loadimage(r"MATH FIGHTER GUI\fight animation\hit animation transparent\char1 right 2.png",(1200,900)),(300,0))
            if charplay[1].charapp == 2:
                main_page.blit(loadimage(r"MATH FIGHTER GUI\fight animation\hit animation transparent\char2 right 2.png",(1200,900)),(175,0))
            if charplay[1].charapp == 3:
                main_page.blit(loadimage(r"MATH FIGHTER GUI\fight animation\hit animation transparent\char3 right 2.png",(1200,900)),(325,0))
            char_hit_miss2 = False

        #character crit hit effect
        if crit_effect1 == True:
            main_page.blit(loadimage(r"MATH FIGHTER GUI\crit effect left.png",(1600,900)),(50,0))
            crit_effect1 = False

        if crit_effect2 == True:
            main_page.blit(loadimage(r"MATH FIGHTER GUI\crit effect right.png",(1600,900)),(-50,0))
            crit_effect2 = False

        main_page.blit(loadimage(r"MATH FIGHTER GUI\char menu\char menu 1.png",(1600,900)),(0,0))
        main_page.blit(loadimage(r"MATH FIGHTER GUI\char menu\char menu 2.png",(1600,900)),(0,0))

        if playerturn == 1 and game_start == False:
            main_page.blit(maketext(None,75,"Press","black"),(190,400))
            main_page.blit(maketext(None,75,"[SPACE]","black"),(160,475))
            main_page.blit(maketext(None,75,"to start","black"),(170,550))
        if playerturn == 2 and game_start == False:
            main_page.blit(maketext(None,75,"Press","black"),(1260,400))
            main_page.blit(maketext(None,75,"[SPACE]","black"),(1230,475))
            main_page.blit(maketext(None,75,"to start","black"),(1240,550))

        main_page.blit(loadimage(r"MATH FIGHTER GUI\circle timer.png",(1600,900)),(0,0))

        #no answer result
        if timer <=0 and answer == None:
            game_start = False
            if playerturn == 1:
                S1=0
                if critrate == 1:
                    H1-=1
                    print("selfhit")
                else:
                    H1=H1
                main_page.blit(maketext(None,100,"Too late","black"),(135,400))
                late1 = True
                playerturn = 2
                timer = 5
            else:
                S2=0
                if critrate == 1:
                    H2-=1
                    print("selfhit")
                else:
                    H2=H2
                main_page.blit(maketext(None,100,"Too late","black"),(1200,400))
                late2 = True
                playerturn = 1
                timer = 5

        if H1<=0:
            if charplay[0].charapp == 1:
                main_page.blit(loadimage(r"MATH FIGHTER GUI\end game animation\char1 left fall.png",(1600,900)),(0,0))
            if charplay[0].charapp == 2:
                main_page.blit(loadimage(r"MATH FIGHTER GUI\end game animation\char2 left fall.png",(1600,900)),(0,0))
            if charplay[0].charapp == 3:
                main_page.blit(loadimage(r"MATH FIGHTER GUI\end game animation\char3 left fall.png",(1600,900)),(0,0))
            
            maketextoutline(main_page,"adobegothicstdboldopentype",random.randint(50,100),(charplay[1].charname+" won!!").upper(),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),"white",random.randint(50,1400),random.randint(100,800),2)
            maketextoutline(main_page,"adobegothicstdboldopentype",random.randint(50,100),(charplay[1].charname+" won!!").upper(),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),"white",random.randint(50,1400),random.randint(100,800),2)
            maketextoutline(main_page,"adobegothicstdboldopentype",random.randint(50,100),(charplay[1].charname+" won!!").upper(),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),"white",random.randint(50,1400),random.randint(100,800),2)
            end_game = True

        if H2<=0:
            if charplay[1].charapp == 1:
                main_page.blit(loadimage(r"MATH FIGHTER GUI\end game animation\char1 right fall.png",(1600,900)),(0,0))
            if charplay[1].charapp == 2:
                main_page.blit(loadimage(r"MATH FIGHTER GUI\end game animation\char2 right fall.png",(1600,900)),(0,0))
            if charplay[1].charapp == 3:
                main_page.blit(loadimage(r"MATH FIGHTER GUI\end game animation\char3 right fall.png",(1600,900)),(0,0))
            
            maketextoutline(main_page,"adobegothicstdboldopentype",random.randint(50,100),(charplay[0].charname+" won!!").upper(),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),"white",random.randint(50,1200),random.randint(100,800),2)
            maketextoutline(main_page,"adobegothicstdboldopentype",random.randint(50,100),(charplay[0].charname+" won!!").upper(),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),"white",random.randint(50,1200),random.randint(100,800),2)
            maketextoutline(main_page,"adobegothicstdboldopentype",random.randint(50,100),(charplay[0].charname+" won!!").upper(),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),"white",random.randint(50,1200),random.randint(100,800),2)
            end_game = True


        if end_game == True:
            playagainbtn.draw(main_page,2)
            quitgamebtn.draw(main_page,2)

        if game_start == True:
            if show_question == True:
                main_page.blit(maketext("adobegothicstdboldopentype",100,str(timer),"black"),(773,70))

            if symbols == 1:
                if show_question == True:
                    if playerturn == 1:
                        main_page.blit(maketext(None,115,str(num1)+" + "+str(num2),"Black"),(130,340))
                        pygame.draw.rect(main_page,"white",input_answer1_rect,0)
                        input_name_surface = inputanswerfont.render(input_answer,True,(0,0,0))
                        main_page.blit(input_name_surface,((input_answer1_rect.x+30,input_answer1_rect.y+10)))
                
                    elif playerturn == 2:
                        main_page.blit(maketext(None,115,str(num1)+" + "+str(num2),"Black"),(1200,340))
                        pygame.draw.rect(main_page,"white",input_answer2_rect,0)
                        input_name_surface = inputanswerfont.render(input_answer,True,(0,0,0))
                        main_page.blit(input_name_surface,((input_answer2_rect.x+30,input_answer2_rect.y+10)))

                if check_answer == True:
                    if str(answer) == str(num1+num2):
                        if playerturn == 1:
                            skill1btn.draw2(main_page,2)
                            ultimate1btn.draw2(main_page,2)
                        else:
                            skill2btn.draw2(main_page,2)
                            ultimate2btn.draw2(main_page,2)
                        H1,H2,S1,S2,playerturn,game_start,attack,char_hit1,char_hit2,char_hit_miss1,char_hit_miss2,crit_effect1,crit_effect2 = check_answer_correct(playerturn,show_answer,attack,H1,H2,S1,S2,game_start,critrate,char_hit1,char_hit2,char_hit_miss1,char_hit_miss2,crit_effect1,crit_effect2)

                    elif str(answer) != str(num1+num2):
                        playerturn,H1,H2,S1,S2,game_start,incorrect1,incorrect2 = check_answer_wrong(playerturn,show_answer,game_start,H1,H2,S1,S2,critrate,incorrect1,incorrect2)

            elif symbols == 2:
                if show_question == True:
                    if playerturn == 1:
                        main_page.blit(maketext(None,115,str(num1)+" - "+str(num2),"Black"),(130,340))
                        pygame.draw.rect(main_page,"white",input_answer1_rect,0)
                        input_name_surface = inputanswerfont.render(input_answer,True,(0,0,0))
                        main_page.blit(input_name_surface,((input_answer1_rect.x+30,input_answer1_rect.y+10)))
                
                    elif playerturn == 2:
                        main_page.blit(maketext(None,115,str(num1)+" - "+str(num2),"Black"),(1200,340))
                        pygame.draw.rect(main_page,"white",input_answer2_rect,0)
                        input_name_surface = inputanswerfont.render(input_answer,True,(0,0,0))
                        main_page.blit(input_name_surface,((input_answer2_rect.x+30,input_answer2_rect.y+10)))

                if check_answer == True:
                    if str(answer) == str(num1-num2):
                        if playerturn == 1:
                            skill1btn.draw2(main_page,2)
                            ultimate1btn.draw2(main_page,2)
                        else:
                            skill2btn.draw2(main_page,2)
                            ultimate2btn.draw2(main_page,2)
                        H1,H2,S1,S2,playerturn,game_start,attack,char_hit1,char_hit2,char_hit_miss1,char_hit_miss2,crit_effect1,crit_effect2 = check_answer_correct(playerturn,show_answer,attack,H1,H2,S1,S2,game_start,critrate,char_hit1,char_hit2,char_hit_miss1,char_hit_miss2,crit_effect1,crit_effect2)

                    elif str(answer) != str(num1-num2):
                        playerturn,H1,H2,S1,S2,game_start,incorrect1,incorrect2 = check_answer_wrong(playerturn,show_answer,game_start,H1,H2,S1,S2,critrate,incorrect1,incorrect2)

            elif symbols == 3 or symbols == 4 or symbols == 5:
                if show_question == True:
                    if playerturn == 1:
                        main_page.blit(maketext(None,115,str(num1)+" x "+str(num2),"Black"),(130,340))
                        pygame.draw.rect(main_page,"white",input_answer1_rect,0)
                        input_name_surface = inputanswerfont.render(input_answer,True,(0,0,0))
                        main_page.blit(input_name_surface,((input_answer1_rect.x+30,input_answer1_rect.y+10)))
                
                    elif playerturn == 2:
                        main_page.blit(maketext(None,115,str(num1)+" x "+str(num2),"Black"),(1200,340))
                        pygame.draw.rect(main_page,"white",input_answer2_rect,0)
                        input_name_surface = inputanswerfont.render(input_answer,True,(0,0,0))
                        main_page.blit(input_name_surface,((input_answer2_rect.x+30,input_answer2_rect.y+10)))

                if check_answer == True:
                    if str(answer) == str(num1*num2):
                        if playerturn == 1:
                            skill1btn.draw2(main_page,2)
                            ultimate1btn.draw2(main_page,2)
                        else:
                            skill2btn.draw2(main_page,2)
                            ultimate2btn.draw2(main_page,2)
                        H1,H2,S1,S2,playerturn,game_start,attack,char_hit1,char_hit2,char_hit_miss1,char_hit_miss2,crit_effect1,crit_effect2 = check_answer_correct(playerturn,show_answer,attack,H1,H2,S1,S2,game_start,critrate,char_hit1,char_hit2,char_hit_miss1,char_hit_miss2,crit_effect1,crit_effect2)

                    elif str(answer) != str(num1*num2):
                        playerturn,H1,H2,S1,S2,game_start,incorrect1,incorrect2 = check_answer_wrong(playerturn,show_answer,game_start,H1,H2,S1,S2,critrate,incorrect1,incorrect2)

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
            if event.type == MOUSEBUTTONDOWN:
                if end_game == True:
                    if playagainbtn.isOver(pos):
                        global player
                        player = 1
                        intro_menu()

                    if quitgamebtn.isOver(pos):
                        run = False

            if event.type == MOUSEMOTION:
                if playagainbtn.isOver(pos):
                    playagainbtn.color = "green"
                else:
                    playagainbtn.color = "azure3"
                
                if quitgamebtn.isOver(pos): 
                    quitgamebtn.color = "green"
                else:
                    quitgamebtn.color = "azure3"

            if event.type == KEYDOWN:
                if event.key == K_SPACE and game_start == False and end_game == False:
                    game_start = True
                    show_question = True
                    check_answer = False
                    show_answer = False
                    preattack = 0
                    attack = 0
                    input_answer = ""
                    answer = None
                    if difficulty == 1:
                        symbols = random.randint(1,2)
                        num1 = random.randint(5,30)
                        num2 = random.randint(5,30)
                    if difficulty == 2:
                        symbols = random.randint(1,5)
                        if symbols == 1 or symbols == 2:
                            num1 = random.randint(20,99)
                            num2 = random.randint(20,99)
                        else:
                            num1=random.randint(2,20)
                            num2=random.randint(2,20)
                    if difficulty == 3:
                        symbols = random.randint(3,5)
                        num1 = random.randint(16,31)
                        num2= random.randint(16,31)
                    
                    critrate = random.randint(1,5)
                    countdown_thread=threading.Thread(target = countdown)
                    countdown_thread.start()
                
                if end_game == True:
                    if event.key == K_BACKSPACE:
                        pass
                if game_start == True:
                    if show_question == True:
                        if event.key == K_BACKSPACE:
                            input_answer = input_answer[:-1]
                        elif event.key == K_TAB or event.key == K_ESCAPE:
                            pass
                        elif event.key == K_RETURN:
                            show_question = False
                            show_answer = True
                            check_answer = True
                            answer = input_answer

                        elif event.key == K_SPACE:
                            pass
                        else:
                            if len(input_answer)<=2:
                                input_answer += event.unicode
                            else:
                                pass
                    if show_answer == True:
                        if event.key == K_s:
                            if playerturn == 1:
                                if S1>=2:
                                    skill1btn.color = "green"
                                    ultimate1btn.color = "azure3"
                                    preattack = 1
                                else:
                                    skill1btn.color = "green"
                                    ultimate1btn.color = "red"
                                    preattack = 1
                            if playerturn == 2:
                                if S2>=2:
                                    skill2btn.color = "green"
                                    ultimate2btn.color = "azure3"
                                    preattack = 1
                                else:
                                    skill2btn.color = "green"
                                    ultimate2btn.color = "red"
                                    preattack = 1

                        elif event.key == K_u:
                            if playerturn == 1:
                                if S1>=2:
                                    skill1btn.color = "azure3"
                                    ultimate1btn.color = "green"
                                    preattack = 2
                                else:
                                    skill1btn.color = "azure3"
                                    ultimate1btn.color = "red"
                                    preattack = 0
                            if playerturn == 2:
                                if S2>=2:
                                    skill2btn.color = "azure3"
                                    ultimate2btn.color = "green"
                                    preattack = 2
                                else:
                                    skill2btn.color = "azure3"
                                    ultimate2btn.color = "red"
                                    preattack = 0
                        
                        elif event.key == K_RETURN and preattack == 1:
                            attack = 1
                        elif event.key == K_RETURN and preattack == 2:
                            attack = 2
                        
                        else:
                            skill1btn.color = "azure3"
                            if S1>=2:
                                ultimate1btn.color = "azure3"
                            else:
                                ultimate1btn.color = "red"
                            skill2btn.color = "azure3"
                            if S2>=2:
                                ultimate2btn.color = "azure3"
                            else:
                                ultimate2btn.color = "red"
                            preattack = 0

        pygame.display.update()
    quit()


intro_menu()