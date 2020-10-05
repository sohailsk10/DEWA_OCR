import cv2
import pytesseract
import csv
import os
import pandas as pd

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def image_extract(path, images_dir, csv_dir):
    # fname = os.path.splitext(os.path.basename(path))[0]

    output_dir = path[:-4]
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    image = cv2.imread(path)
    print("Image read[]",image)
    pytesseract

    abcd = output_dir + os.sep + 'images\\' + path[:-4] + '.jpg'
    # image.save(abcd, 'JPEG')
    cv2.imwrite(abcd, img)

    csv_filename = output_dir + os.sep + "csv\\" + path[:-4] + ".csv"
    print(csv_filename)
    # df = pd.read_csv(csv_filename, encoding="ISO-8859-1", engine='python')
    # # print(df)
    # df = df.dropna()
    # # concatenate the string
    # df['t e x t'] = df.groupby(['h e i g h t'])['t e x t'].transform(lambda x: ' '.join(x))
    # df.drop(columns=['l e v e l ', 'p a g e _ n u m', 'b l o c k _ n u m', 'p a r _ n u m', 'l i n e _ n u m', 'w o r d _ n u m', 'l e f t', 't o p', 'w i d t h', 'h e i g h t', 'c o n f'], inplace=True)
    #
    #
    # # drop duplicate data
    # df = df.drop_duplicates('t e x t')
    # df = df.to_csv(csv_filename,"w+", index=False)
    # # show the dataframe
    # print(df)

    with open(csv_filename, "w+") as file:
        writer = csv.writer(file)
        text = []
        boxes = pytesseract.image_to_data(img)
        for a, b in enumerate(boxes.splitlines()):
            print(b)
            if a != 0:
                print(b)
                b = b.split()
                print(b)

                writer.writerow(b)
                # print("------", b[10])
                if len(b) == 12:
                    x, y, w = int(b[6]), int(b[7]), int(b[8])
                    h = int(b[9])
                    cv2.putText(img, b[11], (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)
                    temp = [x, y, w, h]
                    z = [temp[1], temp[3], b[11]]
                    text.append(z)
                    cv2.rectangle(img, (x, y), (x + w, y + h), (50, 50, 255), 2)

    # with open(csv_filename, "w+") as file:
    #     writer = csv.writer(file, delimiter=' ')
    #     boxes = pytesseract.image_to_data(img)
    #     print("Boxes ",boxes)
    #     for a, b in enumerate(boxes.splitlines()):
    #         print(b)
    #         writer.writerow(b)
    #         if a != 0:
    #             b = b.split()
    #             if len(b) == 12:
    #                 x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
    #                 # print(x,y,w,h)
    #                 cv2.putText(img, b[11], (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 1)
    #                 # print("B[11]", b[11])
    #                 cv2.rectangle(img, (x, y), (x + w, y + h), (50, 50, 255), 2)

    cv2.imshow('img', img)
    cv2.waitKey(0)

if __name__ == '__main__':
    path = 'layout.jpg'
    folder_name = path.split(".")[0]
    csv_dir = folder_name + os.sep + "csv"
    image_dir = folder_name + os.sep + "images"
    os.makedirs(csv_dir)
    os.makedirs(image_dir)
    image_extract(path, image_dir, csv_dir)


