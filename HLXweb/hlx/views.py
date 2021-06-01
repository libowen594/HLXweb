import base64
import json

from django.core import serializers
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from hlx import models
import requests


def to_json(data):
    res = serializers.serialize("json", data)
    return res


def addCategory(request):
    if request.method == 'POST':
        try:
            requestBody = request.body
            requestData = json.loads(requestBody)
            categoryObject = {
                "id": requestData.get('categoryId', None),
                "title": requestData.get('title', None),
                "description": requestData.get('description', None)
            }
            resourcesOld = models.Category.objects.filter(id=categoryObject["id"])
            if resourcesOld:
                models.Category.objects.filter(id=categoryObject["id"]).update(**categoryObject)
            else:
                models.Category.objects.create(**categoryObject)
            data = list(models.Category.objects.all().values())
            response = {"code": 0, 'data': data, 'msg': '插入成功'}
        except Exception:
            response = {"code": 1001, 'data': None, 'msg': '服务器内部错误，插入失败'}
    else:
        response = {"code": -1, 'data': None, 'msg': '请求错误'}
    return JsonResponse(response, json_dumps_params={'ensure_ascii': False})


def addPost(request):
    if request.method == 'POST':
        try:
            requestBody = request.body
            requestData = json.loads(requestBody)
            postObject = {
                'id': requestData.get('postID', None),
                'category': requestData.get('categoryID', None),
                'title': requestData.get('title', None),
                'text': requestData.get('text', None),
                'user': requestData.get('userID', None),
                'tag': requestData.get('tagID', None),
                'hit': requestData.get('hit', None),
                'creatTime': requestData.get('creatTime', None),
                # 'images': requestData.get('images', None),
                # 'imageUrls': requestData.get('imageUrls', None),
                # 'video': requestData.get('video', None),
            }
            resourcesOld = models.Post.objects.filter(id=postObject['id'])
            if resourcesOld:
                models.Category.objects.filter(id=postObject["id"]).update(**postObject)
            else:
                models.Category.objects.create(**postObject)
                if isinstance(requestData["imageUrls"], list):
                    for imgUrl in requestData["imageUrls"]:
                        imgName = imgUrl.split("/")[-1]
                        SourceObj = {
                            'post': postObject['id'],
                            'comment': None,
                            'filename': imgName,
                            'url': imgUrl,
                            'type': '图片',
                            'creatTime': postObject['creatTime']
                        }
                        models.Source.objects.create(**SourceObj)
                        res = requests.get(imgUrl, timeout=5)
                        if res.status_code == 200:
                            img = base64.b64encode(res.content)
                        else:
                            img = None
                        postSourceObj = {
                            'post': postObject['id'],
                            'url': imgUrl,
                            'imgName': imgName,
                            'imgFile': img,
                            'video': requestData['videoUrl'],
                        }
                        models.PostSource.objects.create(**postSourceObj)
                if requestData['video']:
                    SourceObj = {
                        'post': postObject['id'],
                        'comment': None,
                        'filename': None,
                        'url': requestData['video'],
                        'type': '视频',
                        'creatTime': postObject['creatTime']
                    }
                    models.Source.objects.create(**SourceObj)
        except Exception:
            pass
