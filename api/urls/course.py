from django.urls import path
from api.views.course import CourseListView

urlpatterns = [
    path("courses/", CourseListView.as_view())
]
