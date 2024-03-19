from datetime import timezone

from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    ban_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
                'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = ('name', 'image', 'description', 'price')

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        for ban_word in self.ban_list:
            if ban_word in cleaned_data:
                raise ValidationError('В названии имеются запрещенные продукты')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        for ban_word in self.ban_list:
            if ban_word in cleaned_data:
                raise ValidationError('В описании имеются запрещенные продукты')

        return cleaned_data


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = ('name_ver', 'number_ver', 'sign_ver')


