from django import forms
from stream.models import Class
class AddClassForm(forms.ModelForm):
    
    class Meta:
        model = Class
        fields = ('id_name','faculty')
        widgets = {
            'id_name' : forms.TextInput(attrs = {'class':'form-control','placeholder':'Nhập mã lớp','required': 'true'}),
            'faculty' : forms.Select(attrs = {'class':'form-control choices form-select','required': 'true'}),
        }