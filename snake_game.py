
#Author: Filip Navrkal

import sys
import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (400, 400)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the window title
pygame.display.set_caption("Snake")

# Set the background color
bg_color = (0, 0, 0)

# Set the snake's starting position and velocity
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

# Set the food's starting position
food_pos = [random.randrange(1, (window_size[0] // 10)) * 10, random.randrange(1, (window_size[1] // 10)) * 10]
food_spawn = True

# Set the direction the snake is moving
direction = 'RIGHT'
change_to = direction

# Set the score to 0
score = 0

# Set the clock to control the game's frame rate
clock = pygame.time.Clock()

# Set the game's font
font = pygame.font.SysFont('times new roman', 20)

# Set the game's FPS (frames per second)
fps = 15

# Set the colors
red = pygame.Color(255, 0, 0)  # game over
green = pygame.Color(0, 255, 0)  # snake
black = pygame.Color(0, 0, 0)  # score
white = pygame.Color(255, 255, 255)  # background
brown = pygame.Color(165, 42, 42)  # food

# Game Over function
def game_over():
    my_font = pygame.font.SysFont('times new roman', 30)
    game_over_font = my_font.render('Your score was: {}'.format(score), True, red)
    screen.blit(game_over_font, (100, 200))
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

        # If the direction the snake is moving is opposite to the direction it was previously moving, don't do anything
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Move the snake
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()
    
    if food_spawn == False:
        food_pos = [random.randrange(1, (window_size[0] // 10)) * 10, random.randrange(1, (window_size[1] // 10)) * 10]
    food_spawn = True
    
    screen.fill(bg_color)
    
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))
        
    pygame.draw.rect(screen, brown, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
    
    # Game Over conditions
    if snake_pos[0] < 0 or snake_pos[0] > window_size[0]-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > window_size[1]-10:
        game_over()
        
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()
    
    # Score
    score_font = font.render('Score: {}'.format(score), True, white)
    screen.blit(score_font, (5, 5))
    
    # Refresh the screen
    pygame.display.update()
    
    # Set the frame rate
    clock.tick(fps)

