import pygame
from math import sqrt
import os

import pygame.draw 

pygame.init()

WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")
clock = pygame.time.Clock()
FPS = 60
running = True 
load_image = pygame.image.load("Lab 7/Music_Player/player/plane.png").convert_alpha()
load_image = pygame.transform.scale_by(load_image, 0.7)


def checkCollision(posMouse,rect):
        if sqrt((posMouse[0]-rect.center[0])**2 + (posMouse[1]-rect.center[1])**2) < rect.width//2:
            return True
        else:
            return False
    

def TracksLoad(dir):
    Tracks = []
    for file in os.listdir(dir):
        if file.endswith(".mp3"):
            Tracks.append(os.path.join(dir,file))
    return Tracks


Tracks = TracksLoad("Lab 7/Music_Player/player/TrackList")
iterator = 0
time = 0
currentsong = pygame.mixer.music.load(Tracks[iterator])
currentsound = pygame.mixer.Sound(Tracks[iterator])
"""

here need file manager

"""

pygame.mixer.music.set_volume(0.1)
stoppedtime = 0
class PauseButton():
    def __init__(self,scale=1):
        self.pause = pygame.image.load("Lab 7/Music_Player/player/pause.png").convert_alpha()
        self.play = pygame.image.load("Lab 7/Music_Player/player/play.png").convert_alpha()
        self.choice = self.play
        self.image = pygame.transform.scale_by(self.choice,scale)
        self.rect = self.play.get_rect(center = (WIDTH/2 , 400) )
        self.clicked = False
    
    def draw(self,surface):
        surface.blit(self.choice,self.rect)
        
        global pos
        pos = pygame.mouse.get_pos()
        
        if checkCollision(pos,self.rect):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                if self.choice == self.play:
                    if pygame.mixer.music.get_pos() == -1:
                        pygame.mixer.music.play()
                    else: 
                        pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()
                self.clicked = True
                self.choice = self.pause if self.choice == self.play else self.play

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

class Backfront():
    def __init__(self):
        
        self.front = pygame.image.load("Lab 7/Music_Player/player/front.png").convert_alpha()
        self.back = pygame.image.load("Lab 7/Music_Player/player/back.png").convert_alpha()
        self.front_rect = self.front.get_rect(center = (WIDTH/2 + 150, 400))
        self.back_rect = self.back.get_rect(center = (WIDTH/2 - 150, 400))
        self.clicked = False
    def draw(self,surface):
        surface.blit(self.front, self.front_rect)
        surface.blit(self.back, self.back_rect)
    def update(self):
        global iterator
        global time
        if checkCollision(pos, self.front_rect) and not self.clicked and pygame.mouse.get_pressed()[0]:
            #print("its front")
            pygame.mixer.music.stop()
            self.clicked = True
            iterator += 1
            currentsong = pygame.mixer.music.load(Tracks[iterator])
            currentsound = pygame.mixer.Sound(Tracks[iterator])
            time = 0
            pygame.mixer.music.play()        
        if checkCollision(pos, self.back_rect) and not self.clicked and pygame.mouse.get_pressed()[0]:
            #print("its back")
            pygame.mixer.music.stop()
            self.clicked = True
            iterator -= 1
            currentsong = pygame.mixer.music.load(Tracks[iterator])
            currentsound = pygame.mixer.Sound(Tracks[iterator])
            time = 0
            pygame.mixer.music.play()
        if pygame.mouse.get_pressed()[0] == False:
            self.clicked = False

class Musicline():
    def __init__(self):
        self.startpoint = (WIDTH/2-200, 330)
        self.endpoint =  (WIDTH/2+200, 330)
        self.pressed = False
        
    def draw(self,surface):
        pygame.draw.line(surface, (160, 32, 240), self.startpoint, self.endpoint, 10)
    def update(self,surface):
        """
            процент пройденной музыки = миллисекунды/1000 поделать на длину
            *написать фикс чтобы саунд with определял длину и удалялся из памяти
            точка сейчас определяется по проценту на всю длину строки
            дальше проверка на нажатие если находится в области и нажата мышь свойство нажато становится тру
            и при следующем каждом кадре провереятся не отжали ли мышь если в кадре мышь все еще нажата отрисовка
            все еще идет отнасительно координаты икс
        """
        global time
        #print(time,pygame.mixer.music.get_pos())
        #01:02 как отпускание то написать - cadr kogda pressed true no uzhe ne pressed 01:46
        #выявлен баг пока держишь линию коснувшись паузы она срабатывает
        percentage_song =  0.01 if pygame.mixer.music.get_pos() <=1600 else  ((pygame.mixer.music.get_pos()/1000)+time)/currentsound.get_length()  #get pos gives 1 sec is 1000 and get length give in seconds
        currentpoint = pygame.Vector2(self.startpoint)+(+percentage_song*398, 0)
        #print(pygame.mouse.get_pressed()[0])
        if pos[0] < WIDTH/2 - 200 + 2:
            x = WIDTH/2-200 + 2   #check для границ
        elif pos[0] > WIDTH/2 + 200 - 2:
            x = WIDTH/2+200 - 2 
        else:
            x = pos[0]
        

        if self.pressed and not pygame.mouse.get_pressed()[0]:
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.rewind()
                pygame.mixer.music.set_pos(((x-self.startpoint[0])/398 * currentsound.get_length()))
            else:
                pygame.mixer.music.play()
                pygame.mixer.music.set_pos(((x-self.startpoint[0])/398 * currentsound.get_length()))
                
                #pygame.mixer.music.set_pos(((x-self.startpoint[0])/398 * currentsound.get_length()))
            #current position + secs so rewind need
            #print(currentsound.get_length())
            #print((x-self.startpoint[0])/398*currentsound.get_length())
            #print(pygame.mixer.music.get_pos())
            time = (x-self.startpoint[0])/398 * currentsound.get_length() -pygame.mixer.music.get_pos()/1000 #get_pos gives whole time that music played so by subscracting selected we can avoid problems with above code we can 
            #print(self.time)

        if not pygame.mouse.get_pressed()[0]:
            self.pressed = False
        elif self.pressed == True:
            currentpoint = pygame.Vector2(x,330)
        elif sqrt((x-currentpoint[0])**2 + (pos[1]-currentpoint[1]+1)**2) < 10 and pygame.mouse.get_pressed()[0]==1:
            self.pressed = True 
            currentpoint = pygame.Vector2(pos[0],330) #В этот блок после первого нажатия не залетает благодаря прессед
        

        pygame.draw.line(surface, (255, 255, 255), pygame.Vector2(self.startpoint)+(2, 0), currentpoint, 6)
        pygame.draw.circle(surface, (255, 255, 255), currentpoint+(0,1), 8)
        pygame.draw.circle(surface, (160, 32, 240), currentpoint+(0,1), 5)
        


        
pause = PauseButton(1)
backfront = Backfront()
musline = Musicline()

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    screen.fill((230,230,230))
    
    pause.draw(screen)
    
    backfront.draw(screen)
    backfront.update()
    musline.draw(screen)    
    musline.update(screen)
    screen.blit(load_image,(135, 40))
    
    pygame.display.flip()
pygame.quit()


#get pos 