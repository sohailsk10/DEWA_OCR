from pdf2image import convert_from_path
from glob import glob
import os

filename = glob('Hotel_Apartment' + os.sep + '*.pdf')
print(filename)
# print(len(filename))
i = 1
for file in filename:
    images = convert_from_path(file)
    print(images)

    for image in images:
        print(image)
        image.save('Hotel_Apartment_Images\\' + str(i) + '.jpg', 'JPEG')
        i = i + 1
        print(i)
