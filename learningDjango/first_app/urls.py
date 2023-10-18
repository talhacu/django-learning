from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:num1>/", views.course_number_view, name="coursenumnerview"),
    path("<str:item>", views.course, name="course"),
    path("<int:num1>/<int:num2>/", views.multiply_view, name="multiply"),
    
]
