from django.conf.urls import url

from .views import IndexPageView, SettingsPageView

urlpatterns = [
    url(r'^$', IndexPageView.as_view(), name='index'),
    url(r'^settings/$', SettingsPageView.as_view(), name='settings'),
]
