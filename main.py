import pygame
import random
from enum import Enum
from collections import namedtuple

from src.utils import Direction, Point
from src.colors import WHITE, BLACK, BLUE1, BLUE2, RED
from settings import *

pygame.init()

font = pygame.font.Font("fonts/arial.ttf",25)

class SnakeGame:
    def __init__(self, w=640, h=480) -> None:
        self.w = w # how many pixels for the width
        self.h = h # how many pixels for the height
        # init display
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()
        # init game state1q   
        self.direction = Direction.RIGHT
        
        self.head = Point(self.w//2, self.h//2)
        self.snake = [self.head, 
                      Point(self.head.x - BLOCK_SIZE, self.head.y),
                      Point(self.head.x - 2*BLOCK_SIZE, self.head.y)]
        
        self.score = 0
        self.food = None
        self._place_food()

    def _update_ui(self):
        self.display.fill(BLACK)
        
        for pt in self.snake:
            pygame.draw.rect(self.display, BLUE1, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, BLUE2, pygame.Rect(pt.x+4, pt.y+4, 12, 12))

        pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))
        
        text = font.render("Score: " + str(self.score), True, WHITE)
        last_key = font.render("Key: " + str(self.direction), True, WHITE)
        
        # event.key
        
        self.display.blit(text, [0, 0])
        self.display.blit(last_key, [0, BLOCK_SIZE])
        pygame.display.flip()
        
    def _place_food(self):
        
        x = random.randint(0, (self.w - BLOCK_SIZE)//BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (self.h - BLOCK_SIZE)//BLOCK_SIZE) * BLOCK_SIZE
        
        self.food = Point(x, y)
        # DOnt want to place food inside the snake!
        if self.food in self.snake:
            self._place_food()
    
    def _move(self, direction):
        x = self.head.x
        y = self.head.y
        if direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif direction == Direction.DOWN:
            y += BLOCK_SIZE
        elif direction == Direction.UP:
            y -= BLOCK_SIZE
        
        self.head = Point(x, y)
        
    def _is_collision(self):
        # hits bndy?
        if self.head.x > self.w - BLOCK_SIZE or self.head.x < 0 or self.head.y < 0 or self.head.y > self.h - BLOCK_SIZE:
            return True
        
        if self.head in self.snake[1:]:
            return True
        
        return False
        # hits itsnake?
        
    def play_step(self):
        # 1. collect the user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT:
                    self.direction = Direction.RIGHT
                elif event.key == pygame.K_UP:
                    self.direction = Direction.UP
                elif event.key == pygame.K_DOWN:
                    self.direction = Direction.DOWN
        # 2. move
        self._move(self.direction) # updates the head
        self.snake.insert(0, self.head)
        # 3.  check if game over
        #     check if hit boundary or itself.
        game_over = False
        if self._is_collision():
            game_over = True
            return game_over, self.score
        
        # 4. place new food or just move
        #    if no food is caught we need to pop the last element from the snake array
        if self.head == self.food:
            self.score += 1
            self._place_food()
        else:
            self.snake.pop()
        
        # 5. update the ui and clock
        self._update_ui()
        self.clock.tick(SPEED)
        # 6. return if game over and score
        game_over = False
        return game_over, self.score

if __name__ == "__main__":
    
    print("Start of game")
    
    game = SnakeGame()
    
    while True:
        game_over, score = game.play_step()
        
        if game_over:
            break

        # show the score

    print(f"Final Score {score}")
    pygame.quit()