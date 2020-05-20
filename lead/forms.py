from django import forms
from .models import Register
from .models import Login
from .models import StudLeads
from .models import TrainLeads



class Reg_Form(forms.ModelForm):
	class Meta:
		model=Register
		fields=('name','password','mailid','phno')

class Log_Form(forms.Form):
	name=forms.CharField(widget=forms.textinput(attr={'placeholder':'enter name here'}))
	password=forms.CharField(max_length=30)
	'''
	class Meta:
		model=Login
		fields=('name','password')
	

class Stud_Form(forms.ModelForm):
	class Meta:
	model=StudLeads
	fields=('sname','scourse','sphno','sfee','source','status')

class Train_Form(forms.ModelForm):
	class Meta
	model=TrainLeads
	fields=('tname','tcourse','texperiance','tphno')

'''

