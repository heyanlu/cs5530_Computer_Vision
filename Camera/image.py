import cv2 

def roiImage(image): 
    if image is None: 
        print("Image cannot found")
        exit()

    startY, endY = 60, 160
    startX, endX = 320, 420 

    roi = image[startY:endY, startX:endX]

    cv2.imshow('ROI', roi)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def resizeImage(image): 
    resizedImage = cv2.resize(image, (300, 300))

    cv2.imshow('Resized Image', resizedImage)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def rotateImage(image): 
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)

    M = cv2.getRotationMatrix2D(center, 45, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))

    cv2.imshow('Rotated Image', rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def smoothImage(image): 
    blurred = cv2.GaussianBlur(image, (11, 11), 0)

    cv2.imshow('Blurred Image', blurred)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def edgeDetection(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edge = cv2.Canny(gray, 30, 150)

    cv2.imshow('Edge Detection', edge)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def thresholdImage(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    cv2.imshow('Threshold Image', threshold)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def detectContours(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    print(f'{len(contours)} contours found')

    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

    cv2.imshow('Contours', image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main(): 
    image = cv2.imread('Flower.jpg')
    thresholdImage(image)


if __name__ == "__main__": 
    main()