from django.contrib.auth.forms import (UserCreationForm, SetPasswordForm, UserChangeForm)
from django.contrib.auth.views import PasswordResetView
from django.forms import forms
from django.urls import reverse_lazy

from users.models import User
from catalog.forms import StyleFormMixin


class UserForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)


class UserResetPasswordView(StyleFormMixin, PasswordResetView):
    """
    Стартовая страница сброса пароля почте
    """
    success_url = reverse_lazy('users:user_password_reset.html')
    template_name = "registration/user_password_reset.html"


class UserProfileForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'avatar', 'phone_number', 'country')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()


class UserSetNewPasswordForm(StyleFormMixin, SetPasswordForm):
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

