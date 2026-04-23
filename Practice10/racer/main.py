import pygame, sys
import time
from car import Player, Enemy, Coin 

# Initialize
pygame.init()

# Settings
FPS = 60
FramePerSec = pygame.time.Clock()
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 600
SPEED = 5
SCORE = 0
COIN_SCORE = 0
BLACK, RED = (0, 0, 0), (255, 0, 0)

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")

# Assets - Updated with 'mater/' prefix
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
background = pygame.image.load("mater/AnimatedStreet.png")

# Sprite Groups
P1 = Player()
E1 = Enemy(SPEED)
C1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

# Speed Increase Event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5      
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw Background
    DISPLAYSURF.blit(background, (0,0))
    
    # UI Text
    scores_label = font_small.render(f"Scores: {SCORE}", True, BLACK)
    coins_label = font_small.render(f"Coins: {COIN_SCORE}", True, BLACK)
    DISPLAYSURF.blit(scores_label, (10, 10))
    DISPLAYSURF.blit(coins_label, (280, 10))

    # Move and Draw all entities
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        if isinstance(entity, Enemy):
            if entity.move(SPEED): SCORE += 1
        elif isinstance(entity, Coin):
            entity.move(5)
        else:
            entity.move()

    # Coin Collision
    if pygame.sprite.spritecollideany(P1, coins):
        COIN_SCORE += 1
        C1.spawn()
        try:
            # Matches the filename background.mp3 seen in your sidebar
            pygame.mixer.Sound('mater/coin_take.mp3').play()
        except: pass

    # Enemy Collision
    if pygame.sprite.spritecollideany(P1, enemies):
        try: 
            pygame.mixer.Sound('mater/crash.wav').play()
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