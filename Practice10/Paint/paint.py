import pygame

class Painter:
    def __init__(self):
        self.color = (0, 0, 255)
        self.tool = 'brush'

        # Storage for drawing elements
        self.strokes = []      # List of (stroke_points, color)
        self.rectangles = []   # List of (pygame.Rect, color)
        self.circles = []      # List of (center, radius, color)

        # Temporary state for current drawing
        self.drawing = False
        self.current_stroke = []
        self.rect_start = None
        self.rect_current = None
        self.circle_start = None
        self.circle_current = None
        
        self.eraser_radius = 20

    def set_color(self, key):
        colors = {'r': (255, 0, 0), 'g': (0, 255, 0), 'b': (0, 0, 255)}
        if key in colors:
            self.color = colors[key]

    def set_tool(self, tool):
        self.tool = tool

    def make_rect(self, start, end):
        x = min(start[0], end[0])
        y = min(start[1], end[1])
        w = abs(end[0] - start[0])
        h = abs(end[1] - start[1])
        return pygame.Rect(x, y, w, h)
    
    def make_radius(self, start, end):
        return int(((end[0] - start[0])**2 + (end[1] - start[1])**2) ** 0.5)
    
    def mouse_down(self, pos):
        if self.tool == 'brush':
            self.drawing = True
            self.current_stroke = [pos]
        elif self.tool == 'rect':
            self.rect_start = pos
            self.rect_current = pos
        elif self.tool == 'circle':
            self.circle_start = pos
            self.circle_current = pos

    def mouse_move(self, pos):
        if self.tool == 'brush' and self.drawing:
            self.current_stroke.append(pos)
        elif self.tool == 'rect' and self.rect_start:
            self.rect_current = pos
        elif self.tool == 'circle' and self.circle_start:
            self.circle_current = pos
        elif self.tool == 'eraser':
            self.erase(pos)

    def mouse_up(self, pos):
        if self.tool == 'brush' and self.drawing:
            if self.current_stroke:
                self.strokes.append((self.current_stroke, self.color))
            self.drawing = False
            self.current_stroke = []
        elif self.tool == 'rect' and self.rect_start:
            rect = self.make_rect(self.rect_start, pos)
            self.rectangles.append((rect, self.color))
            self.rect_start = self.rect_current = None
        elif self.tool == 'circle' and self.circle_start:
            radius = self.make_radius(self.circle_start, pos)
            self.circles.append((self.circle_start, radius, self.color))
            self.circle_start = self.circle_current = None

    def erase(self, pos):
        px, py = pos
        r = self.eraser_radius
        
        # Erase rects
        self.rectangles = [(rect, col) for rect, col in self.rectangles 
                           if (((rect.centerx - px)**2 + (rect.centery - py)**2)**0.5) > r]
        
        # Erase circles
        self.circles = [(c, rad, col) for c, rad, col in self.circles 
                        if (((c[0] - px)**2 + (c[1] - py)**2)**0.5) > r]

        # Erase strokes
        new_strokes = []
        for stroke, color in self.strokes:
            if all((((x - px)**2 + (y - py)**2)**0.5) > r for x, y in stroke):
                new_strokes.append((stroke, color))
        self.strokes = new_strokes

    def draw(self, screen):
        # 1. Draw permanent items
        for stroke, color in self.strokes:
            for i in range(len(stroke) - 1):
                pygame.draw.line(screen, color, stroke[i], stroke[i+1], 5)
        for rect, color in self.rectangles:
            pygame.draw.rect(screen, color, rect, 2)
        for center, radius, color in self.circles:
            pygame.draw.circle(screen, color, center, radius, 2)

        # 2. Draw live previews
        if self.tool == 'brush' and self.drawing:
            for i in range(len(self.current_stroke) - 1):
                pygame.draw.line(screen, self.color, self.current_stroke[i], self.current_stroke[i+1], 5)
        elif self.tool == 'rect' and self.rect_start and self.rect_current:
            pygame.draw.rect(screen, self.color, self.make_rect(self.rect_start, self.rect_current), 2)
        elif self.tool == 'circle' and self.circle_start and self.circle_current:
            pygame.draw.circle(screen, self.color, self.circle_start, self.make_radius(self.circle_start, self.circle_current), 2)

    def get_color_name(self):
        mapping = {(255, 0, 0): "red", (0, 255, 0): "green", (0, 0, 255): "blue"}
        return mapping.get(self.color, "None")