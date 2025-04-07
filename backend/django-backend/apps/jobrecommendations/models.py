from django.db import models
from django.contrib.auth.models import User
from apps.joblistings.models import JobListing
from django.utils import timezone


class JobRecommendation(models.Model):
    """Model to store AI-generated job recommendations for users"""
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='job_recommendations'
    )
    job_listing = models.ForeignKey(
        JobListing,
        on_delete=models.SET_NULL,
        null=True,
        related_name='recommendations'
    )
    relevance_score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text="AI-generated score based on match percentage (0-100)"
    )
    recommended_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        if self.job_listing:
            return f"Recommendation for {self.user.username}: {self.job_listing.job_title} ({self.relevance_score}%)"
        return f"Recommendation for {self.user.username}: [Deleted Job] ({self.relevance_score}%)"

    class Meta:
        verbose_name = "Job Recommendation"
        verbose_name_plural = "Job Recommendations"
        ordering = ['-relevance_score', '-recommended_at']  # Order by relevance score, then recommendation date
        indexes = [
            models.Index(fields=['-relevance_score']),
            models.Index(fields=['-recommended_at']),
        ]