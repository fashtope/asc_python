from django import forms
from asc_management.models import Course, Department, School, Session
from lecturer.models import Lecturer
from student.models import Student, StudentAddition
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget, PhoneNumberInternationalFallbackWidget


class DateInput(forms.DateInput):
    input_type = "date"

class AddLecturerForm(forms.Form):
    title = forms.CharField(label="Title", max_length=255,
                            required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your title"}))
    firstname = forms.CharField(label="Firstname", max_length=255,
                                required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your Firstname"}))
    lastname = forms.CharField(label="Lastname", max_length=255, required=True,
                               widget=forms.TextInput(attrs={"class": "form-control"}))
    lecturer_number = forms.CharField(label="Lecturer number", max_length=50,
                                      required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    address = forms.CharField(label="Address", max_length=50, required=False,
                              widget=forms.TextInput(attrs={"class": "form-control"}))
    username = forms.CharField(label="Username", max_length=20, required=True,
                               widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(
        label="Email", widget=forms.EmailInput(attrs={"class": "form-control"}))
    password = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))


class AddSchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['name', 'dean']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter school name'
            }),
            'dean': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select'
            })
        }
    # name = forms.CharField(label="School Name", max_length=255,
    #                         required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your School Name"}))

    # staffs = Lecturer.objects.all()
    # staff_list = []
    # for staff in staffs:
    #     small_staff = (staff.id, staff.first_name + " " + staff.last_name)
    #     staff_list.append(small_staff)

    # dean = forms.ChoiceField(
    #                             label="Dean",
    #                             choices=staff_list,
    #                             required=True,
    #                             widget=forms.Select(attrs={
    #                                 "class": "form-control",
    #                                 "placeholder": "Enter your Firstname"
    #                                 })
    #                             )


class AddDepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = 'name', 'school', 'hod'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter department name'
            }),
            'school': forms.Select(attrs={
                'class': 'form-control',
            }),
            'hod': forms.Select(attrs={
                'class': 'form-control',
            })
        }


class AddSessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = 'start', 'end'
        widgets = {
            'start': DateInput(attrs={
                'class': 'form-control',
            }),
            'end': DateInput(attrs={
                'class': 'form-control',
            }),
        }
        
        
class DepartmentChoice():
    department_choice = []
    try:
        department_query = Department.objects.all()
        for department_q in department_query:
            department = (department_q.id, department_q.name)
            department_choice.append(department)
    except: 
        department_choice=[]
        
        
class SessionChoice():
    session_choice = []
    try:
        __session_query = Session.objects.all()
        for session_q in __session_query:
            __session = (session_q.id, str(session_q.start)+"|"+str(session_q.end))
            session_choice.append(__session)
    except:
        session_choice = []
        
        
        
class AddStudentForm(forms.Form):
    first_name = forms.CharField(label="Firstname", max_length=255,
                                required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your Firstname"}))
    
    last_name = forms.CharField(label="Lastname", max_length=255, required=True,
                               widget=forms.TextInput(attrs={"class": "form-control"}))
    
    other_name = forms.CharField(label="Othernames", max_length=255, required=True,
                               widget=forms.TextInput(attrs={"class": "form-control"}))
    
    gender = forms.ChoiceField(label="Gender", choices=StudentAddition.GENDER_CHOICES,
                            required=True, widget=forms.Select(attrs={"class": "form-control"}))
    
    dob = forms.DateField(
        label='Date Of Birth',
        widget=DateInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    phone_number = PhoneNumberField(
        widget=PhoneNumberInternationalFallbackWidget(
            attrs={
                'class': 'form-control'
            },
        )
    )
    
    address = forms.CharField(label="Address", max_length=50, required=False,
                              widget=forms.TextInput(attrs={"class": "form-control"}))
    
    index_number = forms.CharField(label="Index number", max_length=50,
                                      required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    
    session_start = forms.ChoiceField(
        label="Session Start", 
        choices=SessionChoice.session_choice,
        required=True,
        widget=forms.Select(
            attrs={
                "class": "form-control"
                }
            )
        )
    
    session_end = forms.ChoiceField(
        label="Session End",
        choices=SessionChoice.session_choice,
        required=True,
        widget=forms.Select(
            attrs={
                "class": "form-control",
                }
            )
        )
    
    department = forms.ChoiceField(
        label="Department",
        choices=DepartmentChoice.department_choice,                    
        required=True, 
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your title"
                }
            )
        )
    
    username = forms.CharField(
        label="Username", 
        max_length=20, 
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
                }
            )
        )
    
    email = forms.EmailField(
        label="Email", 
        widget=forms.EmailInput(
            attrs={
                "class": "form-control"
                }
            )
        )
    
    password = forms.CharField(
        label="Password", 
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )    
    
    profile_pic = forms.ImageField(
        label='Profile Picture',
        required=False,
        widget=forms.FileInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
     
     
class EditStudentForm(forms.Form):
    first_name = forms.CharField(label="Firstname", max_length=255,
                                required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your Firstname"}))
    
    last_name = forms.CharField(label="Lastname", max_length=255, required=True,
                               widget=forms.TextInput(attrs={"class": "form-control"}))
    
    other_name = forms.CharField(label="Othernames", max_length=255, required=True,
                               widget=forms.TextInput(attrs={"class": "form-control"}))
    
    gender = forms.ChoiceField(label="Gender", choices=StudentAddition.GENDER_CHOICES,
                            required=True, widget=forms.Select(attrs={"class": "form-control"}))
    
    dob = forms.DateField(
        label='Date Of Birth',
        widget=DateInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    phone_number = PhoneNumberField(
        widget=PhoneNumberInternationalFallbackWidget(
            attrs={
                'class': 'form-control'
            },
        )
    )
    
    address = forms.CharField(label="Address", max_length=50, required=False,
                              widget=forms.TextInput(attrs={"class": "form-control"}))
    
    index_number = forms.CharField(label="Index number", max_length=50,
                                      required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    
    session_start = forms.ChoiceField(
        label="Session Start", 
        choices=SessionChoice.session_choice,
        required=True,
        widget=forms.Select(
            attrs={
                "class": "form-control"
                }
            )
        )
    
    session_end = forms.ChoiceField(
        label="Session End",
        choices=SessionChoice.session_choice,
        required=True,
        widget=forms.Select(
            attrs={
                "class": "form-control",
                'span': 'True'
                }
            )
        )
    
    department = forms.ChoiceField(
        label="Department",
        choices=DepartmentChoice.department_choice,                    
        required=True, 
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your title"
                }
            )
        )
    
    username = forms.CharField(
        label="Username", 
        max_length=20, 
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
                }
            )
        )
    
    email = forms.EmailField(
        label="Email", 
        widget=forms.EmailInput(
            attrs={
                "class": "form-control"
                }
            )
        )
    
    
        
        
class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = 'title', 'code', 'department', 'lecturer'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'code': forms.TextInput(attrs={
               'class': 'form-control' 
            }),
            'department': forms.Select(attrs={
                'class': 'form-control',
            }),
            'lecturer': forms.Select(attrs={
                'class': 'form-control',
            }),
        }