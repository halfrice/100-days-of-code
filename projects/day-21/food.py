import random
import pygame


class Food:
    def __init__(self, size=12):
        self.size = size
        self.rect = None
        self.create_food()

    def create_food(self, board_size=(320, 240)):
        x = random.randint(0, int(board_size[0] / self.size) - 1)
        y = random.randint(0, int(board_size[1] / self.size) - 1)
        new_food = pygame.Rect(x * self.size, y * self.size, self.size, self.size)
        self.rect = new_food

    def ate_food(self, snake_head):
        collide = pygame.Rect.colliderect(self.food, snake_head)
        # if collide:
        #     self.create_food()
        return collide
