from .models import post_Model
from rest_framework import serializers

class post_serial(serializers.ModelSerializer):
    class Meta:
        model = post_Model
        fields = ['id', 'date', 'title', 'content']
   