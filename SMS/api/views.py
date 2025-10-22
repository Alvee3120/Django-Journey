from rest_framework import viewsets
from .models import DB_COURSE, DB_DEPARTMENT, DB_FACULTY , DB_STUDENT
from .serializer import DB_COURSE_SERIALIZER , DB_DEPARTMENT_SERIALIZER , DDB_FACULTY_SERIALIZER, DB_STUDENT_SERIALIZER

class CourseViewSet(viewsets.ModelViewSet):
    queryset = DB_COURSE.objects.all()
    serializer_class = DB_COURSE_SERIALIZER

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = DB_DEPARTMENT.objects.all()
    serializer_class = DB_DEPARTMENT_SERIALIZER

class FacultyViewSet(viewsets.ModelViewSet):
    queryset = DB_FACULTY.objects.all()
    serializer_class = DDB_FACULTY_SERIALIZER

class StudentViewSet(viewsets.ModelViewSet):
    queryset = DB_STUDENT.objects.all()
    serializer_class = DB_STUDENT_SERIALIZER