from django.urls import path, include
from .views import user_login, user_logout, LoginView, LogoutView,\
    PasswordChangeView, PasswordChangeDoneView, dashboard


app_name = 'account'
urlpatterns = [
    # previous login/logout views
    # path('login/', user_login, name='login'),
    # path('logout/', user_logout, name='logout')
    # path('auth/', include('django.contrib.auth.urls')),

    # login / logout urls
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', dashboard, name='dashboard'),

    # change password urls
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
]