from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from api.models.course import Course
from api.models.teacher import Teacher
from api.models.sms_verfication import SMSVerification
from api.utils.sms import generate_code


class TestAuthTest(APITestCase):
    def setUp(self):
        self.teacher = Teacher.objects.create(
            phone=123456789,
            name="Test Teacher",
            is_active=True
        )
        self.client = APIClient()

    def test_login(self):
        code = generate_code()
        SMSVerification.objects.create(
            phone=123456789,
            code=code
        )

        url = "/api/teacher/auth/login"
        response = self.client.post(url, data={
            "phone": "123456789",
            "code": code,
        })

        self.assertEqual(response.status_code, 200)
