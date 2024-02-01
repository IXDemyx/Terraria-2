import pygame

class Player():
    def __init__(self,x,y) -> None:
        self.rect = pygame.Rect(x,y,5,5)
        self.x = x
        self.y = y
        self.jump = False
        self.velocity = 3
        self.direction = pygame.math.Vector2()
        
    def input(self):
        keys = pygame.key.get_pressed()
        
        self.direction.y = 0
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = 'right'
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'
        else:
            self.direction.x = 0
        # if keys[pygame.K_SPACE] and self.can_jump:
        #     self.can_jump = False
        #     self.jump_time = pygame.time.get_ticks()
        #     self.jumping = True
        
    def draw(self,screen):
        pygame.draw.rect(screen,(255,0,0),self.rect)
        
        
    def update(self,screen):
        self.move()
        self.draw(screen)