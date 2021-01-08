import shutil

path = "/home/robert/Desktop/objects_and_annotations/person_images_clean/"
path_annot="/home/robert/Desktop/objects_and_annotations/person_annotation_list/annotations_person/"
import os
destination_annot ="/home/robert/Desktop/objects_and_annotations/person_annotation_list/clean_annot_person/"
img_ids_list = []
for imag in os.listdir(path):
         img_id = imag.rstrip('.jpg')+'.txt'
         print("imageee iddd",img_id)
#         print(os.listdir(path_annot))
         if img_id in os.listdir(path_annot):
                   print('entering loop')
                   path_annot_1 = path_annot +img_id
                   dest_annot_1 = destination_annot +img_id
                   shutil.copyfile(path_annot_1,dest_annot_1)
                   print("copy done for one")
         
                   
