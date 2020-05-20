from django.db import models

# Create your models here.
class Register(models.Model):
	name=models.CharField(max_length=30,unique=True)
	password=models.CharField(max_length=30)
	mailid=models.EmailField(max_length=30)
	phno=models.IntegerField(max_length=30)


'''
class StudLeads(models.Model):
	sname=models.CharField(max_length=30)
	scourse=models.CharField(max_length=30)
	sphno=models.IntegerField(max_length=30)
	sfee=models.IntegerField(max_length=30)
	source=models.CharField(max_length=30)
	status=models.CharField(max_length=30)

class TrainLeads(models.Model):
	tname=models.CharField(max_length=30)
	tcourse=models.CharField(max_length=30)
	texperiance=models.CharField(max_length=30)
	tphno=models.IntegerField(max_length=30)
	'''