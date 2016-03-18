from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import RegistrationForm, EmailForm

class LoginPageView(View):
    def get(self, request):
        if request.user.is_authenticated():
            return redirect(reverse('dashboard:index'))

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
            return redirect(reverse('dashboard:index'))

        return render(request, 'users/login.html', {'is_login_error': True})

class ForgotPwdPageView(View):
    def get(self, request):
        if request.user.is_authenticated():
            return redirect(reverse('dashboard:index'))

        return render(request, 'users/forgot-password.html')

    def post(self, request):
        pass

class RegisterPageView(View):
    def get(self, request):
        if request.user.is_authenticated():
            return redirect(reverse('dashboard:index'))

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

            user = authenticate(
                username=request.POST.get('email'),
                password=request.POST.get('password')
            )
            login(request, user)

            # set greeting message
            request.session['greeting_message'] = True

            return redirect(reverse('dashboard:index'))

        return render(request, 'users/register.html')


class LogoutView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users:login')
    redirect_field_name = 'next'

    def get(self, request):
        logout(request)
        return redirect(reverse('users:login'))

def is_valid_email(request):
    form = EmailForm({'email': request.POST.get('email')})
    if form.is_valid():
        return JsonResponse({'valid': True})

    return JsonResponse({'valid': False})
