import pygame
import sys
from pygame.locals import *
from random import randint
import time
pygame.init()
#инициализация пайгейма
FPS = 60
WIDTH = 600
HEIGHT = 650
speed = 5
SCORE = 0
#основные настройки

Screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Vip Kazakh Simulator")
Clock = pygame.time.Clock()
Running = True 

#ubuntumono is font
font = pygame.font.SysFont("ubuntumono", 60)
font_small = pygame.font.SysFont("ubuntumono", 20)
game_over = font.render("GAME OVER", True, (255, 255, 255)) #text, antialising, color

#print(pygame.font.get_fonts())
class Enemy (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Lab 8/RacerGame/sprites/enemy.png").convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 0.28)
        self.rect = self.image.get_rect()
        self.rect.center = (randint(48,WIDTH-48), 0) 
    def update(self):
        global SCORE
        if self.rect.top < WIDTH:
            self.rect.move_ip(0, speed)
        else:
            self.rect.center = (randint(48,WIDTH-48), randint(-100, 0))
            SCORE += 1

    def draw(self,surf):
        surf.blit(self.image, self.rect)

class Camry (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Lab 8/RacerGame/sprites/camry.png").convert_alpha()
        self.image = pygame.transform.scale_by(self.image,0.3)
        self.rect = self.image.get_rect()
        self.rect.center = (540,550)
        
    def update(self):
        keys = pygame.key.get_pressed()
        if self.rect.right < WIDTH and keys[K_RIGHT]:
            self.rect.move_ip(10, 0)
        if self.rect.left > 0 and keys[K_LEFT]:
            self.rect.move_ip(-10, 0)
    def draw(self,surf):
        surf.blit(self.image, self.rect)


class Lines():
    def __init__(self, surf):
        self.Surface = surf
    def update(self):
        delta = int(self.Surface.get_width()/4)
        for i in range(delta,WIDTH,delta):
            pygame.draw.line(self.Surface,(255, 255, 255),(i,0),(i,HEIGHT),20)

        
        
            
lines = Lines(Screen)
camry = Camry()
E1 = Enemy()
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(camry)
all_sprites.add(E1)


#Creating special own event
SPEED_UP = pygame.USEREVENT + 1 #+1 for unique ID
pygame.time.set_timer(SPEED_UP, 5000)
while Running:
    Clock.tick(FPS)
    scores = font_small.render(str(SCORE), True , "BLACK")
    
    for event in pygame.event.get():
        if event.type == SPEED_UP:
            speed += 2
        if event.type == QUIT:  #pygame.QUIT
            pygame.quit()
            sys.exit()  #pygame.error: display Surface quit

    Screen.fill((128, 128, 128))
    lines.update()
    
    all_sprites.update()
    for sprite in all_sprites:
        sprite.draw(Screen)
    Screen.blit(scores, (10,10))
    if pygame.sprite.spritecollideany(camry, enemies):
        end = pygame.mixer.Sound('Lab 8/RacerGame/sounds/fail-wha-wha-version.mp3')
        end.set_volume(0.2)
        end.play()
        Screen.fill("RED")
        Screen.blit(game_over, (170,250))
        pygame.display.update()
        for sprite in all_sprites:
            sprite.kill() 
        time.sleep(4)
        pygame.quit()
    
    pygame.display.update()
