from django import forms
from .models import Post
from .models import ContactForms


class ContactForm(forms.Form):
	contact_name=forms.CharField(max_length=30,required=True)
	phno=forms.CharField(max_length=20)
	contact_email=forms.CharField(required=True)
	content=forms.CharField(widget=forms.Textarea())

class PostForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=('author','title','text')

