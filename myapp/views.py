from __future__ import unicode_literals

from django.shortcuts import render,redirect
from myapp.forms import *
from django.http import HttpResponse, HttpResponseRedirect
from myapp.models import *
import sqlite3

def signin(request):
    data=Customersignup(request.GET)
    if data.is_valid():
        username = data.cleaned_data['uname']
        emailid = data.cleaned_data['email']
        password = data.cleaned_data['psw']
        repassword = data.cleaned_data['pswrepeat']
        e=webpage(name=username,Email=emailid,password=password,repassword=repassword)
        # request.session["name"]=e.name
        # request.session["password"]=e.password
        e.save()
        # def logout():
        #     try:
        #         del request.session.name
        #         del request.session.password
        #     except:
        #         pass
        # logout()
    # return render(request,'travelworld/userinterface.html',{})
    # return HttpResponseRedirect("login.html")

    return render(request,'register.html',{})
def contact1(request):
    data=contactus(request.GET)
    if data.is_valid():
        fullname = data.cleaned_data['fullname']
        Email = data.cleaned_data['Email']
        msg = data.cleaned_data['msg']

        e=contact(fullname=fullname,Email=Email,msg=msg)
        # request.session["name"]=e.name
        # request.session["password"]=e.password
        e.save()
    return render(request, 'contact.html', {})
def loginforms(request):
    if request.method=="GET":
        data = Loginform(request.GET)
    try:
        if data.is_valid():
            u = data.cleaned_data['uname']
            p = data.cleaned_data['psw']
            user = webpage.objects.get(name=u, password=p)

            if u == user.name and p == user.password:
                request.session["name"] = user.name
                request.session["password"] = user.password
                # return  HttpResponse("suucess..")
                # return HttpResponse("")
            # return HttpResponseRedirect("loggedin.html")
            # return HttpResponseRedirect('/prot/loggedin')

            return redirect(request, "/prot/loggedin.html/", {})

    except:
        return render(request, "loggedin.html", {})
#
# def loginforms(request):
#         if request.method == "GET":
#             data = Loginform(request.GET)
#
#             if data.is_valid():
#                 u = data.cleaned_data['uname']
#                 p = data.cleaned_data['psw']
#                 user = webpage.objects.get(name=u, password=p)
#
#                 if u == user.name and p == user.password:
#                     request.session["name"] = user.name
#                     request.session["password"] = user.password
#                     # return  HttpResponse("suucess..")
#                     # return HttpResponse("")
#                 return HttpResponseRedirect("loggedin.html")
#                 # return HttpResponseRedirect('/prot/loggedin')
#
#                 # return redirect(request, "loggedin.html", {})
#
#         else:
#             return HttpResponseRedirect("loggedin.html")
#
#             # return render(request, "loggedin.html", {})


# def loginforms(request):
#     if request.method == "GET":
#         form = Loginform(request.GET)
#         if form.is_valid():
#             try:
#                 return redirect('loggedin.html')
#             except:
#                 pass
#         else:
#             form = Loginform()
#     return render(request, 'index.html', {'form': form})

        # return render(request,"travelagency/loginform.html",{})
            # else:

            #     request.session["error"] = "error"
            #     e = 'error'
            #     return render(request, "travelagency/loginform.html")
            # if u == 'Admin' and p == 'admin123':
            #     request.session["name"]='Admin'
            #     request.session["password"]='admin123'
            #     details = webpage.objects.all()
            #     userdetails = Userdetais.objects.all()
            #     return render(request,"travelworld/Admin.html",{'detail':details,'userdetail':userdetails})


                # return render(request,"travelagency/loginform.html")
# def pacakgeview(request):
#     pckg=addpackages.objects.all()
#     context={'pckg':pckg}
#     return render(request, 'travelagency/packages.html',context)
def logout(request):
    try:
      del request.session["name"]


    except:
        pass
    # return HttpResponse("<strong>You are logged out.</strong>")
    return redirect('/myapp/login/')
    # return render(request,'travelagency/index.html',{})


# Create your views here.



#
# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals
#
# from myapp.forms import *
# from django.http import HttpResponse, HttpResponseRedirect
# from myapp.models import *
# import sqlite3
#
#
#
# from django.shortcuts import render,redirect
# from myapp.models import package
#
#
#
# def package_detail_view(request):
#    obj=package.objects.get(id=1)
#    context={
#       'title':obj.title,
#       'description':obj.description
#    }
#    return render(request,"package.html",context)
#
#
#
#
# #
# # def indexo (request):
# #
# #    members = Member.objects.all()
# #    context={"members" :members}
# #    return render (request,'contact.html',context)
# #
# #
# # def contact (request):
# #    member=Member(Name=request.POST['Name'],Email=request.POST['Email'],Message=request.POST['Message'])
# #    member.save()
# #    return redirect('/')
#
#
# def contact1(request):
#     data=contactus(request.GET)
#     if data.is_valid():
#         fullname = data.cleaned_data['fullname']
#         Email = data.cleaned_data['Email']
#         msg = data.cleaned_data['msg']
#
#         e=contact(fullname=fullname,Email=Email,msg=msg)
#         # request.session["name"]=e.name
#         # request.session["password"]=e.password
#         e.save()
#
# # # def index(request):
# # #    con=contactForm()
# # #    return render(request,{'form':con})
# # #
# #
# #
# #
# # def signin(request):
# #    members=signups.objects.all()
# #    context={"members" :members}
# #    return render (request,'register.html',context)
# #
# # def register(request):
# #    member=signups(username=request.POST['username'],Name=request.POST['Name'],Email=request.POST['Email'],Password=request.POST['Password'])
# #    member.save()
# #    return redirect('/')
#
#
#
# # from myapp.forms import LoginForm
# #
# # def login(request):
# #    username="not logged in"
# #
# #    if request.method=="POST":
# #       MyLoginForm=LoginForm(request.POST)
# #
# #       if MyLoginForm.is_valid():
# #          username=MyLoginForm.cleaned_data['username']
# #
# #       else:
# #          MyLoginForm=LoginForm()
# #       return render (request,'loggedin.html',{"username":username})
# #
# #
# #
# #
# #
# #
#
