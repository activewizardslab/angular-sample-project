from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from myapps.users.forms import ChangeNameForm, ChangePwdForm

class IndexPageView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users:login')
    redirect_field_name = 'next'

    def get(self, request):
        return render(request, 'dashboard/index.html')

class SettingsPageView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users:login')
    redirect_field_name = 'next'

    def get(self, request):
        return render(request, 'dashboard/settings.html')

    def post(self, request):
        print(request.POST)
        if 'first_name' in request.POST:
            self.validate_change_name_form(request)
        elif 'current_password' in request.POST:
            self.validate_change_pwd_form(request)

        return redirect(reverse('dashboard:settings'))

    def validate_change_name_form(self, request):
        form = ChangeNameForm({
            'first_name': request.POST.get('first_name'),
            'last_name': request.POST.get('last_name')
        })

        if form.is_valid():
            request.user.first_name = request.POST.get('first_name')
            request.user.last_name = request.POST.get('last_name')
            request.user.save()

            messages.success(request, 'Your name successfully chaged!')
        else:
            messages.error(request, 'Back end validation error!')

    def validate_change_pwd_form(self, request):
        form = ChangePwdForm({
            'current_password': request.POST.get('current_password'),
            'new_password': request.POST.get('new_password'),
            'confirm_new_password': request.POST.get('confirm_new_password')
        }, user=request.user)

        if form.is_valid():
            email = request.user.email
            request.user.set_password(request.POST.get('new_password'))
            request.user.save()

            logout(request)
            user = authenticate(
                username=email,
                password=request.POST.get('new_password')
            )
            if user:
                login(request,user)

            messages.success(request, 'Your password successfully chaged!')
        else:
            messages.error(request, 'Back end validation error!')
