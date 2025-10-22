from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from cbvapp import views

urlpatterns = [
    path("student/", views.StudentsList.as_view()),
    path("student/<int:pk>/", views.StudentDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)