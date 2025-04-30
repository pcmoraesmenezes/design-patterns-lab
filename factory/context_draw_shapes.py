import pygame
import random
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    @abstractmethod
    def draw(self, surface):
        pass
    
    
class Circle(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.radius = random.randint(10, 50)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        
        
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
        
        
class Rectangle(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = random.randint(20, 100)
        self.height = random.randint(20, 100)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
        
    
class ShapeContext:
    def __init__(self, shape_type, x, y):
        self.shape_type = shape_type   
        self.x = x
        self.y = y
        
    
class ShapeFactory:
    @staticmethod
    def create_shape(context):
        if context.shape_type == "circle":
            return Circle(context.x, context.y)
        elif context.shape_type == "rectangle":
            return Rectangle(context.x, context.y)
        else:
            raise ValueError("Unknown shape type")
        
        
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    
    pygame.display.set_caption("Shape Factory")
    clock = pygame.time.Clock()
    
    shape_factory = ShapeFactory()
    
    shapes = []
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                
                shape_type = random.choice(["circle", "rectangle"])
                shape = shape_factory.create_shape(shape_type, x, y)
                shapes.append(shape)
                
        screen.fill((255, 255, 255))
        
        # buffer the shapes
        for shape in shapes:
            shape.draw(screen)
            
        pygame.display.flip()
        clock.tick(60)
        
    pygame.quit()
    
    
if __name__ == "__main__":
    main()