from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('myapps.users.urls', namespace='users')),
    url(r'^dashboard/', include('myapps.dashboard.urls', namespace='dashboard')),
]
