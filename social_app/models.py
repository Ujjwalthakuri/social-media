from django.db import models
# Create your models here.
class post_Model(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=20)
    content = models.TextField()
    # user = models.ForeignKey()
    