import pygame
import os
import math

pygame.init()
W,H = 1000 ,500
c = pygame.display.set_mode((W,H))
pygame.display.set_caption("HANGMAN ASRTO QUIZ! :)")

#color
white= (255,255,255)
black = (0,0,0)
blue= (0,80,200)
grey=(128,128,128)









#button 
RADIUS= 20
gap  = 15
letters=[]
startx = round(W - (RADIUS * 2+ gap)*13) 
starty = 400
A = 65 

for i in range(26):
    x = startx + gap*2 +((RADIUS*2 + gap)* (i%13))
    y = starty + ((i//13)*(gap + RADIUS*2))
    letters.append([x,y,chr(A+i),True])
 # font
font = pygame.font.SysFont('comicsans',20 )
font1 = pygame.font.SysFont('comicsans',40)


#image section
image=[]
for i in range(7):
    images = pygame.image.load("hangman" + str(i) + ".png")
    image.append(images)

# variables
hangman_status = 0
words = {"WHAT IS THE NAME OF OUR PLANET": "EATRH"}
e= words.keys()

guessed=[]

for j in e:
    print(j)
#main game loop 
FPS = 60
clock = pygame.time.Clock()
a  = True

def draw():
    c.fill(grey)
    t2=font.render(j,1,black)
    c.blit(t2,(W/4+t2.get_width()/2,H/4 +t2.get_height()/2))
    # time to show words
    display_word =""
    for letter in words[str(j)]:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word+= "_ "
    text = font1.render(display_word,1,white)
    c.blit(text,(400,200))
    
    # draw button
    for letter in letters:
        x,y,ltr,visible= letter
        if visible:
            pygame.draw.circle(c,black,(x,y),RADIUS,3)
            text = font.render(ltr,1,black)
            c.blit(text,(x - text.get_width()/2,y - text.get_height()/2))

    c.blit(image[hangman_status],(50,50))
    pygame.display.update()
  
while a:
    clock.tick(FPS)
    draw()
      
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            a = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x,m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y,ltr ,visible= letter
                if visible:
                    dis = math.sqrt((x-m_x)**2+ (y-m_y)**2)          
                    if dis < RADIUS:
                        letter[3]=False
                        guessed.append(ltr)
                        if ltr not in words[str(j)]:
                            hangman_status +=1
    
    won= True
    for letter in words[str(j)]:
        if letter not in guessed:
            won = False
            break
    print(letter)
    if won :
        c.fill(blue)
        text1 = font1.render("NEXT QUESTION PLEASE :) ",1,black)
        c.blit(text1, (W/2 -text1.get_width()/2, H/2 -text1.get_height()/2))
        pygame.display.update()
        pygame.time.delay(3000)
        break

    if hangman_status == 6:
        c.fill(blue)
        text1 = font1.render("BETTER LUCK NEXT TIME :(",1,black)
        c.blit(text1, (W/2 -text1.get_width()/2, H/2 -text1.get_height()/2))
        pygame.display.update()
        pygame.time.delay(3000)
        break

pygame.quit()

#second section
 
pygame.init()
W,H = 1000 ,500
c = pygame.display.set_mode((W,H))
pygame.display.set_caption("HANGMAN ASRTO QUIZ! :)")
#button 
RADIUS= 20
gap  = 15
letters=[]
startx = round(W - (RADIUS * 2+ gap)*13) 
starty = 400
A = 65 

for i in range(26):
    x = startx + gap*2 +((RADIUS*2 + gap)* (i%13))
    y = starty + ((i//13)*(gap + RADIUS*2))
    letters.append([x,y,chr(A+i),True])
 # font
font = pygame.font.SysFont('comicsans',20 )
font1 = pygame.font.SysFont('comicsans',40)
#color
white= (255,255,255)
black = (0,0,0)
blue= (0,80,200)
grey=(128,128,128)

#image section
image=[]
for i in range(7):
    images = pygame.image.load("hangman" + str(i) + ".png")
    image.append(images)

# variables
hangman_status = 0
words = {"HOW MANY MOONS EARTH HAVE": "ONE"}
e= words.keys()

guessed=[]

for j in e:
    c.fill(grey)
    t1= font.render(j,1,black)
    c.blit(t1,(W/2-t1.get_width()/2,H/2 -t1.get_height()/2))
    pygame.display.update()
    pygame.time.delay(6000)
#main game loop 
FPS = 60
clock = pygame.time.Clock()
a  = True

def draw():
    c.fill(grey)
    # time to show words
    display_word =""
    for letter in words[str(j)]:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word+= "_ "
    text = font1.render(display_word,1,white)
    c.blit(text,(400,200))
    
    # draw button
    for letter in letters:
        x,y,ltr,visible= letter
        if visible:
            pygame.draw.circle(c,black,(x,y),RADIUS,3)
            text = font.render(ltr,1,black)
            c.blit(text,(x - text.get_width()/2,y - text.get_height()/2))

    c.blit(image[hangman_status],(50,50))
    pygame.display.update()
     
while a:
    clock.tick(FPS)
    draw() 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            a = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x,m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y,ltr ,visible= letter
                if visible:
                    dis = math.sqrt((x-m_x)**2+ (y-m_y)**2)          
                    if dis < RADIUS:
                        letter[3]=False
                        guessed.append(ltr)
                        if ltr not in words[str(j)]:
                            hangman_status +=1
    
    won= True
    for letter in words[str(j)]:
        if letter not in guessed:
            won = False
            break
    print(letter)
    if won :
        c.fill(blue)
        text1 = font1.render("NEXT AGAIN :)",1,black)
        c.blit(text1, (W/2 -text1.get_width()/2, H/2 -text1.get_height()/2))
        pygame.display.update()
        pygame.time.delay(3000)
        break

    if hangman_status == 6:
        c.fill(blue)
        text1 = font1.render("BETTER LUCK NEXT TIME :(",1,black)
        c.blit(text1, (W/2 -text1.get_width()/2, H/2 -text1.get_height()/2))
        pygame.display.update()
        pygame.time.delay(3000)
        break

pygame.quit()

# THIRD section

pygame.init()
W,H = 1000 ,500
c = pygame.display.set_mode((W,H))
pygame.display.set_caption("HANGMAN ASRTO QUIZ! :)")
#button 
RADIUS= 20
gap  = 15
letters=[]
startx = round(W - (RADIUS * 2+ gap)*13) 
starty = 400
A = 65 

for i in range(26):
    x = startx + gap*2 +((RADIUS*2 + gap)* (i%13))
    y = starty + ((i//13)*(gap + RADIUS*2))
    letters.append([x,y,chr(A+i),True])
 # font
font = pygame.font.SysFont('comicsans',20 )
font1 = pygame.font.SysFont('comicsans',40)
#color
white= (255,255,255)
black = (0,0,0)
blue= (0,80,200)
grey=(128,128,128)

#image section
image=[]
for i in range(7):
    images = pygame.image.load("hangman" + str(i) + ".png")
    image.append(images)

# variables
hangman_status = 0
words = {"HOW MANY LAGRANGE POINT ARE THERE BETWEEN EARTH AND SUN": "FIVE"}
e= words.keys()

guessed=[]

for j in e:
    c.fill(grey)
    t1= font.render(j,1,black)
    c.blit(t1,(W/2-t1.get_width()/2,H/2 -t1.get_height()/2))
    pygame.display.update()
    pygame.time.delay(6000)
#main game loop 
FPS = 60
clock = pygame.time.Clock()
a  = True

def draw():
    c.fill(grey)
    # time to show words
    display_word =""
    for letter in words[str(j)]:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word+= "_ "
    text = font1.render(display_word,1,white)
    c.blit(text,(400,200))
    
    # draw button
    for letter in letters:
        x,y,ltr,visible= letter
        if visible:
            pygame.draw.circle(c,black,(x,y),RADIUS,3)
            text = font.render(ltr,1,black)
            c.blit(text,(x - text.get_width()/2,y - text.get_height()/2))

    c.blit(image[hangman_status],(50,50))
    pygame.display.update()
         
while a:
    clock.tick(FPS)
    draw()
      
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            a = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x,m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y,ltr ,visible= letter
                if visible:
                    dis = math.sqrt((x-m_x)**2+ (y-m_y)**2)          
                    if dis < RADIUS:
                        letter[3]=False
                        guessed.append(ltr)
                        if ltr not in words[str(j)]:
                            hangman_status +=1
    
    won= True
    for letter in words[str(j)]:
        if letter not in guessed:
            won = False
            break
    print(letter)
    if won :
        c.fill(blue)
        text1 = font1.render("YOU ARE FABULOUS :)",1,black)
        c.blit(text1, (W/2 -text1.get_width()/2, H/2 -text1.get_height()/2))
        pygame.display.update()
        pygame.time.delay(3000)
        break

    if hangman_status == 6:
        c.fill(blue)
        text1 = font1.render("BETTER LUCK NEXT TIME :(",1,black)
        c.blit(text1, (W/2 -text1.get_width()/2, H/2 -text1.get_height()/2))
        pygame.display.update()
        pygame.time.delay(3000)
        break

pygame.quit()

# fouth section

pygame.init()
W,H = 1000 ,500
c = pygame.display.set_mode((W,H))
pygame.display.set_caption("HANGMAN ASRTO QUIZ! :)")
#button 
RADIUS= 20
gap  = 15
letters=[]
startx = round(W - (RADIUS * 2+ gap)*13) 
starty = 400
A = 65 

for i in range(26):
    x = startx + gap*2 +((RADIUS*2 + gap)* (i%13))
    y = starty + ((i//13)*(gap + RADIUS*2))
    letters.append([x,y,chr(A+i),True])
 # font
font = pygame.font.SysFont('comicsans',20)
font1 = pygame.font.SysFont('comicsans',40)
#color
white= (255,255,255)
black = (0,0,0)
blue= (0,80,200)
grey=(128,128,128)

#image section
image=[]
for i in range(7):
    images = pygame.image.load("hangman" + str(i) + ".png")
    image.append(images)

# variables
hangman_status = 0
words = {"RECENTLY OUR ISRO'S SUN OBSERVERVATION SATELLITE ADTIYA SET UP TO WHICH POINT": "LAGRANGEONE"}
e= words.keys()

guessed=[]

for j in e:
    c.fill(grey)
    t1= font.render(j,1,black)
    c.blit(t1,(W/2-t1.get_width()/2,H/2 -t1.get_height()/2))
    pygame.display.update()
    pygame.time.delay(6000)
#main game loop 
FPS = 60
clock = pygame.time.Clock()
a  = True

def draw():
    c.fill(grey)
    # time to show words
    display_word =""
    for letter in words[str(j)]:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word+= "_ "
    text = font1.render(display_word,1,white)
    c.blit(text,(400,200))
    
    # draw button
    for letter in letters:
        x,y,ltr,visible= letter
        if visible:
            pygame.draw.circle(c,black,(x,y),RADIUS,3)
            text = font.render(ltr,1,black)
            c.blit(text,(x - text.get_width()/2,y - text.get_height()/2))

    c.blit(image[hangman_status],(50,50))
    pygame.display.update()
     
while a:
    clock.tick(FPS)
    draw()
      
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            a = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x,m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y,ltr ,visible= letter
                if visible:
                    dis = math.sqrt((x-m_x)**2+ (y-m_y)**2)          
                    if dis < RADIUS:
                        letter[3]=False
                        guessed.append(ltr)
                        if ltr not in words[str(j)]:
                            hangman_status +=1
    
    won= True
    for letter in words[str(j)]:
        if letter not in guessed:
            won = False
            break
    print(letter)
    if won :
        c.fill(blue)
        text1 = font1.render(" BOOYAH YOU WON!! ",1,black)
        c.blit(text1, (W/2 -text1.get_width()/2, H/2 -text1.get_height()/2))
        pygame.display.update()
        pygame.time.delay(3000)
        break

    if hangman_status == 6:
        c.fill(blue)
        text1 = font1.render("BETTER LUCK NEXT TIME :(",1,black)
        c.blit(text1, (W/2 -text1.get_width()/2, H/2 -text1.get_height()/2))
        pygame.display.update()
        pygame.time.delay(3000)
        break

pygame.quit()