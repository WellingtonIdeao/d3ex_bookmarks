from django.urls import path, include
from .views import user_login, user_logout, Login, Logout,\
    PasswordChange, PasswordChangeDone, PasswordReset, PasswordResetDone, PasswordResetConfirm,\
    PasswordResetComplete, dashboard, register


app_name = 'account'
urlpatterns = [
    # previous login/logout views
    # path('login/', user_login, name='login'),
    # path('logout/', user_logout, name='logout')
    # path('auth/', include('django.contrib.auth.urls')),

    # login / logout urls
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('', dashboard, name='dashboard'),

    # change password urls
    path('password_change/', PasswordChange.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDone.as_view(), name='password_change_done'),

    # reset password urls
    path('password_reset/', PasswordReset.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDone.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetComplete.as_view(), name='password_reset_complete'),

    # register user urls
    path('register/', register, name='register')
]