from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Test(request):
	return HttpResponse("<h1>welcome to my test page</h1>")

def Product(request):
	return HttpResponse("<h1>welcome to product page</h1>")

def Contact(request):
	return HttpResponse("<h1>This is contact information</h1>")

def Flower(request):
	context={}
	return render(request,'flowers.html',context)

def Test(request):
	contex={}
	return render(request,'testapp/test.html',context)

def StaticTest(request):
	context={}
	return render(request,'testapp/static_test.html',context)