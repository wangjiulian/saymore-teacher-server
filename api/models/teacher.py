from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    GENDER_CHOICES = (
        (0, 'Unknown'),
        (1, 'Male'),
        (2, 'Female'),
    )

    EDUCATION_LEVEL_CHOICES = (
        (0, 'Unknown'),
        (1, 'Bachelor'),
        (2, 'Master'),
        (3, 'PhD'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone = models.CharField(max_length=20, unique=True, default='', verbose_name='Phone Number')
    name = models.CharField(max_length=50, default='', verbose_name='Full Name')
    nickname = models.CharField(max_length=50, default='', verbose_name='Nickname')
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='Gender')
    course_hours = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='Teaching Hours')
    avatar_url = models.CharField(max_length=255, default='', verbose_name='Avatar URL')
    background = models.TextField(null=True, blank=True, verbose_name='Personal Background')
    video_url = models.CharField(max_length=255, default='', verbose_name='Introduction Video URL')
    education_school = models.CharField(max_length=100, default='', verbose_name='Alma Mater')
    education_level = models.PositiveSmallIntegerField(choices=EDUCATION_LEVEL_CHOICES, default=0,
                                                       verbose_name='Education Level')
    teaching_start_date = models.DateField(null=True, blank=True, verbose_name='Start Date of Teaching')
    notes = models.TextField(null=True, blank=True, verbose_name='Notes')
    teaching_experience = models.TextField(null=True, blank=True, verbose_name='Teaching Experience')
    success_cases = models.TextField(null=True, blank=True, verbose_name='Success Cases')
    teaching_achievements = models.TextField(null=True, blank=True, verbose_name='Teaching Achievements')
    evaluation = models.DecimalField(max_digits=4, decimal_places=1, default=0.0, verbose_name='Rating')
    is_active = models.BooleanField(default=False, verbose_name='Is Active')
    is_recommend = models.BooleanField(default=False, verbose_name='Is Recommended')
    updated_at = models.IntegerField(default=0, verbose_name='Updated Timestamp')
    created_at = models.IntegerField(default=0, verbose_name='Created Timestamp')

    class Meta:
        db_table = 'teachers'
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    def __str__(self):
        return f"{self.name} ({self.phone})"
