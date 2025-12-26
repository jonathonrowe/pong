import pygame

class RectangleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass

