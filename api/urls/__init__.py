from django.urls import path, include

urlpatterns = [
    path("auth/", include("api.urls.auth")),
    path("user/", include("api.urls.user"))
]
