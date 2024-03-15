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
    class Meta:
        model = Product
        fields = ('name', 'image', 'description', 'price')



class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = ('name_ver', 'number_ver', 'sign_ver')



