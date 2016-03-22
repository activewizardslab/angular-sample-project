from django.conf.urls import url, include
from django.contrib import admin

from django.views.generic import RedirectView
from django.core.urlresolvers import reverse

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('myapps.users.urls', namespace='users')),
    url(r'^dashboard/', include('myapps.dashboard.urls', namespace='dashboard')),
    url(r'^$', RedirectView.as_view(url='/auth/login/'))
]
