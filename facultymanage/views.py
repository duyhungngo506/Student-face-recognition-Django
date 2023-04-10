from django.shortcuts import render,redirect
from .forms import AddFacultyForm
from stream.models import Faculty
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
@login_required(login_url='/admin/login')
# Create your views here.
def index(request):
    form = AddFacultyForm()
    facultys = Faculty.objects.all()
    content = {'form': form,'facultys': facultys}
    return render(request,'facultymanage.html',content);


def addfaculty(request):
    if request.method == 'POST':
        form = AddFacultyForm(request.POST)
        if form.is_valid():
            facultyName = request.POST['facultyName']
            facultys = Faculty()
            facultys.facultyName = facultyName
            facultys.save()
            messages.add_message(request, messages.SUCCESS, 'Thêm khoa thành công!')
            return redirect('/faculymanage')
    else:
        form = AddFacultyForm()
    return render(request,'facultymanage.html',{'form': form})
        
    # return HttpResponse('add')

def deletefaculty(request,pk):
    facultys = Faculty.objects.get(id = pk)
    facultys.delete()
    messages.add_message(request, messages.INFO, 'Xóa khoa thành công!')
    return redirect('/faculymanage')
    return HttpResponse('delete')
def editfaculty(request,pk):
    facultyEdit = Faculty.objects.get(id = pk)
    form = AddFacultyForm(instance=facultyEdit)
    return render(request,'updatefaculty.html',{'form': form, 'pk': pk})
    # return HttpResponse('add')
def updatefaculty(request,pk):
    # return HttpResponse(pk)
    if request.method == 'POST':
        form = AddFacultyForm(request.POST)
        if form.is_valid():
            
            facultyName = request.POST['facultyName']
            facultys = Faculty.objects.get(id = pk)
            facultys.facultyName = facultyName
            facultys.save()
            messages.add_message(request, messages.SUCCESS, 'Cập nhật khoa thành công!')
            return render(request,'updatefaculty.html',{'form': form,'pk': pk})
    else:
        facultyEdit = Faculty.objects.get(id = pk)
        form = AddFacultyForm(instance=facultyEdit)
    return render(request,'updatefaculty.html',{'form': form,'pk': pk})
   