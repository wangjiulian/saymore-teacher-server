from django.db import transaction, DatabaseError
from rest_framework.views import APIView
from api.utils import response
from api.models.teacher import Teacher
from api.models.teacher_subject import TeacherSubject
from api.serializers.user import UpdateProfileSerializer

import logging

logger = logging.getLogger(__name__)


class ProfileView(APIView):
    # noinspection PyMethodMayBeStatic
    def get(self, request):
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
            return response.response_400("teacher doesn't exist.")
        except Exception as e:
            logger.exception("Unexpected error when fetching teacher detail.")
            return response.response_500()

    # noinspection PyMethodMayBeStatic
    def put(self, request):
        serializer = UpdateProfileSerializer(data=request.data)
        if not serializer.is_valid():
            return response.response_400(serializer.errors)

        name = serializer.validated_data['name']
        nickname = serializer.validated_data['nickname']
        gender = serializer.validated_data['gender']
        avatar_url = serializer.validated_data['avatar_url']
        background = serializer.validated_data['background']
        education_school = serializer.validated_data['education_school']
        education_level = serializer.validated_data['education_level']
        teaching_experience = serializer.validated_data['teaching_experience']
        success_cases = serializer.validated_data['success_cases']
        teaching_achievements = serializer.validated_data['teaching_achievements']
        subject_ids = serializer.validated_data["subject_ids"]
        unique_subject_ids = list(set(subject_ids))
        teacher_id = request.user.id

        try:
            teacher = Teacher.objects.get(id=teacher_id)
            with transaction.atomic():
                teacher.name = name
                teacher.nickname = nickname
                teacher.gender = gender
                teacher.avatar_url = avatar_url
                teacher.background = background
                teacher.education_school = education_school
                teacher.education_level = education_level
                teacher.teaching_experience = teaching_experience
                teacher.success_cases = success_cases
                teacher.teaching_achievements = teaching_achievements
                teacher.save()

                # Clear all existing subject associations for the teacher
                TeacherSubject.objects.filter(teacher_id=teacher_id).delete()
                # Bulk insert new subject associations for the teacher
                TeacherSubject.objects.bulk_create([
                    TeacherSubject(teacher_id=teacher_id, subject_id=sid)
                    for sid in unique_subject_ids
                ])

                return response.response_success("Profile updated.")

        except Teacher.DoesNotExist:
            return response.response_400("teacher doesn't exist.")

        except Exception as e:
            logger.exception("Unexpected error when update profile.")
            return response.response_500()
