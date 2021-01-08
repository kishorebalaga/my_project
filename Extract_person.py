f = open("list_person_annotation_1.txt","r")
imag= ""
x=0
y=0
width_bbox =0
height_bbox =0
height_img = 608
width_img = 608
for line in f:
        print(line)
        lnhalf1 = line.split('.')[0]
        print((lnhalf1[2:]))
        imag = (lnhalf1[2:])
        lnhalf2 = line.split('.')[1]
        x = int((lnhalf2.split(',')[1]).strip())
        y = int((lnhalf2.split(',')[2]).strip())
        width_bbox = int((lnhalf2.split(',')[3]).strip())
        height_bbox = int(((lnhalf2.split(',')[4]).strip())[:-1])
        #height_temp = lnhalf2.split(',')[5]
        #width_temp = lnhalf2.split(',')[6]
        #height_img = int(height_temp.split('=')[1])
        #width_img = int(width_temp.split('=')[1])
        # CALICULATIONS STARTS FROM HERE
        value_1 = x/width_img
        value_2 = y/height_img
        value_3 = width_bbox/width_img
        value_4 = height_bbox/height_img
        print("height =",height_img)
        print("width =",width_img)
        print(x)
        print(y)
        print(width_bbox)
        print(height_bbox)
        print(value_1)
        print(value_2)
        print(value_3)
        print(value_4)
        f1 = open(imag+".txt","a")
        f1.write('1')
        f1.write(" ")
        f1.write(str(value_1)[:8])
        f1.write(" ")
        f1.write(str(value_2)[:8])
        f1.write(" ")
        f1.write(str(value_3)[:8])
        f1.write(" ")
        f1.write(str(value_4)[:8])
        f1.write("\n")
        
      
        
         
