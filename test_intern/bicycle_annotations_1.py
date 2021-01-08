from pycocotools.coco import COCO
import requests
import csv

coco = COCO('/home/robert/Desktop/annotations_train/instances_train2017.json')
cats = coco.loadCats(coco.getCatIds())
nms=[cat['name'] for cat in cats]
#print('COCO categories: \n{}\n'.format(' '.join(nms)))

catIds = coco.getCatIds(catNms=['bicycle'])
#print(catIds)
imgIds = coco.getImgIds(catIds=catIds)

images = coco.loadImgs(imgIds)
#print("images: ", images)


with open('/home/robert/Desktop/test_intern/cycl_annot/'+ 'cycle_annotations' + '.csv', mode='w', newline='')as annot:
        for imag in images:
                 annIds = coco.getAnnIds(imgIds=imag['id'], catIds=catIds, iscrowd=None)
                 anns = coco.loadAnns(annIds)
                 for i in range(len(anns)):
                          annot_writer = csv.writer(annot)
                          annot_writer.writerow(['downloaded_images/' + imag['file_name'], int(round(anns[i]['bbox'][0])), int(round(anns[i]['bbox'][1])), int(round(anns[i]['bbox'][0] + anns[i]['bbox'][2])), int(round(anns[i]['bbox'][1] + anns[i]['bbox'][3])), 'bicycle'])
                          print('annotation for one is done')
                
annot.close()













