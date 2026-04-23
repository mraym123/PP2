import pygame
import sys
from snake import Snake, generate_food  # Import our logic

# Configuration
WIDTH, HEIGHT = 600, 400
LEVEL_FPS = {1: 7, 2: 10, 3: 12}  # Slower speeds for easier play
LEVEL_COLORS = {1: (255, 255, 255), 2: (255, 215, 0), 3: (0, 183, 235)}

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mini Snake - Organized Version")
    clock = pygame.time.Clock()
    
    # Initialize Game Objects
    snake = Snake()
    food_pos = generate_food(snake.body, WIDTH, HEIGHT, snake.size)
    score = 0
    game_over = False
    font_small = pygame.font.SysFont("Georgia", 20)
    font_big = pygame.font.SysFont(None, 50)

    running = True
    while running:
        # 1. Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and not game_over:
                if event.key == pygame.K_UP:    snake.change_direction(0, -snake.size)
                elif event.key == pygame.K_DOWN:  snake.change_direction(0, snake.size)
                elif event.key == pygame.K_LEFT:  snake.change_direction(-snake.size, 0)
                elif event.key == pygame.K_RIGHT: snake.change_direction(snake.size, 0)

        # 2. Game Logic Updates
        if not game_over:
            snake.move()
            head = snake.body[0]

            # Check Collisions (Walls or Self)
            if (head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT or head in snake.body[1:]):
                game_over = True

            # Check Food
            if head == food_pos:
                snake.grow = True
                score += 1
                food_pos = generate_food(snake.body, WIDTH, HEIGHT, snake.size)

            # Determine Level
            level = 1 if score < 5 else 2 if score < 10 else 3

        # 3. Rendering (Drawing)
        if not game_over:
            screen.fill(LEVEL_COLORS.get(level))
            # Draw Snake
            for seg in snake.body:
                pygame.draw.rect(screen, (0, 200, 0), (seg[0], seg[1], snake.size, snake.size))
            # Draw Food
            pygame.draw.rect(screen, (200, 0, 0), (food_pos[0], food_pos[1], snake.size, snake.size))
            # Draw UI
            screen.blit(font_small.render(f"Score: {score}", True, (0,0,0)), (5, 0))
            screen.blit(font_small.render(f"Level: {level}", True, (0,0,0)), (5, 25))
        else:
            screen.fill((200, 0, 0))
            screen.blit(font_big.render("Game Over!", True, (255, 255, 255)), (WIDTH//2 - 100, HEIGHT//2 - 50))
            screen.blit(font_big.render(f"Final Score: {score}", True, (255, 255, 255)), (WIDTH//2 - 100, HEIGHT//2))

        pygame.display.flip()
        clock.tick(LEVEL_FPS.get(level, 7))

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()