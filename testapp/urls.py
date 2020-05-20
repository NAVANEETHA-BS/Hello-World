from django.conf.urls import url,include
#from . views import Test,Product
from django.contrib import admin
import testapp.views as v2
from . views import StaticTest

urlpatterns=[
	#url(r'^test/',Test),
	#url(r'product/',Product)
	url(r'^admin/',admin.site.urls),
	url(r'^test/',v2.Test),
	url(r'^product/',v2.Product),
	url(r'^contact/',v2.Contact),
	url(r'^neetha/',v2.Flower),
	url(r'^statictest/',StaticTest),

]