from django.db import models

# Create your models here.

class Access(models.Model):
	time = models.FloatField(max_length=40)
	elapsed = models.IntegerField(default=0)
	ip = models.CharField(max_length=16)
	code = models.CharField(max_length=25)
	data = models.IntegerField(default=0)
	method = models.CharField(max_length=8)
	url = models.CharField(max_length=100)
	date = models.DateTimeField(auto_now=False)

class LastKey(models.Model):
	time = models.FloatField(max_length=40)