from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse

from account.models import User
from asc_management.models import Course, Session


# Create your views here.

@login_required
def home(request):
    if request.user.type == User.Types.LECTURER:
        return render(request,'lecturer/home.html')
    else:
        return redirect(reverse('account:logout'))


@login_required
def take_attendance(request):
    if request.user.type == User.Types.LECTURER:
        courses = Course.objects.filter(lecturer=request.user.id)
        current_session = Session.current_session()
        
        context = {'courses': courses}
        return render(request,'lecturer/take_attendance.html', context)
    else:
        return redirect(reverse('account:logout'))


