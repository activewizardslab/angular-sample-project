from django.conf.urls import url

from .views import LoginPageView, ForgotPwdPageView, RegisterPageView

urlpatterns = [
    url(r'^login/$', LoginPageView.as_view(), name='login'),
    #url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', RegisterPageView.as_view(), name='register'),
    url(r'^forgot_pwd/$', ForgotPwdPageView.as_view(), name='forgot_pwd'),
]