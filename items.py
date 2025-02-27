import pygame

class draggableText:
    def __init__(self, text, x, y, font_size):
        self.text = text
        self.font_size = font_size
        self.font = pygame.font.Font(None, font_size)
        self.x, self.y = x, y
        self.dragging = False
        self.color = (0, 0, 0)  # Default color
        self.selected = False

    def draw(self, screen):
        text_surf = self.font.render(self.text, True, self.color)
        screen.blit(text_surf, (self.x, self.y))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_mouse_on_text(event.pos):
                if event.button == 1:
                    self.dragging = True
                    self.selected = True
                    self.mouse_x, self.mouse_y = event.pos
                    self.offset_x = self.x - self.mouse_x
                    self.offset_y = self.y - self.mouse_y
                if self.selected == True:
                    if event.button == 4:
                        self.change_font_size(self.font_size + 1)
                    if event.button == 5:
                        self.change_font_size(self.font_size - 1)

                
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                self.mouse_x, self.mouse_y = event.pos
                self.x = self.mouse_x + self.offset_x
                self.y = self.mouse_y + self.offset_y
            else:
                if self.is_mouse_on_text(event.pos):
                    self.selected = True
                    self.color = (0, 0, 255)  # Change color to blue when hovered
                else:
                    self.selected = False
                    self.color = (0, 0, 0)  # Change color back to black when not hovered
    def is_mouse_on_text(self, pos):
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        rect = text_surface.get_rect(topleft=(self.x, self.y))
        return rect.collidepoint(pos)

    def change_font_size(self, new_font_size):
        self.font_size = new_font_size
        self.font = pygame.font.Font(None, new_font_size)