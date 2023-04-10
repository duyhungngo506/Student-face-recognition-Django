
from django import forms
class LoginForm(forms.Form):
        username = forms.CharField(max_length=199)
        email = forms.EmailField(max_length=199)
        password = forms.CharField(max_length=199,widget= forms.PasswordInput)
        # fields = [username,email,password]

        # widgets = {
        #     'username' : forms.TextInput(attrs = {'class':'form-control','placeholder':'Nhập tài khoản','required': 'true'}),
        #     'password' : forms.PasswordInput(attrs = {'class' : 'form-control','required': 'true','placeholder':'Nhập mật khẩu'}),
        #     'username' : forms.EmailInput(attrs = {'class':'form-control','placeholder':'Nhập email','required': 'true'}),
            
        # }

