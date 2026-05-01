import math
from collections import deque
import pygame

class Painter:
    def __init__(self):
        self.color = (0, 0, 255)
        self.tool = 'brush'
        self.text_font = pygame.font.SysFont(None, 32)

        # brush
        self.drawing = False
        self.current_stroke = []
        self.brush_size = 5

        # shape states
        self.rect_start = self.rect_current = None
        self.circle_start = self.circle_current = None
        self.square_start = self.square_current = None
        self.rtri_start = self.rtri_current = None
        self.etri_start = self.etri_current = None
        self.rhombus_start = self.rhombus_current = None
        self.line_start = self.line_current = None

        # eraser
        self.eraser_radius = 20

        # text
        self.text_position = None
        self.text_buffer = ''
        self.text_active = False

    def set_color(self, key):
        colors = {'r': (255, 0, 0), 'g': (0, 255, 0), 'b': (0, 0, 255), 'w': (255, 255, 255)}
        if key in colors:
            self.color = colors[key]

    def set_tool(self, tool):
        self.tool = tool

    def start_draw(self, pos):
        self.drawing = True
        self.current_stroke = [pos]

    def add_point(self, pos):
        if self.drawing:
            self.current_stroke.append(pos)

    def stop_draw(self, canvas):
        if not (self.drawing and self.current_stroke):
            self.drawing = False
            return

        color = (255, 255, 255) if self.tool == 'eraser' else self.color
        width = self.eraser_radius if self.tool == 'eraser' else self.brush_size
        
        if len(self.current_stroke) == 1:
            pygame.draw.circle(canvas, color, self.current_stroke[0], max(1, width // 2))
        else:
            pygame.draw.lines(canvas, color, False, self.current_stroke, width)

        self.drawing = False
        self.current_stroke = []

    def start_text(self, pos):
        self.text_position = pos
        self.text_buffer = ''
        self.text_active = True

    def commit_text(self, canvas):
        if self.text_active and self.text_position and self.text_buffer:
            text_surface = self.text_font.render(self.text_buffer, True, self.color)
            canvas.blit(text_surface, self.text_position)
        self.text_active = False

    def handle_text_input(self, event, canvas):
        if self.tool != 'text' or not self.text_active:
            return False
        if event.key == pygame.K_RETURN:
            self.commit_text(canvas)
        elif event.key == pygame.K_ESCAPE:
            self.text_active = False
        elif event.key == pygame.K_BACKSPACE:
            self.text_buffer = self.text_buffer[:-1]
        elif event.unicode.isprintable():
            self.text_buffer += event.unicode
        return True

    def flood_fill(self, pos, canvas):
        x, y = pos
        width, height = canvas.get_size()
        if not (0 <= x < width and 0 <= y < height): return
        target_color = canvas.get_at((x, y))[:3]
        if target_color == self.color: return
        queue = deque([(x, y)])
        while queue:
            px, py = queue.popleft()
            if 0 <= px < width and 0 <= py < height and canvas.get_at((px, py))[:3] == target_color:
                canvas.set_at((px, py), self.color)
                queue.extend([(px+1, py), (px-1, py), (px, py+1), (px, py-1)])

    # Helper math for shapes
    def make_rect(self, start, end):
        return pygame.Rect(min(start[0], end[0]), min(start[1], end[1]), abs(end[0]-start[0]), abs(end[1]-start[1]))

    def make_radius(self, start, end):
        return int(math.hypot(end[0]-start[0], end[1]-start[1]))

    def make_square(self, start, end):
        side = min(abs(end[0]-start[0]), abs(end[1]-start[1]))
        x = start[0] if end[0] >= start[0] else start[0] - side
        y = start[1] if end[1] >= start[1] else start[1] - side
        return pygame.Rect(x, y, side, side)

    def make_rtriangle(self, start, end):
        return [(start[0], start[1]), (start[0], end[1]), (end[0], end[1])]

    def make_etriangle(self, start, end):
        side = math.hypot(end[0]-start[0], end[1]-start[1])
        height = (math.sqrt(3)/2) * side
        sign = 1 if end[1] >= start[1] else -1
        return [(start[0], start[1]), (start[0] - side/2, start[1] + sign*height), (start[0] + side/2, start[1] + sign*height)]

    def make_rhombus(self, start, end):
        dx, dy = abs(end[0]-start[0]), abs(end[1]-start[1])
        return [(start[0], start[1]-dy), (start[0]+dx, start[1]), (start[0], start[1]+dy), (start[0]-dx, start[1])]

    def mouse_down(self, pos, canvas=None):
        if self.tool in ('brush', 'eraser'): self.start_draw(pos)
        elif self.tool == 'rect': self.rect_start = self.rect_current = pos
        elif self.tool == 'circle': self.circle_start = self.circle_current = pos
        elif self.tool == 'square': self.square_start = self.square_current = pos
        elif self.tool == 'rtriangle': self.rtri_start = self.rtri_current = pos
        elif self.tool == 'etriangle': self.etri_start = self.etri_current = pos
        elif self.tool == 'rhombus': self.rhombus_start = self.rhombus_current = pos
        elif self.tool == 'line': self.line_start = self.line_current = pos
        elif self.tool == 'text': self.start_text(pos)
        elif self.tool == 'fill' and canvas: self.flood_fill(pos, canvas)

    def mouse_move(self, pos):
        if self.tool in ('brush', 'eraser'): self.add_point(pos)
        elif self.tool == 'rect': self.rect_current = pos
        elif self.tool == 'circle': self.circle_current = pos
        elif self.tool == 'square': self.square_current = pos
        elif self.tool == 'rtriangle': self.rtri_current = pos
        elif self.tool == 'etriangle': self.etri_current = pos
        elif self.tool == 'rhombus': self.rhombus_current = pos
        elif self.tool == 'line': self.line_current = pos

    def mouse_up(self, pos, canvas):
        if self.tool in ('brush', 'eraser'):
            self.stop_draw(canvas)
        elif self.tool == 'rect' and self.rect_start:
            pygame.draw.rect(canvas, self.color, self.make_rect(self.rect_start, pos), self.brush_size)
        elif self.tool == 'circle' and self.circle_start:
            pygame.draw.circle(canvas, self.color, self.circle_start, self.make_radius(self.circle_start, pos), self.brush_size)
        elif self.tool == 'square' and self.square_start:
            pygame.draw.rect(canvas, self.color, self.make_square(self.square_start, pos), self.brush_size)
        elif self.tool == 'rtriangle' and self.rtri_start:
            pygame.draw.polygon(canvas, self.color, self.make_rtriangle(self.rtri_start, pos), self.brush_size)
        elif self.tool == 'etriangle' and self.etri_start:
            pygame.draw.polygon(canvas, self.color, self.make_etriangle(self.etri_start, pos), self.brush_size)
        elif self.tool == 'rhombus' and self.rhombus_start:
            pygame.draw.polygon(canvas, self.color, self.make_rhombus(self.rhombus_start, pos), self.brush_size)
        elif self.tool == 'line' and self.line_start:
            pygame.draw.line(canvas, self.color, self.line_start, pos, self.brush_size)
        
        # Reset all
        self.rect_start = self.circle_start = self.square_start = self.rtri_start = self.etri_start = self.rhombus_start = self.line_start = None

    def draw(self, surface):
        if self.tool in ('brush', 'eraser') and self.drawing and len(self.current_stroke) > 1:
            color = (255, 255, 255) if self.tool == 'eraser' else self.color
            width = self.eraser_radius if self.tool == 'eraser' else self.brush_size
            pygame.draw.lines(surface, color, False, self.current_stroke, width)
        
        # Previews
        if self.tool == 'rect' and self.rect_start:
            pygame.draw.rect(surface, self.color, self.make_rect(self.rect_start, self.rect_current), self.brush_size)
        elif self.tool == 'circle' and self.circle_start:
            pygame.draw.circle(surface, self.color, self.circle_start, self.make_radius(self.circle_start, self.circle_current), self.brush_size)
        elif self.tool == 'square' and self.square_start:
            pygame.draw.rect(surface, self.color, self.make_square(self.square_start, self.square_current), self.brush_size)
        elif self.tool == 'rtriangle' and self.rtri_start:
            pygame.draw.polygon(surface, self.color, self.make_rtriangle(self.rtri_start, self.rtri_current), self.brush_size)
        elif self.tool == 'etriangle' and self.etri_start:
            pygame.draw.polygon(surface, self.color, self.make_etriangle(self.etri_start, self.etri_current), self.brush_size)
        elif self.tool == 'rhombus' and self.rhombus_start:
            pygame.draw.polygon(surface, self.color, self.make_rhombus(self.rhombus_start, self.rhombus_current), self.brush_size)
        elif self.tool == 'line' and self.line_start:
            pygame.draw.line(surface, self.color, self.line_start, self.line_current, self.brush_size)
        
        if self.tool == 'text' and self.text_active:
            txt = self.text_font.render(self.text_buffer, True, self.color)
            surface.blit(txt, self.text_position)
            if (pygame.time.get_ticks() // 500) % 2 == 0:
                pygame.draw.line(surface, self.color, (self.text_position[0]+txt.get_width(), self.text_position[1]), (self.text_position[0]+txt.get_width(), self.text_position[1]+32), 2)

        if self.tool == 'eraser':
            pygame.draw.circle(surface, (0,0,0), pygame.mouse.get_pos(), self.eraser_radius, 1)

    def get_color(self):
        mapping = {(255,0,0):'red', (0,255,0):'green', (0,0,255):'blue', (255,255,255):'white'}
        return mapping.get(self.color, 'Custom')

    def get_tool_type(self):
        return str(self.tool)