from pycocotools.coco import COCO
import requests
import csv

coco = COCO('/home/robert/Desktop/annotations_train/instances_train2017.json')

import os 
path = "/home/robert/Desktop/objects_and_annotations/person_images_clean/"


cats = coco.loadCats(coco.getCatIds())
nms=[cat['name'] for cat in cats]
catIds = coco.getCatIds(catNms=['person'])
imgIds = coco.getImgIds(catIds=catIds)
#print("image ids",imgIds)
import os
img_ids_list = []
for imag in os.listdir(path):
           print("image id's",imag.rstrip('.jpg')[6:])
           img_id = imag.rstrip('.jpg')[6:]
           img_ids_list.append(img_id)
           print("imageeee list",img_ids_list)

for imagee in imgIds :
           print("imageeeeeeeeee",imagee)
           break
           if imagee in img_ids_list:
                    #images = coco.loadImgs(img_ids_list)
                    print("enters the loop")
                
    
#images = coco.loadImgs(img_ids_list)

#with open('/home/robert/Desktop/images_annotations_person_test/'+ 'person_annotation_list' + '.txt', mode='a', newline='')as annot:
#        for imag in images:
#                 print("imagessss id i think",imag)
#                 annIds = coco.getAnnIds(imgIds=imag['id'], catIds=catIds, iscrowd=None)
#                 anns = coco.loadAnns(annIds)
#                 for i in range(len(anns)):
#                          annot.write(str([imag['file_name'], int(round(anns[i]['bbox'][0])),int(round(anns[i]['bbox'][1])), int(round(anns[i]['bbox'][2])), int(round(anns[i]['bbox'][3]))]))
                          #annot.write('6')
                          
#                          annot.write(',')
#                          annot.write("height=")
#                          annot.write(str(imag['height']))
#                          annot.write(',')
#                          annot.write("width=")
#                          annot.write(str(imag['width']))
#                          annot.write('\n')
#                          print('annotation for one is done')

                                        
#annot.close()

