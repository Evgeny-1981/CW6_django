from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from blogs.models import Blog


class FormMixin:
    """Класс для стилизации форм"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class BlogForm(FormMixin, ModelForm):
    class Meta:
        model = Blog
        exclude = ('count_views', 'slug', 'created_at',)


class BlogModeratorForm(FormMixin, ModelForm):
    class Meta:
        model = Blog
        exclude = ('count_views', 'slug', 'created_at',)
