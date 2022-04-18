from django.db import models
from lecturer.models import Lecturer


class Session(models.Model):
    start = models.DateField()
    end = models.DateField()
    is_current_session = models.BooleanField(default=False)
    
    def current_session():
        session = Session.objects.get(is_current_session=True)
        return session
    
    def __str__(self):
        return str(self.start) + "|" + str(self.end)


class Semester(models.Model):
    name = models.CharField(max_length=50)
    is_current_semester = models.BooleanField(default=False)
    
    
    def current_semester():
        semester = Semester.objects.get(is_current_semester=True)
        return semester

    def __str__(self):
        return self.name
    
    

class School(models.Model):
    name = models.CharField(max_length=255)
    dean = models.OneToOneField(Lecturer, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
    
    
class Department(models.Model):
    name = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    hod = models.ForeignKey(Lecturer, on_delete=models.DO_NOTHING)
    def __str__(self):
    
        return self.name
    

class Course(models.Model):
    title = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    code = models.CharField(max_length=255)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.DO_NOTHING,)
    
    
    

class Attendance(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    attendance_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, default=Semester.current_semester)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, default=Session.current_session)
    
    def __str__(self):
        return self.course_id + ' ' + self.date_time