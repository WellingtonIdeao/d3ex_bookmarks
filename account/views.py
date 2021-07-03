from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


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

class Login(LoginView):
    template_name = 'account/registration/login.html'


class Logout(LogoutView):
    template_name = 'account/registration/logged_out.html'


class PasswordChange(PasswordChangeView):
    template_name = 'account/registration/password_change_form.html'
    success_url = reverse_lazy('account:password_change_done')


class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'account/registration/password_change_done.html'


class PasswordReset(PasswordResetView):
    template_name = 'account/registration/password_reset_form.html'
    email_template_name = 'account/registration/password_reset_email.html'
    success_url = reverse_lazy('account:password_reset_done')


class PasswordResetDone(PasswordResetDoneView):
    template_name = 'account/registration/password_reset_done.html'


class PasswordResetConfirm(PasswordResetConfirmView):
    template_name = 'account/registration/password_reset_confirm.html'
    success_url = reverse_lazy('account:password_reset_complete')


class PasswordResetComplete(PasswordResetCompleteView):
    template_name = 'account/registration/password_reset_complete.html'


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/register_done.html', {'news_user': new_user})
    else:
        form = UserRegistrationForm()
    return render(request, 'account/register.html', {'form': form})

