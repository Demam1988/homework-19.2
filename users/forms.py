from django.contrib.auth.forms import (UserCreationForm,
                                       PasswordResetForm, SetPasswordForm)
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy

from users.models import User
from catalog.forms import StyleFormMixin


class UserForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)


class UserResetPasswordView(PasswordResetView):
    """
    Стартовая страница сброса пароля почте
    """
    success_url = reverse_lazy('users:user_password_reset.html')
    template_name = "registration/user_password_reset.html"


class UserForgotPasswordForm(PasswordResetForm):
    """
    Запрос на восстановление пароля
    """

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })


class UserSetNewPasswordForm(SetPasswordForm):
    """
    Изменение пароля пользователя после подтверждения
    """

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })