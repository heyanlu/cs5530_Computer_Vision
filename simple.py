from simpleimage import SimpleImage

def darker(image): 
    for pixel in image: 
        pixel.red = pixel.red // 2
        pixel.green = pixel.green // 2
        pixel.blue = pixel.blue // 2

def red_channel(image): 
    for pixel in image: 
        pixel.green = 0
        pixel.blue = 0
    return image     


def right_half_darker(image): 
    for pixel in image: 
        if pixel.x > image.width // 2:
            pixel.red = pixel.red // 2
            pixel.green = pixel.green // 2
            pixel.blue = pixel.blue // 2
    return image

def grayscale(image):
    for pixel in image:
        intensity = (pixel.red + pixel.green + pixel.blue) // 3
        pixel.red = intensity
        pixel.green = intensity
        pixel.blue = intensity
    return image

def main(): 
    filename = 'icon.jpg'  
    my_image = SimpleImage(filename)    
    # red_channel(my_image)
    # right_half_darker(my_image)
    grayscale(my_image)
    my_image.show()


if __name__ == "__main__":
    main()