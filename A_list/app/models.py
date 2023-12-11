from django.db import models

class Course(models.Model):
    idc = models.CharField(max_length=300)
    name = models.CharField(max_length=300)