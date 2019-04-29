"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home' ),
    path('note/', include('note.urls')),
    path('blog/', include('blog.urls')),
    path('dic/', include('dic.urls')),
    path('about/', views.index,name='about'),
    path('contact/', views.index,name='contact'),
    path('download/', views.download,name='download'),
    path('signin', views.signin),
    path('signin_page', views.signin_page,name='signin_page'),
    path('sign_out', views.sign_out,name='sign_out'),
    path('help', views.sign_out,name='help'),
    path('settings', views.sign_out,name='settings'),
    path('doc_list', views.sign_out,name='doc_list'),
]
