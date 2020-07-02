from django.db import models

# Create your models here.

class Bank(models.Model):
	bank_id = models.IntegerField(default=0)
	name = models.CharField(max_length=50)

class Branch(models.Model):
	ifsc = models.CharField(max_length=11)
	bank_id = models.IntegerField()
	branch = models.CharField(max_length=74)
	address = models.CharField(max_length=195)
	city = models.CharField(max_length=50)
	district = models.CharField(max_length=50)
	state = models.CharField(max_length=50)

	def __str__(self):
		return str(self.branch)