# Run this file to test your solution!
# You should not need to make any changes to this code
# Written by Brian Fraser, copyright 2023
import draw
import cmpt120image
import os
import pygame

###############################################################
# Keep this block at the beginning of your code. Do not modify.
#
def read_input_with_screen(prompt):
    """
    Returns the input from the user, but also allows the user to close the window.
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

# Global constants
HEIGHT = 600
WIDTH = 400
IMG_PATH = "images/apples.png"
IMG2_PATH = "images/child.png"
IMG3_PATH = "images/fish.png"



def get_gray_image(width, height):
    img = cmpt120image.get_black_image(width, height)
    for row in range(height):
        for col in range(width):
            img[row][col] = [155, 155, 155]
    return img


def test_draw_item():
    canvas = get_gray_image(WIDTH, HEIGHT)

    # Draw one image
    img = cmpt120image.get_image(IMG_PATH)
    draw.draw_item(canvas, img, 10, 0)

    # Draw images in horizontal row
    img2 = cmpt120image.get_image(IMG2_PATH)
    for col in [0, 100, 200]:
        draw.draw_item(canvas, img2, 100, col)

    # Draw images overlapping
    img1 = cmpt120image.get_image(IMG_PATH)
    for col in range(0, 300, 10):
        draw.draw_item(canvas, img1, 200, col)

    cmpt120image.show_image(canvas, "Draw Item Test")


def test_recolor_image():
    canvas = get_gray_image(WIDTH, HEIGHT)
    colours = [ [128, 0, 128],  [255, 0, 0],  [0, 255, 0],  [0, 0, 255]]
    col = 0

    # Recolour image 
    for colour in colours:
        img = cmpt120image.get_image(IMG_PATH)
        rc_img = draw.recolor_image(img, colour)
        draw.draw_item(canvas, rc_img, 10, col)
        col += 100

    # Check that original is unchanged
    img = cmpt120image.get_image(IMG_PATH)
    rc_img = draw.recolor_image(img, colour)
    draw.draw_item(canvas, img, 100, 0)
    cmpt120image.show_image(canvas, "Recolour test")


def test_minify():
    canvas = get_gray_image(WIDTH, HEIGHT)
    col = 0

    # Minify
    img = cmpt120image.get_image(IMG_PATH)
    small_img = draw.minify(img)
    draw.draw_item(canvas, small_img, 10, col)
    col += 100

    # Check that original is unchanged
    draw.draw_item(canvas, img, 100, 0)
    cmpt120image.show_image(canvas, "Minify test")


def test_mirror():
    canvas = get_gray_image(WIDTH, HEIGHT)

    # Mirror image 1
    img = cmpt120image.get_image(IMG_PATH)
    mirror_img = draw.mirror(img)
    draw.draw_item(canvas, mirror_img, 10, 0)

    # Check that original is unchanged
    draw.draw_item(canvas, img, 10, 100)

    # Check 2nd image
    img2 = cmpt120image.get_image(IMG2_PATH)
    mirror_img2 = draw.mirror(img2)
    draw.draw_item(canvas, mirror_img2, 100, 0)
    draw.draw_item(canvas, img2, 100, 100)

    cmpt120image.show_image(canvas, "Mirror test")


def test_distribute_items():
    canvas = get_gray_image(WIDTH, HEIGHT)
    section_height = 200
    section_width = len(canvas[0])

    # Test a sparse distribution
    img2 = cmpt120image.get_image(IMG2_PATH)
    sub_canvas = get_gray_image(section_width, section_height)
    draw.distribute_items(sub_canvas, img2, 10)
    draw.draw_item(canvas, sub_canvas, 10, 0)
    
    # Test a dense distribution, going right to the edge
    img3 = cmpt120image.get_image(IMG3_PATH)
    sub_canvas = get_gray_image(section_width, section_height)
    draw.distribute_items(sub_canvas, img3, 1000)
    draw.draw_item(canvas, sub_canvas, 300, 0)

    cmpt120image.show_image(canvas, "Distribute test")

def draw_line(img, row):
    for col in range(len(img[0])):
        img[row][col] = [0, 0, 0]

def test_different_size():
    canvas = get_gray_image(WIDTH, HEIGHT)
    col = 0

    # Get 3 sizes of images:
    img = cmpt120image.get_image(IMG2_PATH)
    img_1 = draw.minify(img)
    img_2 = draw.minify(img_1)
    images = [img, img_1, img_2]
    
    for i in range(len(images)):
        row = 200 * i
        col = 0
        img = images[i]

        # Show image
        draw.draw_item(canvas, img, row, col)
        col += 100

        # Recolour and show
        rc_img = draw.recolor_image(img, [0, 155, 128])
        draw.draw_item(canvas, rc_img, row, col)
        col += 100

        # Mirror and show
        mirror_img = draw.mirror(img)
        draw.draw_item(canvas, mirror_img, row, col)
        col += 100

        # Show image (ensure original unchanged)
        draw.draw_item(canvas, img, row, col)
        col += 100

        # Distribute
        section_height = 100
        section_width = len(canvas[0])
        section_canvas = get_gray_image(section_width, section_height)
        draw.distribute_items(section_canvas, img, 5)
        draw.draw_item(canvas, section_canvas, row + 90, 0)

        draw_line(canvas, row + 190)

    
    # Show canvas
    cmpt120image.show_image(canvas, "Test Different Sizes")


def main():
    # Position window on the left of the screen:
    x = 100
    y = 45
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

    # Work around for MacOS
    # On MacOS, it seems that the first time one calls to display an image
    # that nothing is displayed. So, we'll start by displaying the window with
    # nothing in it (a couple times!) to get past MacOS's "feature"
    canvas = get_gray_image(WIDTH, HEIGHT)
    cmpt120image.show_image(canvas, "Tests will appear here!")
    cmpt120image.show_image(canvas, "Tests will appear here!")


    # Run main menu
    while True:
        print()
        print("Which function would you like to test?")
        print("1. draw_item(canvas, img, row, col)")
        print("2. recolor_image(img, color)")
        print("3. minify(img)")
        print("4. mirror(img)")
        print("5. distribute_items(canvas, img, n)")
        print("6. Test different sizes")
        choice_text = read_input_with_screen("(Enter to exit) : ")
        print(choice_text)
        
        if len(choice_text.strip()) == 0:
            break
        
        choice = int(choice_text)
        if choice == 1:
            test_draw_item()
        elif choice == 2:
            test_recolor_image()
        elif choice == 3:
            test_minify()
        elif choice == 4:
            test_mirror()
        elif choice == 5:
            test_distribute_items()
        elif choice == 6:
            test_different_size()

    print("Have a great day!")

main()