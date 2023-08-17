#coding:utf-8
import os
from flask import Flask, request, jsonify, abort, Response
import multiprocessing as mp
import threading
import time
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import logging
from transformers import BertModel,BertConfig,BertTokenizer

tokenizer = None
model = None
model_dir = "./models/pp_model_v3"
device=torch.device("cuda:{}".format(0) if torch.cuda.is_available() else "cpu")

def init(n):
    # RGB bert_wb_251m
    global tokenizer,model,device
    tokenizer = AutoTokenizer.from_pretrained(model_dir)
    model = AutoModelForSequenceClassification.from_pretrained(model_dir)
    model.to(device)

def run(vedio_list):
    global tokenizer,model,device
    tokenized_text = tokenizer(vedio_list, padding=True, truncation=True, return_tensors="pt").to(device)
    with torch.no_grad():
        outputs = model(**tokenized_text)
        outputs_distribution = outputs[0]
        predictions = torch.nn.functional.softmax(outputs_distribution, dim=-1).to(torch.device('cpu'))

    return predictions.tolist()

PARALLEL_CNT = 3
app = Flask(__name__)

def init_fn(n):
    init(n)
    return True

def init_cb(v):
    logging.error('rel')
    global init_count_down
    init_count_down_lock.acquire()
    init_count_down -= len(v)
    init_count_down_lock.release()

def init_ecb(err):
    print("init_ecb", err, os.getpid())


@app.route('/pp_predict', methods=['post'])
def predict():
    try:
        video_list = request.get_json()
        print(video_list)
        ret = run(video_list['str'])
        print(ret)
        return jsonify({"logits":ret})
    except ValueError:
        return jsonify({"status":400, "msg":"请求失败"})

if __name__ == "__main__":
    init(1)
    # app.run(host="172.17.0.1", port=6301, debug=False, threaded=True, processes=1)
    app.run(host="0.0.0.0", port=6301, debug=False, threaded=True, processes=1)
