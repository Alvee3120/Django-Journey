from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, FacultyViewSet, StudentViewSet, DepartmentViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')
router.register(r'faculties', FacultyViewSet, basename='faculty')
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'departments', DepartmentViewSet, basename='department')



urlpatterns = [

    path('', include(router.urls))
]