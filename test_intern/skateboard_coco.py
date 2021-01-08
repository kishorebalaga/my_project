from pycocotools.coco import COCO
import requests

coco = COCO('/home/robert/Desktop/annotations_train/instances_train2017.json')
cats = coco.loadCats(coco.getCatIds())
nms=[cat['name'] for cat in cats]
#print('COCO categories: \n{}\n'.format(' '.join(nms)))

catIds = coco.getCatIds(catNms=['skateboard'])
#print(catIds)
imgIds = coco.getImgIds(catIds=catIds)

images = coco.loadImgs(imgIds)
#print("images: ", images)

img_data = requests.get(images[3]['coco_url']).content

with open('/home/robert/Desktop/test_intern/test_coco/'+images[1]['file_name'],'wb') as handler:
                       handler.write(img_data)
#for imag in images:
#        img_data = requests.get(imag['coco_url']).content
#        with open('/home/robert/Desktop/test_intern/backpack_img_dwnld/'+imag['file_name'],'wb') as handler:
#                   handler.write(img_data)
#                   print('image downloaded')
