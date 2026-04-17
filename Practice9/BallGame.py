import pygame
import sys

def main():
    pygame.init()
    
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Moving Red Ball")
    clock = pygame.time.Clock()

    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    radius = 25
    step = 20
    
    x = WIDTH // 2
    y = HEIGHT // 2

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if (y - step) - radius >= 0:
                        y -= step
                
                elif event.key == pygame.K_DOWN:
                    if (y + step) + radius <= HEIGHT:
                        y += step
                
                elif event.key == pygame.K_LEFT:
                    if (x - step) - radius >= 0:
                        x -= step
                
                elif event.key == pygame.K_RIGHT:
                    if (x + step) + radius <= WIDTH:
                        x += step

        screen.fill(WHITE)
        pygame.draw.circle(screen, RED, (x, y), radius)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()