import pygame
from paint import Painter

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Mini Paint")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 25)

    painter = Painter()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: running = False
                # Color Keys
                if event.key in [pygame.K_r, pygame.K_g, pygame.K_b]:
                    painter.set_color(pygame.key.name(event.key))
                # Tool Keys
                tools = {pygame.K_t: 'rect', pygame.K_p: 'brush', pygame.K_c: 'circle', pygame.K_e: 'eraser'}
                if event.key in tools:
                    painter.set_tool(tools[event.key])
                # Eraser Size
                if event.key == pygame.K_z: painter.eraser_radius += 5
                if event.key == pygame.K_x: painter.eraser_radius = max(5, painter.eraser_radius - 5)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                painter.mouse_down(event.pos)
            if event.type == pygame.MOUSEMOTION:
                painter.mouse_move(event.pos)
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                painter.mouse_up(event.pos)

        # Rendering
        screen.fill((255, 255, 255))
        painter.draw(screen)

        # UI Text
        ui_tool = font.render(f"Tool: {painter.tool}", True, (0, 0, 0))
        ui_info = f"Eraser Radius: {painter.eraser_radius}" if painter.tool == 'eraser' else f"Color: {painter.get_color_name()}"
        ui_detail = font.render(ui_info, True, (0, 0, 0))
        
        screen.blit(ui_tool, (10, 10))
        screen.blit(ui_detail, (10, 30))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()