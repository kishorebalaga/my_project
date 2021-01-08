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


with open('/home/robert/Desktop/codes/'+ 'cycle_annot_test_1' + '.txt', mode='a', newline='')as annot:
        for imag in images:
                 annIds = coco.getAnnIds(imgIds=imag['id'], catIds=catIds, iscrowd=None)
                 anns = coco.loadAnns(annIds)
                 for i in range(len(anns)):
                          #annot.write(str([imag['file_name']))#, #int(round(anns[i]['bbox'][0])),int(round(anns[i]['bbox'][1])), int(round(anns[i]['bbox'][2])), int(round(anns[i]['bbox'][3]))]))
                          #annot.write('6')
                          annot.write(str([imag['file_name']]))
                          xmin = anns[i]['bbox'][0]
                          ymin = anns[i]['bbox'][1]
                          xmax = anns[i]['bbox'][2] + anns[i]['bbox'][0]
                          ymax = anns[i]['bbox'][3] + anns[i]['bbox'][1]
                          dh = 1. /imag['height']
                          dw = 1. /imag['width']
                          x1 = (xmin + xmax)/2.0
                          y1 = (ymin +ymax)/2.0
                          wid = xmax-xmin
                          hgt = ymax -ymin
                          x1 = x1*dw
                          y1 = y1*dh
                          wid = wid*dw
                          hgt = hgt*dh
                          annot.write(str(round(x1,3)))
                          annot.write(' ')
                          annot.write(str(round(y1,3)))
                          annot.write(' ')
                          annot.write(str(round(wid,3)))
                          annot.write(' ')
                          annot.write(str(round(hgt,3)))
                          #annot.write("height=")
                          #annot.write(str(imag['height']))
                          #annot.write(',')
                          #annot.write("width=")
                          #annot.write(str(imag['width']))
                          #annot.write('\n')
                          print('annotation for one is done')
                          break
                                        
annot.close()


#bndbox = {
#                    "xmin": anno["bbox"][0],
#                    "ymin": anno["bbox"][1],
#                    "xmax": anno["bbox"][2] + anno["bbox"][0],
#                    "ymax": anno["bbox"][3] + anno["bbox"][1]
#                }





#                size = {
#                    "width": img_width,
#                    "height": img_height,
#                    "depth": "3"
#                }




#    def coordinateCvt2YOLO(self,size, box):
#        dw = 1. / size[0]
#        dh = 1. / size[1]

        # (xmin + xmax / 2)
#        x = (box[0] + box[1]) / 2.0
        # (ymin + ymax / 2)
#        y = (box[2] + box[3]) / 2.0

        # (xmax - xmin) = w
#        w = box[1] - box[0]
        # (ymax - ymin) = h
#        h = box[3] - box[2]

#        x = x * dw
#        w = w * dw
#        y = y * dh
#        h = h * dh
#        return (round(x,3), round(y,3), round(w,3), round(h,3))




