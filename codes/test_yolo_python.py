from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_api import status
from flask_restful import reqparse
import json
from multiprocessing import Process
import psutil
import os
import pandas as pd
from time import sleep
from kafka import KafkaProducer
from json import dumps


# GPU setting
import os
from keras import backend as K
import tensorflow as tf


import time
import pexpect

cmdpath = '/home/robert/darknet/'
cmd_certisai = '/home/robert/darknet/darknet detector test cfg/jessica-ai.data cfg/jessica-ai.cfg -thresh 0.50 data/jessica-ai/backup/jessica-ai_final.weights '
#cmd_certisai = '/home/robert/darknet/darknet detector test cfg/lta-t305.data cfg/lta-t305.cfg -thresh 0.50 data/lta-t305/backup/lta-t305_final.weights '
#cmd_certisai = '/home/robert/darknet/darknet detector test cfg/coco.data cfg/yolov3.cfg -thresh 0.50 yolov3.weights '

os.environ["CUDA_VISIBLE_DEVICES"]='0'
config0 = tf.ConfigProto()
with K.tf.device('/gpu:0'):
   config0.gpu_options.allow_growth = True
   session0 = tf.Session(config=config0)
   K.set_session(session0)
__certisai = pexpect.spawn(cmd_certisai, cwd=cmdpath)
print("load certis-ai")
if __certisai:
    time.sleep(7)
else:
    print("load certis-ai error")
print("load all success....")
app = Flask(__name__)
CORS(app)

@app.route("/aidetect", methods=['POST'])
def postAIdetect():
    global __certisai
    try:       
        current=""
        data = ""
        parser = reqparse.RequestParser()
        parser.add_argument("value",type=str, location='form', store_missing="")
        parser.add_argument("ai_class",type=str, location='form', store_missing="")
        if request.get_json() and request.get_json() != None:
            data = request.get_json()

        elif parser.parse_args() and parser.parse_args() != None and parser.parse_args() != "":
            data = parser.parse_args()
        
        else:
            return jsonify({'Status':'No accepted inputs'}), status.HTTP_417_EXPECTATION_FAILED

        if 'value' in data:
                    if __certisai and ((data['ai_class'] =="all") or (data['ai_class'] == "jaywalk") or (data['ai_class'] == "wheelchair") or (data['ai_class'] == "olb") or (data['ai_class'] == "falldown") or (data['ai_class'] == "walkstick") or (data['ai_class'] == "person")):
                        print("certis-ai send message:"+data['value'])
                        inputurl=data['value']
                        __certisai.sendline(data['value'])
                        current='all'
                        __certisai.expect('Enter Image Path:',timeout=None)
                        print(__certisai.before)
                        resposetxt=data['value'] +' Done.' 
                        #return jsonify({'Status':resposetxt} ), status.HTTP_200_OK
                        time.sleep(0.2)
                        read_tmp=(inputurl.replace('input','output'))
                        print("1 read_tmp--->"+read_tmp)
                        readfile=(read_tmp.replace('jpg','json'))
                        print("2 readfile--->"+readfile)
                        with open(readfile,'r') as f:
                            jsondata = json.load(f)
                            print(jsondata)
                        #    producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda x: dumps(x).encode('utf-8'))
                        #    producer.send('test', value=jsondata)
                        #    producer.flush()                       
                        return jsonify(jsondata), status.HTTP_200_OK
                        #return jsonify({'Status':resposetxt} ), status.HTTP_200_OK 
                    else:
                        print("data format error")
                        resposetxt=data['value']+' Fail.' 
                        return jsonify({'Status':resposetxt}), status.HTTP_417_EXPECTATION_FAILED

        else: 
            jsonify({'Status':'Invalid inputs'}), status.HTTP_417_EXPECTATION_FAILED            
                    
    except Exception as e:
        print(current)
        if current=='all':
            print('get Exception:'+str(e))
            os.environ["CUDA_VISIBLE_DEVICES"]='0'
            config0 = tf.ConfigProto()
            with K.tf.device('/gpu:0'):
               config0.gpu_options.allow_growth = True
               session0 = tf.Session(config=config0)
               K.set_session(session0)
            __certisai = pexpect.spawn(cmd_certisai, cwd=cmdpath)
            print("reload certis-ai")
            if __certisai:
                time.sleep(5)
            else:
                print("reload certis-ai error")
            print("reload unknown error")   
        
    return jsonify({'Status':'Failed'}), status.HTTP_400_BAD_REQUEST1077,


if __name__ == '__main__':

    app.run(debug=True)




