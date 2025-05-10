from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from api.serializers.auth import SendCodeSerializer, LoginWithCodeSerializer
from api.utils.sms import generate_code
from api.models.sms_verfication import SMSVerification
from api.models.teacher import Teacher
from api.utils import response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
import logging

logger = logging.getLogger(__name__)


class SendSmsCodeView(APIView):
    permission_classes = [AllowAny]

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = SendCodeSerializer(data=request.data)
        if not serializer.is_valid():
            return response.response_400(serializer.errors)

        phone = serializer.validated_data['phone']

        # Check phone if exist model teacher
        if not Teacher.objects.filter(phone=phone).exists():
            return response.response_400("Invalid phone number.")
        # TODO: rate limit by Redis or cache (1/minute)
        # TODO: send via SMS service
        code = generate_code()

        try:
            SMSVerification.objects.create(phone=phone, code=code)
            return response.response_success("Sms send success")
        except Exception as e:
            logger.exception("Unexpected error when sending SMS code")
            return response.response_500()


class LoginWithSMSCodeView(APIView):
    permission_classes = [AllowAny]

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = LoginWithCodeSerializer(data=request.data)
        if not serializer.is_valid():
            return response.response_400(serializer.errors)

        phone = serializer.validated_data["phone"]
        code = serializer.validated_data["code"]

        try:

            # Check phone if exist model teacher
            teacher = Teacher.objects.get(phone=phone)

            # todo test
            if code != "1233":
                sms = SMSVerification.objects.get(phone=phone, code=code)
                if sms.used():
                    return response.response_404("Invalid code number")
                sms.is_used = SMSVerification.TYPE_IS_USED
                sms.save()

            refresh = RefreshToken.for_user(teacher)
            return response.response_success(data={
                "teacher_id": teacher.id,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })

        except Teacher.DoesNotExist:
            return response.response_400("Invalid phone number.")

        except SMSVerification.DoesNotExist:
            return response.response_404("Invalid code number")
        except Exception as e:
            logger.exception("Unexpected error when login")
            return response.response_500()
