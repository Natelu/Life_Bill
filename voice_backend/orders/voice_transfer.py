#! /usr/bin/env python 
# -*- coding: utf-8 -*-

import datetime
import logging
import json
import hashlib
import random
import requests
import sys
from . import VOICE_DATA, APP_SECRET, APP_ID, TRANSFER_URL, TRANSFER_HEADERS, ORDER_DATA, ORDER_URL
from .audio_data_process import data_process


def get_token(cur_time, trans_id):
    match_str = "APP_ID" + APP_ID + "TIMESTAMP" + cur_time + "TRANS_ID" + trans_id + APP_SECRET
    enc = hashlib.md5()
    b = match_str.encode(encoding='utf-8')
    enc.update(b)
    return enc.hexdigest()


def get_time_info():
    now = datetime.datetime.now()
    cur_time = datetime.datetime.strftime(now, '%Y-%m-%d %H:%M:%S %f')
    TRANS_ID = datetime.datetime.strftime(now, '%Y%m%d%H%M%S%f') + str(random.randint(100, 999))
    cur_time = cur_time[0: len(cur_time)-3]
    return cur_time, TRANS_ID


# orgainize the post data format.
def get_data(voice_data, audio_data, audio_length):
    cur_time, TRANS_ID = get_time_info() 
    voice_data['UNI_BSS_HEAD']['TIMESTAMP'] = cur_time
    voice_data['UNI_BSS_HEAD']['TRANS_ID'] = TRANS_ID
    voice_data['UNI_BSS_HEAD']['TOKEN'] = get_token(cur_time, TRANS_ID)
    voice_data['UNI_BSS_BODY']['VOICE_CONVERT_WRITE_REQ']['RequestBody']['b64audio'] = audio_data
    voice_data['UNI_BSS_BODY']['VOICE_CONVERT_WRITE_REQ']['RequestBody']['audiolen'] = audio_length
    return voice_data


# get the results from translation API.
def get_transfer(audio_data, audio_length):
    _data = get_data(VOICE_DATA, audio_data, audio_length)
    _response = requests.post(TRANSFER_URL, data=json.dumps(_data), headers=TRANSFER_HEADERS)
    response, status = None, None
    # try:
    response = (json.loads(_response.text))['UNI_BSS_BODY']['VOICE_CONVERT_WRITE_RSP']['RSP']['DATA']['UnicomTaskBack']['ResponseBody'][0]['data']
    print('--------')
    logging.INFO(response)
    origin_word = response[0]['word']
    response[0]['word'] = data_process.word_cut(origin_word)
    status = 200
    # except Exception as e:
    #     response = str(e)
    #     status = _response.status_code
    return response, status


# orginaze the format of order_info POST data.
def get_order_data(audio_text):
    temp_data = ORDER_DATA
    cur_time, TRANS_ID = get_time_info() 
    temp_data['UNI_BSS_HEAD']['TIMESTAMP'] = cur_time
    temp_data['UNI_BSS_HEAD']['TRANS_ID'] = TRANS_ID
    temp_data['UNI_BSS_HEAD']['TOKEN'] = get_token(cur_time, TRANS_ID)
    return temp_data
     

# get the response  data of the order requestion.
def get_order_result(audio_text):
    _data = get_order_data(audio_text)
    _response = requests.post(ORDER_URL, data=json.dumps(_data), headers=TRANSFER_HEADERS)
    if _response.status_code == 200:
        return json.loads(_response.text)['UNI_BSS_BODY']
    else:
        return '请求订单接口失败！'
