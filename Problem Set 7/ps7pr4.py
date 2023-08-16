#
# ps7pr4.py  (Problem Set 7, Problem 4)
#
# Images as 2-D lists  
#
# Computer Science 111
# 

from hmcpng import *

def create_uniform_image(height, width, pixel):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels have the RGB values
        given by pixel
        inputs: height and width are non-negative integers
                pixel is a 1-D list of RBG values of the form [R,G,B],
                     where each element is an integer between 0 and 255.
    """
    pixels = []

    for r in range(height):
        row = [pixel] * width
        pixels += [row]

    return pixels

def blank_image(height, width):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels are green.
        inputs: height and width are non-negative integers
    """
    all_green = create_uniform_image(height, width, [0, 255, 0])
    return all_green

def brightness(pixel):
    """ takes a pixel (an [R, G, B] list) and returns a value
        between 0 and 255 that represents the brightness of that pixel.
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    return (21*red + 72*green + 7*blue) // 100

## put your functions below

def grayscale(pixels):
    """ creates and returns a new 2D list of pixels for the grayscale 
        version of the original image
    """
    new_pixel = blank_image(len(pixels), len(pixels[0]))
    for r in range(len(pixels)):
        for c in range(len(pixels[0])):
            bright = brightness(pixels[r][c])
            new_pixel[r][c] = [bright, bright, bright]
    return new_pixel

def mirror_vert(pixels):
    """ creates and returns a new 2D list of pixels for which the pixels
        of the orignial image are mirrored vertically.
    """
    mirrored = blank_image(len(pixels), len(pixels[0]))
    for r in range(len(pixels)):
        for c in range(len(pixels[0])):
            if len(pixels) % 2 == 0:
                if r < (len(pixels) / 2):
                    mirrored[r][c] = pixels[r][c]
                else:
                    mirrored[r][c] = pixels[len(pixels) - r - 1][c]
            else:
                if r <= (len(pixels) / 2):
                    mirrored[r][c] = pixels[r][c]
                else:
                    mirrored[r][c] = pixels[len(pixels)-r-1][c]
    return mirrored

def flip_horiz(pixels):
    """ creates and returns a new 2D list of pixels for an image in whiche
        the pixels have been flipped horizontally, 
        meaning the left side and the right side switched
    """
    flipped = blank_image(len(pixels), len(pixels[0]))
    for r in range(len(pixels)):
        for c in range(len(pixels[0])):
            flipped[r][c] = pixels[r][len(pixels[0]) - c -1]
    return flipped

def reduce(pixels):
    """ creates and returns a new 2D list of pixels for an image
        that is half the size of the orignial image
    """
    reduced = blank_image(len(pixels)//2, len(pixels[0])//2)
    for r in range(len(pixels) // 2):
        for c in range(len(pixels[0]) // 2):
            reduced[r][c] = pixels[r *2][c * 2]
    return reduced

def transpose(pixels):
    """ creates and returns a new 2D list of pixels for an image in which
        the pixels have been transposed from r * c grid to a c * r grid
    """
    rotated = blank_image(len(pixels[0]), len(pixels))
    for r in range(len(pixels[0])):
        for c in range(len(pixels)):
            rotated[r][c] = pixels[c][r]
    return rotated