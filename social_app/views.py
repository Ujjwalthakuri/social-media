from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import post_Model
from .serializer import post_serial
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.
def postview(request):
    if request.method == "GET":
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        id = py_data.objects.get('id', None)
        if id is not None:
            post_id = post_Model.objects.get(id = id)
            serialize = post_serial(post_id)
            json_data = JSONRenderer().render(serialize.data)
            return HttpResponse(json_data)
        post = post_Model.objects.all()
        serialize = post_serial(post, many=True)
        json_data = JSONRenderer().render(serialize.data)
        return HttpResponse(json_data)
            
        