import json

from django.core.serializers import serialize
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Update
from django.views.generic import View
from profiles_project.mixins import JsonResponseMixin

# def detial_view(request): 
#     return render()


def json_example_view(request):
    data = {
        "count":1000,
        "conent":"Some new content"
    }
    json_data = json.dumps(data)
    return HttpResponse(json_data,content_type='application/json')


class JsonCBV(View):
    def get(self,request,*args, **kwargs):
        data = {
        "count":1000,
        "content":"Some new content"
         }
        return JsonResponse(data)




class JsonCBV2(JsonResponseMixin,View):
    def get(self,request,*args, **kwargs):
        data = {
        "count":1000,
        "content":"Some new content"
         }
        return self.render_to_json_response(data)


class SerializedDetialView(View):
    def get(self,request,*args, **kwargs):
        obj = Update.objects.all()
        data = serialize("json",obj,fields=('user','content'))
        # data = {
        # "user":qs.user.username,
        # "content":qs.content
        # }   
        #json_data = json.dumps(data)
        json_data = data
        return HttpResponse(json_data,content_type='application/json')


class SerializedListView(View):
    def get(self,request,*args, **kwargs):
        qs = Update.objects.all() 
        json_data = Update.objects.all().serialize()
        return HttpResponse(json_data,content_type='application/json')


