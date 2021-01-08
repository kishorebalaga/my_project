import pexpect
import sys
from pexpect import *
import shutil

location_image = '/home/robert/Desktop/test_intern/person_images/'
image_copy_location = '/home/robert/Desktop/test_intern/person_images_clean/'
cmdpath = '/home/robert/darknet/'
import os 
for img in os.listdir(location_image):
	
	
	image = img
	
	cmd_certisai = '/home/robert/darknet/darknet detector test cfg/coco.data cfg/yolov3.cfg yolov3.weights'+" "+location_image+image
#child_cmd = pexpect.spawn(cmd_certisai,cwd = cmdpath,encoding='utf-8',logfile = sys.stdout)
	(command_output, exitstatus) = run(cmd_certisai, withexitstatus=1)
#child_cmd.expect(pexpect.EOF)
	print('command_output =====',command_output)
	print('exitstatus========',exitstatus)
#print("result = ",child_cmd.before)
	fout = open('kishore_file.txt','wb')
	fout.write(command_output)
	fout.close()
	file1 = open('kishore_file.txt','r')
	for line1 in file1:
	       if "person:" in line1:
	               print(line1)
	               print(line1.split(':')[0])
	               percent = line1.split(':')[1].strip().rstrip("%")
	               print(percent)
	               percent =int(percent)
	               if percent>90 :
	                      print(line1)
	                      shutil.copy(location_image+image,image_copy_location+image)
               

                      
#child_cmd.logfile = sys.stdout
#child_cmd.logfile_read = sys.stdout
#print('child_cmd.logfile_read===================',child_cmd.logfile)
#child_cmd.logfile = fout
#child_cmd.expect(pexpect.EOF)


