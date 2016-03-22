from django.shortcuts import render, redirect
from django.http import JsonResponse, Http404
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.mail import send_mail
from django.template import loader
from django.conf import settings

from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .forms import RegistrationForm, EmailForm, ForgotPwdForm, ConfirmationPwdForm
from .mixins import NotLoginRequiredMixin

class LoginPageView(NotLoginRequiredMixin, View):
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
            return redirect(reverse('dashboard:index'))

        messages.error(request, 'Wrong email or password.')
        return render(request, 'users/login.html')

class ForgotPwdPageView(NotLoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'users/forgot-password.html')

    def post(self, request):
        form = ForgotPwdForm({'email': request.POST.get('email')})
        if form.is_valid():
            self.send_email(request, form.user)
            messages.success(request, 'Email has been sent to ' + request.POST.get('email') +\
                "'s email address. Please check its inbox to continue reseting password.")
            return redirect(reverse('users:forgot_pwd'))

        messages.error(request, 'Back end validation error.')
        return redirect(reverse('users:forgot_pwd'))

    def send_email(self, request, user):
        context = {
            'email': user.email,
            'domain': request.META['HTTP_HOST'],
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'user': user,
            'token': default_token_generator.make_token(user),
            'protocol': 'http',
        }
        email_template_name='users/password_reset_email.html'
        email = loader.render_to_string(email_template_name, context)

        send_mail('Change password', email , settings.EMAIL_HOST_USER, [user.email], fail_silently=False)

class RegisterPageView(NotLoginRequiredMixin, View):
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

            user = authenticate(
                username=request.POST.get('email'),
                password=request.POST.get('password')
            )
            login(request, user)

            # set greeting message
            messages.success(request, 'Welcome %s %s. You have successfully registered and logged in.' % (user.first_name, user.last_name))

            return redirect(reverse('dashboard:index'))

        return render(request, 'users/register.html')


class LogoutView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users:login')
    redirect_field_name = 'next'

    def get(self, request):
        logout(request)
        return redirect(reverse('users:login'))

class RegisterFormValidationView(View):
    def post(self, request):
        form = EmailForm({'email': request.POST.get('email')})
        if form.is_valid():
            return JsonResponse({'valid': True})

        return JsonResponse({'valid': False})

class ForgotPwdFormValidationView(View):
    def post(self, request):
        form = ForgotPwdForm({'email': request.POST.get('email')})
        if form.is_valid():
            return JsonResponse({'valid': True})

        return JsonResponse({'valid': False})

class ResetPwdConfirmPageView(NotLoginRequiredMixin, View):
    def get(self, request, uidb64=None, token=None):
        user = self.get_user(uidb64, token)
        if not user:
            raise Http404()

        return render(request, 'users/reset-password-confirm.html')

    def post(self, request, uidb64=None, token=None):
        form = ConfirmationPwdForm({
            'password': request.POST.get('password'),
            'confirm_password': request.POST.get('confirm_password')
        })

        user = self.get_user(uidb64, token)
        if not user:
            raise Http404()

        if form.is_valid():
            user.set_password(request.POST.get('password'))
            user.save()

            messages.success(request, 'Password successfully changed.')
            return redirect(reverse('users:login'))

        messages.error(request, 'Back end validation error.')
        return redirect(reverse('users:reset_pwd_confirm', args=(uidb64,token)))

    def get_user(self, uidb64, token):
        uid = urlsafe_base64_decode(uidb64)
        try:
            user = User.objects.get(pk=uid)
        except (ValueError, User.DoesNotExist):
            user = None

        if user and default_token_generator.check_token(user, token):
            return user

        return None
