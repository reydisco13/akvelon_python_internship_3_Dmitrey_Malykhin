from django.db import models

# Create your models here.


class Agent(models.Model):
    id = models.CharField(verbose_name='id', db_index=True, primary_key=True, max_length=64, unique=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
