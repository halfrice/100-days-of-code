import pygame

UP = -1
DOWN = 1
LEFT = -1
RIGHT = 1


class Snake:
    def __init__(self, size):
        self.size = size
        self.xheading = RIGHT
        self.yheading = None
        self.parts = []
        self.create_snake()
        self.head = self.parts[0]

    def create_snake(self, starting_pos=(0, 0), length=3):
        for i in range(length):
            new_seg = pygame.Rect(
                starting_pos[0] - (self.size * i), starting_pos[1], self.size, self.size
            )
            self.parts.append(new_seg)

    def grow(self):
        tail = self.parts[-1]
        new_seg = pygame.Rect(tail.x, tail.y, self.size, self.size)
        self.parts.append(new_seg)

    def ate_tail(self):
        for part in self.parts[3:]:
            if pygame.Rect.colliderect(self.head, part):
                return True
        return False

    def ate_food(self, food):
        collide = pygame.Rect.colliderect(self.head, food)
        return collide

    def move(self, board_size):
        for i in range(len(self.parts) - 1, 0, -1):
            new_x = self.parts[i - 1].x
            new_y = self.parts[i - 1].y
            self.parts[i].x = new_x
            self.parts[i].y = new_y

        if self.xheading == LEFT:
            if self.head.x - self.size < 0:
                self.head.x = board_size[0] - self.size
            else:
                self.head.x += self.size * self.xheading
        elif self.xheading == RIGHT:
            if self.head.x + self.size > board_size[0] - self.size:
                self.head.x = 0
            else:
                self.head.x += self.size * self.xheading
        elif self.yheading == UP:
            if self.head.y - self.size < 0:
                self.head.y = board_size[1] - self.size
            else:
                self.head.y += self.size * self.yheading
        elif self.yheading == DOWN:
            if self.head.y + self.size > board_size[1] - self.size:
                self.head.y = 0
            else:
                self.head.y += self.size * self.yheading

    def up(self):
        if self.yheading != DOWN:
            self.xheading = None
            self.yheading = UP

    def down(self):
        if self.yheading != UP:
            self.xheading = None
            self.yheading = DOWN

    def left(self):
        if self.xheading != RIGHT:
            self.xheading = LEFT
            self.yheading = None

    def right(self):
        if self.xheading != LEFT:
            self.xheading = RIGHT
            self.yheading = None
