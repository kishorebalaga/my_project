from pycocotools.coco import COCO
import requests
import csv

coco = COCO('/home/robert/Desktop/annotations_train/instances_train2017.json')
cats = coco.loadCats(coco.getCatIds())
nms=[cat['name'] for cat in cats]
#print('COCO categories: \n{}\n'.format(' '.join(nms)))

catIds = coco.getCatIds(catNms=['person'])
#print(catIds)
imgIds = coco.getImgIds(catIds=catIds)

images = coco.loadImgs(imgIds)
#print("images: ", images)


with open('/home/robert/Desktop/codes/'+ 'list_person_annotation_1' + '.txt', mode='a', newline='')as annot:
        for imag in images:
                 annIds = coco.getAnnIds(imgIds=imag['id'], catIds=catIds, iscrowd=None)
                 anns = coco.loadAnns(annIds)
                 for i in range(len(anns)):
                          annot.write(str([imag['file_name'], int(round(anns[i]['bbox'][0])),int(round(anns[i]['bbox'][1])), int(round(anns[i]['bbox'][2])), int(round(anns[i]['bbox'][3]))]))
                          #annot.write('6')
                          
                          annot.write(',')
                          annot.write("height=")
                          annot.write(str(imag['height']))
                          annot.write(',')
                          annot.write("width=")
                          annot.write(str(imag['width']))
                          annot.write('\n')
                          print('annotation for one is done')
                                        
annot.close()













