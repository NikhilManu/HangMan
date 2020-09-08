import pygame
import math

#setup display
pygame.init()
WIDTH,HEIGHT=800,500
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("HangMan 1.0")

#Font
LETTER_FONT = pygame.font.SysFont('comicsans',40)
WORD_FONT = pygame.font.SysFont('comicsans',60)
TITLE_FONT = pygame.font.SysFont('comicsans',70)



#Load images
images=[]
for i in range(7):
    image=pygame.image.load("hangman{}.png".format(i))
    images.append(image)

#button variables
RADIUS=20
GAP=15
letters=[]
startx=round((WIDTH - (RADIUS * 2 + GAP) * 12 - 2* RADIUS) / 2)
starty=400 
A=65
for i in range(26):
    x= startx + RADIUS + ((RADIUS * 2 + GAP) * (i % 13))
    y=starty + ((i//13) * (GAP + RADIUS*2))
    letters.append([x,y,chr(A+i),True])



#game Variables
hangman_status=0
WORD="HAPPY"
guessed=[]

#colours
WHITE=(255,255,255)
BLACK=(0,0,0)

#function for Drawing
def draw():
    win.fill(WHITE)
    #title of the Game 
    text=TITLE_FONT.render("HANGMAN",1,BLACK)
    win.blit(text,(WIDTH/2 - text.get_width()/2,20))

    #draw word
    display_word=''
    for letter in WORD:
        if letter in guessed:
            display_word+=letter+' '
        else:
            display_word+="_ "

    text=WORD_FONT.render(display_word,1,BLACK)
    win.blit(text,(400,200))


    #draw Buttons
    for ltr in letters:
        x,y,letter,visible=ltr
        if visible:
            pygame.draw.circle(win,BLACK,(x,y),RADIUS,3)
            text=LETTER_FONT.render(letter,1,BLACK)
            win.blit(text,(x - text.get_width()/2,y - text.get_height()/2))



    win.blit(images[hangman_status],(150,100))
    pygame.display.update()


#display won or lost
def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text=WORD_FONT.render(message,1,BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2,HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)


#Game Loop 
FPS=60
clock=pygame.time.Clock()
run = True

while run:
    clock.tick(FPS)


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False
        if event.type==pygame.MOUSEBUTTONDOWN:
            mx,my=pygame.mouse.get_pos()
            for ltr in letters:
                x,y,letter,visible=ltr
                if visible:
                    dis = math.sqrt((x - mx)**2 + (y - my)**2)
                    if dis<RADIUS:
                        ltr[3]=False
                        guessed.append(letter)
                        if letter not in WORD:
                            hangman_status+=1

    draw()

    won=True
    for letter in WORD:
        if letter  not in guessed:
            won=False
            break
    
    if won:
        display_message("YOU WON")
        break
        

    if hangman_status==6:
        display_message("YOU LOST")
        break

        


pygame.quit()



