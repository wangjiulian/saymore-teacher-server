from rest_framework import serializers

from api.models.course import Course


class CourseListSerializer(serializers.Serializer):
    status = serializers.IntegerField(default=0, min_value=0, max_value=4)


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'subject_id', 'teacher_id', 'student_id', 'status', 'cancel_reason', 'start_time',
                  'end_time', 'trial_status', 'trial_feedback', 'is_evaluated', 'updated_at', 'created_at']
