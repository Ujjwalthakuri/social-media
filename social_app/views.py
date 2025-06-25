from django.shortcuts import render
from .serializer import post_serial
from .models import post_Model
from rest_framework import viewsets

class postCRUD(viewsets.ModelViewSet):
    queryset = post_Model.objects.all()
    serializer_class = post_serial