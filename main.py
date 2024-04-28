import pygame
import os
import random
from time import sleep
import time

def my_function_name(): 

    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    w, h = screen.get_size()
    pygame.mixer.init()

    # Create a font object
    font = pygame.font.SysFont('Arial', 248, bold=True)

    # Render the text as a surface
    text = font.render('ERROR', True, (255, 255, 255))

    # Get the rectangle of the text surface
    text_rect = text.get_rect()

    # Set the position of the text surface
    text_rect.center = (w // 2, h // 2)

    # Set the screen background color to black
    screen.fill((0, 0, 0))

    # Draw the text surface onto the screen
    screen.blit(text, text_rect)

    # Update the display
    pygame.display.update()

    # Get a list of all the files in a sounds folder
    sounds_folder = 'sounds'
    sound_files = [f for f in os.listdir(sounds_folder) if f.endswith('.mp3')]

    # Load and play the first sound file
    pygame.mixer.music.load(os.path.join(sounds_folder, random.choice(sound_files)))
    pygame.mixer.music.play()

    # Blink the text surface very fast
    for i in range(100):
        # Toggle the visibility of the text surface
        if i % 2 == 0:
            screen.fill((0, 0, 0))
        else:
            screen.blit(text, text_rect)

        # Update the display
        pygame.display.update()

        # Pause for a short time
        pygame.time.Clock().tick(60)

    # Get a list of all the files in an images folder
    images_folder = 'images'
    image_files = [f for f in os.listdir(images_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

    # Load the image and display it on the screen
    image = pygame.image.load(os.path.join(images_folder, random.choice(image_files)))
    image = pygame.transform.scale(image, (w, h))
    screen.blit(image, (0,0))
    pygame.display.update()

    # Blink the image very fast
    for i in range(100):
        # Toggle the visibility of the image
        if i % 2 == 0:
            screen.fill((0, 0, 0))
        else:
            screen.blit(image, (0,0))

        # Update the display
        pygame.display.update()

        # Pause for a short time
        pygame.time.Clock().tick(60)

    # Load the image and display it on the screen
    image = pygame.image.load(os.path.join(images_folder, random.choice(image_files)))
    image = pygame.transform.scale(image, (w, h))
    screen.blit(image, (0,0))
    pygame.display.update()
    sleep(3)

while True: 
    time.sleep(2400) # pause the script for 20 seconds
    my_function_name()
    pygame.quit() # quit Pygame