from PIL import Image

class SimpleImage:
    def __init__(self, filename):
        self.image = Image.open(filename)
        self.pixels = self.image.load()
        self.width, self.height = self.image.size

    def show(self):
        self.image.show()

    def save(self, filename):
        self.image.save(filename)

    def get_pixel(self, x, y):
        r, g, b = self.pixels[x, y]
        return Pixel(self.pixels, x, y)

    def __iter__(self):
        for y in range(self.height):
            for x in range(self.width):
                yield Pixel(self.pixels, x, y)

    def resize(self, width, height):
        self.image = self.image.resize((width, height))
        self.pixels = self.image.load()
        self.width, self.height = self.image.size


class Pixel:
    def __init__(self, pixels, x, y):
        self.pixels = pixels
        self.x = x
        self.y = y

    @property
    def red(self):
        return self.pixels[self.x, self.y][0]

    @red.setter
    def red(self, value):
        r, g, b = self.pixels[self.x, self.y]
        self.pixels[self.x, self.y] = (value, g, b)

    @property
    def green(self):
        return self.pixels[self.x, self.y][1]

    @green.setter
    def green(self, value):
        r, g, b = self.pixels[self.x, self.y]
        self.pixels[self.x, self.y] = (r, value, b)

    @property
    def blue(self):
        return self.pixels[self.x, self.y][2]

    @blue.setter
    def blue(self, value):
        r, g, b = self.pixels[self.x, self.y]
        self.pixels[self.x, self.y] = (r, g, value)


INTENSITY_THRESHOLD = 1.6

def greenscreen(main_filename, background_filename): 
    image = SimpleImage(main_filename)
    background = SimpleImage(background_filename)

    if image.width != background.width or image.height != background.height:
        background.resize(image.width, image.height)

    for pixel in image: 
        average = (pixel.red + pixel.green + pixel.blue) // 3
        if pixel.green >= average * INTENSITY_THRESHOLD: 
            background_pixel = background.get_pixel(pixel.x, pixel.y)
            pixel.red = background_pixel.red
            pixel.green = background_pixel.green
            pixel.blue = background_pixel.blue

    return image

def main():
    main_image_file = './simpleimage/main.jpg'
    background_image_file = './simpleimage/background.jpg'
    result = greenscreen(main_image_file, background_image_file)
    result.show()
    result.save('result.jpg')

if __name__ == "__main__":
    main()
