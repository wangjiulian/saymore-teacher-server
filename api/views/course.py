from rest_framework.views import APIView
import logging

from api.serializers.course import CourseListSerializer, CourseSerializer
from api.utils import response
from api.models.course import Course

logger = logging.getLogger(__name__)


class CourseListView(APIView):

    # noinspection PyMethodMayBeStatic
    def get(self, request):
        serializer = CourseListSerializer(data=request.query_params)
        if not serializer.is_valid():
            return response.response_400(serializer.errors)

        status = serializer.validated_data["status"]
        try:

            query = Course.objects.filter(teacher_id=request.user.id)
            if not status:
                query = query.filter(status=status)
            courses = query.order_by("-created_at")

            courseSerializer = CourseSerializer(courses, many=True)

            return response.response_success(data=courseSerializer.data)

        except Exception:
            logger.exception("Unexpected error when getting course list")
            return response.response_500()
