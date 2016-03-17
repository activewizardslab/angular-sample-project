from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('apps.users.urls', namespace='users')),
    url(r'^dashboard/', include('apps.dashboard.urls', namespace='dashboard')),
]
