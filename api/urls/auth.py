from django.urls import path
from api.views.auth import SendSmsCodeView, LoginWithSMSCodeView

urlpatterns = [
    path('send-code/', SendSmsCodeView.as_view()),
    path('login/', LoginWithSMSCodeView.as_view())
]
