from datetime import datetime
from django import forms
from stream.models import Students
class AddStudentForm(forms.ModelForm):
    
    class Meta:
        DateNow = datetime.now().strftime("%Y-%m-%d")
        yearMax = datetime.now().strftime("%Y")
        yearMin = int(yearMax)-99
        model = Students
        fields = ('fullName','birthday','phoneNumber','address','classs','id')

        widgets = {
            'fullName' : forms.TextInput(attrs = {'class':'form-control','placeholder':'Nhập họ tên sinh viên','required': 'true'}),
            'birthday' : forms.DateInput(attrs = {'class' : 'form-control','type':'date','required': 'true','min':f'{yearMin}-01-01','max':f'{DateNow}'}),
            'phoneNumber' : forms.NumberInput(attrs = {'class' : 'form-control','maxlength': '10','placeholder':'Nhập số điện thoại','minlength': '10','required': 'true'}),
            'address' : forms.TextInput(attrs = {'class' : 'form-control','required': 'true','placeholder':'Nhập địa chỉ'}),
            'classs' : forms.Select(attrs = {'required': 'true', 'class':'form-control choices form-select'}),
            'id' : forms.TextInput(attrs = {'class' : 'form-control','required': 'true'}),

            
        }


class UpdateStudentForm(forms.ModelForm):
    
    class Meta:
        DateNow = datetime.now().strftime("%Y-%m-%d")
        yearMax = datetime.now().strftime("%Y")
        yearMin = int(yearMax)-99
        model = Students
        fields = ('fullName','birthday','phoneNumber','address','classs')

        widgets = {
            'fullName' : forms.TextInput(attrs = {'class':'form-control','placeholder':'Nhập họ tên sinh viên','required': 'true'}),
            'birthday' : forms.DateInput(attrs = {'class' : 'form-control','type':'date','required': 'true','min':f'{yearMin}-01-01','max':f'{DateNow}'}),
            'phoneNumber' : forms.NumberInput(attrs = {'class' : 'form-control','maxlength': '10','placeholder':'Nhập số điện thoại','minlength': '10','required': 'true'}),
            'address' : forms.TextInput(attrs = {'class' : 'form-control','required': 'true','placeholder':'Nhập địa chỉ'}),
            'classs' : forms.Select(attrs = {'class' : 'form-control','required': 'true'}),
          

            
        }