import pygame
import datetime
import sys

WIDTH, HEIGHT = 800, 800
FPS = 60

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mickey's Clock")
    clock = pygame.time.Clock()

    try:
        bg_image = pygame.image.load("assets/mickey_clock.png").convert_alpha()
        left_hand_img = pygame.image.load("assets/left_hand.png").convert_alpha()
        right_hand_img = pygame.image.load("assets/right_hand.png").convert_alpha()
    except FileNotFoundError:
        sys.exit()

    left_hand_img = pygame.transform.smoothscale(left_hand_img, 
        (left_hand_img.get_width() // 6, left_hand_img.get_height() // 6))
    right_hand_img = pygame.transform.smoothscale(right_hand_img, 
        (right_hand_img.get_width() // 1.1, right_hand_img.get_height() // 1.1))

    bg_rect = bg_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        current_time = datetime.datetime.now()
        second = current_time.second
        minute = current_time.minute

        sec_angle = -(second * 6)
        min_angle = -(minute * 6)

        rotated_left_hand = pygame.transform.rotate(left_hand_img, sec_angle)
        left_hand_rect = rotated_left_hand.get_rect(center=bg_rect.center)

        rotated_right_hand = pygame.transform.rotate(right_hand_img, min_angle)
        right_hand_rect = rotated_right_hand.get_rect(center=bg_rect.center)

        screen.fill((255, 255, 255))
        
        screen.blit(bg_image, bg_rect)
        screen.blit(rotated_right_hand, right_hand_rect)
        screen.blit(rotated_left_hand, left_hand_rect)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()