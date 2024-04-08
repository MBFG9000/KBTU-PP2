from typing import Any
import pygame
pygame.init()

WIDTH = 500
HEIGHT = 500

Screen = pygame.display.set_mode((WIDTH, HEIGHT))
Clock = pygame.time.Clock() 
FPS = 60
Running = True

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pass
    def update(self,surface,coordinates = (WIDTH/2, HEIGHT/2)):
        pygame.draw.circle(surface, "red", coordinates, 25)
        
ball = Ball()
coordinates = pygame.Vector2(WIDTH/2, HEIGHT/2)

while Running:
    Clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and (coordinates[1] > 10) :
                coordinates[1] = coordinates[1] - 20
                #print(coordinates)
            if event.key == pygame.K_DOWN and (coordinates[1] < HEIGHT-10):
                
                coordinates[1] = coordinates[1] + 20
                #print(coordinates)
            if event.key == pygame.K_LEFT and (coordinates[0] > 10):
                coordinates[0] = coordinates[0] - 20
                #print(coordinates)
            if event.key == pygame.K_RIGHT and (coordinates[0] < WIDTH-10):
                coordinates[0] = coordinates[0] + 20
                #print(coordinates)
    
    Screen.fill((255,255,255))
    ball.update(Screen, coordinates)
    pygame.display.flip()
