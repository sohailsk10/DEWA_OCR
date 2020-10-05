import cv2
import pytesseract
import csv
import os
# image_name = '68.jpg'
# pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# img = cv2.imread(image_name)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
# x=2524
# y=1997
# h=24+900
# w=110+70
#
# crop_img = img[y:y+h, x:x+w]
# # crop_img = img[27:27+27,372:372+228]
# cv2.imshow("cropped", crop_img)
# cv2.waitKey

SLD_LIST = ["CHILLER-O1","MCC-CHW","SMDB-CWH","SMDB-2F","CHILLER-02","SMDB-ROOF","SMDB-3F","CHILLER-03","ISO","SPARE","FAHU","LIFT-1","LIFT-5","SPARE","SPARE","SPARE","DB-H.C",
            "SW.POOL","SAUNA","STEAM","JACUZZI","DB-REST","DB-ADMIN","DB-FF","DB-2F","DB-5F","DB-8F","DB-11F","DB-14F","LIFT-3","LIFT-6","LIFT-2","DB-KIT","COLD.STORAGE-2",
            "COLD.STORAGE-1","COLD.STORAGE-3","FAHU-KIT","DB-ROOF","ROOF","SMDB-LIFT","LPG","EXF-P1-01", "EXF-P1-02", "EXF-P1-03", "EXF-P1-04", "EXF-P2-01_", "EXF-P2-02",
            "EXF-P2-03", "EXF-P2-04","EXF-P3-01", "EXF-P3-02", "EXF-P3-03", "EXF-P3-04","EXF-P4-01", "EXF-P4-02", "EXF-P4-03", "EXF-P4-04","EXF-P5-01_", "EXF-P5-02", "EXF-P5-03",
            "EXF-P5-04","SPF-2","SPF-1","SEF","LPF","TXF+1","TXF-2","MKF-1","MKF-2","KEF","BOOSTER","GSM-02","GSM-01","TR.PUMP","SMDB-UPS","JOCKEY","EDB-GF","LIFT-4","EDB-P1","EDB-P2",
            "EDB-P3","EDB-P4","EDB-P5","EDB-FF","EDB-2F","EDB-5F","EDB-8F","EDB-11F","EDB-14F","EDB-HC","DB-SPV","ESMDB-ROOF","ESMDB-P1","ESMDB-P4",
            "DB-RET-1","DB-RET-2","DB-GF","DB-LAU","DB-P1","DB-P2","DB-P3","DB-P4","DB-P5","DB-FAC","DBFL-","DBST-2","DBST-3","DBST-4","DBST-5","DBST-6","DBST-7","DBFL-8",
            "DBST-9","DBST-10","DBST-11","DBST-12","DBST-13","DBST-14","DBST-15","DBST-16","DBFL-17","CWH-1","CWH-2","CWH-3(STD","PRESS.PUMP","CHEM.DOSE","DBFL-9","DBST-","DB",
            "DBST-19","DBEFL-",""]
IMAGE_NAME = "68.jpg"
if not os.path.exists(IMAGE_NAME.split('.')[0]):
    os.mkdir(IMAGE_NAME.split('.')[0])
CSV_FOLDER = "csv\\"+ IMAGE_NAME.split(".")[0] + ".csv"
img = cv2.imread(IMAGE_NAME)
with open(CSV_FOLDER, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        if row != []:
            row = row[0].split()
            if len(row)>11:
                for index, word in enumerate(SLD_LIST):
                    if word == row[11]:
                        LEFT = int(row[6])
                        TOP = int(row[7])
                        WIDTH = int(row[8])
                        HEIGHT = int(row[9])
                        crop_img = img[TOP:TOP+(HEIGHT+900), LEFT-30:LEFT+(WIDTH+120)]
                        # crop_img = img[27:27+27,372:372+228]
                        cv2.imshow("cropped", crop_img)
                        cv2.waitKey(0)
                        cv2.imwrite(IMAGE_NAME.split('.')[0]+'\\'+ word + str(index)+'.jpg',crop_img)
                        print(LEFT,TOP,WIDTH,HEIGHT)



# 2 5 1 3 	 3 7 2 	 2 2 8 	 2 7
#
# L              T      W       H

