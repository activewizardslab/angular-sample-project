from django.conf.urls import url

from .views import LoginPageView, ForgotPwdPageView, RegisterPageView, ResetPwdConfirmPageView
from .views import LogoutView, RegisterFormValidationView, ForgotPwdFormValidationView

urlpatterns = [
    url(r'^login/$', LoginPageView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', RegisterPageView.as_view(), name='register'),
    url(r'^forgot_pwd/$', ForgotPwdPageView.as_view(), name='forgot_pwd'),
    url(r'^reset_pwd_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})$',
        ResetPwdConfirmPageView.as_view(), name='reset_pwd_confirm'),
    # validators
    url(r'^is_unique_email/$', RegisterFormValidationView.as_view(), name='is_unique_email'),
    url(r'^is_exist_email/$', ForgotPwdFormValidationView.as_view(), name='is_exist_email'),
]
