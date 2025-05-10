from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from api.models.course import Course
from api.models.teacher import Teacher


class TestCourseListTest(APITestCase):
    def setUp(self):
        self.teacher = Teacher.objects.create(
            phone=123456789,
            name="Test Teacher",
            is_active=True
        )

        Course.objects.create(
            name="Math",
            teacher_id=self.teacher.id,
            status=1,
            start_time=1715000000,
            end_time=1715003600,
        )

        refresh = RefreshToken.for_user(self.teacher)
        self.access_token = str(refresh.access_token)

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

    def test_course_list(self):
        url = "/api/teacher/courses/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('data', response.data)
        self.assertEqual(len(response.data['data']), 1)
