import pygame
pygame.init()

FPS = 60
running = True
clock = pygame.time.Clock()
WIDTH = 800
HEIGHT = 600
painting = []
 
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Paint")

def draw_menu():
    pygame.draw.rect(screen, 'gray', (0, 0, WIDTH, 90))
    pygame.draw.line(screen, 'black', (0,90), (WIDTH, 90), 5)
    c_brush = pygame.draw.rect(screen, 'black', (10,10,70,70))
    pygame.draw.circle(screen, "white", (45,45) , 30)
    r_brush = pygame.draw.rect(screen, 'black', (90,10,70,70))
    pygame.draw.rect(screen, "white", (100,20,50,50))
    e_brush = pygame.draw.rect(screen, 'black', (170,10,70,70))
    font = pygame.font.SysFont("ubuntumono", 20)

    text = font.render("Eraser",True,"white")
    textrect =(e_brush.left+5, e_brush.top +20)
    screen.blit(text,textrect)

    brushes_rect = [c_brush, r_brush, e_brush]
    blue = pygame.draw.rect(screen, (0, 0, 255), [WIDTH-35,15,25,25])
    red = pygame.draw.rect(screen, (255, 0, 0), [WIDTH-35,40,25,25])
    green = pygame.draw.rect(screen, (0, 255, 0), [WIDTH-60,15,25,25])
    yellow = pygame.draw.rect(screen, (255, 255, 0), [WIDTH-60,40,25,25])
    white = pygame.draw.rect(screen, (255, 255, 255), [WIDTH-85,40,25,25])
    black = pygame.draw.rect(screen, (0, 0, 0), [WIDTH-85,15,25,25])
    

    color_rect = [blue, red, yellow, green, white, black]
    

    return color_rect, brushes_rect 

def draw_painting(painting):
    for item in painting:
        color, pos, brush = item
        if brush == brushes[0]:
            pygame.draw.circle(screen, color, pos , 30)
        elif brush == brushes[1]:
            pygame.draw.rect(screen, color, (pos[0]-35,pos[1]-35,70,70))
        elif brush == brushes[2]:
            pygame.draw.rect(screen, "white", (pos[0]-35,pos[1]-35,70,70))

selectColor = "white"
selectedBrush = pygame.draw.circle(screen, "white", (45,45) , 30)
while running:
    clock.tick(FPS)
    screen.fill((250,250,250))
    
    colors, brushes  = draw_menu()

    rgblist = ["blue", "red", "yellow", "green", "white", "black"]

    pos = pygame.mouse.get_pos()
    draw = False
    
    
    if pos[1] > 90:
        if selectedBrush == brushes[0]:
            pygame.draw.circle(screen, selectColor, pos , 30)

        elif selectedBrush == brushes[1]:
            pygame.draw.rect(screen, selectColor, (pos[0]-35,pos[1]-35,70,70) )
        elif selectedBrush == brushes[2]:
            pygame.draw.rect(screen, "white", (pos[0]-35,pos[1]-35,70,70) )
    pygame.draw.circle(screen,selectColor,(WIDTH/2,45),30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if pos[1] < 90:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(colors)):
                    if colors[i].collidepoint(event.pos):
                        selectColor = rgblist[i]
                for i in range(len(brushes)):
                    if brushes[i].collidepoint(event.pos):
                        selectedBrush = brushes[i]
        else:
            if pygame.mouse.get_pressed()[0]:
                draw = True
            else :
                draw = False
                
            if event.type == pygame.MOUSEMOTION:
                if draw:
                    painting.append((selectColor, event.pos, selectedBrush))
    
        
    draw_painting(painting)
    pygame.display.update()


pygame.quit()
            