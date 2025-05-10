from django.db import models


class SMSVerification(models.Model):
    TYPE_TEACHER_LOGIN = 1
    TYPE_CHOICES = (
        (TYPE_TEACHER_LOGIN, 'Teacher login'),
        # Extendable for other types
    )

    TYPE_IS_USED = 1
    TYPE_UN_USED = 2
    IS_USED_CHOICES = (
        (TYPE_IS_USED, 'Used'),
        (TYPE_UN_USED, 'Unused'),
    )

    phone = models.CharField(max_length=20, default='', verbose_name='Phone number')
    code = models.CharField(max_length=50, default='', verbose_name='Verification code')
    type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, default=1, verbose_name='Code type')
    is_used = models.PositiveSmallIntegerField(choices=IS_USED_CHOICES, default=2, verbose_name='Used or not')
    updated_at = models.IntegerField(default=0, verbose_name='Updated timestamp')
    created_at = models.IntegerField(default=0, verbose_name='Created timestamp')
    expires_at = models.DateTimeField(null=True, blank=True, verbose_name='Expiration time')

    def used(self):
        return self.is_used == SMSVerification.TYPE_IS_USED

    class Meta:
        db_table = 'sms_verifications'
        verbose_name = 'SMS Verification Code'
        verbose_name_plural = 'SMS Verification Code Records'

    def __str__(self):
        return f"{self.phone} - {self.code} ({'Used' if self.is_used == 1 else 'Unused'})"
