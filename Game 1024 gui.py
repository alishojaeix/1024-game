import pygame
import sys
from .game import Game1024

# Initialize pygame
pygame.init()

# Colors
COLORS = {
    0: (204, 192, 179),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}

TEXT_COLOR = (119, 110, 101)
BACKGROUND_COLOR = (187, 173, 160)
GRID_COLOR = (187, 173, 160)
CELL_SIZE = 100
PADDING = 15

class GameGUI:
    def __init__(self, size=4):
        self.game = Game1024(size)
        self.size = size
        self.width = size * CELL_SIZE + (size + 1) * PADDING
        self.height = size * CELL_SIZE + (size + 1) * PADDING + 60
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("1024 Game")
        self.font = pygame.font.SysFont("Arial", 36, bold=True)
        self.small_font = pygame.font.SysFont("Arial", 24)
    
    def draw_grid(self):
        self.screen.fill(BACKGROUND_COLOR)
        
        # Draw score
        score_text = self.small_font.render(f"Score: {self.game.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (PADDING, PADDING))
        
        # Draw grid
        for i in range(self.size):
            for j in range(self.size):
                value = self.game.grid[i][j]
                color = COLORS.get(value, (0, 0, 0))
                
                x = PADDING + j * (CELL_SIZE + PADDING)
                y = 60 + PADDING + i * (CELL_SIZE + PADDING)
                
                pygame.draw.rect(self.screen, color, (x, y, CELL_SIZE, CELL_SIZE))
                
                if value != 0:
                    text = self.font.render(str(value), True, TEXT_COLOR)
                    text_rect = text.get_rect(center=(x + CELL_SIZE//2, y + CELL_SIZE//2))
                    self.screen.blit(text, text_rect)
        
        # Check game status
        if self.game.is_game_over():
            self.show_message("Game Over!")
        elif self.game.has_won():
            self.show_message("You Win!")
        
        pygame.display.flip()
    
    def show_message(self, message):
        overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        overlay.fill((238, 228, 218, 200))
        self.screen.blit(overlay, (0, 0))
        
        text = self.font.render(message
