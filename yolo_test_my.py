from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_api import status
from flask_restful import reqparse
import json
from multiprocessing import Process
import psutil
import os
#import pandas as pd
from time import sleep
#from kafka import KafkaProducer
from json import dumps


# GPU setting
import os
from keras import backend as k
import tensorflow as tf


import time
import pexpect

cmdpath = '/home/robert/darknet/'
cmd_certisai = '/home/robert/darknet/darknet detector test cfg/yolov3.cfg yolov3.weights data/dog.jpg -thresh 0.50'

#print("##########################################################################################")
child_cmd = pexpect.spawn(cmd_certisai, cwd=cmdpath)

#__certisai.expect('enter the image path',timeout=None)
#print("##########################################################################################")
child_cmd.expect(pexpect.EOF)
print("result = ",child_cmd.readline(size: int=-1))
#print("load certis-ai")
#if __certisai:
#    time.sleep(7)
#else:
#    print("load certis-ai error")





#__certisai.expect(pexpect.EOF)
#print("##############################################################CHECK###################################################################")

#__certisai.expect(pexpect.EOF)
#print("load all success....")


