from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.contrib.auth.models import User

from .forms import RegistrationForm, EmailForm

class LoginPageView(View):
    def get(self, request):
        return render(request, 'users/login.html')

    def post(self, request):
        user = authenticate(
            username=request.POST.get('email'),
            password=request.POST.get('password')
        )
        if user:
            if not request.POST.get('remember_me'):
                request.session.set_expiry(0)

            login(request, user)
            return redirect(reverse('users:register'))

        return render(request, 'users/login.html', {'is_login_error': True})

class ForgotPwdPageView(View):
    def get(self, request):
        return render(request, 'users/forgot-password.html')

    def post(self, request):
        pass

class RegisterPageView(View):
    def get(self, request):
        return render(request, 'users/register.html')

    def post(self, request):
        form = RegistrationForm({
            'first_name': request.POST.get('first_name'),
            'last_name': request.POST.get('last_name'),
            'password': request.POST.get('password'),
            'confirm_password': request.POST.get('confirm_password'),
            'email': request.POST.get('email')
        })

        if form.is_valid():
            user = User.objects.create_user(
                username=request.POST.get('email'),
                email=request.POST.get('email'),
                password=request.POST.get('password'),
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name')
            )
            user.save()
            login(request, user)
            return redirect(reverse('dashboard:index'))

        return render(request, 'users/register.html')

def is_valid_email(request):
    form = EmailForm({'email': request.POST.get('email')})
    if form.is_valid():
        return JsonResponse({'valid': True})

    return JsonResponse({'valid': False})
