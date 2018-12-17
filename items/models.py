from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=120)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.name

class FavoriteItem(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	item = models.ForeignKey(Item, default=1, on_delete=models.CASCADE)