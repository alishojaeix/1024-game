import random
import numpy as np

class Game1024:
    def __init__(self, size=4):
        self.size = size
        self.grid = np.zeros((size, size), dtype=int)
        self.score = 0
        self.add_new_tile()
        self.add_new_tile()
    
    def add_new_tile(self):
        """Add a new 2 or 4 tile to a random empty position"""
        empty_cells = [(i, j) for i in range(self.size) 
                      for j in range(self.size) if self.grid[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.grid[i][j] = 2 if random.random() < 0.9 else 4
    
    def move(self, direction):
        """Move tiles in the specified direction (0: up, 1: right, 2: down, 3: left)"""
        moved = False
        original_grid = self.grid.copy()
        
        # Rotate grid to treat all directions as left movement
        self.grid = np.rot90(self.grid, direction)
        
        for i in range(self.size):
            # Remove zeros
            row = [num for num in self.grid[i] if num != 0]
            
            # Merge adjacent equal numbers
            new_row = []
            skip = False
            for j in range(len(row)):
                if skip:
                    skip = False
                    continue
                if j < len(row) - 1 and row[j] == row[j+1]:
                    merged = row[j] * 2
                    new_row.append(merged)
                    self.score += merged
                    skip = True
                else:
                    new_row.append(row[j])
            
            # Fill with zeros
            new_row += [0] * (self.size - len(new_row))
            self.grid[i] = new_row
            
            # Check if this row changed
            if not np.array_equal(original_grid[i], self.grid[i]):
                moved = True
        
        # Rotate back
        self.grid = np.rot90(self.grid, -direction)
        
        if moved:
            self.add_new_tile()
            return True
        return False
    
    def is_game_over(self):
        """Check if the game is over (no moves left)"""
        if 0 in self.grid:
            return False
        
        for i in range(self.size):
            for j in range(self.size):
                if j < self.size - 1 and self.grid[i][j] == self.grid[i][j+1]:
                    return False
                if i < self.size - 1 and self.grid[i][j] == self.grid[i+1][j]:
                    return False
        
        return True
    
    def has_won(self):
        """Check if the player has reached 1024"""
        return 1024 in self.grid
    
    def __str__(self):
        return str(self.grid)
