# from django.http import HttpResponseRedirect
# from django.shortcuts import redirect
# from django.urls import reverse
# from django.utils.deprecation import MiddlewareMixin

# from account.models import User


# class LoginCheckMiddleWare(MiddlewareMixin):
    
#     def process_view(self, request, view_func, view_args, view_kwargs):
#         modulename = view_func.__module__
#         user = request.user
#         if user.is_authenticated:
#             if user.type == User.Types.HOD:
#                 if modulename == 'hod.views':
#                     pass
#                 if modulename == 'account.views':
#                     pass
#                 else:
                    
#                     return redirect(reverse('hod:home'))
                
#             if user.type == User.Types.LECTURER:                
                
#                 if modulename == 'lecturer.views':
#                     pass
#                 if modulename == 'account.views':
#                     pass
#                 else:
#                     print("i'm here")
#                     return redirect('lecturer:home')
                
#             if user.type == User.Types.STUDENT:
#                 if modulename == 'student.views':
#                     pass
#                 if modulename == 'account.views':
#                     pass
#                 else:
#                     return HttpResponseRedirect(reverse('student:home'))
#         else:
#             if request.path == reverse('account:login'):
#                 pass
#             else:
#                 return redirect(reverse('account:login'))
    