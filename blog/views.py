from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import EmailMessage
from .forms import PostForm
from .forms import ContactForm
from .models import Post,ContactForms
#from .models import Post,Thanks
#from . models import Post

# Create your views here.

def Thanks(request):
	return HttpResponse("Thank you and Have a great day!!!, I will inform soon")


def Contact(request):
	#GET REQUEST
	form_class=ContactForm #class not a instance
	context={'form':form_class}

	#POST REQUEST
	if request.method=='POST':
		form=ContactForm(request.POST)
		#print(form.is_valid())
		if form.is_valid():
			contact_name=form.cleaned_data['contact_name']
			contact_email=form.cleaned_data['contact_email']
			content=form.cleaned_data['content']
			subject="A new contact or lead - {}".format(contact_name)
			email=EmailMessage(subject , contact_name + '\n' + contact_email + '\n' + content , to=['neetha123bs@gmail.com'])
			email.send()
			return HttpResponseRedirect('/blog/thanks/')	
	return render(request,'blog/contact_blog.html',context)		




def BlogInsert(request):
	#print(request.method)
	#POST
	if request.method=='POST':
		form=PostForm(request.POST)
		#print(form.is_valid())
		#when your form is valid
		if form.is_valid():
			author=form.cleaned_data['author']
			title=form.cleaned_data['title']
			text=form.cleaned_data['text']
			Post.objects.create(author=author,title=title,text=text)
			return HttpResponseRedirect('/blog/thanks/')
		#when my form is not valid
		else:
			context={'form':form}
			return render(request,'blog/blog_form.html',context)

	#GET
	else:
		form=PostForm
		context={'form':form}
		return render(request,'blog/blog_form.html',context)


def Thanks(request):
	return HttpResponse("Thank you and have a great day!!!, I will inform soon")


def BlogData(request):
	context={'blogdb':Post.objects.all()}
	return render(request,'blog/blog_data.html',context)


def StudentSingleRecord(request):
	context={'sid':101,'sname':'vishnu','course':'python','fee':6000.00}
	return render(request,'student_form.html',context)


def StudentMultipleRecord(request):
	context={'studlist':[
	{'sid':101,'sname':'vishnu','course':'python','fee':6000.00},
	{'sid':102,'sname':'lakshmi','course':'Django','fee':8000.00},
	{'sid':103,'sname':'latha','course':'aws','fee':10000.00},
	{'sid':104,'sname':'geetha','course':'devops','fee':15000},
	{'sid':105,'sname':'neetha','course':'linux','fee':3000.00}

	]}
	return render(request,'students_form.html',context)


def Product(request):
	context={'prodlist':[
	{'pid':101,'pname':'chocolate','pprice':150.00},
	{'pid':102,'pname':'icecream','pprice':250.00},
	{'pid':103,'pname':'biscuit','price':350.00},
	{'pid':104,'pname':'apple','pprice':500.00}

	]}
	return render(request,'prod_list.html',context)		


'''
def Home(request):
	context={}
	return render(request,'home.html',context)
'''

def Home(request):
	context={'blogdb': Post.objects.all()}
	return render(request,'home.html',context)


def BlogInserts(request):
	#print(request.method)
	#POST
	#form_class=PostForm
	#context={'form':form_class}
	if request.method=='POST':
		form=PostForm(request.POST)
		#print(form.is_valid())
		#when your form is valid
		if form.is_valid():
			author=form.cleaned_data['author']
			title=form.cleaned_data['title']
			text=form.cleaned_data['text']
			Post.objects.create(author=author,title=title,text=text)
			#context={'author':author,'title':title,'text':text}
			return HttpResponseRedirect('/blog/thankyou/')
		#when my form is not valid
		else:
			context={'form':form}
			return render(request,'blog/blogform.html',context)


	else:
		form=PostForm
		context={'form':form}
		return render(request,'blog/blogform.html',context)


def Thanks(request):
	context={}
	return render(request,'blog/thankyou.html',context)



def ContactsForm(request):
	#print(request.method)
	#POST
	form_class=ContactForm
	context={'form':form_class}
	if request.method=='POST':

		form=ContactForm(request.POST)
		print(form.is_valid())
		#when your form is valid
		if form.is_valid():
			contact_name=form.cleaned_data['contact_name']
			phno=form.cleaned_data['phno']
			contact_email=form.cleaned_data['contact_email']
			#ContactForms.objects.create(contact_name=contact_name,phno=phno,contact_email=contact_email)
			#context={'author':author,'title':title,'text':text}
			subject="A new contact or lead - {}".format(contact_name)
			email=EmailMessage(subject,contact_name + '\n' + contact_email + '\n' + str(phno), to=['neetha123bs@gmail.com'])
			email.send()
			return HttpResponseRedirect('/blog/contacts/')
		#when my form is not valid
		#else:
			#context={'form':form}
	return render(request,'blog/contactform.html',context)


	#else:
		#form=ContactForm
		#context={'form':form}
		#return render(request,'blog/contactform.html',context)


def Contacts(request):
	context={}
	return render(request,'blog/contacts.html',context)


def AboutUs(request):
	context={}
	return render(request,'blog/aboutus.html',context)