import pygame, sys
import time
from car import Player, Enemy, Coin 

# Инициализация
pygame.init()

# Настройки экрана и FPS
FPS = 60
FramePerSec = pygame.time.Clock()
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 600
SPEED = 5
SCORE = 0
COIN_SCORE = 0
BLACK, RED, WHITE = (0, 0, 0), (255, 0, 0), (255, 255, 255)

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer Game")

# --- ЗАГРУЗКА МУЗЫКИ ---
try:
    pygame.mixer.music.load("background.mp3") # Или .wav, проверь файл
    pygame.mixer.music.play(-1)               # -1 для бесконечного повтора
except:
    print("Фоновая музыка не найдена")

# Шрифты и фон
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
background = pygame.image.load("AnimatedStreet.png")

# Создание объектов
P1 = Player()
E1 = Enemy(SPEED)
C1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

# Событие ускорения
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5      
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Отрисовка фона
    DISPLAYSURF.blit(background, (0,0))
    
    # Текст счета
    scores_label = font_small.render(f"Scores: {SCORE}", True, BLACK)
    coins_label = font_small.render(f"Coins: {COIN_SCORE}", True, BLACK)
    DISPLAYSURF.blit(scores_label, (10, 10))
    DISPLAYSURF.blit(coins_label, (280, 10))

    # Движение и отрисовка всех объектов
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        if isinstance(entity, Enemy):
            if entity.move(SPEED): SCORE += 1
        elif isinstance(entity, Coin):
            entity.move(5)
        else:
            entity.move()

    # Сбор монеток
    if pygame.sprite.spritecollideany(P1, coins):
        COIN_SCORE += 1
        C1.spawn()
        try:
            pygame.mixer.Sound('coin_take.mp3').play()
        except: pass

    # Столкновение с врагом
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.music.stop() # Останавливаем музыку при аварии
        try: 
            pygame.mixer.Sound('crash.mp3').play() # Убедись, что это .wav или .mp3
        except: pass
        
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(font.render("Game Over", True, BLACK), (30, 200))
        pygame.display.update()
        
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()        
        
    pygame.display.update()
    FramePerSec.tick(FPS)