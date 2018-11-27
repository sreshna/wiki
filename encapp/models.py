from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Favorites(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
