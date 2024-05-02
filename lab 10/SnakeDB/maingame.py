import pygame
import time
import random
from config import load_config
import psycopg2

snake_speed = 15
 
# Window size
window_x = 720
window_y = 480
 
# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
 
# Initialising pygame
pygame.init()
 
# Initialise game window
pygame.display.set_caption('Turbo Snake')
game_window = pygame.display.set_mode((window_x, window_y))
 
# FPS (frames per second) controller
fps = pygame.time.Clock()
 
# defining snake default position
snake_position = [100, 50]
 
# defining first 4 blocks of snake body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]
 
fruit_spawn = True

# setting default snake direction towards
# right
direction = 'RIGHT'
change_to = direction
 
# initial score
score = 0
 
# displaying Score function
def show_score(choice, color, font, size):
   
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)
     
    # create the display surface object 
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)
     
    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()
     
    # displaying text
    game_window.blit(score_surface, score_rect)
 
# game over function
def game_over():
   
    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)
     
    # creating a text surface on which text 
    # will be drawn
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
     
    # create a rectangular object for the text 
    # surface object
    game_over_rect = game_over_surface.get_rect()
     
    # setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)
     
    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
     
    # after 2 seconds we will quit the program
    time.sleep(2)
     
    # deactivating pygame library
    pygame.quit()
     
    # quit the program
    quit()

def show_message(msg, color, font, size):
    font_style = pygame.font.SysFont(font, size)
    mesg = font_style.render(msg, True, color)
    game_window.blit(mesg, [window_x / 6, window_y / 3])

def GetUsername(username):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM user_score WHERE name = %s", (username,))
                user = cur.fetchone()
                return user is not None
            
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
def create_user(username):
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO user_score (name,score) VALUES (%s,%s) RETURNING id", (username,0))
                conn.commit()
                return cur.fetchone()[0]
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
def GetScore(username):
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT score FROM user_score WHERE name = %s", (username,))
                score = cur.fetchone()
                return score[0] if score else None
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def add_score_to_user(username, score_to_add):

    # Получаем текущий счет пользователя
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT score FROM user_score WHERE name = %s", (username,))
                current_score = cur.fetchone()
                if current_score is None:
                    print(f"Пользователь {username} не найден в базе данных.")
                    return
                
                new_score = current_score[0] + score_to_add
                # Обновляем счет пользователя в базе данных
                cur.execute("UPDATE user_score SET score = %s WHERE name = %s", (new_score, username))
                conn.commit()
                print(f"Счет пользователя {username} обновлен. Новый счет: {new_score}")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def create_walls(level):
    walls = []
    if level == 1:
        # Уровень 1: создание стен
        for _ in range(5):  # Создаем 5 стен
            x = random.randrange(0, window_x, 10)
            y = random.randrange(0, window_y, 10)
            walls.append([x, y])

    elif level == 2:
        # Уровень 2: создание более сложных стен
        for _ in range(10):  # Создаем 10 стен
            x = random.randrange(0, window_x, 10)
            y = random.randrange(0, window_y, 10)
            walls.append([x, y])

    elif level == 3:
        # Уровень 3: создание еще более сложных стен
        for _ in range(15):  # Создаем 15 стен
            x = random.randrange(0, window_x, 10)
            y = random.randrange(0, window_y, 10)
            walls.append([x, y])

    return walls

def draw_walls(walls):
    for wall in walls:
        pygame.draw.rect(game_window, blue, pygame.Rect(wall[0], wall[1], 10, 10))

started = False
user = ''
# Main Function
paused = True

while True:
    if not started:
        fps.tick(60)
        username = input("Enter your name: ")
        user = username
        if GetUsername(username):
            print (f"Пользователь с таким именем существует, количество очков {GetScore(username)}, приятной игры")
            started = True

        else:
            print("Пользователь с таким именем не найден в базе данных. Зарегистрирован новый пользователь.")
            user_id = create_user(username)
            print("ID нового пользователя:", user_id, f"приятной игры, количество очков {GetScore(username)}" )
            started = True
    
    if started:
        # handling key events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'
                if event.key == pygame.K_ESCAPE:
                    if paused:
                        paused = False
                    else:
                        paused = True
                if event.key == pygame.K_s:
                    add_score_to_user(user,score)
                    score = 0
                    

    if paused:
        show_message(f"Paused Press 'S' to safe", white, 'Comic Sans', 30)
        pygame.display.flip()
        continue
            
    if not paused:
            
            # If two keys pressed simultaneously
            # we don't want snake to move into two 
            # directions simultaneously
            if change_to == 'UP' and direction != 'DOWN':
                direction = 'UP'
            if change_to == 'DOWN' and direction != 'UP':
                direction = 'DOWN'
            if change_to == 'LEFT' and direction != 'RIGHT':
                direction = 'LEFT'
            if change_to == 'RIGHT' and direction != 'LEFT':
                direction = 'RIGHT'
        
            # Moving the snake
            if direction == 'UP':
                snake_position[1] -= 10
            if direction == 'DOWN':
                snake_position[1] += 10
            if direction == 'LEFT':
                snake_position[0] -= 10
            if direction == 'RIGHT':
                snake_position[0] += 10
        
            # Snake body growing mechanism
            # if fruits and snakes collide then scores
            # will be incremented by 10
            snake_body.insert(0, list(snake_position))
            if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
                score += 10
                fruit_spawn = False
            else:
                snake_body.pop()
                
            if not fruit_spawn:
                fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                                random.randrange(1, (window_y//10)) * 10]
                
            fruit_spawn = True
            game_window.fill(black)
            
            for pos in snake_body:
                pygame.draw.rect(game_window, green,
                                pygame.Rect(pos[0], pos[1], 10, 10))
            pygame.draw.rect(game_window, white, pygame.Rect(
                fruit_position[0], fruit_position[1], 10, 10))
        
            # Game Over conditions
            if snake_position[0] < 0 or snake_position[0] > window_x-10:
                game_over()
            if snake_position[1] < 0 or snake_position[1] > window_y-10:
                game_over()
        
            # Touching the snake body
            for block in snake_body[1:]:
                if snake_position[0] == block[0] and snake_position[1] == block[1]:
                    game_over()
        
            # displaying score continuously
            show_score(1, white, 'times new roman', 20)
        
            # Refresh game screen
            pygame.display.update()
        
            # Frame Per Second /Refresh Rate
            fps.tick(snake_speed)