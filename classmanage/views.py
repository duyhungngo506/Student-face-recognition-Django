from django.contrib import messages
from django.shortcuts import render,redirect
from .forms import AddClassForm
from stream.models import Class
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
@login_required(login_url='/admin/login')
# Create your views here.
def index(request):
    form = AddClassForm()
    classs = Class.objects.all()
    content = {'form': form,'classs': classs}
    return render(request,'classmanage.html',content)

def addClass(request):
    if request.method == 'POST':
        form = AddClassForm(request.POST)
        if form.is_valid():
            idclass = request.POST['id_name']
            faculty = request.POST['faculty']
            classs = Class()
            classs.id_name = idclass
            classs.faculty_id = faculty
            classs.save()
            messages.add_message(request, messages.SUCCESS, 'Thêm lớp thành công!')
            return redirect('/classmanage')
    else:
        form = AddClassForm()
    return render(request,'classmanage.html',{'form': form})
        
    return HttpResponse('add')

def deleteClass(request,pk):
    classs = Class.objects.get(id_name = pk)
    classs.delete()
    messages.add_message(request, messages.INFO, 'Xóa lớp thành công!')
    return redirect('/classmanage')
    return HttpResponse('delete')
def editClass(request,pk):
    classEdit = Class.objects.get(id_name = pk)
    form = AddClassForm(instance=classEdit)
    return render(request,'updateclass.html',{'form': form, 'pk': pk})
    # return HttpResponse('add')
def updateClass(request,pk):
    # return HttpResponse(pk)
    if request.method == 'POST':
        form = AddClassForm(request.POST)
        if form.is_valid():
            idclass = request.POST['id_name']
            faculty = request.POST['faculty']
            classs = Class.objects.get(id_name = pk)
            classs.delete()
            classss = Class()
            classss.id_name = idclass
            classss.faculty_id = faculty
            classss.save()
            messages.add_message(request, messages.SUCCESS, 'Cập nhật lớp thành công!')
            return render(request,'updateclass.html',{'form': form,'pk': pk})
    else:
        classEdit = Class.objects.get(id_name = pk)
        form = AddClassForm(instance=classEdit)
    return render(request,'updateclass.html',{'form': form,'pk': pk})
   