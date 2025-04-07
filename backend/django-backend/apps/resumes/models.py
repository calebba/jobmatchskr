from django.db import models
from django.contrib.auth.models import User


class Skill(models.Model):
    """Model to represent individual skills"""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Education(models.Model):
    """Model to represent educational background"""
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255, blank=True)
    field_of_study = models.CharField(max_length=255, blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.degree} at {self.institution}"


class Experience(models.Model):
    """Model to represent work experience"""
    company = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.job_title} at {self.company}"


class Resume(models.Model):
    """Model to represent a user's resume"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='resumes'
    )
    title = models.CharField(max_length=255, default="My Resume")
    summary = models.TextField(blank=True)
    skills = models.ManyToManyField('Skill', blank=True, related_name='resumes')
    experiences = models.ManyToManyField('Experience', blank=True, related_name='resumes')
    education = models.ManyToManyField('Education', blank=True, related_name='resumes')
    resume_file = models.FileField(upload_to='resumes/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.user.username}"
