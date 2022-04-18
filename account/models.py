from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    class Types(models.TextChoices):
        STUDENT = "STUDENT", "Student"
        HOD = "HOD", "Hod"
        LECTURER = "LECTURER", "Lecturer"
    type = models.CharField(_("Type"), max_length=50, choices=Types.choices, default=Types.HOD)
    