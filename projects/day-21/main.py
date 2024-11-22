# Snake
# Python Turtle is alright, but let's build it with PyGame 💪

import pygame
import snake
import food

pygame.init()
pygame.display.set_caption('Snake')
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

sw, sh = pygame.display.get_surface().get_size()
board_size = (sw, sh)
grid_size = 32
unit_size = int(sw / grid_size)

# colors
bg_color = '#a9e011'  # Snake game background color from the Nokia 3310
snake_color = '#202020'  # Snake color from the Nokia 3310
food_color = '#ff775e'  # Dark Peach
text_color = '#16161d'  # Eigengrau
you_died_color = '#B20F11'  # Dark souls 'you died' text color

snake = snake.Snake(unit_size)
food = food.Food(unit_size)


def draw_score(score, color=text_color):
    score_font = pygame.font.Font('freesansbold.ttf', int(unit_size * 1.5))
    score_text = score_font.render(f'Score: {score}', True, color)
    screen.blit(score_text, ((sw / 2) - (score_text.get_width() / 2), 0))


def draw_game_over(score):
    """Give em the Dark Souls PTSD"""
    screen.fill(pygame.Color(0, 0, 0, 255))
    gameover_font = pygame.font.Font('freesansbold.ttf', unit_size * 4)
    gameover_text = gameover_font.render('YOU DIED', True, you_died_color)

    draw_score(score, '#ffffff')
    screen.blit(
        gameover_text,
        (
            (sw / 2) - (gameover_text.get_width() / 2),
            (sh / 2) - (gameover_text.get_height() / 2),
        ),
    )
    pygame.display.update()


score = 0
game_state = 'game'

while True:
    # Process inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Game Over
    if game_state == 'game_over':
        draw_game_over(score)

    # Game
    elif game_state == 'game':
        keys = pygame.key.get_pressed()
        # Try WASD if you're a true gamer
        # Try VIM movement keys if you're a true software engineer
        if keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[pygame.K_h]:
            snake.left()
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d] or keys[pygame.K_l]:
            snake.right()
        elif keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_k]:
            snake.up()
        elif keys[pygame.K_DOWN] or keys[pygame.K_s] or keys[pygame.K_j]:
            snake.down()

        # Game Logic
        snake.move(board_size)

        if snake.ate_food(food.rect):
            score += 1
            snake.grow()
            food.create_food(board_size)
        if snake.ate_tail():
            print(f'You lose. Score: {score}')
            game_state = 'game_over'

        # Render graphics
        screen.fill(bg_color)

        draw_score(score)

        for s in snake.parts:
            pygame.draw.rect(screen, snake_color, s)

        pygame.draw.rect(screen, food_color, food.rect)

        # Update display
        pygame.display.flip()
        clock.tick(15)
