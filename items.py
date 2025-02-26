import pygame
class draggableText:
    def __init__(self, text, x, y, font_size):
        self.text = text
        self.font = pygame.font.Font(None,font_size)
        self.x, self.y = x,y
        self.dragging = False
    
    def draw(self, screen):
        text_surf = self.font.render(self.text,True,(0,0,0))
        screen.blit(text_surf,(self.x,self.y))
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.x < event.pos[0] < self.x + 100 and self.y < event.pos[1] < self.y + 50:
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            self.x, self.y = event.pos

