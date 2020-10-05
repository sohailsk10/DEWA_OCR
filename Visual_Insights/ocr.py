import json
import requests
import cv2
import os
import glob
import csv

from coverage import config
from pytesseract import pytesseract
from PIL import Image, ImageEnhance

fetchDir = "fetchedImages"
# list= ['project_title','contract_number',
# 'substation_name',
# 'equipments',
# 'drawing_id',
# 'drawing_title',
# 'drawing_number',
# 'standard_drawing','decleration',
# 'authorizes_signature',
# 'description_change',
# 'place_date'
# ]
# list_1 = [
#     'project_title','contract_number',
# 'substation_name',
# 'drawing_id',
# 'drawing_title',
# 'drawing_number',
# 'standard_drawing','decleration',
# 'authorizes_signature',
# 'description_change',
# 'place_date'
# ]
#
# label_list = []
#
def area_crop(file_name):
    if not len(os.listdir(fetchDir)) == 0:
        for file in glob.glob(fetchDir + os.sep + "*.jpg"):
            # print(file)
            os.remove(file)
            print("[INFO] removing " + file + "from fetched Images directory.")

    requests.packages.urllib3.disable_warnings()
    # api_url_label = "https://10.150.20.61/powerai-vision/api/dlapis/92c84cad-3ab9-448a-bcad-2e208d1209aa"
    # api_url_label = "https://10.150.20.61/powerai-vision/api/dlapis/34215727-7346-4914-bafa-a5b0ec2a08c3"
    # api_url_label = "https://195.229.90.114/visual-insights/api/dlapis/59ecc426-a8c6-4501-a3aa-1aa93764ac89"
    # api_url_label_box = "https://195.229.90.114/visual-insights/api/dlapis/042c4207-252d-4ee6-8335-c253ef216a19"
    # api_url_label_text_sha = "https://195.229.90.114/visual-insights/api/dlapis/f4d7ae20-337d-4382-95b9-3b4290710053"
    # api_url_label_text = "https://195.229.90.114/visual-insights/api/dlapis/cfa0a430-03c4-49e8-a68f-81d2095a572b"
    # api_url_label_text_zah = "https://195.229.90.114/visual-insights/api/dlapis/a38758a3-9060-4076-9869-cb23df6b8866"
    # api_url_label_whole = "https://195.229.90.114/visual-insights/api/dlapis/acfc8f35-ab15-4387-862d-c6bc190e53b6"
    # api_url_label_ocr = "https://195.229.90.114/visual-insights/api/dlapis/88a8c7d3-d7bc-4918-b2d4-da6eb3876386"
    # api_url_label_ocr_3 = "https://195.229.90.114/visual-insights/api/dlapis/cf0ee1f8-612d-4192-a2c4-7d1cdc0cd222"
    # api_url_label_ocr_3 = "https://195.229.90.114/visual-insights/api/dlapis/88a8c7d3-d7bc-4918-b2d4-da6eb3876386"
    # api_url_label_ocr_3 = "https://195.229.90.114/visual-insights/api/dlapis/2ce09849-52ff-4a7a-a236-d4d338ca6837"
    api_url_label_ocr_3 = "https://195.229.90.114/visual-insights/api/dlapis/912ff901-0e1c-4193-b424-e14c8b02faeb"
    with open(file_name, 'rb') as f:
        s = requests.Session()
        r = s.post(api_url_label_ocr_3, files={'files': (file_name, f), 'confthre': '0.90'}, verify=False, timeout=10)
        data = json.loads(r.text)
        testdata = data["classified"]
        print(testdata)
        image = cv2.imread(file_name)

        count = 0
        for counter in range((len(testdata))):
            minX = int(testdata[counter].get('xmin'))

            minY = int(testdata[counter].get('ymin'))

            maxX = int(testdata[counter].get('xmax'))
            maxY = int(testdata[counter].get('ymax'))
            label = testdata[counter].get('label')
            # print("label", label)
            # [label_list.append(label) for label in testdata if label not in label_list]
            # label_list.append(label)
        #     for i in list:
        #         if i not in label_list:
        #             label_list.append(i)
        # print("label_list:", len(label_list))
        # print("list", len(list))
        # print("list_1", len(list_1))
        # # str(label).sort()
        # # str(label_list).sort()
        #     # print(label, minX, minY, maxX, maxY)
        # if str(label_list) == str(list):
        #     print("this is decleration form")
        # # elif str(label_list) == str(list_1):

        # #     print("this is a  template decleration form")
        # else:
        #     print("this is not a decleration form")


            # croppedImage = image[maxY:maxY + 50, minX - 40:maxX + 50]
            # croppedImage = image[minX - 100:maxX + 100, minY - 200:maxY + 200]
            # croppedImage = image[minY - 130:maxY + 190, minX - 150:maxX + 160]
            # croppedImage = image[minY - 130:maxY+170, minX-70:maxX+70]
            # croppedImage = image[minY-10:maxY+490, minX:maxX+90]
            # croppedImage = image[minY:maxY, minX :maxX]
            # croppedImage = image[minY-200:maxY + 850, minX-83 :maxX+80]
            # croppedImage = image[minY-70:maxY+800, minX-70:maxX+120]
            croppedImage = image[minY:maxY+800, minX-7:maxX+100]
            filename = "fetchedImages" + os.sep + image_name.split("\\")[-1]
            # filename.resize((800, 800))
            # print('----',filename)
            cv2.imwrite(filename, croppedImage)
            config = '-l eng --oem 1 --psm 3'


            text = pytesseract.image_to_string(filename, config=config)
            # print('output', text)
            img_rotate_90_clockwise = cv2.rotate(croppedImage, cv2.ROTATE_90_CLOCKWISE)
            text_rotate = pytesseract.image_to_string(img_rotate_90_clockwise, config=config)
            # print("Text_Rotate",text_rotate)
            print("CSV\\"+filename.split('\\')[-1][:-4]+'.csv')

            with open("CSV\\"+filename.split('\\')[-1][:-4]+'.csv',"w+") as file:
                writer =  csv.writer(file)
                writer.writerow([text])
                writer.writerow([text_rotate])


            # f = open('horizontal.txt', 'w')
            # f.write(text)
            # f.close()
            cv2.imshow(label, croppedImage)
            cv2.waitKey(0)

for image_name  in glob.glob(r'E:\PycharmProjects\TextDetection\68\*.jpg'):
    var = cv2.imread(image_name)
    height, width = var.shape[:2]
    print(height, width)
    cv2.imshow("before", var)
    cv2.waitKey(0)
    area_crop(image_name)

# file = cv2.imread('fetchedImages\\0box.jpg')
# print(file)

# # img_resize = cv2.resize(file, (500, 200))
# enhancer = ImageEnhance.Sharpness(file)
# enhanced_im = enhancer.enhance(10.0)
# enhanced_im.save('enhanced.jpg')
# cv2.imshow('img_resize', enhanced_im)
# cv2.waitKey(0)
# img_resize.save('resize.jpg')
# print('image', img_resize)
# print('filename', file)
#



# from PIL import Image, ImageEnhance
# im = Image.open("0box.jpg")
# enhancer = ImageEnhance.Sharpness(im)
# enhanced_im = enhancer.enhance(10.0)
# enhanced_im.save("enhanced.sample3.png")