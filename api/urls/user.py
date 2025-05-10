from django.urls import path
from api.views.user import UserDetailView

urlpatterns = [
    path("detail/", UserDetailView.as_view())
]
