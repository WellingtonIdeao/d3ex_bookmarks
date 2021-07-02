from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.decorators import login_required

# function based views


def user_login(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Desabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect(reverse('account:login'))


# class based views

class LoginView(LoginView):
    template_name = 'account/registration/login.html'


class LogoutView(LogoutView):
    template_name = 'account/registration/logged_out.html'


class PasswordChangeView(PasswordChangeView):
    template_name = 'account/registration/password_change_form.html'
    success_url = reverse_lazy('account:password_change_done')


class PasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'account/registration/password_change_done.html'


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})