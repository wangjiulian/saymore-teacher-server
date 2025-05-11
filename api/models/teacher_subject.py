from django.db import models
from api.utils.datetime_utils import get_utc_timestamp


class TeacherSubject(models.Model):
    teacher_id = models.BigIntegerField(default=0, verbose_name="Teacher ID")
    subject_id = models.IntegerField(default=0, verbose_name="Subject ID")
    updated_at = models.IntegerField(default=get_utc_timestamp, verbose_name="Updated At (timestamp)")
    created_at = models.IntegerField(default=get_utc_timestamp, verbose_name="Created At (timestamp)")

    def save(self, *args, **kwargs):
        self.updated_at = get_utc_timestamp()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'teacher_subjects'
        verbose_name = 'Teacher Subject'
        verbose_name_plural = 'Teacher Subjects'
        constraints = [
            models.UniqueConstraint(fields=['teacher_id', 'subject_id'], name='uidx_teacher_subject'),
        ]

    def __str__(self):
        return f"Teacher {self.teacher_id} - Subject {self.subject_id}"
