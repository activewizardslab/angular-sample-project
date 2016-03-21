from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib import messages

from apps.users.forms import SettingsForm

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
        form = SettingsForm({
            'first_name': request.POST.get('first_name'),
            'last_name': request.POST.get('last_name')
        })

        if form.is_valid():
            request.user.first_name = request.POST.get('first_name')
            request.user.last_name = request.POST.get('last_name')
            request.user.save()

            messages.success(request, 'Your account settings successfully chaged!')
        else:
            messages.error(request, 'Back end validation error!')

        return redirect(reverse('dashboard:settings'))
