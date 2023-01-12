
#Author: Filip Navrkal

import pygame

# constants for the width and height of the window
WIDTH = 300
HEIGHT = 300

# create a 2D list to store the state of the board
board = [[0, 0, 0] for _ in range(3)]

# initialize Pygame
pygame.init()

# create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# create a font for rendering the text
font = pygame.font.Font(None, 32)

# create a function to draw the board on the screen
def draw_board():
  # draw a horizontal line for each row
  for y in range(1, 3):
    pygame.draw.line(screen, (0, 0, 0), (0, y * 100), (300, y * 100), 2)
  # draw a vertical line for each column
  for x in range(1, 3):
    pygame.draw.line(screen, (0, 0, 0), (x * 100, 0), (x * 100, 300), 2)

# create a function to draw the player's symbol on the board
def draw_symbol(player, x, y):
  if player == 1:
    # draw an "X" for player 1
    pygame.draw.line(screen, (255, 0, 0), (x * 100 + 10, y * 100 + 10), (x * 100 + 90, y * 100 + 90), 2)
    pygame.draw.line(screen, (255, 0, 0), (x * 100 + 90, y * 100 + 10), (x * 100 + 10, y * 100 + 90), 2)
  else:
    # draw an "O" for player 2
    pygame.draw.circle(screen, (0, 0, 255), (x * 100 + 50, y * 100 + 50), 40, 2)

# create a function to check if the game is over
def game_over():
  # check for a win by rows
  for row in board:
    if row[0] == row[1] == row[2] and row[0] != 0:
      return True
  # check for a win by columns
  for col in range(3):
    if board[0][col] == board[1][col] == board[2][col] and board[0][col] != 0:
      return True
  # check for a win by diagonals
  if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
    return True
  if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
    return True
  # check for a draw
  for row in board:
    for cell in row:
      if cell == 0:
        return False
  # if no cell is empty, it's a draw
  return True

# create a function to display the result of the game
def show_result(player):
  # clear the screen
  screen.fill((255, 255, 255))
  # display the result message
  if player == 0:
        result_text = font.render("It's a draw!", True, (0, 0, 0))
  else:
    result_text = font.render(f"Player {player} wins!", True, (0, 0, 0))
  result_rect = result_text.get_rect()
  result_rect.center = (WIDTH // 2, HEIGHT // 2)
  screen.blit(result_text, result_rect)
  pygame.display.flip()

# create a variable to store the current player
player = 1

# main game loop
running = True
while running:
  # handle events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
      # get the coordinates of the mouse click
      x, y = event.pos
      # convert the coordinates to indices for the board
      i = x // 100
      j = y // 100
      # check if the cell is empty
      if board[j][i] == 0:
        # update the board
        board[j][i] = player
        # switch players
        player = 2 if player == 1 else 1
  # clear the screen
  screen.fill((255, 255, 255))
  # draw the board
  draw_board()
  # draw the symbols
  for y, row in enumerate(board):
    for x, cell in enumerate(row):
      if cell != 0:
        draw_symbol(cell, x, y)
  # check if the game is over
  if game_over():
    show_result(player)
    pygame.time.wait(3000)
    running = False
  # update the display
  pygame.display.flip()

# quit Pygame
pygame.quit()

