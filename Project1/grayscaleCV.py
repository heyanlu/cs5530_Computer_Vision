import cv2

def grayscale_image(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('grayscale_image.jpg', gray_image)
    return gray_image

def main(): 
    input_image = 'icon.jpg'
    output_image = grayscale_image(input_image)
    
    cv2.imshow('Grayscale Image', output_image)
    
    cv2.waitKey(0)  
    
    cv2.destroyAllWindows()

if __name__ == "__main__": 
    main()
