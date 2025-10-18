import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
YELLOW = (255, 255, 102)
DARK_GREEN = (0, 155, 0)

# Screen Settings
DIS_WIDTH = 600
DIS_HEIGHT = 400
dis = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT))
pygame.display.set_caption('Snake Game with Wrap-Around')

# Snake Properties
snake_block = 15
snake_speed = 12

clock = pygame.time.Clock()

# Fonts
score_font = pygame.font.SysFont("comicsansms", 30, bold=True)
message_font = pygame.font.SysFont("comicsansms", 35, bold=True)

# Helper Functions
def draw_grid():
    """Draw background grid for retro effect."""
    block_size = 20
    for x in range(0, DIS_WIDTH, block_size):
        for y in range(0, DIS_HEIGHT, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(dis, (40, 100, 160), rect, 1)

def draw_snake(snake_list):
    """Draw snake with rounded segments."""
    for x in snake_list:
        pygame.draw.rect(dis, DARK_GREEN, [x[0], x[1], snake_block, snake_block], border_radius=5)

def show_score(score, high_score):
    """Display score and high score."""
    value = score_font.render(f"Score: {score}   High Score: {high_score}", True, YELLOW)
    dis.blit(value, [10, 10])

def message(msg, color, y_shift=0):
    """Display a message in the center of the screen."""
    mesg = message_font.render(msg, True, color)
    mesg_rect = mesg.get_rect(center=(DIS_WIDTH/2, DIS_HEIGHT/2 + y_shift))
    dis.blit(mesg, mesg_rect)

# Main Game Loop
def game_loop():
    game_over = False
    game_close = False
    high_score = 0
    score = 0

    # Starting position
    x1 = DIS_WIDTH // 2
    y1 = DIS_HEIGHT // 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    # Food Position
    foodx = round(random.randrange(0, DIS_WIDTH - snake_block) / 15.0) * 15.0
    foody = round(random.randrange(0, DIS_HEIGHT - snake_block) / 15.0) * 15.0

    while not game_over:

        while game_close:
            dis.fill(BLUE)
            message("Game Over!", RED, -50)
            message("Press C to Play Again or Q to Quit", YELLOW, 20)
            show_score(score, high_score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        return True  # Restart
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        x1 += x1_change
        y1 += y1_change

        # Wrap-around
        if x1 >= DIS_WIDTH:
            x1 = 0
        elif x1 < 0:
            x1 = DIS_WIDTH - snake_block

        if y1 >= DIS_HEIGHT:
            y1 = 0
        elif y1 < 0:
            y1 = DIS_HEIGHT - snake_block

        dis.fill(BLUE)
        draw_grid()

        # Draw food
        pygame.draw.rect(dis, RED, [foodx, foody, snake_block, snake_block], border_radius=3)

        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(snake_list)
        show_score(score, high_score)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, DIS_WIDTH - snake_block) / 15.0) * 15.0
            foody = round(random.randrange(0, DIS_HEIGHT - snake_block) / 15.0) * 15.0
            length_of_snake += 1
            score += 10
            if score > high_score:
                high_score = score
            snake_speed_increase = min(score // 50, 10)  # Increase difficulty
            clock.tick(snake_speed + snake_speed_increase)

        else:
            clock.tick(snake_speed)

    pygame.quit()
    sys.exit()

# Run Game with Restart Option
if __name__ == "__main__":
    while True:
        restart = game_loop()
        if not restart:
            break
