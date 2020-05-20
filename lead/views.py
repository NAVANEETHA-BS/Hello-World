from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Register
from .forms import Reg_Form
'''
from .models import Login
from .forms import Log_Form
from .models import StudLeads
from .models import TrainLeads
from .forms import Stud_Form
from .forms import Train_Form
'''

# Create your views here.

def Home(request):
	context={}
	return render(request,'lead/home.html',context)

def RegisterForm(request):
	form_class=Reg_Form
	context={'form':form_class}
	if request.method=='POST':
		form=Reg_Form(request.POST)
		print(form.is_valid())
		if form.is_valid():
			name=form.cleaned_data['name']
			password=form.cleaned_data['password']
			mailid=form.cleaned_data['mailid']
			phno=form.cleaned_data['phno']
			Register.objects.create(name=name,password=password,mailid=mailid,phno=phno)
			#return render(request,'lead/reg.html',d1)
			return HttpResponseRedirect('/lead/common')


		else:
			context={'form':form}
	return render(request,'lead/register.html',context)


def LoginForm(request):
	form_class=Log_Form
	context={'form':form_class}
	if request.method=='POST':
		form=Log_Form(request.POST)
		print(form.is_valid())
		if form.is_valid():
			name=form.cleaned_data['name']
			password=form.cleaned_data['password']
			#d1={'name':name,'password':password}
			#return render(request,'lead/log.html',d1)
			Login.objects.create(name=name,password=password)
			return HttpResponseRedirect('/lead/common')
		else:
			context={'form':form}
	return render(request,'lead/login.html',context)



def Common(request):
	context={}
	return render(request,'lead/common.html',context)

def Sleads(request):
	form_class=Stud_Form
	context={'form':form_class}
	if request.method=='POST':
		form=Stud_Form(request.POST)
		print(form.is_valid())
		if form.is_valid():
			sname=form.cleaned_data['sname']
			scourse=form.cleaned_data['scourse']
			sphno=form.cleaned_data['sphno']
			sfee=form.cleaned_data['sfee']
			source=form.cleaned_data['source']
			status=form.cleaned_data['status']
			StudLeads.objects.create(sname=sname,scourse=scourse,sphno=sphno,sfee=sfee,source=source,status=status)
			return HttpResponseRedirect('/lead/options')
		else:
			context={'form':form}
	return render(request,'lead/studform.html',context)


def Tleads(request):
	form_class=Train_Form
	context={'form':form_class}
	if request.method=='POST':
		form=Train_Form(request.POST)
		print(form.is_valid())
		if form.is_valid():
			tname=form.cleaned_data['tname']
			tcourse=form.cleaned_data['tcourse']
			texperiance=form.cleaned_data['texperiance']
			tphno=form.cleaned_data['tphno']
			TrianLeads.objects.create(tname=tname,tcourse=tcourse,texperiance=texperiance,tphno=tphno)
			return HttpResponseRedirect('/lead/options')
		else:
			context={'form':form}
	return render(request,'lead/trainform.html',context)




	









