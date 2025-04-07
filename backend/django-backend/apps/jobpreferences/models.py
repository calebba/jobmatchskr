from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class JobPreference(models.Model):
    """Model to store user job preferences"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='job_preferences'
    )
    desired_location = models.CharField(max_length=255, blank=True)
    desired_job_title = models.CharField(max_length=255, blank=True)
    min_salary = models.IntegerField(blank=True, null=True)
    max_salary = models.IntegerField(blank=True, null=True)
    remote = models.BooleanField(default=False)
    preferred_industry = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Job Preferences - {self.desired_job_title}"

    class Meta:
        verbose_name = "Job Preference"
        verbose_name_plural = "Job Preferences"