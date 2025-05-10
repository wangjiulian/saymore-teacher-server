from rest_framework.response import Response
from rest_framework import status


def response_400(detail="Bad request", code=400):
    return Response({"error": detail}, status=status.HTTP_400_BAD_REQUEST)


def response_404(detail="Not found", code=404):
    return Response({"error": detail}, status=status.HTTP_404_NOT_FOUND)


def response_500(detail="Internal server error", code=500):
    return Response({"error": detail}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def response_success(message="success", data=None, code=200):
    return Response({"message": message, "data": data}, status=status.HTTP_200_OK)
