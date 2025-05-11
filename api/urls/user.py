from django.urls import path
from api.views.user import ProfileView

urlpatterns = [
    path("profile/", ProfileView.as_view())
]
