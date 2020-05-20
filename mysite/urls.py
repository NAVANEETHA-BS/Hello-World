"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
#from blog.views import Hello
#from blog import views as v1
#from testapp import views as v2

urlpatterns=[
    url(r'^admin/',admin.site.urls),
    url(r'^blog/',include('blog.urls')),
    url(r'^test/',include('testapp.urls')),
    url(r'^accounts/',include('registration.backends.default.urls'))
    #url(r'^hello/',Hello),
    #url(r'^home/',v1.Home),
    #url(r'^contact/',v1.Contact),
    
    #url(r'^about/',v1.About),
    #url(r'^test/',v2.Test),
    #url(r'^product/',v2.Product),
]
