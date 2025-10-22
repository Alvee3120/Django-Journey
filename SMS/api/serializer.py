from rest_framework import serializers
from .models import DB_COURSE,DB_DEPARTMENT,DB_FACULTY,DB_STUDENT

class DB_COURSE_SERIALIZER(serializers.ModelSerializer):
    class Meta:
        model =  DB_COURSE 
        fields = '__all__'

class DB_DEPARTMENT_SERIALIZER(serializers.ModelSerializer):
    class Meta:
        model =  DB_DEPARTMENT 
        fields = '__all__'

class DDB_FACULTY_SERIALIZER(serializers.ModelSerializer):
    class Meta:
        model = DB_FACULTY 
        fields = '__all__'

class DB_STUDENT_SERIALIZER(serializers.ModelSerializer):
    class Meta:
        model =  DB_STUDENT 
        fields = '__all__'