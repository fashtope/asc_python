from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib import messages
from asc_management.models import Course, Department, School, Semester, Session

from hod.forms import AddCourseForm, AddLecturerForm, AddSchoolForm, AddDepartmentForm, AddSessionForm, AddStudentForm, EditStudentForm
from lecturer.models import Lecturer, LecturerAddition, User
from student.models import Student, StudentAddition

# Create your views here.


def home(request):
    return render(request, 'hod/home.html')


def add_lecturer(request):
    if request.method == "POST":
        form = AddLecturerForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data["firstname"]
            lastname = form.cleaned_data["lastname"]
            title = form.cleaned_data["title"]
            address = form.cleaned_data["address"]
            email = form.cleaned_data["email"]
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            lecturer_number = form.cleaned_data["lecturer_number"]

            try:
                lecturer = User.objects.create_user(
                    username=username,
                    password=password,
                    first_name=firstname,
                    last_name=lastname,
                    email=email,
                    type=User.Types.LECTURER
                )

                lecturer_addition = LecturerAddition.objects.create(
                    user=lecturer,
                    title=title,
                    lecturer_number=lecturer_number,
                    address=address
                )

                lecturer.save()
                lecturer_addition.save()
                messages.success(request, "Successfully added lecturer")
                return redirect('hod:add_lecturer')

            except IntegrityError:
                messages.error(request, 'Username already exist')
                return redirect('hod:add_lecturer')

            except:
                messages.error(request, 'Unable to add student')
                return redirect('hod:add_lecturer')
    form = AddLecturerForm(request.POST)
    context = {'form': form}
    return render(request, 'hod/add_lecturer.html', context)


def set_current_session(request):
    if request.method == 'POST':
        select_session = request.POST.get('current_session')
        sessions = Session.objects.all()
        for session in sessions:
            session.is_current_session = False
            session.save()
            
        current_session = Session.objects.get(id=select_session)
        current_session.is_current_session = True
        current_session.save()
        
        
    sessions = Session.objects.all()
    context = {'sessions': sessions}
    return render(request, 'hod/set_current_session.html', context)


def set_current_semester(request):
    if request.method == 'POST':
        select_semester = request.POST.get('current_semester')
        semesters = Semester.objects.all()
        for semester in semesters:
            semester.is_current_semester = False
            semester.save()
            
        current_semester = Semester.objects.get(id=select_semester)
        current_semester.is_current_semester = True
        current_semester.save()
        
        
    semesters = Semester.objects.all()
    context = {'semesters': semesters}
    return render(request, 'hod/set_current_semester.html', context)

def manage_lecturer(request):
    lecturers = Lecturer.objects.all()
    context = {
        "lecturers": lecturers
    }
    return render(request, "hod/manage_lecturer.html", context)


def add_school(request):
    if request.method == "POST":
        form = AddSchoolForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            dean = form.cleaned_data.get('dean')

            try:
                school = School.objects.create(dean=dean, name=name)
                school.save()
            except:
                messages.error(request, 'Unable to add school')
                return redirect('hod:add_school')

    form = AddSchoolForm()
    context = {'form': form}
    return render(request, 'hod/add_school.html', context)


def add_department(request):
    if request.method == 'POST':
        form = AddDepartmentForm(request.POST)
        if form.is_valid():
            hod = form.cleaned_data.get('hod')
            name = form.cleaned_data.get('name')
            school = form.cleaned_data.get('school')

            try:
                department = Department.objects.create(
                    hod=hod, name=name, school=school)
                department.save()
                messages.success(request, 'Successfully added department')
                return redirect('hod:add_department')
            except:
                messages.error(request, 'Unable to add department')
                return redirect('hod:add_department')

    form = AddDepartmentForm()
    context = {'form': form}
    return render(request, 'hod/add_department.html', context)


def manage_department(request):
    departments = Department.objects.all()
    context = {'departments': departments}
    return render(request, 'hod/manage_department.html', context)


def add_session(request):
    if request.method == "POST":
        form = AddSessionForm(request.POST)
        if form.is_valid():
            start = form.cleaned_data.get('start')
            end = form.cleaned_data.get('end')

            session = Session(start=start, end=end)
            session.save()
            messages.success(request, 'Successfully added session')
            return redirect('hod:add_session')

    form = AddSessionForm()
    context = {'form': form}
    return render(request, 'hod/add_session.html', context)


def manage_session(request):
    sessions = Session.objects.all()
    context = {'sessions': sessions}
    return render(request, 'hod/manage_session.html', context)


def add_student(request):
    if request.method == 'POST':
        form = AddStudentForm(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            other_name = form.cleaned_data.get('other_name')
            gender = form.cleaned_data.get('gender')
            dob = form.cleaned_data.get('dob')
            phone_number = form.cleaned_data.get('phone_number')
            address = form.cleaned_data.get('address')
            index_number = form.cleaned_data.get('index_number')
            start = form.cleaned_data.get('session_start')
            end = form.cleaned_data.get('session_end')
            department = form.cleaned_data.get('department')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            profile_pic = form.files.get('profile_pic')
            department_obj = Department.objects.get(id=department)
            start_obj = Session.objects.get(id=start)
            end_obj = Session.objects.get(id=end)

            student = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password,
                type=User.Types.STUDENT
            )

            student_addition = StudentAddition.objects.create(
                user=student,
                othername=other_name,
                gender=gender,
                dob=dob,
                phone_number=phone_number,
                address=address,
                index_number=index_number,
                department=department_obj,
                start=start_obj,
                end=end_obj,
                profile_pic=profile_pic
            )

            student.save()
            student_addition.save()
            messages.success(request, "Successfully added student")
            return redirect('hod:add_student')
    form = AddStudentForm()
    context = {'form': form}
    return render(request, 'hod/add_student.html', context)


def manage_student(request):
    students = Student.objects.all()
    context = {
        "students": students
    }
    return render(request, "hod/manage_student.html", context)


def edit_student(request, pk):
    if request.method == 'POST':
        form = EditStudentForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            other_name = form.cleaned_data.get('other_name')
            gender = form.cleaned_data.get('gender')
            dob = form.cleaned_data.get('dob')
            phone_number = form.cleaned_data.get('phone_number')
            address = form.cleaned_data.get('address')
            index_number = form.cleaned_data.get('index_number')
            start = form.cleaned_data.get('session_start')
            end = form.cleaned_data.get('session_end')
            department = form.cleaned_data.get('department')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            department_obj = Department.objects.get(id=department)
            start_obj = Session.objects.get(id=start)
            end_obj = Session.objects.get(id=end)

            student = Student.objects.get(id=pk)
            student.first_name = first_name
            student.last_name = last_name
            student.username = username
            student.more.gender = gender
            student.more.department = department_obj
            student.more.start = start_obj
            student.more.end = end_obj
            student.more.index_number = index_number
            student.more.dob = dob
            student.email = email
            student.more.address = address
            student.more.othername = other_name
            student.more.phone_number = phone_number

            student.save()
            student.more.save()
            messages.success(request, "Successfully added student")
            return redirect('hod:add_student')
    initial_student = Student.objects.get(id=pk)
    form = EditStudentForm(
        initial={
            'first_name': initial_student.first_name,
            'last_name': initial_student.last_name,
            'username': initial_student.username,
            'gender': initial_student.more.gender,
            'department': initial_student.more.department.id,
            'session_start': initial_student.more.start.id,
            'session_end': initial_student.more.end.id,
            'index_number': initial_student.more.index_number,
            'dob': initial_student.more.dob,
            'email': initial_student.email,
            'address': initial_student.more.address,
            'other_name': initial_student.more.othername,
            'phone_number': initial_student.more.phone_number
        }
    )

    context = {'form': form}

    return render(request, 'hod/edit_student.html', context)


def add_course(request):
    if request.method == 'POST':
        form = AddCourseForm(request.POST)
        if form.is_valid():
            lecturer = form.cleaned_data.get('lecturer')
            title = form.cleaned_data.get('title')
            department = form.cleaned_data.get('department')
            code = form.cleaned_data.get('code')

            try:
                course = Course.objects.create(
                    lecturer=lecturer, title=title, department=department, code=code)
                course.save()
                messages.success(request, 'Successfully added Course')
                return redirect('hod:add_course')
            except:
                messages.error(request, 'Unable to add course')
                return redirect('hod:add_course')
    form = AddCourseForm()
    context = {'form': form}
    return render(request, 'hod/add_course.html', context)


def manage_course(request):
    courses = Course.objects.all()
    context = {
        "courses": courses
    }
    return render(request, "hod/manage_course.html", context)
