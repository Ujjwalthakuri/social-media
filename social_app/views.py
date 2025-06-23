from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializer import post_serial
from .models import post_Model
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE',])
def postview(request, pk=None):
    # for get request
    if request.method == 'GET':
        id=pk
        if id is not None:
            postid = post_Model.objects.get(id=id)
            serializer = post_serial(postid)
            return Response (serializer.data)
        post = post_Model.objects.all()
        serializer = post_serial(post, many =True)
        return Response(serializer.data)
    
    # for post request
    if request.method == 'POST':
        serializer = post_serial(data = request.data)
        if serializer.is_valid():
            serializer.save()
            result = {'msg': 'New data has been inserted'}
            return Response(result, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # for put request
    if request.method == 'PUT':
        id = pk
        postid = post_Model.objects.get(id=id)
        serializer = post_serial(postid, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            result = {'msg': "Data has been edited using put method"}
            return Response(result)
        return Response(serializer.errors)
    
    # for delete request
    if request.method == 'DELETE':
        id = pk
        postid = post_Model.objects.get(id=id)
        postid.delete()
        return Response({"msg": "Data has been deleted"})
    