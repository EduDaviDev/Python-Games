import pygame


# Inicialização
pygame.init()
tela = pygame.display.set_mode((768+128, 512+128))

# O primeiro número (500) é o atraso inicial em milissegundos
# O segundo número (50) é a velocidade da repetição
pygame.key.set_repeat(150, 150)

tileX = 0
tileY = 0

pygame.display.set_caption("PyPaint")

desenho=[]

def desenhar():
    for tile in desenho:
        if tile[2] == 1:
            color = (255,255,255)
        else:
            color = (0,0,0)
        pygame.draw.rect(tela, color, ((tile[0]*16),(tile[1]*16),16,16))

def desenhar_cursor(TX, TY):
    # Desenha o quadrado na posição correta da grade
    pygame.draw.rect(tela, (255,0,0), (TX * 16, TY * 16, 16, 16))


relogio = pygame.time.Clock() # 1. Cria o relógio

# Loop principal
rodando = True
while rodando:
    # Dentro do seu loop principal
    teclas = pygame.key.get_pressed()

    # Pega a posição (x, y)
    CursorX, CursorY = pygame.mouse.get_pos()

    # Pega o estado dos botões: (Esquerdo, Meio, Direito)
    clique = pygame.mouse.get_pressed()   
    
    tela.fill((0, 0, 0)) # Fundo preto
    
    X = round(CursorX)
    Y = round(CursorY)
        
    desenhar()
    
    desenhar_cursor(tileX, tileY)
    
    if clique[0] or teclas[pygame.K_SPACE]:
        desenho.append([tileX,tileY,1])
    if clique[2] or teclas[pygame.K_RSHIFT]:
        desenho.append([tileX,tileY,0])
    if teclas[pygame.K_DELETE]:
        desenho.clear()
    
    # No início do loop principal
    mouse_parado = True 
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            
        if evento.type == pygame.MOUSEMOTION:
            mouse_parado = False # Se houve movimento, ele não está parado
            tileX = X // 16
            tileY = Y // 16
        
        if evento.type == pygame.QUIT:
            rodando = False

        # É AQUI que o set_repeat funciona:
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:    tileY -= 1
            if evento.key == pygame.K_DOWN:  tileY += 1
            if evento.key == pygame.K_LEFT:  tileX -= 1
            if evento.key == pygame.K_RIGHT: tileX += 1
    
    pygame.display.flip()

pygame.quit()
