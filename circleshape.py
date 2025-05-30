import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def check_collision(self, shape):
        # 1. Calculate distance between the centers
        distance = self.position.distance_to(shape.position)

        # 2. Calculate the sum of the radius
        sum_of_radius = self.radius + shape.radius
        
        # 3. Check if distance is less than or equal to sum of radius
        return distance <= sum_of_radius