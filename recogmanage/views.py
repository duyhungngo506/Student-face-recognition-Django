import os
from django.shortcuts import render,redirect
from django.contrib import messages
from stream.models import Students,Recognition,Stranger
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def deleteRecognition(request,pk):
    # return HttpResponse(pk)
    recognition = Recognition.objects.get(id = pk)
    recognition.delete()
    messagedelete = "Xóa thành công"
    messages.add_message(request, messages.SUCCESS, 'Xóa thành công!')
    return redirect('/admin')
# Create your views here.
def DeleteAllStranger(request):
    stg = Stranger.objects.all()
    for stgg in stg:
        path = "stream/static/Unknow/"+stgg.imgName
        delete_file(path)
    stg.delete()
    return redirect('/admin/stranger')
def deleteStranger(request,pk):
    path = "stream/static/Unknow/"+pk+".jpg"
    delete_file(path)
    stg = Stranger.objects.get(id = pk)
    stg.delete()
    return redirect('/admin/stranger')

def delete_file(path):
    """ Deletes file from filesystem. """
    if os.path.exists(path):
       os.remove(path)
    else:
        return

def ShowStranger(request):
    strangers = Stranger.objects.all()
    return render(request,'stranger.html',{'strangers': strangers})


@login_required(login_url='/admin/login')
def recogmanage(request):
    students = Students.objects.raw("SELECT tbl_recognition.id AS id_recogmanage,tbl_students.id,tbl_students.fullName,tbl_students.address,tbl_students.classs_id,tbl_students.birthday,tbl_students.phoneNumber,tbl_recognition.date,tbl_recognition.time AS time ,tbl_faculty.facultyName FROM `tbl_students`,`tbl_recognition`,`tbl_faculty`,`tbl_class` WHERE tbl_students.id = tbl_recognition.students_id AND tbl_class.faculty_id = tbl_faculty.id and tbl_students.classs_id = tbl_class.id_name ORDER BY tbl_recognition.id DESC") 
    # return render(request,'recogmanage.html')
  

    return render(request,'recogmanage.html',{'students': students})