# import cv2 to capture videofeed
import cv2

import numpy as np

# attach camera indexed as 0
camera = cv2.VideoCapture(0)

# setting framewidth and frameheight as 640 X 480
camera.set(3 , 640)
camera.set(4 , 480)

# loading the mountain image
mountain = cv2.imread('mount everest.jpg')

# resizing the mountain image as 640 X 480
image = mountain.resize((640, 480))

while True:

    # read a frame from the attached camera
    status , frame = camera.read()

    # if we got the frame successfully
    if status:

        # flip it
        frame = cv2.flip(frame , 1)

        # converting the image to RGB for easy processing
        frame_rgb = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)

        # creating thresholds
        lower_bound = np.array([])
        upper_bound = np.array([])

        # thresholding image
        thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
        # inverting the mask
        def invert_mask(mask):
            inv_mask = cv2.bitwise_not(mask)
            return inv_mask
        # bitwise and operation to extract foreground / person
        def extract_foreground(image, mask):
            foreground = cv2.bitwise_and(image, image, mask=mask)
            return foreground
        # final image
        final_image = cv2.bitwise_and(image,foreground)
        # show it
        cv2.imshow('frame' , frame)

        # wait of 1ms before displaying another frame
        code = cv2.waitKey(1)
        if code  ==  32:
            break

# release the camera and close all opened windows
camera.release()
cv2.destroyAllWindows()
