import cv2
import pytesseract
import csv
import pandas as pd
from glob import glob

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# image_name =  glob('Trial_Images' + os.sep + '*.jpg')
for image in glob('Trial_Images\\*.jpg'):
    image = image.split("\\")[-1]
    print(image)
    img = cv2.imread('Trial_Images\\' +image)
    print(img.shape)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
    pytesseract


##############################################
##### Detecting Words  ######
##############################################
# #[   0          1           2           3           4          5         6       7       8        9        10       11 ]
# #['level', 'page_num', 'block_num', 'par_num', 'line_num', 'word_num', 'left', 'top', 'width', 'height', 'conf', 'text']
    csv_file = "NOC_CSV\\" + image.split(".")[0] + ".csv"
    with open(csv_file, "w+") as file:
        writer = csv.writer(file)
        writer.writerow(['A', 'B', 'C', 'D', 'E','F','G','Height', 'J','K','I','Text'])
        text = []
        boxes = pytesseract.image_to_data(img)
        for a,b in enumerate(boxes.splitlines()):
        # print(b)
            if a!=0:
                # print(b)
                b = b.split()
                # print(b)
                writer.writerow(b)
                if len(b)==12:
                    x,y,w = int(b[6]),int(b[7]),int(b[8])
                    h = int(b[9])
                # print(list)
                    cv2.putText(img,b[11],(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)
                    temp = [x,y,w,h]
                    z = [temp[1], temp[3], b[11]]
                    text.append(z)
                    cv2.rectangle(img, (x,y), (x+w, y+h), (50, 50, 255), 2)

    df = pd.read_csv(csv_file, encoding="ISO-8859-1", engine='python')
    # print(df)
    df = df.dropna()

    # concatenate the string
    df['Text'] = df.groupby(['Height'])['Text'].transform(lambda x: ' '.join(x))

    df.drop(columns=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'Height', 'J', 'K', 'I'], inplace=True)

    # df.drop(columns=[', '', '', '', '','','','Height', '','', ''], inplace=True)

    # drop duplicate data
    df = df.drop_duplicates('Text')
    # output_dir = 'converted_csv'
    # conv_csv_filename = output_dir + os.sep + "csv\\" + file_name[:-4] + ".csv"
    csv_output_file = "OUTPUT_CROSS_SECTIONS\\" + image.split(".")[0] + ".csv"
    df = df.to_csv(csv_output_file, index=False)

    # show the dataframe
    # print(df)



    # y_pre = 0
    # h_pre = 0
    #
    # for i in range(len(text)):
    #     y_pre, h_pre = text[i][0], text[i][1]
    #
    #     # print(y_pre, h_pre, text[i], type(text[i]))
    # print(text)

    # img = cv2.resize(img, (1000,800))
    # cv2.imshow('img', img)
    # cv2.waitKey(5)





