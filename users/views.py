import secrets
from datetime import time

from django.contrib.auth import login
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect

from django.urls import reverse_lazy, reverse
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_decode

from .forms import UserSetNewPasswordForm, UserProfileForm
from django.views.generic import CreateView, View, TemplateView, UpdateView

from config import settings
from users.forms import UserForm
from users.models import User


# Create your views here.
class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class UserForgotPasswordView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:user_password_reset.html')

    def get_object(self, queryset=None):
        return self.request.user


def generate_pass(request):
    password = User.objects.make_random_password()
    request.user.set_password(password)
    request.user.save()
    send_mail(
        subject='Восстановление пароля',
        message=f'Ваш новый пароль - {password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )

    return redirect(reverse('users:login'))


class UserPasswordResetConfirmView(SuccessMessageMixin,
                                   PasswordResetConfirmView):
    """Представление установки нового пароля"""
    form_class = UserSetNewPasswordForm
    template_name = 'users/user_password_set_new.html'
    success_url = reverse_lazy('catalog:home')
    success_message = 'Пароль успешно изменен. Можете авторизоваться на сайте.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Установить новый пароль'
        return context


# далее контроллеры для подтверждения почты

class RegisterView(CreateView):
    """Представление регистрации на сайте с формой регистрации"""
    form_class = UserForm
    success_url = reverse_lazy('users:email_confirmation_sent')
    template_name = 'users/register.html'


def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Регистрация на сайте'
    return context


def form_valid(self, form):
    token = secrets.token_hex(16)
    user = form.save()
    user.token = token
    user.is_active = False
    user.save()
    host = self.request.get_host()
    link = f'http://{host}/users/register/{token}/'
    message = f'''Для активации вашего аккаунта перейдите по ссылке:
                {link}'''
    time.sleep(10)
    send_mail("Верификация почты", message, settings.EMAIL_HOST_USER, [user.email, ])
    return super().form_valid(form)


class UserConfirmEmailView(View):
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if (user is not None and default_token_generator.check_token(user,
                                                                     token)):
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('users:email_confirmed')
        else:
            return redirect('users:email_confirmation_failed')


class EmailConfirmationSentView(TemplateView):
    template_name = 'users/email_confirmation_sent.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Письмо активации отправлено'
        return context


class EmailConfirmedView(TemplateView):
    template_name = 'users/email_confirmed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ваш электронный адрес активирован'
        return context


class EmailConfirmationFailedView(TemplateView):
    template_name = 'users/email_confirmation_failed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ваш электронный адрес не активирован'
        return context
