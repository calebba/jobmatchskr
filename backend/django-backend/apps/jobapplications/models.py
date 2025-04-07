from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from apps.joblistings.models import JobListing


class JobApplication(models.Model):
    """Model to track user job applications"""
    
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('applied', 'Applied'),
        ('screening', 'Screening'),
        ('interviewing', 'Interviewing'),
        ('offered', 'Offered'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('withdrawn', 'Withdrawn'),
    )
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='job_applications'
    )
    job_listing = models.ForeignKey(
        JobListing,
        on_delete=models.CASCADE,
        related_name='applications'
    )
    applied_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='pending'
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s application for {self.job_listing.job_title} at {self.job_listing.company_name}"

    class Meta:
        verbose_name = "Job Application"
        verbose_name_plural = "Job Applications"
        unique_together = ['user', 'job_listing']
        ordering = ['-applied_at']