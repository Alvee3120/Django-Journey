from rest_framework import serializers
from .models import Student

class Student_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        