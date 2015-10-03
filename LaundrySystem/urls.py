"""LaundrySystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from laundry import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.home,name='home'),
    url(r'^login/',views.login,name='login'),
    url(r'^register$',views.PersonRegister,name='register'),
    url(r'^check/$',views.check,name='check'),
    url(r'^dispalydata',views.register,name='registerdata'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^cloth',views.addCloth,name='morecloth'),
    url(r'^newCloth',views.newCloth,name='addcloth'),
    url(r'^clothdisplay/',views.clothdisplay,name='clothdisplay')
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    #urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
