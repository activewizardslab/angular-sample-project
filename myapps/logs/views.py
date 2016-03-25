from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, Http404

from .models import TemperatureLog, StatusLog, MultiDataLog
from .utils import create_fake_temperature_log, create_fake_multi_data_log, create_fake_status_log

import json

class TemparatureLogView(LoginRequiredMixin, View):
    def get(self, request):
        create_fake_temperature_log(request.user.pk)

        logs = TemperatureLog.objects.\
            filter(user_id=request.user.pk).\
            order_by('-timestamp')[:30]

        result = []
        for log in logs:
            result.append({
                field.name: getattr(log, field.name) for field in TemperatureLog._meta.get_fields()
            })

        return JsonResponse({'data': result})

class StatusLogView(LoginRequiredMixin, View):
    def get(self, request):
        create_fake_status_log(request.user.pk)

        logs = StatusLog.objects.\
            filter(user_id=request.user.pk).\
            order_by('-timestamp')[:30]

        result = []
        for log in logs:
            result.append({
                field.name: getattr(log, field.name) for field in StatusLog._meta.get_fields()
            })

        return JsonResponse({'data': result})

class MultiDataLogView(LoginRequiredMixin, View):
    def get(self, request):
        create_fake_multi_data_log(request.user.pk)

        log = MultiDataLog.objects.\
            filter(user_id=request.user.pk).\
            order_by('-timestamp').first()

        if log:
            result = {
                field.name: getattr(log, field.name) for field in MultiDataLog._meta.get_fields()
            }
        else:
            result = None

        return JsonResponse({'data': result})
