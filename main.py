# TODO: Your header

import cmpt120image
import draw
import pygame
import os

###############################################################
# Keep this block at the beginning of your code. Do not modify.
def play_sound(soundfilename):
    """
        Play a wave file by passing in the filename without the .wav extension.
        e.g. playSound(apples) plays apples.wav
    """
    dir = os.path.dirname(os.path.abspath(__file__))
    pygame.mixer.init()
    pygame.mixer.music.load(dir + "/sounds/" + soundfilename + ".wav")
    pygame.mixer.music.play()

def read_input_with_screen(prompt):
    """
    Read input from the user either from the console or from a pygame window.
    - If pygame is not initialized, it will read from the console.
    - If pygame is initialized, it will read from the pygame window.
    """
    # If pygame video is not initialized, do a normal input:
    if not pygame.display.get_init():
        return input("<Text> " + prompt)

    if prompt:
        print("<Screen> " + prompt)

    run = True
    user_input = ""
    while run:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                elif event.key == pygame.K_RETURN:
                    run = False
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode

    return user_input

###############################################################


# How to play a sound (plays from the sounds/ folder automatically)
play_sound("apples")

# How to show an image
img = cmpt120image.get_image("images/apples.png")
cmpt120image.show_image(img, f"Showing picture for `apples`")

read_input_with_screen("Press enter when sound has finished to exit...")
