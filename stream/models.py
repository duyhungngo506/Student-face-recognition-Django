from django.db import models

# Create your models here.

class Faculty(models.Model):
    facultyName = models.CharField(max_length=100,null=False,unique=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    class Meta:
        db_table = "tbl_faculty"
    def __str__(self):
        return self.facultyName
        

class Class(models.Model):
    id_name = models.CharField(primary_key=True,max_length=100)
    faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    class Meta:
        db_table = "tbl_class"
    def __str__(self):
        return self.id_name

class Students(models.Model):
    id = models.CharField(primary_key=True,max_length=100)
    fullName = models.CharField(max_length=100,null=False)
    classs = models.ForeignKey(Class,on_delete=models.CASCADE)
    address = models.CharField(max_length=200,null=False)
    phoneNumber = models.CharField(max_length=10, null=False)
    birthday = models.DateField(null=False)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    class Meta:
        db_table = "tbl_students"
    def __str__(self):
        return self.fullName

class Recognition(models.Model):
    students = models.ForeignKey(Students, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    class Meta:
        db_table = "tbl_recognition"

class Stranger(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    imgName = models.CharField(max_length=100,null=False)
    class Meta:
        db_table = "tbl_strangers"


