from django.urls import reverse

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    def __str__(self):
        return self.Item_name
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    Item_name = models.CharField(max_length=200)
    Item_desc = models.CharField(max_length=200)
    Item_Price = models.IntegerField()
    Item_image = models.CharField(max_length=500,default='https://cookinupastorm.biz/wp-content/uploads/2023/04/EmptyDinnerPlates.jpg')

    def get_absolute_url(self):
        return reverse('food:detail',kwargs={'pk':self.pk})
