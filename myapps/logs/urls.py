from django.conf.urls import url

from .views import TemparatureLogView, StatusLogView, MultiDataLogView

urlpatterns = [
    url(r'^temperature/$', TemparatureLogView.as_view(), name='temperature'),
    url(r'^status/$', StatusLogView.as_view(), name='status'),
    url(r'^multi_data/$', MultiDataLogView.as_view(), name='multi_data'),
]
