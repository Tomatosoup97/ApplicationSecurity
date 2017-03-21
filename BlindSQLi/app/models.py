from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class Patient(AbstractUser):
    DISEASES = (
        ('tuberculosis', 'tuberculosis'),
        ('AIDS', 'AIDS'),
        ('malaria', 'malaria'),
    )
    disease = models.CharField(max_length=16, choices=DISEASES)
    PESEL = models.CharField(max_length=12)
