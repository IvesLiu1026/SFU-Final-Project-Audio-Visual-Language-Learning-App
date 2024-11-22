# cmpt120image.py
# Some helper functions to wrap the Pygame image functions
# CMPT 120; version Fall 2024 
# (modified by Brian Fraser; some code written with help of CoPilot)

import pathlib
import pygame
import numpy

def is_valid_pixels(pixels):
    """
    Input: pixels - 3d list of lists of RGB values (a height-by-width-by-3 list)
    Returns: True if pixels is a valid 3d list of lists of RGB values, False otherwise
    """
    if type(pixels) != list or len(pixels) == 0:
        return False
    if type(pixels[0]) != list or len(pixels[0]) == 0:
        return False
    if type(pixels[0][0]) != list or len(pixels[0][0]) == 0:
        return False
    return True

def get_image(filename):
    """
    Input: filename - string containing image filename to open relative
        to the folder of the current python file.
    Returns: 3d list of lists (a height-by-width-by-3 list)
    """
    # Check argument types to help catch passing in the wrong type of argument
    # NOTE: If you are told there is an error on these lines, it _very_ likely
    # means you are passing in the wrong type of argument to this function.
    # Check your calling code carefully, using the debugger, to see what you are passing in.
    assert type(filename) == str, "get_image(): `filename` argument must be a string"

    folder_of_code = pathlib.Path(__file__).parent.resolve()
    full_name = folder_of_code / filename
    image = pygame.image.load(full_name)

    # do a transpose so its rows correspond to height of the image
    return pygame.surfarray.array3d(image).transpose(1, 0, 2).tolist()


def save_image(pixels, filename):
    """
    Input:  pixels - 3d list of lists of RGB values (a height-by-width-by-3 list)
        filename - string containing filename to save image, relative to the 
                    folder of the current python file.
    Output: Saves a file containing pixels
    """
    # Check argument types to help catch passing in the wrong type of argument
    # NOTE: If you are told there is an error on these lines, it _very_ likely
    # means you are passing in the wrong type of argument to this function.
    # Check your calling code carefully, using the debugger, to see what you are passing in.
    assert is_valid_pixels(pixels), "save_image(): `pixels` argument must be a a 3d list of lists of RGB values (a height-by-width-by-3 list)"
    assert type(filename) == str, "save_image(): `filename` argument must be a string"
    assert filename.endswith('.jpg') or filename.endswith('.png'), "save_image(): `filename` argument must end with '.jpg' or '.png'"

    # do a transpose so its rows correspond to width of the image (used by Pygame)
    nparray = numpy.asarray(pixels).transpose(1, 0, 2)
    surf = pygame.surfarray.make_surface(nparray)

    folder_of_code = pathlib.Path(__file__).parent.resolve()
    full_name = folder_of_code / filename
    pygame.image.save(surf, full_name)


def show_image(pixels,title):
    """
    Input:  pixels - 3d list of list of RGB values (a height-by-width-by-3 list)
    Output: show the image in a window

    *this function uses the Pygame to display a window in a not-so-conventional way
    (without an event loop) so it might appear frozen.
    Suggested use: use it at the end of the program to show how the image looks like
    and make it stay by a this line:
    input("Press enter to quit")
    """

    # Check argument types to help catch passing in the wrong type of argument
    # NOTE: If you are told there is an error on these lines, it _very_ likely
    # means you are passing in the wrong type of argument to this function.
    # Check your calling code carefully, using the debugger, to see what you are passing in.
    assert is_valid_pixels(pixels), "show_image(): `pixels` argument must be a a 3d list of lists of RGB values (a height-by-width-by-3 list)"
    assert type(title) == str, "show_image(): `title` argument must be a string"

    # do a transpose so its rows correspond to width of the image (used by Pygame)
    nparray = numpy.asarray(pixels).transpose(1, 0, 2)
    surf = pygame.surfarray.make_surface(nparray)
    (width, height, colours) = nparray.shape

    # for pixels2
    pygame.display.init()
    pygame.display.set_caption(title)
    screen = pygame.display.set_mode((width, height))
    screen.fill((225, 225, 225))
    screen.blit(surf, (0, 0))
    pygame.display.update()


def get_black_image(width, height):
    """
    Input:  width - width of the image
        height - height of the image
    Output: 3d list of lists of a black image (a height-by-width-by-3 list)
    """
    return [[[0, 0, 0] for i in range(width)] for j in range(height)]

def wait_for_escape():
    """
    Output: waits for the user to press the escape key
    """
    print("Program done. Press escape in the window to quit.")
    run = True
    while run:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
    pygame.quit()
