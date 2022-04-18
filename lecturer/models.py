from django.db import models

from account.models import User
# Create your models here.

class LecturerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.LECTURER)
    
    

class Lecturer(User):
    objects = LecturerManager()
    
    class Meta:
        proxy = True
        
    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.LECTURER
        return super().save(*args, **kwargs)
    
    
    @property
    def more(self):
        return self.lectureraddition
    
    
    
class LecturerAddition(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    updated_at = models.DateField(auto_now=True)
    title = models.CharField(max_length=50)
    lecturer_number = models.CharField(max_length=50)
    address = models.CharField(max_length=255)