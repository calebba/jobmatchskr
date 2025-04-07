from django.db import models
from django.contrib.auth.models import User  # Use Django's default User model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _

class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
	address = models.TextField(blank=True, null=True)
	phone_number = models.CharField(max_length=15, blank=True, null=True)
	date_of_birth = models.DateField(blank=True, null=True)

	def __str__(self):
		return f"{self.user.username}'s Customer Profile"