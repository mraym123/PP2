import pygame, sys
from pygame.locals import *
import random, time
from car import Player, Enemy, Coin # Импорт наших классов

# Инициализация 
pygame.init()

# Настройки
FPS = 60
FramePerSec = pygame.time.Clock()

# Цвета
BLUE, RED, GREEN, BLACK, WHITE = (0,0,255), (255,0,0), (0,255,0), (0,0,0), (255,255,255)

# Глобальные переменные
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 600
SPEED, SCORE, COIN_SCORE = 5, 0, 0
COIN_SPEED = 5
SUFFICIENT_COIN_INCREASE = 5

# Интерфейс
DISPLAYSURF = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Game")
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
background = pygame.image.load("AnimatedStreet.png")

# Создание объектов
P1 = Player()
E1 = Enemy()
COIN = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(COIN)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, COIN)

# События
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Основной цикл
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
            if COIN_SCORE >= SUFFICIENT_COIN_INCREASE:
                SPEED += 1
                SUFFICIENT_COIN_INCREASE = (SUFFICIENT_COIN_INCREASE // 5 + 1) * 5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0,0))
    
    # Отрисовка текста
    DISPLAYSURF.blit(font_small.render("Scores", True, BLACK), (5, 0))
    DISPLAYSURF.blit(font_small.render(str(SCORE), True, BLACK), (10, 25))
    DISPLAYSURF.blit(font_small.render("Coins", True, BLACK), (345, 0))
    DISPLAYSURF.blit(font_small.render(str(COIN_SCORE), True, BLACK), (360, 25))
    DISPLAYSURF.blit(font_small.render(f"Speed: {round(SPEED, 1)}", True, BLACK), (5, 45))

    # Движение и отрисовка
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        if isinstance(entity, Enemy):
            if entity.move(SPEED): # Если враг проехал мимо
                SCORE += 1
        elif isinstance(entity, Coin):
            entity.move(COIN_SPEED)
        else:
            entity.move()

    # Сбор монет
    if pygame.sprite.spritecollideany(P1, coins):
        COIN_SCORE += COIN.earn_point()
        try:
            pygame.mixer.Sound('coin_take.mp3').play()
        except: pass

    # Столкновение с врагом
    if pygame.sprite.spritecollideany(P1, enemies):
        try: pygame.mixer.Sound('crash.wav').play()
        except: pass
        
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 200))
        DISPLAYSURF.blit(font.render(f"Scores: {SCORE}", True, BLACK), (60, 285))
        DISPLAYSURF.blit(font.render(f"Coins: {COIN_SCORE}", True, BLACK), (60, 365))
        pygame.display.update()
        
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()        

    pygame.display.update()
    FramePerSec.tick(FPS)