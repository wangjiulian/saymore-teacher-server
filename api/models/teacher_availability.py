from django.db import models


class TeacherAvailability(models.Model):
    teacher_id = models.BigIntegerField(default=0, verbose_name="Teacher ID (FK)")
    course_id = models.BigIntegerField(default=0, verbose_name="Course ID (FK)")
    start_time = models.BigIntegerField(verbose_name="Available Start Time (Unix timestamp, seconds)")
    end_time = models.BigIntegerField(verbose_name="Available End Time (Unix timestamp, seconds)")
    updated_at = models.IntegerField(default=0, verbose_name="Updated At (Unix timestamp)")
    created_at = models.IntegerField(default=0, verbose_name="Created At (Unix timestamp)")

    class Meta:
        db_table = "teacher_availabilities"
        verbose_name = "Teacher Availability"
        verbose_name_plural = "Teacher Availabilities"
        indexes = [
            models.Index(fields=['teacher_id'], name='idx_teacher_id'),
            models.Index(fields=['course_id'], name='idx_course_id'),
            models.Index(fields=['start_time', 'end_time'], name='idx_start_time_end_time'),
        ]

    def __str__(self):
        return f"Teacher {self.teacher_id} Available: {self.start_time} - {self.end_time}"