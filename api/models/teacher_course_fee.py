from django.db import models


class TeacherCourseFee(models.Model):
    # ----- Type Choices -----
    TYPE_NORMAL = 1  # Normal settlement
    TYPE_COMPENSATION = 2  # Compensation for class hours

    TYPE_CHOICES = (
        (TYPE_NORMAL, 'Normal'),
        (TYPE_COMPENSATION, 'Compensation'),
    )

    teacher_id = models.BigIntegerField(default=0, verbose_name='Teacher ID (FK)')
    student_id = models.BigIntegerField(default=0, verbose_name='Student ID (FK)')
    student_package_id = models.BigIntegerField(default=0, verbose_name='Student Package ID')
    course_id = models.BigIntegerField(default=0, verbose_name='Course ID')
    title = models.CharField(max_length=255, default='', verbose_name='Title')
    hours = models.DecimalField(max_digits=6, decimal_places=1, default=0.0, verbose_name='Teaching Hours')
    fees = models.DecimalField(max_digits=6, decimal_places=1, default=0.0, verbose_name='Fee Amount')
    type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, default=TYPE_NORMAL, verbose_name='Fee Type')
    remark = models.CharField(max_length=255, default='', verbose_name='Remark')
    updated_at = models.IntegerField(default=0, verbose_name='Updated At (timestamp)')
    created_at = models.IntegerField(default=0, verbose_name='Created At (timestamp)')

    class Meta:
        db_table = 'teacher_course_fees'
        verbose_name = 'Teacher Course Fee'
        verbose_name_plural = 'Teacher Course Fees'
        indexes = [
            models.Index(fields=['created_at'], name='idx_created_at'),
        ]
        constraints = [
            models.UniqueConstraint(fields=['course_id'], name='uidx_course_id'),
        ]

    def __str__(self):
        return f"Fee[{self.id}] - Teacher {self.teacher_id} - ¥{self.fees} for {self.hours} hrs"
