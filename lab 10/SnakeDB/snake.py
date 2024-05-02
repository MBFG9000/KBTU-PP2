import pygame

pygame.init()

WIDTH = 1000
HEIGHT = 700
FPS = 60
Running = True

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    
    
    
    
    clock.tick(FPS)

