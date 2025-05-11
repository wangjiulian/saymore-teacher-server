from rest_framework import serializers


class UpdateProfileSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    nickname = serializers.CharField(max_length=50)
    gender = serializers.IntegerField(min_value=1, max_value=2)
    avatar_url = serializers.CharField(max_length=255)
    background = serializers.CharField(max_length=500)
    education_school = serializers.CharField(max_length=100)
    education_level = serializers.IntegerField(min_value=1, max_value=3)
    teaching_experience = serializers.CharField(max_length=500)
    success_cases = serializers.CharField(max_length=500)
    teaching_achievements = serializers.CharField(max_length=500)
    subject_ids = serializers.ListField(
        child=serializers.IntegerField(min_value=1),
        allow_empty=False,
        required=True
    )
