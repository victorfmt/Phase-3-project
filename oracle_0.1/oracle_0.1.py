import pygame
import sys
from god import gods
import random
import time

pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('ORACLE OF THE UNKNOWN GODS')

# #button with image, randomizes the god
# button_image = pygame.image.load('assets/sphere.png')
# button_x = 350
# button_y = 450
# button_width = 50
# button_height = 50

# Calculate the position and dimensions for the button
button_width = 60
button_height = 50
button_x = (window_width - button_width) // 6  # Center the button horizontally
button_y = window_height // 4  # Place it at the top half of the screen



# Set up the colors
black = (0, 0, 0)
white = (255, 255, 255)

# Load images
original_sphere_image = pygame.image.load('assets/sphere.png').convert_alpha()
sphere_image = pygame.transform.scale(original_sphere_image, (110, 60))
black_pyramid_image = pygame.image.load('assets/blackpyramidtransparent.gif')
background_image = pygame.image.load('assets/background.png')

# Load god images into a dictionary, similar to how you have the `gods` array in React.
original_gods_images = {god['name']: pygame.image.load(god['image']) for god in gods}
gods_images = {}
for god_name, god_image in original_gods_images.items():
    scaled_image = pygame.transform.scale(god_image, (300, 300))
    gods_images[god_name] = scaled_image

# def draw_button():
#     # window.blit(sphere_image, (button_x, button_y)  + (button_width, button_height))
#     pygame.draw.rect(window, black, (button_x, button_y) + (button_width, button_height))


    



def display_random_god():
    # Pick a random god
    god_name = random.choice(gods)['name']
    god_image = gods_images[god_name]

    x = 300
    y = 200

    # Draw the god
    window.blit(god_image, (x, y))

    # Update the screen
    pygame.display.update()

    # Wait for a second
    time.sleep(1)

def draw_button():
    # Draw the button image at the calculated position
    window.blit(sphere_image, (button_x, button_y))

def game_loop():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if (
                        button_x < mouse_x < button_x + button_width and
                        button_y < mouse_y < button_y + button_height
                    ):

                    # Handle left mouse button click
                        display_random_god()

        # Clear the screen
        window.fill((255, 255, 255))
        window.blit(background_image, (0, 0))

        #display the button
        draw_button()

        # Draw your game elements, text, and images here
        pygame.display.update()

        pygame.display.flip()

    pygame.quit()
    sys.exit()

# Start the game loop
game_loop()

