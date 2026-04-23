import pygame
import sys
from paint import Painter  # Импортируем наш класс из соседнего файла

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
                
                # Выбор цвета
                if event.key == pygame.K_r: painter.set_color('r')
                elif event.key == pygame.K_g: painter.set_color('g')
                elif event.key == pygame.K_b: painter.set_color('b')
                
                # Выбор инструмента
                if event.key == pygame.K_t: painter.set_tool('rect')
                elif event.key == pygame.K_p: painter.set_tool('brush')
                elif event.key == pygame.K_c: painter.set_tool('circle')
                elif event.key == pygame.K_e: painter.set_tool('eraser')
                elif event.key == pygame.K_s: painter.set_tool('square')
                elif event.key == pygame.K_d: painter.set_tool('rtriangle')
                elif event.key == pygame.K_f: painter.set_tool('etriangle')
                elif event.key == pygame.K_h: painter.set_tool('rhombus')
                
                # Размер ластика
                if event.key == pygame.K_z: painter.eraser_radius += 5
                elif event.key == pygame.K_x: painter.eraser_radius = max(5, painter.eraser_radius - 5)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: painter.mouse_down(event.pos)

            if event.type == pygame.MOUSEMOTION:
                painter.mouse_move(event.pos)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: painter.mouse_up(event.pos)

        # Рендеринг
        screen.fill((255, 255, 255))
        painter.draw(screen)

        # Отображение UI
        txt_tool = font.render(f"tool: {painter.get_tool_type()}", True, (0, 0, 0))
        txt_color = font.render(f"color: {painter.get_color()}", True, (0, 0, 0))
        txt_eraser = font.render(f"Eraser radius: {painter.eraser_radius}", True, (0, 0, 0))
        
        screen.blit(txt_tool, (5, 5))
        if painter.get_tool_type() == "eraser":
            screen.blit(txt_eraser, (5, 25))
        else:
            screen.blit(txt_color, (5, 25))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()