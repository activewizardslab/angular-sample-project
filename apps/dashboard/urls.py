from django.conf.urls import url

from .views import IndexPageView

urlpatterns = [
    url(r'^$', IndexPageView.as_view(), name='index'),
]
