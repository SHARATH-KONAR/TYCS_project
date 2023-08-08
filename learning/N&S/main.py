import pygame 

pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("War_Of_Hidden_Leaf")

walk_right = [pygame.image.load('pics\\NR2.png'),pygame.image.load('pics\\NR3.png'),pygame.image.load('pics\\NR1.png')]
walk_left =  [pygame.image.load('pics\\NL2.png'),pygame.image.load('pics\\NL3.png'),pygame.image.load('pics\\NL1.png')]

b_g= pygame.image.load('pics\\bg.png')
stand = pygame.image.load('pics\\Nstanding.png')

x = 50 
y = 400
width = 40 
height = 60
speed = 10
is_jump=False 

jump_height= 10

run = True

def redraw_win():
    win.blit(bg,(0,0,0))
while run :
    
    pygame.time.delay(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False
 
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= speed 
    if keys[pygame.K_RIGHT]and x < 500-width :
        x += speed 
    
    if is_jump == False:
        if keys[pygame.K_SPACE]:
            is_jump = True

    else:
        if jump_height >= -10:
            neg = 1

            if jump_height <0:
                neg = -1  
            y -= (jump_height **2)*0.5*neg
            jump_height -= 1

        else:
            is_jump = False
            jump_height = 10

    win.fill((0,0,0))
    pygame.draw.rect(win,(250,250,250),(x,y,width,height))
    pygame.display.update()

pygame.quit()