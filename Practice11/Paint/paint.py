import pygame
import math

class Painter:
    def __init__(self):
        self.color = (0, 0, 255)
        self.tool = 'brush'

        # brush
        self.drawing = False
        self.strokes = []
        self.current_stroke = []
        self.brush_size = 5

        # rectangle
        self.rectangles = []
        self.rect_start = None
        self.rect_current = None

        # circle
        self.circles = []
        self.circle_start = None
        self.circle_current = None
        
        # eraser
        self.eraser_radius = 20
        self.eraser_strokes = []

        # square
        self.squares = []
        self.square_start = None
        self.square_current = None

        # right triangle
        self.rtriangles = []
        self.rtri_start = None
        self.rtri_current = None

        # equilateral triangle
        self.etriangles = []
        self.etri_start = None
        self.etri_current = None

        # rhombus
        self.rhombuses = []
        self.rhombus_start = None
        self.rhombus_current = None

    def set_color(self, key):
        if key == 'r': self.color = (255, 0, 0)
        elif key == 'g': self.color = (0, 255, 0)
        elif key == 'b': self.color = (0, 0, 255)
        elif key == 'w': self.color = (255, 255, 255)

    def set_tool(self, tool):
        self.tool = tool

    def start_draw(self, pos):
        self.drawing = True
        self.current_stroke = [pos]

    def add_point(self, pos):
        if self.drawing:
            self.current_stroke.append(pos)

    def stop_draw(self):
        if self.drawing and self.current_stroke:
            if self.tool == 'eraser':
                self.eraser_strokes.append((self.current_stroke, self.eraser_radius))
            else:
                self.strokes.append((self.current_stroke, self.color))
        self.drawing = False
        self.current_stroke = []

    def make_rect(self, start, end):
        x1, y1 = start
        x2, y2 = end
        return pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
    
    def make_radius(self, start, end):
        return int(((end[0] - start[0])**2 + (end[1] - start[1])**2) ** 0.5)

    def make_square(self, start, end):
        x1, y1 = start
        x2, y2 = end
        side = min(abs(x2 - x1), abs(y2 - y1))
        x = x1 if x2 >= x1 else x1 - side
        y = y1 if y2 >= y1 else y1 - side
        return pygame.Rect(x, y, side, side)

    def make_rtriangle(self, start, end):
        return [start, (start[0], end[1]), end]

    def make_etriangle(self, start, end):
        x1, y1 = start
        side = ((end[0] - x1)**2 + (end[1] - y1)**2) ** 0.5
        h = (math.sqrt(3) / 2) * side
        sign = 1 if end[1] >= y1 else -1
        return [(x1, y1), (x1 - side / 2, y1 + sign * h), (x1 + side / 2, y1 + sign * h)]

    def make_rhombus(self, start, end):
        dx, dy = abs(end[0] - start[0]), abs(end[1] - start[1])
        cx, cy = start
        return [(cx, cy - dy), (cx + dx, cy), (cx, cy + dy), (cx - dx, cy)]

    def mouse_down(self, pos):
        if self.tool in ['brush', 'eraser']: self.start_draw(pos)
        elif self.tool == 'rect': self.rect_start = self.rect_current = pos
        elif self.tool == 'circle': self.circle_start = self.circle_current = pos
        elif self.tool == 'square': self.square_start = self.square_current = pos
        elif self.tool == 'rtriangle': self.rtri_start = self.rtri_current = pos
        elif self.tool == 'etriangle': self.etri_start = self.etri_current = pos
        elif self.tool == 'rhombus': self.rhombus_start = self.rhombus_current = pos

    def mouse_move(self, pos):
        if self.tool in ['brush', 'eraser']: self.add_point(pos)
        elif self.tool == 'rect': self.rect_current = pos
        elif self.tool == 'circle': self.circle_current = pos
        elif self.tool == 'square': self.square_current = pos
        elif self.tool == 'rtriangle': self.rtri_current = pos
        elif self.tool == 'etriangle': self.etri_current = pos
        elif self.tool == 'rhombus': self.rhombus_current = pos

    def mouse_up(self, pos):
        if self.tool in ['brush', 'eraser']: self.stop_draw()
        elif self.tool == 'rect' and self.rect_start:
            self.rectangles.append((self.make_rect(self.rect_start, pos), self.color))
            self.rect_start = None
        elif self.tool == 'circle' and self.circle_start:
            self.circles.append((self.circle_start, self.make_radius(self.circle_start, pos), self.color))
            self.circle_start = None
        elif self.tool == 'square' and self.square_start:
            self.squares.append((self.make_square(self.square_start, pos), self.color))
            self.square_start = None
        elif self.tool == 'rtriangle' and self.rtri_start:
            self.rtriangles.append((self.make_rtriangle(self.rtri_start, pos), self.color))
            self.rtri_start = None
        elif self.tool == 'etriangle' and self.etri_start:
            self.etriangles.append((self.make_etriangle(self.etri_start, pos), self.color))
            self.etri_start = None
        elif self.tool == 'rhombus' and self.rhombus_start:
            self.rhombuses.append((self.make_rhombus(self.rhombus_start, pos), self.color))
            self.rhombus_start = None

    def draw(self, screen):
        # Отрисовка сохраненных объектов
        for stroke, color in self.strokes:
            for i in range(len(stroke) - 1):
                pygame.draw.line(screen, color, stroke[i], stroke[i+1], self.brush_size)
        for rect, color in self.rectangles: pygame.draw.rect(screen, color, rect, 2)
        for center, radius, color in self.circles: pygame.draw.circle(screen, color, center, radius, 2)
        for sq, color in self.squares: pygame.draw.rect(screen, color, sq, 2)
        for tri, color in self.rtriangles: pygame.draw.polygon(screen, color, tri, 2)
        for tri, color in self.etriangles: pygame.draw.polygon(screen, color, tri, 2)
        for rh, color in self.rhombuses: pygame.draw.polygon(screen, color, rh, 2)
        for stroke, radius in self.eraser_strokes:
            for i in range(len(stroke) - 1):
                pygame.draw.line(screen, (255, 255, 255), stroke[i], stroke[i+1], radius)

        # Отрисовка предпросмотра (Preview)
        if self.drawing and self.tool == 'brush':
            for i in range(len(self.current_stroke) - 1):
                pygame.draw.line(screen, self.color, self.current_stroke[i], self.current_stroke[i+1], 5)
        if self.tool == 'rect' and self.rect_start:
            pygame.draw.rect(screen, self.color, self.make_rect(self.rect_start, self.rect_current), 2)
        if self.tool == 'circle' and self.circle_start:
            pygame.draw.circle(screen, self.color, self.circle_start, self.make_radius(self.circle_start, self.circle_current), 2)
        if self.tool == 'square' and self.square_start:
            pygame.draw.rect(screen, self.color, self.make_square(self.square_start, self.square_current), 2)
        if self.tool == 'rtriangle' and self.rtri_start:
            pygame.draw.polygon(screen, self.color, self.make_rtriangle(self.rtri_start, self.rtri_current), 2)
        if self.tool == 'etriangle' and self.etri_start:
            pygame.draw.polygon(screen, self.color, self.make_etriangle(self.etri_start, self.etri_current), 2)
        if self.tool == 'rhombus' and self.rhombus_start:
            pygame.draw.polygon(screen, self.color, self.make_rhombus(self.rhombus_start, self.rhombus_current), 2)
        
        if self.tool == 'eraser':
            mx, my = pygame.mouse.get_pos()
            pygame.draw.circle(screen, (0, 0, 0), (mx, my), self.eraser_radius, 1)

    def get_color(self):
        colors = {(255,0,0): "red", (0,255,0): "green", (0,0,255): "blue", (255,255,255): "white"}
        return colors.get(self.color, "None")
    
    def get_tool_type(self):
        return str(self.tool)