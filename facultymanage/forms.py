from django import forms
from stream.models import Faculty
class AddFacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['facultyName']
        widgets = {
            'facultyName' : forms.TextInput(attrs = {'class':'form-control','placeholder':'Nhập tên khoa','required': 'true'}),
        }