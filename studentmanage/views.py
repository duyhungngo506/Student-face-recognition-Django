from django.shortcuts import render,redirect
from .forms import AddStudentForm,UpdateStudentForm
from stream.models import Students
import os
import cv2
import pickle
import face_recognition
import numpy
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def addStudent(request):
    global face_names
    global encodeListKnow
    if request.method == 'POST':
        form = AddStudentForm(request.POST, request.FILES)
        if form.is_valid():
            fullname = request.POST['fullName']
            birthday = request.POST['birthday']
            phoneNumber = request.POST['phoneNumber']
            classs = request.POST['classs']
            address = request.POST['address']
            nameimg = request.POST['id']
            file = request.FILES['file'] 
            resultPhone  = str(phoneNumber)
         
            # kiểm tra số điện thoại
            if (len(phoneNumber) > 10 or len(phoneNumber) < 10 or resultPhone[0] != '0'):
                messages.add_message(request, messages.ERROR, 'Số điện thoại không đúng định dạng')   
                return redirect('/studentmanage')

            curentImg = cv2.imdecode(numpy.fromstring(request.FILES['file'].read(), numpy.uint8), cv2.IMREAD_UNCHANGED)
            curentImgRGB = cv2.cvtColor(curentImg, cv2.COLOR_BGR2RGB)
            faceloc = face_recognition.face_locations(curentImgRGB)
            if len(faceloc)==1:
                filename = file.name
                filename = "%s.%s" % ( nameimg,"jpg")
                attach= FileSystemStorage(location='stream/DataRaw')
                attach.save(filename,file)
                curentImg = cv2.imread(f"stream/DataRaw/{filename}")
                curentImgRGB = cv2.cvtColor(curentImg, cv2.COLOR_BGR2RGB)
                #Cắt khuôn mặt và lưu vào DataTrain
                top, right, bottom, left = faceloc[0]
                sub_face = curentImg[top :bottom ,left :right ]
                sub_faceRGB = curentImgRGB[top :bottom ,left :right ]
                folder_out = "stream/DataTrain"
                folder_out2 = "stream/static"
                file_path = folder_out + "/" + filename
                file_path2 = folder_out2 + "/" + filename
                cv2.imwrite(file_path, sub_faceRGB)
                cv2.imwrite(file_path2, sub_face)
                print(f"Process: {filename}")
                #lưu encode khuôn mặt vào data mẫu:
                all_face_encodings=[]
                with open('dataset_faces.dat', 'rb') as f1:
                    all_face_encodings = pickle.load(f1)
                all_face_encodings[nameimg] = face_recognition.face_encodings(curentImgRGB)[0]
                with open('dataset_faces.dat', 'wb') as f1:
                    pickle.dump(all_face_encodings, f1)
                with open('dataset_faces.dat', 'rb') as f1:
                    all_face_encodings = pickle.load(f1)
                    face_names = list(all_face_encodings.keys())
                    encodeListKnow = numpy.array(list(all_face_encodings.values()))
                std = Students()
                std.id = nameimg
                std.fullName = fullname
                std.address = address
                std.phoneNumber = phoneNumber
                std.birthday = birthday
                std.classs_id = classs
                std.save()      
                messages.add_message(request, messages.SUCCESS, 'Thêm sinh viên thành công!')
                # std = Students.objects.create(nameimg,fullname,address,phoneNumber,birthday,classs)
                return redirect('/studentmanage')
            else:
                messages.add_message(request, messages.ERROR, 'Hình ảnh bắt buộc phải có duy nhất một khuôn mặt')   
                # std = Students.objects.create(nameimg,fullname,address,phoneNumber,birthday,classs)
                return redirect('/studentmanage')
           
           
    else:
        form = AddStudentForm()
    return render(request,'studentmanage.html',{'form': form})

def deleteStudent(request,pk):
    pathDataRaw = "stream/DataRaw/" + pk + ".jpg"
    pathDataTrain = "stream/DataTrain/" + pk + ".jpg"
    pathstatic = "stream/static/" + pk + ".jpg"
    std = Students.objects.get(id = pk)
    
    std.delete()
    delete_file(pathDataRaw)
    delete_file(pathDataTrain)
    delete_file(pathstatic)
    all_face_encodings=[]
    with open('dataset_faces.dat', 'rb') as f1:
        all_face_encodings = pickle.load(f1)
        print(len(all_face_encodings))
    del all_face_encodings[pk]
    with open('dataset_faces.dat', 'wb') as f1:
        pickle.dump(all_face_encodings, f1)
    with open('dataset_faces.dat', 'rb') as f1:
        all_face_encodings = pickle.load(f1)
        face_names = list(all_face_encodings.keys())
        encodeListKnow = numpy.array(list(all_face_encodings.values()))
    messages.add_message(request, messages.SUCCESS, 'Xóa thành công')   
    return redirect('/studentmanage')
  
def delete_file(path):
    """ Deletes file from filesystem. """
    if os.path.exists(path):
       os.remove(path)
    else:
        return

def updateStudent(request,pk):
    global face_names
    global encodeListKnow
    if request.method == 'POST':
        form = UpdateStudentForm(request.POST, request.FILES)
        if form.is_valid():
            fullname = request.POST['fullName']
            birthday = request.POST['birthday']
            phoneNumber = request.POST['phoneNumber']
            classs = request.POST['classs']
            address = request.POST['address']
            nameimg = pk
            if (request.FILES.get('file')):
                file = request.FILES['file']   
                resultPhone  = str(phoneNumber)
            
                # kiểm tra số điện thoại
                if (len(phoneNumber) != 10 or resultPhone[0] != '0'):
                    messages.add_message(request, messages.ERROR, 'Số điện thoại không đúng định dạng')
                    return redirect('/studentmanage/edit-std/'+pk+'/')

                curentImg = cv2.imdecode(numpy.fromstring(request.FILES['file'].read(), numpy.uint8), cv2.IMREAD_UNCHANGED)
                curentImgRGB = cv2.cvtColor(curentImg, cv2.COLOR_BGR2RGB)
                faceloc = face_recognition.face_locations(curentImgRGB)
                if len(faceloc)==1:
                    filename = file.name
                    filename = "%s.%s" % ( nameimg,"jpg")
                    path = "stream/DataRaw/"+filename
                    cv2.imwrite(path, curentImg)
                    curentImg = cv2.imread(f"stream/DataRaw/{filename}")
                    curentImgRGB = cv2.cvtColor(curentImg, cv2.COLOR_BGR2RGB)
                    #Cắt khuôn mặt và lưu vào DataTrain
                    top, right, bottom, left = faceloc[0]
                    sub_face = curentImg[top :bottom ,left :right ]
                    sub_faceRGB = curentImgRGB[top :bottom ,left :right ]
                    folder_out = "stream/DataTrain"
                    folder_out2 = "stream/static"
                    file_path = folder_out + "/" + filename
                    file_path2 = folder_out2 + "/" + filename
                    cv2.imwrite(file_path, sub_faceRGB)
                    cv2.imwrite(file_path2, sub_face)
                    print(f"Process: {filename}")
                    #lưu encode khuôn mặt vào data mẫu:
                    all_face_encodings=[]
                    with open('dataset_faces.dat', 'rb') as f1:
                        all_face_encodings = pickle.load(f1)
                    all_face_encodings[nameimg] = face_recognition.face_encodings(curentImgRGB)[0]
                    with open('dataset_faces.dat', 'wb') as f1:
                        pickle.dump(all_face_encodings, f1)
                    with open('dataset_faces.dat', 'rb') as f1:
                        all_face_encodings = pickle.load(f1)
                        face_names = list(all_face_encodings.keys())
                        encodeListKnow = numpy.array(list(all_face_encodings.values()))
                    std = Students.objects.get(id = pk)
                    std.id = nameimg
                    std.fullName = fullname
                    std.address = address
                    std.phoneNumber = phoneNumber
                    std.birthday = birthday
                    std.classs_id = classs
                    std.save()  
                    messages.add_message(request, messages.SUCCESS, 'Cập nhật sinh viên thành công!')
                    # std = Students.objects.create(nameimg,fullname,address,phoneNumber,birthday,classs)
                    return redirect('/studentmanage/edit-std/'+pk+'/')
                else:
                    messages.add_message(request, messages.ERROR, 'Hình ảnh bắt buộc phải có duy nhất một khuôn mặt') 
                    # std = Students.objects.create(nameimg,fullname,address,phoneNumber,birthday,classs)
                    return redirect('/studentmanage/edit-std/'+pk+'/')
            else:
                
                resultPhone  = str(phoneNumber)
                # kiểm tra số điện thoại
                if (len(phoneNumber) != 10 or resultPhone[0] != '0'):
                    messages.success(request,'Số điện thoại không đúng định dạng')
                    return redirect('/studentmanage/edit-std/'+pk+'/')
                std = Students.objects.get(id = pk)
                std.id = nameimg
                std.fullName = fullname
                std.address = address
                std.phoneNumber = phoneNumber
                std.birthday = birthday
                std.classs_id = classs
                std.save()  
                messages.add_message(request, messages.SUCCESS, 'Cập nhật sinh viên thành công!')
                return render(request,'updatestudent.html',{'form': form,'pk': pk})
                
            
           
           
    else:
        studentEdit = Students.objects.get(id = pk)
        form = UpdateStudentForm(instance=studentEdit)
    return render(request,'updatestudent.html',{'form': form,'pk': pk})

def editStudent(request,pk):
    studentEdit = Students.objects.get(id = pk)
    form = UpdateStudentForm(instance=studentEdit)
    return render(request,'updatestudent.html',{'form': form, 'pk': pk})
@login_required(login_url='/admin/login')
def index(request):
    form = AddStudentForm
    listStudent =  Students.objects.raw("SELECT tbl_students.*,tbl_faculty.facultyName FROM `tbl_class`,`tbl_faculty`,`tbl_students` WHERE tbl_class.id_name = tbl_students.classs_id AND tbl_class.faculty_id = tbl_faculty.id ORDER BY tbl_students.created_at DESC")
    return render(request,'studentmanage.html',{'form': form,'liststudent': listStudent })