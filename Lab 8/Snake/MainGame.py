import pygame
import time
import random
 
snakeSpeed = 15
HEIGHT = 480
WIDTH = 720
 
pygame.init()
pygame.display.set_caption('Snake')
Screen = pygame.display.set_mode((WIDTH, HEIGHT))
 
FPS = pygame.time.Clock()
 
snakePosition = [100, 100]
 
snakeBody = [[100, 100],[90, 100],[80, 100],[70, 100]]
fruitPosition = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
 
fruitSpawn = True
 
# setting default snake direction towards
# right
direction = 'R'
change = direction
score = 0 # initial score
 
def showScore(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score) + "   Level: " + str(score//50), True, color)
    score_rect = score_surface.get_rect()
    Screen.blit(score_surface, score_rect)
 
# game over function
def game_over():
    font = pygame.font.SysFont('ubuntumono', 50)
    gameOverSurf = font.render('Your Score is : ' + str(score), True, 'red')
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (WIDTH/2, HEIGHT/4)

    Screen.blit(gameOverSurf, gameOverRect)
    pygame.display.flip()
    time.sleep(2)
    
    pygame.quit()
    quit()
 
 
# Main Loop
while True:
    snakeSpeed = score/10 + 10
    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change = 'U'
            if event.key == pygame.K_DOWN:
                change = 'D'
            if event.key == pygame.K_LEFT:
                change = 'L'
            if event.key == pygame.K_RIGHT:
                change = 'R'
 
    if change == 'U' and direction != 'D':
        direction = 'U'
    if change == 'D' and direction != 'U':
        direction = 'D'
    if change == 'L' and direction != 'R':
        direction = 'L'
    if change == 'R' and direction != 'L':
        direction = 'R'
    
    # Moving the snake
    if direction == 'U':
        snakePosition[1] -= 10
    if direction == 'D':
        snakePosition[1] += 10
    if direction == 'L':
        snakePosition[0] -= 10
    if direction == 'R':
        snakePosition[0] += 10
    #body mechanism
    snakeBody.insert(0, list(snakePosition))
    if snakePosition[0] == fruitPosition[0] and snakePosition[1] == fruitPosition[1]:
        score += 10
        fruitSpawn = False
    else:
        snakeBody.pop()
    if not fruitSpawn:
        fruitPosition = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
         
    fruitSpawn = True
    Screen.fill('black')
     
    for pos in snakeBody:
        pygame.draw.rect(Screen, 'green',
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(Screen, 'white', pygame.Rect(
        fruitPosition[0], fruitPosition[1], 10, 10))
 
    # Game Over conditions
    if snakePosition[0] < 0 or snakePosition[0] > WIDTH-10:
        game_over()
    if snakePosition[1] < 0 or snakePosition[1] > HEIGHT-10:
        game_over()
 
    # Touching the snake body
    for block in snakeBody[1:]:
        if snakePosition[0] == block[0] and snakePosition[1] == block[1]:
            game_over()
 
    # displaying score continuously
    showScore(1, 'white', 'ubuntu', 20)
    
    # Refresh game screen
    pygame.display.update()
 
    # Frame Per Second /Refresh Rate
    FPS.tick(snakeSpeed)