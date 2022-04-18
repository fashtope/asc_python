from django.db import models
from django.utils.translation import gettext_lazy as _

from account.models import User

# Create your models here.

class HodManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.HOD)

class Hod(User):
    objects = HodManager()
    class Meta:
        proxy = True
        
    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.HOD
        return super().save(*args, **kwargs)
    
    @property
    def more(self):
        return self.hodaddition
    
class HodAddition(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    updated_at = models.DateField(auto_now=True)