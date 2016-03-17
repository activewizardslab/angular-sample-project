from django.conf.urls import url

from .views import LoginPageView, ForgotPwdPageView, RegisterPageView, is_valid_email

urlpatterns = [
    url(r'^login/$', LoginPageView.as_view(), name='login'),
    #url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', RegisterPageView.as_view(), name='register'),
    url(r'^forgot_pwd/$', ForgotPwdPageView.as_view(), name='forgot_pwd'),
    # validators
    url(r'^is_valid_email/$', is_valid_email, name='is_valid_email'),
]