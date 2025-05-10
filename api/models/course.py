from django.db import models


class Course(models.Model):
    # ----- Course Type -----
    TYPE_FORMAL = 1
    TYPE_TRIAL = 2
    COURSE_TYPE_CHOICES = (
        (TYPE_FORMAL, 'Formal'),
        (TYPE_TRIAL, 'Trial'),
    )

    # ----- Course Status -----
    STATUS_PENDING = 1
    STATUS_IN_PROGRESS = 2
    STATUS_COMPLETED = 3
    STATUS_CANCELLED = 4
    STATUS_CHOICES = (
        (STATUS_PENDING, 'Pending'),
        (STATUS_IN_PROGRESS, 'In Progress'),
        (STATUS_COMPLETED, 'Completed'),
        (STATUS_CANCELLED, 'Cancelled'),
    )

    # ----- Trial Status -----
    TRIAL_NONE = 0
    TRIAL_SUCCESS = 1
    TRIAL_FAILURE = 2
    TRIAL_STATUS_CHOICES = (
        (TRIAL_NONE, 'None'),
        (TRIAL_SUCCESS, 'Success'),
        (TRIAL_FAILURE, 'Failure'),
    )

    # ----- Evaluation Status -----
    EVALUATED = 1
    NOT_EVALUATED = 2
    EVALUATION_STATUS_CHOICES = (
        (EVALUATED, 'Evaluated'),
        (NOT_EVALUATED, 'Not Evaluated'),
    )

    course_type = models.PositiveSmallIntegerField(choices=COURSE_TYPE_CHOICES, default=TYPE_FORMAL,
                                                   verbose_name='Course Type')
    name = models.CharField(max_length=100, default='', verbose_name='Course Name')
    subject_id = models.IntegerField(default=0, verbose_name='Subject ID')
    teacher_id = models.BigIntegerField(default=0, verbose_name='Teacher ID')
    student_id = models.BigIntegerField(default=0, verbose_name='Student ID')
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=STATUS_PENDING,
                                              verbose_name='Course Status')
    cancel_reason = models.CharField(max_length=255, default='', verbose_name='Cancel Reason')
    start_time = models.BigIntegerField(default=0, verbose_name='Start Time (Unix Timestamp)')
    end_time = models.BigIntegerField(default=0, verbose_name='End Time (Unix Timestamp)')
    trial_status = models.PositiveSmallIntegerField(choices=TRIAL_STATUS_CHOICES, default=TRIAL_NONE,
                                                    verbose_name='Trial Status')
    trial_feedback = models.TextField(null=True, blank=True, verbose_name='Trial Feedback')
    is_evaluated = models.PositiveSmallIntegerField(choices=EVALUATION_STATUS_CHOICES, default=NOT_EVALUATED,
                                                    verbose_name='Evaluation Status')
    updated_at = models.IntegerField(default=0, verbose_name='Updated At')
    created_at = models.IntegerField(default=0, verbose_name='Created At')

    class Meta:
        db_table = 'courses'
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        indexes = [
            models.Index(fields=['teacher_id'], name='idx_teacher_id'),
            models.Index(fields=['student_id'], name='idx_student_id'),
            models.Index(fields=['subject_id'], name='idx_subject_id'),
            models.Index(fields=['start_time', 'end_time'], name='idx_start_time_end_time'),
        ]

    def __str__(self):
        return f"{self.name} (Teacher: {self.teacher_id}, Student: {self.student_id})"
