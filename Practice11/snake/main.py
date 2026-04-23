import pygame
import sys
import random
from logic import Snake, generate_food 

# Инициализация
pygame.init()

# Параметры окна
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Slow & Steady Snake")

# --- СКОРОСТЬ (FPS) ---
# Чем меньше число, тем медленнее змейка
LEVEL_FPS = {
    1: 7,   # Очень медленно для начала
    2: 10,  # Чуть быстрее
    3: 13   # Максимальная скорость
}

LEVEL_COLORS = {
    1: (255, 255, 255),
    2: (255, 215, 0),
    3: (0, 183, 235)
}

FOOD_LIFETIME = 5000 
clock = pygame.time.Clock()

# Объекты игры
snake = Snake()
food_pos = generate_food(snake, WIDTH, HEIGHT, snake.size)
food_spawn_time = pygame.time.get_ticks()

SCORE = 0
LEVEL = 1

# Шрифты
font_small = pygame.font.SysFont("Georgia", 20)
font_big = pygame.font.SysFont(None, 50)

running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_UP:
                snake.change_direction(0, -snake.size)
            elif event.key == pygame.K_DOWN:
                snake.change_direction(0, snake.size)
            elif event.key == pygame.K_LEFT:
                snake.change_direction(-snake.size, 0)
            elif event.key == pygame.K_RIGHT:
                snake.change_direction(snake.size, 0)

    if not game_over:
        snake.move()
        hx, hy = snake.body[0]

        # Проверка столкновений
        if hx < 0 or hx >= WIDTH or hy < 0 or hy >= HEIGHT or (hx, hy) in snake.body[1:]:
            game_over = True

        # Поедание еды
        if (hx, hy) == food_pos:
            snake.grow = True
            food_pos = generate_food(snake, WIDTH, HEIGHT, snake.size)
            food_spawn_time = pygame.time.get_ticks()
            SCORE += random.randint(1, 3)

        # Таймер еды
        if pygame.time.get_ticks() - food_spawn_time > FOOD_LIFETIME:
            food_pos = generate_food(snake, WIDTH, HEIGHT, snake.size)
            food_spawn_time = pygame.time.get_ticks()

        # Уровни
        if SCORE >= 10: LEVEL = 3
        elif SCORE >= 5: LEVEL = 2
        else: LEVEL = 1

    # Отрисовка
    if not game_over:
        screen.fill(LEVEL_COLORS.get(LEVEL, (255, 255, 255)))
        snake.draw(screen)
        
        # Цвет еды
        time_left = FOOD_LIFETIME - (pygame.time.get_ticks() - food_spawn_time)
        food_color = (255, 100, 100) if time_left < 1000 else (200, 0, 0)
        pygame.draw.rect(screen, food_color, (food_pos[0], food_pos[1], snake.size, snake.size))

        # UI
        screen.blit(font_small.render(f"Score: {SCORE}", True, (0, 0, 0)), (5, 5))
        screen.blit(font_small.render(f"Level: {LEVEL} (Slow Mode)", True, (0, 0, 0)), (5, 25))
    else:
        screen.fill((200, 0, 0))
        screen.blit(font_big.render("Game Over!", True, (255, 255, 255)), (200, 150))
        screen.blit(font_big.render(f"Final Score: {SCORE}", True, (255, 255, 255)), (200, 200))

    pygame.display.flip()
    clock.tick(LEVEL_FPS.get(LEVEL, 7))