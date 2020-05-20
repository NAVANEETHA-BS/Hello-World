from django.conf.urls import url,include
from .views import Home
from .views import RegisterForm
from .views import LoginForm
'''
from .views import Common
from .views import Sleads
from .views import Tleads
'''


urlpatterns=[
url(r'^lead/',Home),
url(r'^register/',RegisterForm,name='register'),
url(r'^login/',LoginForm,name='login'),
'''
url(r'^common/',Common),
url(r'^insert/',Sleads,name='insert')
url(r'^enter/',Tleads,name='enter')
'''
]