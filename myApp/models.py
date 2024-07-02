from django.db import models

# Create your models here.
class Student(models.Model):
	sno=models.IntegerField()
	sname=models.CharField(max_length=40)
	smarks=models.CharField(max_length=30)
	saddr=models.CharField(max_length=100)
	def __str__(self):
		return self.sname
