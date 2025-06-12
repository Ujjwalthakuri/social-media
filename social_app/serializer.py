from .models import post_Model
from rest_framework import serializers

class post_serial(serializers.Serializer):
    date = serializers.DateTimeField(read_only= True)
    title = serializers.CharField(max_length=20)
    content = serializers.CharField()
    # user = models.ForeignKey()