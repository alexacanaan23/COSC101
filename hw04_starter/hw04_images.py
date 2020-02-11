# ----------------------------------------------------------
# --------              HW 4: Part 3               ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Please answer these questions after you have completed this
# program
# ----------------------------------------------------------
# Name: Alexa Canaan
# Time spent on part 3: 3.5 hours
# Collaborators and sources: lab hours 3/7, 3/8
#   (List any collaborators or sources here.)
# ----------------------------------------------------------


import cImage as image


# -------------------------------
# EXAMPLE FUNCTION: RED FILTER
# -------------------------------
# Here is an example of a transformation function. Note that this
# function is called from the main() function below.

def red_filter(img):
    """ (Image object) -> Image object
    Returns a copy of img where the blue and green have been filtered
    out and only red remains.
    """
    red_only_img = img.copy()               # create copy to manipulate
    w = img.getWidth()
    h = img.getHeight()
    for x in range(w):                      # iterate through all (x, y) pixel pairs
        for y in range(h):
            pixel = img.getPixel(x, y)
            red = pixel.getRed()            # get original red value
            redPixel = image.Pixel(red, 0, 0)
            red_only_img.setPixel(x, y, redPixel) # replace pixel
    return red_only_img                     # return filtered image


#--------------------------------
# BEGIN GRADED FUNCTIONS
#--------------------------------
# Fill in docstrings and code for all of the functions required by the
# homework assignment. For your convenience, each of the function
# definitions have been started for you. However, note that all of the
# functions are currently defined to take zero parameters and return
# None. You will need to change this for (at least) some of these
# functions.

def leave_color(img):
    ''' (Image object) -> Image object
    Returns a copy of img where all non-red pixels are set to grayscale
    '''
    leavered = img.copy()           #create copy to manipulate
    w = img.getWidth()
    h = img.getHeight()
    for x in range(w):
        for y in range(h):          #iterate through all (x,y) pixel pairs
            p = img.getPixel(x, y)
            r = p.getRed()
            g = p.getGreen()
            b = p.getBlue()         #get all color values
            grayscale = int((r + g + b)/3)      #average the color values to grayscale
            if r <= 125 or g > 125 or b > 125:  #conditions that make a pixel not red
                graypixel = image.Pixel(grayscale, grayscale, grayscale) #set pixel to grayscale
                leavered.setPixel(x, y, graypixel)  #replace pixel
    return leavered                 #gray and red image

def horizontal_mirror(img):
    ''' (Image object) -> Image object
    Returns an image where it is mirrored horizontally
    so the content on the left is mirrored on the right
    '''
    mirror_img = img.copy()         #create copy to manipulate
    w = img.getWidth()
    h = img.getHeight()
    for y in range(h):              
        pixelx = 0
        for x in range(w-1, int((w+1)/2), -1):  #iterates through all y values on right half of image
            p = img.getPixel(pixelx, y)
            mirror_img.setPixel(x, y, p)        #set pixel color to its mirror opposite on the left
            pixelx += 1             #makes sure left pixel translates to the right and not right to left
    return mirror_img               #return mirrored image
 
def blur(img):
    ''' (Image object) -> Image object
    Returns a blurred image by averaging each pixel with its eight surrounding pixels
    Each color channel is averaged individually
    '''

    blur_img = img.copy()           #create a copy to manipulate
    w = img.getWidth()
    h = img.getHeight()
    for x in range(1, w-1):         #iterates over inner pixels
        for y in range(1, h-1):     #identifies the 8 surrounding pixels
            p = img.getPixel(x, y)
            p1 = img.getPixel(x - 1, y + 1)
            p2 = img.getPixel(x, y + 1)
            p3 = img.getPixel(x + 1, y + 1)
            p4 = img.getPixel(x + 1, y)
            p5 = img.getPixel(x + 1, y - 1)
            p6 = img.getPixel(x, y - 1)
            p7 = img.getPixel(x - 1, y - 1)
            p8 = img.getPixel(x - 1, y)
            list1 = [p1, p2, p3, p4, p5, p6, p7, p8]
            r = 0
            g = 0
            b = 0
            for ps in list1:        #averages the color values of the surrounding 8 pixels
                red = ps.getRed()
                r += red
                green = ps.getGreen()
                g += green
                blue = ps.getBlue()
                b += blue
            ravg = int(r/len(list1))
            gavg = int(g/len(list1))
            bavg = int(b/len(list1))
            setpixel = image.Pixel(ravg, gavg, bavg)    
            blur_img.setPixel(x, y, setpixel) #sets the selected pixel to the average color values
            
    for x in range(0, 1):
        for y in range(0, 1): #iterates on bottom left corner pixel
            p = img.getPixel(x, y)  #identifies the 3 surrounding pixels
            p1 = img.getPixel(x, y + 1)
            p2 = img.getPixel(x + 1, y + 1)
            p3 = img.getPixel(x + 1, y)
            list1 = [p1, p2, p3]
            r = 0
            g = 0
            b = 0
            for ps in list1:    #averages the color values of the 3 surrounding pixels
                red = ps.getRed()
                r += red
                green = ps.getGreen()
                g += green
                blue = ps.getBlue()
                b += blue
            ravg = int(r/3)
            gavg = int(g/3)
            bavg = int(b/3)
            setpixel = image.Pixel(ravg, gavg, bavg)
            blur_img.setPixel(x, y, setpixel)   #sets the selected pixel to the average color values

    for x in range(0):
        for y in range(h-1, h): #iterates on top left corner pixel
            p = img.getPixel(x, y)  #identifies the 3 surrounding pixels
            p1 = img.getPixel(x + 1, y)
            p2 = img.getPixel(x + 1, y - 1)
            p3 = img.getPixel(x, y - 1)
            list1 = [p1, p2, p3]
            r = 0
            g = 0
            b = 0
            for ps in list1:    #averages the color values of the 3 surrounding pixels
                red = ps.getRed()
                r += red
                green = ps.getGreen()
                g += green
                blue = ps.getBlue()
                b += blue
            ravg = int(r/3)
            gavg = int(g/3)
            bavg = int(b/3)
            setpixel = image.Pixel(ravg, gavg, bavg)
            blur_img.setPixel(x, y, setpixel)   #sets the selected pixel to the average color values

    for x in range(w-1, w): 
        for y in range(h-1, h): #iterates over top right corner pixel
            p = img.getPixel(x, y) #identifies the 3 surrounding pixels
            p1 = img.getPixel(x - 1, y)
            p2 = img.getPixel(x - 1, y - 1)
            p3 = img.getPixel(x, y - 1)
            list1 = [p1, p2, p3]
            r = 0
            g = 0
            b = 0
            for ps in list1:    #averages the color values of the 3 surrounding pixels
                red = ps.getRed()
                r += red
                green = ps.getGreen()
                g += green
                blue = ps.getBlue()
                b += blue
            ravg = int(r/3)
            gavg = int(g/3)
            bavg = int(b/3)
            setpixel = image.Pixel(ravg, gavg, bavg)
            blur_img.setPixel(x, y, setpixel)   #sets the seleced pixel to the average color values

    for x in range(w-1, w): 
        for y in range(0): #iterates over bottom right corner pixel
            p = img.getPixel(x, y)  #identifies the 3 surrounding pixels
            p1 = img.getPixel(x, y + 1)
            p2 = img.getPixel(x - 1, y + 1)
            p3 = img.getPixel(x - 1, y)
            list1 = [p1, p2, p3]
            r = 0
            g = 0
            b = 0
            for ps in list1:    #averages the color values of the 3 surrounding pixels
                red = ps.getRed()
                r += red
                green = ps.getGreen()
                g += green
                blue = ps.getBlue()
                b += blue
            ravg = int(r/3)
            gavg = int(g/3)
            bavg = int(b/3)
            setpixel = image.Pixel(ravg, gavg, bavg)
            blur_img.setPixel(x, y, setpixel)   #sets the selected pixel to the average color values

    for x in range(0, 1): 
        for y in range(1, h-1): #iterates over left side pixels except corners
            p = img.getPixel(x, y)  #identifies the 5 surrounding pixels
            p1 = img.getPixel(x, y + 1)
            p2 = img.getPixel(x + 1, y + 1)
            p3 = img.getPixel(x + 1, y)
            p4 = img.getPixel(x + 1, y - 1)
            p5 = img.getPixel(x, y - 1)
            list1 = [p1, p2, p3, p4, p5]
            r = 0
            g = 0
            b = 0
            for ps in list1:    #averages the colors values of the 5 surrounding pixels
                red = ps.getRed()
                r += red
                green = ps.getGreen()
                g += green
                blue = ps.getBlue()
                b += blue
            ravg = int(r/5)
            gavg = int(g/5)
            bavg = int(b/5)
            setpixel = image.Pixel(ravg, gavg, bavg)
            blur_img.setPixel(x, y, setpixel)   #sets the selected pixel to the average color values

       

    for x in range(1, w-1):
        for y in range(h-1, h): #iterates over top side pixels except corners
            p = img.getPixel(x, y)  #identifies the the 5 surrounding pixels
            p1 = img.getPixel(x - 1, y)
            p2 = img.getPixel(x - 1, y - 1)
            p3 = img.getPixel(x, y - 1)
            p4 = img.getPixel(x + 1, y - 1)
            p5 = img.getPixel(x + 1, y)
            list1 = [p1, p2, p3, p4, p5]
            r = 0
            g = 0
            b = 0
            for ps in list1:    #averages the color values of the 5 surrounding pixels
                red = ps.getRed()
                r += red
                green = ps.getGreen()
                g += green
                blue = ps.getBlue()
                b += blue
            ravg = int(r/5)
            gavg = int(g/5)
            bavg = int(b/5)
            setpixel = image.Pixel(ravg, gavg, bavg)
            blur_img.setPixel(x, y, setpixel)   #sets the selected pixel to the average color values

    for x in range(w-1, w):
        for y in range(1, h-1): #iterates over right side pixels except corners
            p = img.getPixel(x, y)  #identifies the 5 surrounding pixels
            p1 = img.getPixel(x, y + 1)
            p2 = img.getPixel(x - 1, y + 1)
            p3 = img.getPixel(x - 1, y)
            p4 = img.getPixel(x - 1, y - 1)
            p5 = img.getPixel(x, y - 1)
            list1 = [p1, p2, p3, p4, p5]
            r = 0
            g = 0
            b = 0
            for ps in list1:    #averages the color values of the 5 surrounding pixels
                red = ps.getRed()
                r += red
                green = ps.getGreen()
                g += green
                blue = ps.getBlue()
                b += blue
            ravg = int(r/5)
            gavg = int(g/5)
            bavg = int(b/5)
            setpixel = image.Pixel(ravg, gavg, bavg)
            blur_img.setPixel(x, y, setpixel)   #sets the selected pixel to the average color values
            
    for x in range(1, w-1): 
        for y in range(0, 1): #iterates over bottom side pixels except corners
            p = img.getPixel(x, y)  #identifies the 5 surrounding pixels
            p1 = img.getPixel(x - 1, y)
            p2 = img.getPixel(x - 1, y + 1)
            p3 = img.getPixel(x, y + 1)
            p4 = img.getPixel(x + 1, y + 1)
            p5 = img.getPixel(x + 1, y)
            list1 = [p1, p2, p3, p4, p5]
            r = 0
            g = 0
            b = 0
            for ps in list1:    #averages the color values of the 5 surroudning pixels
                red = ps.getRed()
                r += red
                green = ps.getGreen()
                g += green
                blue = ps.getBlue()
                b += blue
            ravg = int(r/5)
            gavg = int(g/5)
            bavg = int(b/5)
            setpixel = image.Pixel(ravg, gavg, bavg)
            blur_img.setPixel(x, y, setpixel)   #sets the selected pixel to the average colors values
           
    return blur_img

def save_image(img, fname):
    ''' (ImageObject, str) -> NoneType
    Save an image to the file fname.
    '''
    img.save(fname)
    return None

def display_image(original_img, transformed_img):
    ''' (Image object, Image object) -> NoneType
    Display an original and transformed image.
    '''
    w = original_img.getWidth()
    h = original_img.getHeight()
    win = image.ImageWin("Original and transformed image", w, h*2)
    original_img.draw(win)
    transformed_img.setPosition(0, h)
    transformed_img.draw(win)
    win.exitonclick()
    return None

#--------------------------------
# BEGIN MAIN FUNCTION
#--------------------------------
# Replace the code below to call all of the transformation functions
# you wrote display and save the results. Your main should call every
# graded function you wrote above. You can test your code using the
# provided grid.gif file or another .gif image of your choosing, as
# long as the image file is in the same directory as this .py file.

def main():
    """ () -> NoneType
    Main Program that load image(s) from file(s) and performs
    transformations to those images as required for HW 04. The images
    are then displayed.
    """
    #Test Gray/Red Color
    for img in ['house.gif', 'grid.gif', 'flowers.gif', 'rose.gif']:
        original_img = image.Image(img)
        red_img = red_filter(original_img)
        display_image(original_img, red_img)


    #Test Leave Color
    for img in ['house.gif', 'grid.gif', 'flowers.gif', 'rose.gif']:
        original_img = image.Image(img)
        leave_color_img = leave_color(original_img)
        display_image(original_img, leave_color_img)

    #Test Horizontal Image
    for img in ['house.gif', 'grid.gif', 'flowers.gif', 'rose.gif']:
        original_img = image.Image(img)
        mirror_img = horizontal_mirror(original_img)
        display_image(original_img, mirror_img)

    #Test Blur
    for img in ['house.gif', 'grid.gif', 'flowers.gif', 'rose.gif']:
        original_img = image.Image(img)
        blur_img = blur(original_img)
        display_image(original_img, blur_img)

# To test your code you will run this program and then enter:
#       >>> main()
# at the shell. Do not include an uncommented call to main() here.
