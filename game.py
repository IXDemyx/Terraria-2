import pygame
from config import *


class Game():
    def __init__(self) -> None:
        self.clock = pygame.time.Clock()
        self.running = True
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        pygame.display.set_caption("Terraria 2")
        
    
    def run(self):
        while self.running:
            pygame.display.flip()
            self.clock.tick(FPS)