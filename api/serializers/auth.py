from rest_framework import serializers


class SendCodeSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=15)


class LoginWithCodeSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=15)
    code = serializers.CharField(max_length=6)
