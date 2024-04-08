import pygame as pg
import pygame
from datetime import datetime

pygame.init()

WIDTH = 700
HEIGHT = 525

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")
clock = pygame.time.Clock()
FPS = 1
running = True 
background_image = pygame.image.load("Lab 7/Mickey Clock/mainclock.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

timetoangleminsec = dict(zip(range(0,60),range(0,360,6)))


last_time = datetime.now()
angleofsec = timetoangleminsec[datetime.today().time().second]
angleofminutes = timetoangleminsec[datetime.today().time().minute]



class Left_hand(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Lab 7/Mickey Clock/leftarm.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (31.5,HEIGHT))
        self.rect = self.image.get_rect(center = (WIDTH/2 + 4, HEIGHT/2))
        
    def update(self, angle):
        rotated_image = pygame.transform.rotate(self.image, angle)
        self.rect = rotated_image.get_rect(center=self.rect.center)
        return rotated_image

class Right_hand(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Lab 7/Mickey Clock/rightarm.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (WIDTH,HEIGHT))
        self.rect = self.image.get_rect(center = (WIDTH/2,HEIGHT/2))
    def update(self, angle):
        rotated_image = pygame.transform.rotate(self.image, angle)
        self.rect = rotated_image.get_rect(center=self.rect.center)
        return rotated_image



left_hand = Left_hand()
right_hand = Right_hand()

angle = 0


while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    angle +=1
    screen.blit(background_image, (0, 0))
    angleofsec = timetoangleminsec[datetime.today().time().second]
    angleofminutes = timetoangleminsec[datetime.today().time().minute]
    screen.blit(right_hand.update(-angleofminutes-60), right_hand.rect)
    screen.blit(left_hand.update(-angleofsec+1),left_hand.rect)
    pygame.display.flip()
pygame.quit()
