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
    
    def check_center_collision(self, other):
        center_x_overlap = (self.position.x + self.width > other.position.x) and (self.position.x < other.width + other.position.x)
        center_y_overlap = (
            (self.position.y + self.height < (other.position.y + (other.height * .75))) and
            (self.position.y > (other.position.y + (other.height * .25)))
        )
        return center_x_overlap and center_y_overlap

    def check_top_edge_collision(self, other):
        edge_x_overlap = (self.position.x + self.width > other.position.x) and (self.position.x < other.width + other.position.x)
        edge_y_overlap = (
            (self.position.y + self.height > other.position.y) and
            (self.position.y < (other.position.y + (other.height * .25)))
        )
        return edge_x_overlap and edge_y_overlap

    def check_bottom_edge_collision(self, other):
        edge_x_overlap = (self.position.x + self.width > other.position.x) and (self.position.x < other.width + other.position.x)
        edge_y_overlap = (
            (self.position.y + self.height > (other.position.y + (other.height * .75))) and
            (self.position.y < (other.position.y + other.height))
        )
        return edge_x_overlap and edge_y_overlap