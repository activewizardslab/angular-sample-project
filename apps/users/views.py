from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.views.generic import View

class LoginPageView(View):
    def get(self, request):
        return render(request, 'users/login.html')

    def post(self, request):
        print(request.POST)
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
        pass
