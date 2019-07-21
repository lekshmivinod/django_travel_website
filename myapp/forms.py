
from django import forms

class Customersignup(forms.Form):
    uname = forms.CharField(max_length=100)
    email=forms.CharField(max_length=20)
    psw=forms.CharField(max_length=100)
    pswrepeat=forms.CharField(max_length=100)



class contactus(forms.Form):
    fullname = forms.CharField(max_length=100)
    Email=forms.CharField(max_length=20)
    msg=forms.CharField(max_length=100)


class Loginform(forms.Form):
    uname = forms.CharField(max_length=100)
    psw = forms.CharField(max_length=100)