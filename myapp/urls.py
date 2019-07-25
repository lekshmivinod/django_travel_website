"""samsung URL Configurationmyapp/urls.py

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






from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView,ListView
from .import views
from myapp.models import package



urlpatterns = [
url(r'^packages/',ListView.as_view(model=package,template_name="package.html")),


    #
    #
    # url(r'^register$', views.signin, name='Register'),
    # url(r'^registerwithus$', views.register, name='registerr'),
    # #
    # url(r'^indexo$', views.contact,name='conact'),
    # url(r'^contact', views.indexo,name='contact'),
    url(r'^contact/', views.contact1, name='contact1'),
    url(r'^login/', views.signin, name='signin'),
    url(r'^logged/', views.loginforms,name='loginprocess'),
    url(r'^logout/', views.logout, name='logout'),

    url(r'^index/', TemplateView.as_view(template_name='index.html')),
    url(r'^contact/', TemplateView.as_view(template_name='contact.html')),
    url(r'^register/', TemplateView.as_view(template_name='register.html')),
    url(r'^VARANASI/', TemplateView.as_view(template_name='varanasi.html')),
    url(r'^MANALI/', TemplateView.as_view(template_name='manali.html')),
    url(r'^KASHMIR/', TemplateView.as_view(template_name='kashmir.html')),
    url(r'^RAJASTHAN/', TemplateView.as_view(template_name='rajasthan.html')),
    url(r'^gallery/', TemplateView.as_view(template_name='gallery.html')),
    url(r'^login/', TemplateView.as_view(template_name='login.html')),

    url(r'^loggedin/', TemplateView.as_view(template_name='loggedin.html')),
    url(r'^contact_lo/', TemplateView.as_view(template_name='contact_lo.html')),
    url(r'^payment/', TemplateView.as_view(template_name='payment.html')),
    url(r'^hotdeals/', TemplateView.as_view(template_name='hotdeals.html')),
    url(r'^packages/', TemplateView.as_view(template_name='package.html')),
    url(r'^rajasthan_lo/', TemplateView.as_view(template_name='rajasthan_lo.html')),
    url(r'^varanasi_lo/', TemplateView.as_view(template_name='varanasi_lo.html')),
    url(r'^manali_lo/', TemplateView.as_view(template_name='manali_lo.html')),
    url(r'^kashmir_lo/', TemplateView.as_view(template_name='kashmir_lo.html')),
    url(r'^SOUTH INDIA/', TemplateView.as_view(template_name='south.html')),
    url(r'^NORTH/', TemplateView.as_view(template_name='north.html')),
    url(r'^NORTH EAST/', TemplateView.as_view(template_name='northeast.html')),
    url(r'^GOA/', TemplateView.as_view(template_name='goa.html')),
    url(r'^logout/', TemplateView.as_view(template_name='logout.html')),



    url(r'^base/', TemplateView.as_view(template_name='base.html')),

    #
    # url(r'^login/', TemplateView.as_view(template_name='login.html')),
    # url(r'^ne',views.loginf,name='newlog'),

    # url(r'^$', views.sign, name='sign'),
    #
    # url(r'^contact$', views.contact, name='contact'),
    # url(r'^contact$', views.contact, name='contact')

]
