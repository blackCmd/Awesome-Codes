#코코에서 원하는 클래스만 뽑아내기
#cocoapi 설치는 여기 참고
#https://www.programmersought.com/article/64914737579/

from pycocotools.coco import COCO
import requests

# instantiate COCO specifying the annotations json path
coco = COCO('C:/Users/J5330-3/Pictures/annotations2017/instances_train2017.json')
# Specify a list of category names of interest
catIds = coco.getCatIds(catNms=['car'])
# Get the corresponding image ids and images using loadImgs
imgIds = coco.getImgIds(catIds=catIds)
images = coco.loadImgs(imgIds)

# Save the images into a local folder
for im in images:
    # img_data = requests.get(im['coco_url']).content
    img_data = requests.get(im['coco_url']).content
    with open('C:/Users/J5330-3/J5330-3의 공유폴더/코코에서뽑아내자/2,3-car,carNumberPlate/' + im['file_name'], 'wb') as handler:
        handler.write(img_data)


#코코에서 원하는 데이터만 읽어오는 코드???
# import pycocotools.coco as coco
# import numpy as np
# import io
#
# filterClasses = ['person', 'dog']
#
# # Fetch class IDs only corresponding to the filterClasses
# catIds = coco.getCatIds(catNms=filterClasses)
# # Get all images containing the above Category IDs
# imgIds = coco.getImgIds(catIds=catIds)
# print("Number of images containing all the  classes:", len(imgIds))
#
# # load and display a random image
# img = coco.loadImgs(imgIds[np.random.randint(0,len(imgIds))])[0]
# I = io.imread('{}/images/{}/{}'.format(dataDir, dataType, img['file_name']))/255.0
