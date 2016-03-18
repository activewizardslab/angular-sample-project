from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy

class IndexPageView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users:login')
    redirect_field_name = 'next'

    def get(self, request):
        if request.session.get('greeting_message'):
            greeting_msg = True
            del request.session['greeting_message']
        else:
            greeting_msg = False

        return render(request, 'dashboard/index.html', {'greeting_msg': greeting_msg})
