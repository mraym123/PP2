import pygame
import os
import shutil
from datetime import datetime
from tools import Painter

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Mini Paint')
    clock = pygame.time.Clock()
    
    canvas = pygame.Surface((800, 600))
    canvas.fill((255, 255, 255))
    
    painter = Painter()
    font = pygame.font.SysFont(None, 25)
    brush_sizes = {2: 'small (2)', 5: 'medium (5)', 10: 'large (10)'}
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if painter.handle_text_input(event, canvas):
                    continue
                
                if event.key == pygame.K_ESCAPE: running = False
                
                if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                    filename = f'canvas_{timestamp}.png'
                    pygame.image.save(canvas, filename)
                    if not os.path.exists("images"): os.mkdir("images")
                    shutil.move(filename, f"images/{filename}")
                    continue

                keys_color = {pygame.K_r:'r', pygame.K_g:'g', pygame.K_b:'b', pygame.K_w:'w'}
                keys_tool = {pygame.K_t:'rect', pygame.K_p:'brush', pygame.K_c:'circle', 
                             pygame.K_e:'eraser', pygame.K_s:'square', pygame.K_d:'rtriangle', 
                             pygame.K_f:'etriangle', pygame.K_h:'rhombus', pygame.K_l:'line', 
                             pygame.K_k:'fill', pygame.K_i:'text'}
                
                if event.key in keys_color: painter.set_color(keys_color[event.key])
                if event.key in keys_tool: painter.set_tool(keys_tool[event.key])

                if event.key == pygame.K_z: painter.eraser_radius += 5
                elif event.key == pygame.K_x: painter.eraser_radius = max(5, painter.eraser_radius - 5)
                elif event.key == pygame.K_1: painter.brush_size = 2
                elif event.key == pygame.K_2: painter.brush_size = 5
                elif event.key == pygame.K_3: painter.brush_size = 10

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                painter.mouse_down(event.pos, canvas)
            if event.type == pygame.MOUSEMOTION:
                painter.mouse_move(event.pos)
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                painter.mouse_up(event.pos, canvas)

        screen.fill((255, 255, 255))
        screen.blit(canvas, (0, 0))
        painter.draw(screen)

        # UI Overlay
        tool_name = painter.get_tool_type()
        txt_tool = font.render(f'tool: {tool_name}', True, (0, 0, 0))
        txt_color = font.render(f'color: {painter.get_color()}', True, (0, 0, 0))
        txt_size = font.render(f'size: {brush_sizes.get(painter.brush_size, "N/A")}', True, (0, 0, 0))
        
        screen.blit(txt_tool, (5, 5))
        screen.blit(txt_size, (5, 45))
        if tool_name == 'eraser':
            txt_era = font.render(f'Eraser radius: {painter.eraser_radius}', True, (0, 0, 0))
            screen.blit(txt_era, (5, 25))
        else:
            screen.blit(txt_color, (5, 25))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()