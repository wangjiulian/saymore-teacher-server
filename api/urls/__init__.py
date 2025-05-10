from django.urls import path, include
from api.views.user import ProfileView
from api.views.course import CourseListView

urlpatterns = [
    path("auth/", include("api.urls.auth")),
    path("profile/", ProfileView.as_view()),
    path("courses/", CourseListView.as_view())
]
