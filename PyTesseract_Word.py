import cv2
import pytesseract
import csv
import numpy as np
from PIL import ImageGrab
import time


image_name = '74.jpg'
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


img = cv2.imread(image_name)
# img = 'Proposed Layout superimposed with DEWA Water services-1.jpg'
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
pytesseract


csv_filename = "csv\\"+ image_name.split(".")[0] +".csv"
print(csv_filename)

with open(csv_filename, "w+") as file:
    writer = csv.writer(file,  delimiter=' ', quotechar='|',  quoting=csv.QUOTE_MINIMAL)
    boxes = pytesseract.image_to_data(img)
    for a,b in enumerate(boxes.splitlines()):
        print("A",a)
        b = b.split()
        print(b)
        writer.writerow(b)
        if a!=0:
            # b = b.split()
            if len(b)==12:
                x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
                # print(x,y,w,h)
                cv2.putText(img,b[11],(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),1)
                print("B[11]",b[11])
                cv2.rectangle(img, (x,y), (x+w, y+h), (50, 50, 255), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
