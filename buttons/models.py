from django.db import models


class Button(models.Model):
    number = models.IntegerField()
    text = models.CharField(max_length=8)
