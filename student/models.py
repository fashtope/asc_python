from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

from account.models import User
from asc_management.models import Course, Semester, Session, Department
# Create your models here.

class StudentManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.STUDENT)
        

class Student(User):
    objects = StudentManager()
    
    class Meta:
        proxy = True
        
    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.STUDENT
        return super().save(*args, **kwargs)
    
    
    @property
    def more(self):
        return self.studentaddition
    
class StudentAddition(models.Model):
    GENDER_CHOICES = (('Male','Male'), ('Female', 'Female'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    index_number = models.CharField(max_length=15, null=True, unique=True)
    othername = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=10, null=True, choices=GENDER_CHOICES)
    phone_number = PhoneNumberField(null=True)
    dob = models.DateField(null=True)
    profile_pic = models.ImageField(upload_to='Student Profile Picture', blank=True, null=True)
    start = models.ForeignKey(Session, related_name='start_session' , on_delete=models.DO_NOTHING, null=True)
    end = models.ForeignKey(Session, related_name='end_session' ,on_delete=models.DO_NOTHING, null=True)
    address = models.CharField(max_length=255, null=True)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.index_number
    
    
    
class RegisteredCourses(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    registration_date = models.DateField(auto_now=False, auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.student.more.index_number
