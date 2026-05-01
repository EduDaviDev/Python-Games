import pygame
pygame.init() 
screen = pygame.display.set_mode((768+128, 512+128)) 
pygame.key.set_repeat(150, 150) 
tileX = 0 
tileY = 0 
pygame.display.set_caption("PyPaint") 
drawing=[] 

def draw(): 
    for tile in drawing: 
        if tile[2] == 1: 
            color = (255,255,255) 
        else: 
            color = (0,0,0) 
        pygame.draw.rect(screen, color, ((tile[0]*16),(tile[1]*16),16,16)) 

def draw_cursor(TX, TY): 
    pygame.draw.rect(screen, (255,0,0), (TX * 16, TY * 16, 16, 16)) 

clock = pygame.time.Clock() 
running = True 

while running: 
    key = pygame.key.get_pressed() 
    CursorX, CursorY = pygame.mouse.get_pos() 
    mouseclick = pygame.mouse.get_pressed() 
    screen.fill((0, 0, 0)) 
    X = round(CursorX) 
    Y = round(CursorY) 
    draw() 
    draw_cursor(tileX, tileY) 
    
    if mouseclick[0] or key[pygame.K_SPACE]: 
        drawing.append([tileX,tileY,1]) 
    if mouseclick[2] or key[pygame.K_RSHIFT]: 
        drawing.append([tileX,tileY,0]) 
    if key[pygame.K_DELETE]: 
        drawing.clear() 

    mouse_stopped = True 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            rodando = False 
        if event.type == pygame.MOUSEMOTION: 
            mouse_stopped = False 
            tileX = X // 16 
            tileY = Y // 16 
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_UP: 
                tileY -= 1 
            if event.key == pygame.K_DOWN: 
                tileY += 1 
            if event.key == pygame.K_LEFT: 
                tileX -= 1 
            if event.key == pygame.K_RIGHT: 
                tileX += 1 
                
    pygame.display.flip() 

pygame.quit()
