from pycocotools.coco import COCO
import requests

coco = COCO('/home/robert/Desktop/test_intern/annotations/instances_train2017.json')
cats = coco.loadCats(coco.getCatIds())
nms=[cat['name'] for cat in cats]
print('COCO categories: \n{}\n'.format(' '.join(nms)))

catIds = coco.getCatIds(catNms=['backpack'])
imgIds = coco.getImgIds(catIds=catIds)

images = coco.loadImgs(imgIds)
print(imgIds)
#print("imgIds: ", imgIds)
#print("images: ", images)
