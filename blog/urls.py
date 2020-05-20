from django.conf.urls import url,include
#from .views import Home,Contact,About,Flowers,StudentSingleRecord,StudentMultipleRecord
#from .views import Blogpost
#from .views import Test,StaticTest,BlogInsert
#from .views import BlogInsert
from .views import StudentSingleRecord,StudentMultipleRecord
from .views import Contact,Thanks,BlogInsert,BlogData
from .views import Product,Home,BlogInserts,Thanks
from .views import ContactsForm,Contacts
from .views import AboutUs
urlpatterns=[

	url(r'^contact/',Contact),
	url(r'^thanks/',Thanks),
	url(r'^post/',BlogInsert),
	url(r'^blogdata/',BlogData,name='blogdata'),
	url(r'^student/',StudentSingleRecord),
	url(r'^students/',StudentMultipleRecord),
	url(r'^products/',Product),
	url(r'^$',Home,name='home'),
	url(r'^bloginserts/',BlogInserts,name='bloginserts'),
	url(r'^thankyou/',Thanks),
	url(r'^contactform/',ContactsForm,name='contactform'),
	url(r'^contacts/',Contacts,name='contacts'),
	url(r'^aboutus/',AboutUs,name='aboutus'),

	]
