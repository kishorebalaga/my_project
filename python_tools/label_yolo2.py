import os
import json

path = '/home/robert/Desktop/12_13_14_fire_smoke_fireignition/annotations/'
path_1 = '/home/robert/Desktop/12_13_14_fire_smoke_fireignition/annotations/annotations_txt/'
import os
os.mkdir(path_1)
for tops, dirs, files in os.walk(path):
	for file in files:
		print('roger try print'+file)
		with open(path+file,'r') as f:
			data = json.load(f)
			data_tmp = data['object']
			size = data['size']
			width=int(json.loads(json.dumps(size['width'])))
			height=int(json.loads(json.dumps(size['height'])))
			coef_width=1/width
			coef_height=1/height
			
			#print(width+height)
			for subjsondata in data_tmp:
				#print(subjsondata)
				category= str(3)#for somoke change it to 3
				top_left_x=int(json.loads(json.dumps(subjsondata['top_left_x'])))
				top_left_y=int(json.loads(json.dumps(subjsondata['top_left_y'])))
				bottom_right_x=int(json.loads(json.dumps(subjsondata['bottom_right_x'])))
				bottom_right_y=int(json.loads(json.dumps(subjsondata['bottom_right_y'])))
				x=str(((bottom_right_x-top_left_x)/2+top_left_x)*coef_width)
				y=str(((bottom_right_y-top_left_y)/2+top_left_y)*coef_height)
				w=str((bottom_right_x-top_left_x)*coef_width)
				h=str((bottom_right_y-top_left_y)*coef_height)
				txt=(category+" "+x+" "+y+" "+w+" "+h)
				print(file+"-->"+txt)
				j=os.path.splitext(file)[0]
				name_file = str(file).rstrip('.json')
				txtfilename=path_1+name_file+".txt"
				k = open(txtfilename, 'a',encoding = 'UTF-8')
				k.write(txt+"\n")
				k.close()
		f.close()      
