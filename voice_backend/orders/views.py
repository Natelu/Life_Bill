from django.http import JsonResponse
from .voice_transfer import get_transfer, get_order_result
import json


def index(request):
    resp = JsonResponse({
        "code": 200,
        "msg": "OK",
        })
    return resp


# tranfer the audio to plain text.
def audio_transfer(request):
    if request.method == 'POST':
        raw_dic = json.loads(request.body.decode('utf-8'))
        audio_data, audio_length = raw_dic['b64audio'], raw_dic['audiolen']
        response, _ = get_transfer(audio_data, audio_length)
        return JsonResponse({
            "data": response[0],
            "code": 200,
            "msg": "OK"})
    else:
        return JsonResponse({
            "code": 500,
            "msg": "Internal Error",
        })


# get the order of mobile data flow.
def flow_order(request):
    if request.method == 'POST':
        raw_dic = json.loads(request.body.decode('utf-8'))
        order_data = raw_dic['desc']
        response = get_order_result(order_data)
        return JsonResponse({
            "code": 200,
            "msg": "OK",
            "data": response
        })
    else:
        return JsonResponse({
            "code": 500,
            "msg": "Internal Error",
        })