
#Author: Filip Navrkal

import pygame

# initialize pygame
pygame.init()

# set screen size
size = (700, 500)
screen = pygame.display.set_mode(size)

# set title and icon
pygame.display.set_caption("Hangman")
#icon = pygame.image.load('icon.png')
#pygame.display.set_icon(icon)

container_surface = pygame.Surface((800, 100))

# set font
font = pygame.font.Font(pygame.font.match_font('Monospace'), 30)

# set word to be guessed
word = "python"

# set number of incorrect guesses allowed
max_guesses = 6

# initialize variables
guessed_letters = []
incorrect_guesses = 0
game_over = False

# Draw Hanger
pygame.draw.line(screen, (255, 255, 255), (50, 350), (150, 350), 2) 
pygame.draw.line(screen, (255, 255, 255), (100, 350), (100, 50), 2) 
pygame.draw.line(screen, (255, 255, 255), (100, 50), (250, 50), 2) 
pygame.draw.line(screen, (255, 255, 255), (250, 50), (250, 70), 2) 

# Create a list of underscores that match the length of the word
hidden_word = ["_" for letter in word]

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.unicode.isalpha():
                letter = event.unicode
                if letter in word and letter not in guessed_letters:
                    guessed_letters.append(letter)
                    # replace underscores with correctly guessed letters
                    for i, char in enumerate(word):
                        if char == letter:
                            hidden_word[i] = letter

                elif letter not in word:
                    incorrect_guesses += 1
                    if incorrect_guesses == max_guesses:
                        lose_text = font.render("You Lost!", True, (255, 255, 255))
                        screen.blit(lose_text, (250, 450))
                        game_over = True

    # draw Hangman
    if incorrect_guesses > 0:
        # draw head
        pygame.draw.circle(screen, (255, 255, 255), (250, 100), 30, 2)
    if incorrect_guesses > 1:
        # draw body
        pygame.draw.line(screen, (255, 255, 255), (250, 130), (250, 250), 2)
    if incorrect_guesses > 2:
        # draw left arm
        pygame.draw.line(screen, (255, 255, 255), (250, 160), (200, 200), 2)
    if incorrect_guesses > 3:
        # draw right arm
        pygame.draw.line(screen, (255, 255, 255), (250, 160), (300, 200), 2)
    if incorrect_guesses > 4:
        # draw left leg
        pygame.draw.line(screen, (255, 255, 255), (250, 250), (200, 300), 2)
    if incorrect_guesses > 5:
        # draw right leg
        pygame.draw.line(screen, (255, 255, 255), (250, 250), (300, 300), 2)

    # update screen
    pygame.display.update()
    
    # display underscores
    max_width = max([font.size(letter)[0] for letter in hidden_word])
    x = 100  # starting x position of the first letter
    for letter in hidden_word:
        letter_text = font.render(letter, True, (255, 255, 255))
        letter_rect = letter_text.get_rect()
        letter_rect.x = x
        letter_rect.y = 400
        letter_rect.width = max_width
        screen.blit(letter_text, letter_rect)
        x += max_width + 10  # add letter width plus 10 pixels to x position

    # check for win
    if "_" not in hidden_word:
        win_text = font.render("You Won!", True, (255, 255, 255))
        screen.blit(win_text, (250, 450))
        pygame.display.update()
        pygame.time.wait(3000)
        game_over = True
        pygame.quit()

   
