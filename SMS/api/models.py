from django.db import models

# Create your models here.

class DB_DEPARTMENT(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=20)
    faculty = models.ForeignKey('DB_FACULTY' , on_delete=models.SET_NULL, null=True,blank=True ,related_name='departments')

    def __str__(self):
        return self.department_name
        

class DB_FACULTY(models.Model):
    faculty_id = models.AutoField(primary_key=True)
    faculty_name = models.CharField(max_length=100)
    faculty_email = models.EmailField(unique=True)
    department = models.ForeignKey('DB_DEPARTMENT', on_delete=models.CASCADE, related_name='faculties')

    def __str__(self):
        return self.faculty_name


class DB_COURSE(models.Model):
    course_code = models.CharField(max_length=12, primary_key=True)
    course_name = models.CharField(max_length=100)
    department = models.ForeignKey('DB_DEPARTMENT', on_delete=models.CASCADE , related_name='courses')
    instructor = models.ForeignKey('DB_FACULTY', on_delete=models.SET_NULL, null=True, blank=True, related_name='courses')

    def __str__(self):
        return self.course_name


class DB_STUDENT(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=100)
    student_mail = models.EmailField(unique=True)
    student_age = models.PositiveIntegerField()
    student_department = models.ForeignKey('DB_DEPARTMENT', on_delete=models.CASCADE, related_name='students')
    student_courses = models.ManyToManyField('DB_COURSE', related_name='students')

    def __str__(self):
        return self.student_name








