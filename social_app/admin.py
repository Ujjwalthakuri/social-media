from django.contrib import admin
from .models import post_Model
# Register your models here.
@admin.register(post_Model)
class postAdmin(admin.ModelAdmin):
    list_display = [id, 'date', 'title', 'content']