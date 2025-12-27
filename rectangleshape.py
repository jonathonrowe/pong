import pygame

class RectangleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.width = width
        self.height = height
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
    
    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass

    def check_collision(self, other):
        x_overlap = (self.position.x + self.width > other.position.x) and (self.position.x < other.width + other.position.x)
        y_overlap = (self.position.y + self.height > other.position.y) and (self.position.y < other.height + other.position.y)
        return x_overlap and y_overlap