from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
	author=models.ForeignKey('auth.user')
	title=models.CharField(max_length=200)
	text=models.TextField()
	created_date=models.DateTimeField(default=timezone.now)
	published_date=models.DateTimeField(blank=True,null=True)

def Publish(self):
	self.published_date=timezone.now()
	self.save

def __str__(self):
	return self.title



class ContactForms(models.Model):
	contact_name=models.CharField(max_length=30)
	phno=models.CharField(max_length=20)
	contact_email=models.CharField(max_length=30)
	content=models.CharField(max_length=200)