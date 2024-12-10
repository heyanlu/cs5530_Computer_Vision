import cv2
import numpy as np

def greenscreen(main_filename, background_filename):
    foreground = cv2.imread(main_filename)
    background = cv2.imread(background_filename)

    background = cv2.resize(background, (foreground.shape[1], foreground.shape[0]))  
    
    hsv = cv2.cvtColor(foreground, cv2.COLOR_BGR2HSV)
    
    # get green
    lower_green = np.array([35, 50, 50])
    upper_green = np.array([85, 255, 255])
    
    mask = cv2.inRange(hsv, lower_green, upper_green)
    mask_inv = cv2.bitwise_not(mask)
    
    foreground_no_green = cv2.bitwise_and(foreground, foreground, mask=mask_inv)
    background_only = cv2.bitwise_and(background, background, mask=mask)
    
    result = cv2.add(foreground_no_green, background_only)
    
    return result

def main():
    main_image_file = 'main.jpg'
    background_image_file = 'background.jpg'
    result = greenscreen(main_image_file, background_image_file)
    cv2.imshow('Result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
