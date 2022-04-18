from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from account.models import User
from asc_management.models import Course


# Create your views here.

@login_required
def home(request):
    if request.user.type == User.Types.STUDENT:
        
        
        
        
        
        return render(request,'student/home.html')
    else:
        return redirect(reverse('account:logout'))


@login_required
def register_courses(request):
    
    if request.user.type == User.Types.STUDENT:
        courses = Course.objects.all()
        context = {'courses': courses}
        return render(request,'student/register_course.html', context)
    else:
        return redirect(reverse('account:logout'))


def get_courses(request):
    courses = Course.objects.all()
    
    return JsonResponse({'courses': list(courses.values())})



def save_courses(request):
    if request.method=='POST':
        post_return = request.POST
        reg_courses = post_return.getlist('course_code[]')
        for reg_course in reg_courses:
            print(reg_course)
        
        
    return HttpResponse('we are here')