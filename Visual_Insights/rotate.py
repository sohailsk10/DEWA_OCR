from glob import glob
import cv2
import pytesseract

for image in glob('fetchedImages\\*.jpg'):
    image = image.split("\\")[-1]
    print('image',image)
    img = cv2.imread("fetchedImages\\" +image)
    # print('img',img)
    img_rotate_90_clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    config = '-l eng --oem 1 --psm 3'

    text = pytesseract.image_to_string(img_rotate_90_clockwise, config=config)
    print(text)

    cv2.imwrite('rotate\\'+ '' + image, img_rotate_90_clockwise)