from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone


class JobListing(models.Model):
    """Model to store job listings"""
    JOB_TYPES = (
        ('full-time', 'Full Time'),
        ('part-time', 'Part Time'),
        ('contract', 'Contract'),
        ('remote', 'Remote'),
        ('hybrid', 'Hybrid'),
        ('internship', 'Internship'),
    )
    
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    job_description = models.TextField()
    skills_required = ArrayField(
        models.CharField(max_length=100),
        blank=True,
        default=list
    )
    salary = models.IntegerField(null=True, blank=True)
    job_type = models.CharField(max_length=50, choices=JOB_TYPES)
    url = models.URLField(max_length=255)
    source = models.CharField(max_length=255)
    posted_at = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"

    class Meta:
        verbose_name = "Job Listing"
        verbose_name_plural = "Job Listings"
        indexes = [
            models.Index(fields=['job_title']),
            models.Index(fields=['company_name']),
            models.Index(fields=['location']),
            models.Index(fields=['posted_at']),
        ]