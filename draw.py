# TODO: Your header

import cmpt120image

def recolor_image(img, color):
    height = len(img)
    width = len(img[0])
    new_img = cmpt120image.get_black_image(width, height)
    for row in range(height):
        for col in range(width):
            if any(value < 240 for value in img[row][col]):
                new_img[row][col] = color
            else:
                new_img[row][col] = img[row][col]
    return new_img

def minify(img):
    height = len(img)
    width = len(img[0])
    new_height = height // 2
    new_width = width // 2
    new_img = cmpt120image.get_black_image(new_width, new_height)
    
    for row in range(new_height):
        for col in range(new_width):
            r, g, b = 0, 0, 0
            for i in range(2):
                for j in range(2):
                    r += img[row * 2 + i][col * 2 + j][0]
                    g += img[row * 2 + i][col * 2 + j][1]
                    b += img[row * 2 + i][col * 2 + j][2]
            new_img[row][col] = [r // 4, g // 4, b // 4]
    return new_img

  
def mirror(img):
    height = len(img)
    width = len(img[0])
    new_img = cmpt120image.get_black_image(width, height)
    
    for row in range(height):
        for col in range(width):
            new_img[row][col] = img[row][width - col - 1]
    return new_img

  
def draw_item(canvas, img, row, col):
    for i in range(len(img)):
        for j in range(len(img[0])):
            if any(value < 240 for value in img[i][j]):
                canvas[row + i][col + j] = img[i][j]

  
import random

def distribute_items(canvas, img, n):
    canvas_height = len(canvas)
    canvas_width = len(canvas[0])
    img_height = len(img)
    img_width = len(img[0])
    
    for _ in range(n):
        row = random.randint(0, canvas_height - img_height)
        col = random.randint(0, canvas_width - img_width)
        draw_item(canvas, img, row, col)