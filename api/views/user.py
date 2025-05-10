from rest_framework.views import APIView
from api.utils import response
from api.models.teacher import Teacher
import logging

logger = logging.getLogger(__name__)


class ProfileView(APIView):
    # noinspection PyMethodMayBeStatic
    def post(self, request):
        try:
            teacher = Teacher.objects.get(id=request.user.id)
            data = {
                "id": teacher.id,
                "name": teacher.name,
                "nickname": teacher.nickname,
                "avatar_url": teacher.avatar_url,
                "gender": teacher.gender,
                "course_hours": teacher.course_hours,
                "background": teacher.background,
                "education_school": teacher.education_school,
                "education_level": teacher.education_level,
                "teaching_experience": teacher.teaching_experience,
                "success_cases": teacher.success_cases,
                "teaching_achievements": teacher.teaching_achievements,
                'evaluation': teacher.evaluation,
            }

            return response.response_success(data=data)

        except Teacher.DoesNotExist:
            return response.response_400("teacher doesn't exist")
        except Exception as e:
            logger.exception("Unexpected error when fetching teacher detail")
            return response.response_500()
