import pygame
pygame.init()
screen = pygame.display.set_mode((576,1024))
isRunning=True
bg_surface = pygame.image.load ('assets/background-day.png')
x=5
y=5
clock=pygame.time.Clock()
#screen.blit(bg_surface,(100,100))
#pygame.display.update()
while isRunning:
    clock.tick(60)
    screen.fill((0,0,0))
    x=x+10
    y=y+10
    screen.blit(bg_surface,(x,y))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x:
                isRunning=False
pygame.quit()
