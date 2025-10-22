# from .models import Student
# from .serializers import Student_Serializer
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status


# class StudentsList(APIView):
#     """
#     List all Student, or create a new Student.
#     """

#     def get(self, request, format=None):
#         student = Student.objects.all()
#         serializer = Student_Serializer(student, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = Student_Serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class StudentDetail(APIView):
#     """
#     Retrieve, update or delete a Student instance.
#     """

#     def get_object(self, pk):
#         try:
#             return Student.objects.get(pk=pk)
#         except Student.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         Student = self.get_object(pk)
#         serializer = Student_Serializer(Student)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         Student = self.get_object(pk)
#         serializer = Student_Serializer(Student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         Student = self.get_object(pk)
#         Student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



from .models import Student
from .serializers import Student_Serializer
from rest_framework import generics


class StudentsList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = Student_Serializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
       queryset = Student.objects.all()
       serializer_class = Student_Serializer